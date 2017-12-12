import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams,ToastController } from 'ionic-angular';
import { PerfilPage } from '../perfil/perfil';
import { SessionProvider } from '../../providers/session/session';
import { UsuarioProvider } from '../../providers/usuario/usuario';

/**
 * Generated class for the EditarPerfilPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-editar-perfil',
  templateUrl: 'editar-perfil.html',
})
export class EditarPerfilPage {
  session = this.navParams.get('session');
  user =this.session.user;
  
  
  public dados = {
    email: null,
    emailConf: null
  };

  constructor(public navCtrl: NavController, public navParams: NavParams,public sessionProvider: SessionProvider,private toastCtrl: ToastController,public usuarioProvider:UsuarioProvider) {
  }
  
  public Atualizar(): void {
    // Pega o e-mail do usuário
    var email = this.dados.email;
    var emailConf = this.dados.emailConf;
    //verifica se o campo não está vazio
    if (email ==undefined ) {
      // Faz algo caso não sejam
      this.presentToast('O E-mail é um campo obrigatório.');
      return;
    }
    //verifica se o campo não está vazio
    if (emailConf==undefined) {
      // Faz algo caso não sejam
      this.presentToast('Confirmar E-mail é obrigatório.');
      return;
    }
    
    // Compara se os e-mails digitados são correspondentes
    if (email !== emailConf) {
      // Faz algo caso não sejam
      this.presentToast('Os E-mails não são correspondentes.');
      return;
    }
    var usuario: object = {
      Email: email
    };
    this.session.user.Email=email
    this.usuarioProvider.atualizarPerfilEmpresa(this.session.user,  () => {
      this.navCtrl.push(PerfilPage);
    });

    this.navCtrl.push(PerfilPage,{session: this.sessionProvider})

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
  ionViewDidLoad() {
    console.log('ionViewDidLoad EditarPerfilPage');
  }

  abrirPerfil(){
    this.navCtrl.push(PerfilPage,{session: this.sessionProvider})
  }

}
