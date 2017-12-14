import { SessionProvider } from './../../providers/session/session';
import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, ToastController } from 'ionic-angular';
import { UsuarioProvider } from "../../providers/usuario/usuario";
import { EscolhaCadastroPage } from "../escolha-cadastro/escolha-cadastro";
import { CadastroPage } from "../cadastro/cadastro";
import { HomePage } from "../home/home";
import { RecuperarSenhaPage } from '../recuperar-senha/recuperar-senha';
import { PerfilPage } from '../perfil/perfil';
import { ListaDeEntregasPage } from '../lista-de-entregas/lista-de-entregas';
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
  public credentials = {
    login: "",
    senha: ""
  };

  constructor(
    public navCtrl: NavController, 
    public navParams: NavParams, 
    public toastCtrl: ToastController, 
    public usuarioProvider: UsuarioProvider,
    
  ) {
  }
  
  /**
   * Compara as credenciais fornecidas com as credenciais
   * do banco de dados através da API RESTful, redireciona
   * o usuário para a página Home.
   *
   * Made by: Matheus Campos da Silva, 30/10/2017
   */
  public fazerLogin(): void {
    // Make request to API and pass user data to HomePage
    this.usuarioProvider.logar(this.credentials, (resposta) => {
      if (resposta) {
        
        // Vai para a tela Home e manda os dados do usuário para ela

        SessionProvider.openSession(resposta);
        this.usuarioProvider.pegarTodosPacotes(SessionProvider.getUser().Endereco.Id)
        
        let TIME_IN_MS = 2000;
        let hideFooterTimeout = setTimeout( () => {
             this.navCtrl.push(HomePage);
        }, TIME_IN_MS);

        


      } else {
        this.presentToast('Login ou Senha incorretos, tente novamente.');
      }
    });
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
