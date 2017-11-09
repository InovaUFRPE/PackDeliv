import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { UsuarioProvider } from "../../providers/usuario/usuario";

import { LoginPage } from "../login/login";

/**
 * Generated class for the CadastroPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-cadastro',
  templateUrl: 'cadastro.html',
})
export class CadastroPage {
  
  public dados = {
    nomeUsuario: null,
    cnpj: null,
    senha: null,
    senhaConf: null,
    email: null,
    emailConf: null
  };

  constructor(public navCtrl: NavController, public navParams: NavParams, public usuarioDAO: UsuarioProvider) {
  }

  /**
   * Realiza o cadastro do usuário inserindo as informações
   * no banco de dados.
   * 
   * Feito por: Matheus Campos da Silva, 30/10/2017
   */
  public fazerCadastro(): void {
    // Pega as informações do usuário
    var nomeUsuario = this.dados.nomeUsuario;
    var cnpj = this.dados.cnpj;
    var senha = this.dados.senha;
    var SenhaConf = this.dados.senhaConf;

    // Compara se as senhas digitadas são correspondentes
    if (senha !== SenhaConf) {
      // Faz algo caso não sejam
      senha.innerText = '';
      SenhaConf.innerText = '';
      senha.focus();
      alert('As senhas não são correspondentes.')
      return;
    }

    // Pega o e-mail do usuário
    var email = this.dados.email;
    var emailConf = this.dados.emailConf;

    // Compara se os e-mails digitados são correspondentes
    if (email !== emailConf) {
      // Faz algo caso não sejam
      email.innerText = '';
      emailConf.innerText = '';
      email.focus();
      alert('E-mails não são correspondentes.');
      return;
    }

    // Cria o objeto usuario e o cadastro no BD
    var usuario: object = {
      username: nomeUsuario,
      cnpj: cnpj,
      password: senha,
      email: email
    };
    this.usuarioDAO.cadastrar(usuario);

    this.navCtrl.push(LoginPage);
  }

}
