import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { ConfiguracaoPage } from '../configuracao/configuracao'
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

  constructor(public navCtrl: NavController, public navParams: NavParams) {
  }

  irParaConfiguracao(){
    this.navCtrl.push(ConfiguracaoPage)
  }
  ionViewDidLoad() {
    console.log('ionViewDidLoad EditarPerfilEntregadorPage');
  }

}
