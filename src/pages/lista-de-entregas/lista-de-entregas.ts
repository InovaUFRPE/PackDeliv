import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { UsuarioProvider } from '../../providers/usuario/usuario';
import { SessionProvider } from '../../providers/session/session';

/**
 * Generated class for the ListaDeEntregasPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-lista-de-entregas',
  templateUrl: 'lista-de-entregas.html',
})
export class ListaDeEntregasPage {
  static listaentregas:any;
  lista=ListaDeEntregasPage.listaentregas;
  constructor(public navCtrl: NavController, public navParams: NavParams,sessionProvider:SessionProvider) {
  } 


}
