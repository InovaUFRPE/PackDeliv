import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { SessionProvider } from "../../providers/session/session";

/**
 * Generated class for the PerfilEntregadorPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-perfil-entregador',
  templateUrl: 'perfil-entregador.html',
})
export class PerfilEntregadorPage {
  user = SessionProvider.getUser();

  constructor(public navCtrl: NavController, public navParams: NavParams) {
    console.log(this.user);
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad PerfilEntregadorPage');
  }

}
