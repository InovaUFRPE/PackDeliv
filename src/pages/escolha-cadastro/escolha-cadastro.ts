import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { CadastroPage } from "../cadastro/cadastro";
import { CadastroEntregadorPage } from "../cadastro-entregador/cadastro-entregador";

/**
 * Generated class for the EscolhaCadastroPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-escolha-cadastro',
  templateUrl: 'escolha-cadastro.html',
})
export class EscolhaCadastroPage {


  constructor(public navCtrl: NavController, public navParams: NavParams) {
  }

  ionViewDidLoad() {
  }

  irParaCadastroEmpresa(){
    this.navCtrl.push(CadastroPage)
  }

  
  irParaCadastroEntregador(){
    this.navCtrl.push(CadastroEntregadorPage)
  }

}
