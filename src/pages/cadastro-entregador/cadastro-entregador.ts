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

  /**
   * Vai para a tela de cadastro de veículo,
   * passando as informações do usuário para a próxima tela.
   * 
   * Feito por: Matheus Campos da Silva, 07/11/2017
   */
  public irParaCadastroVeiculo(){
    // Pega as informações do formulário
    var nomeUsuario: string = (<HTMLInputElement>document.getElementById('inputNomeUsuario')).value;
    var nomeCompleto: string = (<HTMLInputElement>document.getElementById('inputNomeCompleto')).value;
    var cnpj: string = (<HTMLInputElement>document.getElementById('inputCNPJ')).value;
    var cnh: string = (<HTMLInputElement>document.getElementById('inputCNH')).value;

    // Cria o objeto usuario
    var usuario: object = {
      nomeUsuario: nomeUsuario,
      nomeCompleto: nomeCompleto,
      cnpj: cnpj,
      cnh: cnh
    };

    // Passa o objeto usuario para a tela de cadastro de veículo
    this.navCtrl.push(CadastroVeiculoPage, usuario);
  }
}
