import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams,ToastController } from 'ionic-angular';
import { CadastroVeiculoPage } from "../cadastro-veiculo/cadastro-veiculo";
import { UsuarioProvider } from "../../providers/usuario/usuario";

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

  constructor(public navCtrl: NavController, public navParams: NavParams,public usuarioProvider: UsuarioProvider,private toastCtrl: ToastController) {
  }
  presentToast(message:string) {
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

  /**
   * Vai para a tela de cadastro de veículo,
   * passando as informações do usuário para a próxima tela.
   * 
   * Feito por: Matheus Campos da Silva, 07/11/2017
   * Editado po: Felipe Morais,11/11/2017
   */
  public irParaCadastroVeiculo(){
    // Pega as informações do formulário
    var login = this.dados.nomeUsuario;
    var nomeCompleto = this.dados.nomeCompleto;
    var cnpj = this.dados.cnpj;
    var cnh=this.dados.cnh;
    var senha = this.dados.senha;
    var SenhaConf = this.dados.senhaConf;
    var email=this.dados.email;
    var emailConf=this.dados.emailConf;


    if (login==undefined ) {
      // Faz algo caso não sejam
      this.presentToast('O login é um campo obrigatório.');
      return;
    }
    
    //verifica se o campo não está vazio
    if (nomeCompleto==undefined ) {
      // Faz algo caso não sejam
      this.presentToast('O Nome é um campo obrigatório.');
      return;
    }

    //verifica se o campo não está vazio
    if (cnpj==undefined ) {
      // Faz algo caso não sejam
      this.presentToast('O CNPJ é um campo obrigatório.');
      return;
    }
    if (cnpj.length !=  14 ) {
      // Faz algo caso não sejam
      this.presentToast('CNPJ inválido.');
      return;
    }
  
    //verifica se o campo não está vazio
    if (cnh==undefined ) {
      // Faz algo caso não sejam
      this.presentToast('O CNH é um campo obrigatório.');
      return;
    }
    if (cnh.length !=  12 ) {
      // Faz algo caso não sejam
      this.presentToast('CNH inválido.');
      return;
    }

    //verifica se o campo não está vazio
    if (senha==undefined ) {
      // Faz algo caso não sejam
      this.presentToast('A senha é um campo obrigatório.');
      return;
    }
    //verifica o tamanho da senha
    if (senha.length < 6 ) {
      // Faz algo caso não sejam
      this.presentToast('A senha deve conter no minimo 6 digitos.');
      return;
    }
     //verifica se o campo não está vazio
    if (SenhaConf==undefined ) {
      // Faz algo caso não sejam
      this.presentToast('Confirmar senha é  obrigatório.');
      return;
    }
    if (senha !== SenhaConf) {
      // Faz algo caso não sejam
      this.presentToast('As senhas não são correspondentes.');
      return;
    }

    if (email ==undefined ) {
      // Faz algo caso não sejam
      this.presentToast('O E-mail é um campo obrigatório.');
      return;
    }
    //verifica se o campo não está vazio
    if (emailConf==undefined) {
      // Faz algo caso não sejam
      this.presentToast('Confirmar E-mail é obrigatório.');
      return;
    }
    
    // Compara se os e-mails digitados são correspondentes
    if (email !== emailConf) {
      // Faz algo caso não sejam
      this.presentToast('Os E-mails não são correspondentes.');
      return;
    }
    // Cria o objeto usuario
    var entregador: object = {
    
      Login: login,
      CNPJ: cnpj,
      Senha: senha,
      Nome_completo:nomeCompleto,
      Email: email,
      CNH: cnh
    };
    

    // Passa o objeto usuario para a tela de cadastro de veículo
    //Caminho para cadastrar o entregador
    this.navCtrl.push(CadastroVeiculoPage, {user: entregador});
    
  }
}
