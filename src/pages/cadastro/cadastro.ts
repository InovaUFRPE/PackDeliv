import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams ,ToastController} from 'ionic-angular';
import { UsuarioProvider } from "../../providers/usuario/usuario";
import { Empresa } from '../../interfaces/usuario';


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
    nomeUsuario: '',
    cnpj: '',
    senha: '',
    senhaConf: '',
    email: '',
    emailConf: ''
  };

  private regexSemMascara = new RegExp('[0-9]{14}');
  private regexComMascara = new RegExp('[0-9]{2}[\.][0-9]{3}[\.][0-9]{3}[\/][0-9]{4}[\-][0-9]{2}');

  constructor(
    public navCtrl: NavController,
    public navParams: NavParams,
    public usuarioProvider: UsuarioProvider,
    private toastCtrl: ToastController) { }

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
  public fazerCadastro(): void {
    // Pega as informações do usuário
    var nomeUsuario = this.dados.nomeUsuario;
    var cnpj = this.dados.cnpj;
    var senha = this.dados.senha;
    var SenhaConf = this.dados.senhaConf;

    // Compara se as senhas digitadas são correspondentes

    if (!nomeUsuario ) {
      // Faz algo caso não sejam
      this.presentToast('O login é um campo obrigatório.');
      return;
    }
    //verifica se o campo não está vazio
    if (!cnpj ) {
      // Faz algo caso não sejam
      this.presentToast('O CNPJ é um campo obrigatório.');
      return;
    }
    // Analisa se o cnpj está de acordo com o padrão
    if (!this.regexComMascara.test(cnpj) && !this.regexSemMascara.test(cnpj)) {
      this.presentToast('CNPJ não está no padrão.');
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
     //verifica se o campo não está vazio
    if (!SenhaConf ) {
      // Faz algo caso não sejam
      this.presentToast('Confirmar senha é  obrigatório.');
      return;
    }


    //compara as senhas
    if (senha !== SenhaConf) {
      // Faz algo caso não sejam
      this.presentToast('As senhas não são correspondentes.');
      return;
    }

    // Pega o e-mail do usuário
    var email = this.dados.email;
    var emailConf = this.dados.emailConf;
    //verifica se o campo não está vazio
    if (!email  ) {
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
    
    // Cria o objeto usuario e o cadastro no BD
    var usuario = {
      Login: nomeUsuario,
      CNPJ: cnpj.split('.')
      .join('')
      .replace('/','')
      .replace('-',''),
      Senha: senha,
      Email: email
    };

    this.usuarioProvider.validarCNPJ(usuario.CNPJ, (resposta) => {
      if (resposta) {
        console.log(resposta);
        let empresa: Empresa = {
          uci: usuario.CNPJ,
          email: usuario.Email,
          login: usuario.Login,
          password: usuario.Senha,
          addresses: [resposta.endereco],
          name: resposta.nome
        };

        this.usuarioProvider.cadastrarEmpresa(empresa)
        .subscribe( response => {
          console.log(response);
          this.navCtrl.popToRoot();
        }, error => console.log('Erro ao cadastrar empresa: ' + error));
      } else {
        this.presentToast('Cadastro não realizado.');
      }
    });
  }

}
