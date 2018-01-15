import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { EditarPerfilEntregadorPage } from '../editar-perfil-entregador/editar-perfil-entregador'

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

  constructor(public navCtrl: NavController, public navParams: NavParams) {
  }

  onChange(selectedValue){
    console.info("Selected:",selectedValue);
  }

  public editarPerfil(){
    this.navCtrl.push(EditarPerfilEntregadorPage)
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad ConfiguracaoPage');
  }

}
