import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { EditarPerfilEntregadorPage } from '../editar-perfil-entregador/editar-perfil-entregador'
import { SessionProvider } from '../../providers/session/session';
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

  public user = SessionProvider.getUser();
  constructor(
    public navCtrl: NavController,
    public navParams: NavParams,
    public sessionProvider: SessionProvider) {
  }

  onChange(SelectedValue){
    //console.info(status,selectedValue);

    SessionProvider.setDeliveryManStatus(SelectedValue)
    console.log("chegou aq")
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
