import { SessionProvider } from './../../providers/session/session';
import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, ToastController, AlertController } from 'ionic-angular';
import { UsuarioProvider } from "../../providers/usuario/usuario";
import { EscolhaCadastroPage } from "../escolha-cadastro/escolha-cadastro";
import { CadastroPage } from "../cadastro/cadastro";
import { HomePage } from "../home/home";
import { RecuperarSenhaPage } from '../recuperar-senha/recuperar-senha';
import { HomeEntregadorPage } from '../home-entregador/home-entregador'
import { Credenciais } from '../../interfaces/usuario';

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
  public credenciais: Credenciais = { login: '', password: ''};

  constructor(
    public navCtrl: NavController,
    public navParams: NavParams,
    public toastCtrl: ToastController,
    public usuarioProvider: UsuarioProvider,
    private alertCtrl: AlertController
  ) { }

  public fazerLogin(): void {
    if (!this.credenciais.login) {
      this.presentAlert('O campo de login é obrigatório!');
      return;
    }

    if (!this.credenciais.password) {
      this.presentAlert('O campo de senha é obrigatório!');
      return;
    }

    this.usuarioProvider.fazerLogin(this.credenciais)
    .subscribe( usuario => {
      SessionProvider.openSession(usuario);
      console.log(SessionProvider.getUser());
      var user = SessionProvider.getUser();
      this.credenciais = {login: '', password: ''};
      if (user.type == "Deliveryman") {
        this.navCtrl.push(HomeEntregadorPage, usuario);
      } else {
        this.navCtrl.push(HomePage, usuario);
      }
    }, error => {
      this.presentAlert('Erro ao fazer login: ' + error);
    });
  }

  public login(){
    this.navCtrl.push(HomeEntregadorPage)
  }
  public irParaEscolhaCadastro() {
    this.navCtrl.push(EscolhaCadastroPage);
  }

  public irParaRecuperarSenha() {
    this.navCtrl.push(RecuperarSenhaPage);
  }

  private presentAlert(message: string): void {
    let alert = this.alertCtrl.create({
      title: 'Alerta',
      subTitle: message,
      buttons: ['Ok']
    });

    alert.present();
  }
}
