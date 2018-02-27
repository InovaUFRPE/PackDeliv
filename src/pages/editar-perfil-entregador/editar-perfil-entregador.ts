import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, ToastController,LoadingController } from 'ionic-angular';
import { ConfiguracaoPage } from '../configuracao/configuracao';
import { SessionProvider } from '../../providers/session/session';
import { UsuarioProvider } from '../../providers/usuario/usuario';
import { FileTransfer, FileUploadOptions, FileTransferObject } from '@ionic-native/file-transfer';
import { Camera, CameraOptions } from '@ionic-native/camera';

/**
 * Generated class for the EditarPerfilEntregadorPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-editar-perfil-entregador',
  templateUrl: 'editar-perfil-entregador.html',
})
export class EditarPerfilEntregadorPage {
  imageURI:any;
  imageFileName='http://192.168.25.4:5000/photo/'+SessionProvider.getUser().id+'.jpg';
  verificarImage(imageFileName)

  public verificarImage(url){
    var http = new XMLHttpRequest();

    http.open('HEAD', url, false);
    http.send();

    if(http.status == 404){
      this.imageFileName='assets/icon/user.png';
    }
  }
  

  user = SessionProvider.getUser();
  url = 'http://192.168.25.4:5000'

  public dados = {
    imageUrl:null,
    nomeCompleto:null,
    email: null,
    emailConf: null,
    cep:null,
    bairro:null,
    complemento:null,
    numero:null,
    logradouro:null
  };

  constructor(
    public navCtrl: NavController,
    public navParams: NavParams,
    public sessionProvider: SessionProvider,
    private toastCtrl: ToastController,
    public usuarioProvider:UsuarioProvider,
    private transfer: FileTransfer,
    private camera: Camera,
    public loadingCtrl: LoadingController) {

  }

  public atualizar():void{
    // Pega o e-mail do usuário
    var email = this.dados.email;
    var emailConf = this.dados.emailConf;
    //verifica se o campo não está vazio
    
    
    // Compara se os e-mails digitados são correspondentes
    if (email !== emailConf) {
      // Faz algo caso não sejam
      this.presentToast('Os E-mails não são correspondentes.');
      return;
    }

    // var nomeCompleto=this.dados.nomeCompleto;
    var cep = this.dados.cep;
    var bairro = this.dados.bairro;
    var complemento = this.dados.complemento;
    var numero = this.dados.numero;
    var logradouro = this.dados.logradouro;
    console.log(this.dados);
    if(cep!=null){
      SessionProvider.getUser().addresses.postal_code=cep
    }
    if(bairro!=null){
      SessionProvider.getUser().addresses.district=bairro
    }
    if(complemento!=null){
      SessionProvider.getUser().addresses.complement=complemento
    }
    if(numero!=null){
      SessionProvider.getUser().addresses.number=numero
    }
    if(logradouro!=null){
      SessionProvider.getUser().addresses.street=logradouro
    }
    
    
    SessionProvider.getUser().email=email
    
    this.uploadFile()
    
    this.usuarioProvider.atualizarPerfilEntregador(SessionProvider.getUser(),  () => {
      this.navCtrl.push(ConfiguracaoPage);
    });

    

  }

  presentToast(message:string) {
    let toast = this.toastCtrl.create({
      message: message,
      duration: 3000,
      position: 'bottom'
    });
  
    toast.onDidDismiss(() => {
      console.log('Dismissed toast');
    });
  
    toast.present();
  }
  irParaConfiguracao(){
    this.navCtrl.push(ConfiguracaoPage)
  }
  ionViewDidLoad() {
    console.log('ionViewDidLoad EditarPerfilEntregadorPage');
    console.log(this.user)
  }
  getImage() {
    const options: CameraOptions = {
      quality: 100,
      destinationType: this.camera.DestinationType.FILE_URI,
      sourceType: this.camera.PictureSourceType.PHOTOLIBRARY
    }
  
    this.camera.getPicture(options).then((imageData) => {
      this.imageURI = imageData;
      this.imageFileName= this.imageURI;
    }, (err) => {
      console.log(err);
      this.presentToast(err);
    });
  }

  uploadFile() {
    let loader = this.loadingCtrl.create({
      content: "Uploading..."
    });
    loader.present();
    const fileTransfer: FileTransferObject = this.transfer.create();
  
    let options: FileUploadOptions = {
      fileKey: SessionProvider.getUser().id,
      fileName: SessionProvider.getUser().id,
      chunkedMode: false,
      mimeType: "image/jpeg",
      headers: {}
    }
  
    fileTransfer.upload(this.imageURI, this.url+'/upload_photo/'+SessionProvider.getUser().id, options)
      .then((data) => {
      console.log(data+" Uploaded Successfully");
      this.imageFileName = this.url+"/photo/"+SessionProvider.getUser().id+'jpg'
      loader.dismiss();
      this.presentToast("Image uploaded successfully");
    }, (err) => {
      console.log(err);
      loader.dismiss();
      this.presentToast(err);
    });
  }


}
