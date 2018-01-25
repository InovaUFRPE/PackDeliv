import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { EditarPerfilEntregadorPage } from '../editar-perfil-entregador/editar-perfil-entregador'
import { SessionProvider } from '../../providers/session/session';
import { UsuarioProvider } from '../../providers/usuario/usuario';
import { LoginPage } from '../login/login'
/**
 * Generated class for the ConfiguracaoPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-configuracao',
  templateUrl: 'configuracao.html',
})
export class ConfiguracaoPage {
  public status:boolean=SessionProvider.getUser().status
  public user = SessionProvider.getUser();
  constructor(
    public usuarioProvider:UsuarioProvider,
    public navCtrl: NavController,
    public navParams: NavParams,
    public sessionProvider: SessionProvider) {
  }

  onChange(){
    //console.info(status,selectedValue);
    this.user=SessionProvider.getUser();
    console.log("chegou aq")
    if (this.status==false){
      console.log("chegou aq 1")
      this.user.status=false
      this.usuarioProvider.atualizarStatusEntregador(SessionProvider.getUser());
    }
    else{
      this.user.status=true
      this.usuarioProvider.atualizarStatusEntregador(SessionProvider.getUser());
      console.log("chegou aq 3")
    }

  }

  public editarPerfil(){
    this.navCtrl.push(EditarPerfilEntregadorPage)
  }




  ionViewDidLoad() {
    console.log('ionViewDidLoad ConfiguracaoPage');

  }


  sair(){
    console.log(status)
    console.log(SessionProvider.getDeliveryManStatus());
    SessionProvider.closeSession();
    this.navCtrl.parent.parent.setRoot(LoginPage);
    console.log(SessionProvider.getUser());
  }

}
