import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, ToastController } from 'ionic-angular';
import { ConfiguracaoPage } from '../configuracao/configuracao';
import { SessionProvider } from '../../providers/session/session';
import { UsuarioProvider } from '../../providers/usuario/usuario';

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

  user = SessionProvider.getUser();

  public dados = {
    nome: null,
    email:null,
    emailConfig:null

  }

  constructor(
    public navCtrl: NavController,
    public navParams: NavParams,
    public sessionProvider: SessionProvider,
    private toastCtrl: ToastController,
    public usuarioProvider:UsuarioProvider) {

  }

  public atualizar():void{
    var email = this.dados.email;
    var emailConfig = this.dados.emailConfig;
    var nome = this.dados.nome;

    if (email != emailConfig) {
      this.presentToast('Os E-mails não são correspondentes.');
      return;
    }
    else{
      SessionProvider.getUser().Email=email      
    }

    if (nome != null){
      SessionProvider.getUser().nome = nome;
    }
    //mexer com o usuario providers

   // this.usuarioProvider.atualizarPerfilEmpresa(SessionProvider.getUser(),  () => {
     // this.navCtrl.push(PerfilPage);
   // });


    


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
  }

}
