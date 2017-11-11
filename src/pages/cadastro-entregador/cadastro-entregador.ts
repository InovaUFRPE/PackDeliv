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
  public dados = {
    nomeCompleto:null,
    cnh:null,
    nomeUsuario: null,
    cnpj: null,
    senha: null,
    senhaConf: null,
    email: null,
    emailConf: null
  };

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
    var nomeUsuario = this.dados.nomeUsuario;
    var cnpj = this.dados.cnpj;
    var senha = this.dados.senha;
    var SenhaConf = this.dados.senhaConf;
    var nomeCompleto = this.dados.nomeCompleto;
    var cnh=this.dados.cnh;
    var email=this.dados.email;
    var emailConf=this.dados.emailConf;
    // Cria o objeto usuario
    var usuario: object = {

      username: nomeUsuario,
      cnpj: cnpj,
      password: senha,
      nomeCompleto:nomeCompleto,
      email: email
    };
    // Passa o objeto usuario para a tela de cadastro de veículo
    this.navCtrl.push(CadastroVeiculoPage, usuario);
  }
}
