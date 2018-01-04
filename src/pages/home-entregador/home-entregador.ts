import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { ListaDeEntregasPage } from '../lista-de-entregas/lista-de-entregas'
import { PerfilPage } from '../perfil/perfil'
import { ConfiguracaoPage } from '../configuracao/configuracao'

/**
 * Generated class for the HomeEntregadorPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-home-entregador',
  templateUrl: 'home-entregador.html',
})
export class HomeEntregadorPage {
  
  entregas = ListaDeEntregasPage;
  perfil = PerfilPage;
  configuracao = ConfiguracaoPage;
  constructor(public navCtrl: NavController, public navParams: NavParams) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad HomeEntregadorPage');
  }

}
