import { SessionProvider } from './../../providers/session/session';
import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, ToastController } from 'ionic-angular';
import { UsuarioProvider } from "../../providers/usuario/usuario";
import { EscolhaCadastroPage } from "../escolha-cadastro/escolha-cadastro";
import { CadastroPage } from "../cadastro/cadastro";
import { HomePage } from "../home/home";
import { RecuperarSenhaPage } from '../recuperar-senha/recuperar-senha';
import { PerfilPage } from '../perfil/perfil';
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
    
  ) { }

  
  
  public fazerLogin(): void {
    this.usuarioProvider.login(this.credenciais)
    .subscribe( usuario => {
      SessionProvider.openSession(usuario);
      console.log(usuario);
      this.usuarioProvider.pegarTodosPacotes(SessionProvider.getUser().Addresses[0].id);

      if (usuario.CNH) {
        this.navCtrl.push(HomeEntregadorPage, usuario);
      } else {
        this.navCtrl.push(HomePage, usuario);
      }
    }, error => {
      console.log('Erro ao fazer login: ' + error);
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

  presentToast(message: string) {
    let toast = this.toastCtrl.create({
      message: message,
      duration: 3000,
      position: 'bottom'
    });

    toast.onDidDismiss(() => {
      console.log('Dismissed toast');
    });

    toast.present();
  }
}
