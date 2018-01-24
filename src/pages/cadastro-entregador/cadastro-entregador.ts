import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams,ToastController } from 'ionic-angular';
import { CadastroVeiculoPage } from "../cadastro-veiculo/cadastro-veiculo";
import { UsuarioProvider } from "../../providers/usuario/usuario";
import { Entregador } from '../../interfaces/usuario';

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
  public dados = {
    nomeCompleto:'',
    cnh:'',
    nomeUsuario: '',
    cnpj: '',
    senha: '',
    senhaConf: '',
    email: '',
    emailConf: ''
  };

  private regexSemMascara = new RegExp('[0-9]{14}');
  private regexComMascara = new RegExp('[0-9]{2}[\.][0-9]{3}[\.][0-9]{3}[\/][0-9]{4}[\-][0-9]{2}');

  constructor(public navCtrl: NavController, public navParams: NavParams,public usuarioProvider: UsuarioProvider,private toastCtrl: ToastController) {
  }

  private presentToast(message:string) {
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


    if (!login ) {
      // Faz algo caso não sejam
      this.presentToast('O login é um campo obrigatório.');
      return;
    }
    
    //verifica se o campo não está vazio
    if (!nomeCompleto ) {
      // Faz algo caso não sejam
      this.presentToast('O Nome é um campo obrigatório.');
      return;
    }

    if (nomeCompleto.length < 6) {
      this.presentToast('Nome precisa ter ao menos 6 caractéres');
      return;
    }

    //verifica se o campo não está vazio
    if (!cnpj ) {
      // Faz algo caso não sejam
      this.presentToast('O CNPJ é um campo obrigatório.');
      return;
    }

    // Analisa se o cnpj está no padrão
    if (!this.regexSemMascara.test(cnpj) && !this.regexComMascara.test(cnpj)) {
      this.presentToast('CNPJ fora do padrão');
      return;
    }
  
    //verifica se o campo não está vazio
    if (!cnh ) {
      // Faz algo caso não sejam
      this.presentToast('O CNH é um campo obrigatório.');
      return;
    }
    if (cnh.length !=  11 ) {
      // Faz algo caso não sejam
      this.presentToast('CNH inválido.');
      return;
    }

    //verifica se o campo não está vazio
    if (!senha ) {
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

    if (senha !== SenhaConf) {
      // Faz algo caso não sejam
      this.presentToast('As senhas não são correspondentes.');
      return;
    }

    if (!email) {
      // Faz algo caso não sejam
      this.presentToast('O E-mail é um campo obrigatório.');
      return;
    }
    
    // Compara se os e-mails digitados são correspondentes
    if (email !== emailConf) {
      // Faz algo caso não sejam
      this.presentToast('Os E-mails não são correspondentes.');
      return;
    }

    cnpj = cnpj.split('.')
      .join('')
      .replace('/', '')
      .replace('-', '');

    // Cria o objeto usuario
    var entregador: Entregador = {
      login: login,
      uci: cnpj,
      password: senha,
      name_deliveryman: nomeCompleto,
      email: email,
      dui: cnh,
      status: false,
      addresses: null,
      name: null,
      ready: false,
      lat: 0,
      long: 0
    };

    this.usuarioProvider.validarCNPJ(cnpj, (resposta) => {
      if (resposta) {
        // Passa o objeto usuario para a tela de cadastro de veículo
        // Caminho para cadastrar o entregador
        
        entregador.addresses = [resposta.endereco];
        entregador.name = resposta.nome;

        console.log(entregador);
        this.usuarioProvider.cadastrarEntregador(entregador).subscribe( res => {
          console.log(res);
          this.navCtrl.push(CadastroVeiculoPage, {id_deliveryman: res.id});
        }, error => console.log('Erro ao cadastrar entregador: ' + error));

      } else {
        this.presentToast('CNPJ inválido!');
      }
    });
    
  }
}
