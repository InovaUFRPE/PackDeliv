import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { CadastroVeiculoPage } from "../cadastro-veiculo/cadastro-veiculo";

/**
 * Generated class for the CadastroEntregadorPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-cadastro-entregador',
  templateUrl: 'cadastro-entregador.html',
})
export class CadastroEntregadorPage {
  public

  constructor(public navCtrl: NavController, public navParams: NavParams) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad CadastroEntregadorPage');
  }
  irParaCadastroVeiculo(){
    this.navCtrl.push(CadastroVeiculoPage)
  }
}
