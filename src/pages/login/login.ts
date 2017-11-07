import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { UsuarioProvider } from "../../providers/usuario/usuario";
import { EscolhaCadastroPage } from "../escolha-cadastro/escolha-cadastro";
import { CadastroPage } from "../cadastro/cadastro";
import { HomePage } from "../home/home";

/**
 * Generated class for the LoginPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-login',
  templateUrl: 'login.html',
})
export class LoginPage {

  public cadastroPage = CadastroPage;
  private usuarioDAO: UsuarioProvider;

  constructor(public navCtrl: NavController, public navParams: NavParams) {
  }

  /**
   * Compara as credenciais fornecidas com as credenciais
   * do banco de dados através da API RESTful, redireciona
   * o usuário para a página Home.
   *
   * Feito por: Matheus Campos da Silva, 30/10/2017
   */
  public fazerLogin(): void {
    // Pega as credenciais do usuário
    let nomeUsuario = (<HTMLInputElement>document.getElementById('inputNomeUsuario')).value;
    let senha = (<HTMLInputElement>document.getElementById('inputSenha')).value;

    // Faz a requisição à API e retorna os dados para o objeto usuario
    var usuario = this.usuarioDAO.getUsuario({
      nomeUsuario: nomeUsuario,
      senha: senha
    });

    // Vai para a tela Home e manda os dados do usuário para ela
    this.navCtrl.push(HomePage, usuario);
  }

  public irParaEscolhaCadastro() {
    this.navCtrl.push(EscolhaCadastroPage)
  }

  /**
    *A função login() é apenas para saber se o menu lateral estava pegando
    *já que pela função fazerLogin() não teria como saber visto que
    *ela não está pegando
    */ 
  public login() {
    this.navCtrl.push(HomePage)
  }
}
