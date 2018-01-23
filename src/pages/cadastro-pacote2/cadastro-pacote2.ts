import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, ToastController} from 'ionic-angular';
import { UsuarioProvider } from "../../providers/usuario/usuario";
import { Pacote } from "../../interfaces/ordem-de-servico";
import { HomePage } from "../home/home";
import { SessionProvider } from '../../providers/session/session';

/**
 * Generated class for the CadastroPacote2Page page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-cadastro-pacote2',
  templateUrl: 'cadastro-pacote2.html',
})
export class CadastroPacote2Page {

  public dados = {
    altura: '',
    largura: '',
    comprimento: '',
    peso: ''
  };

  constructor(
    public navCtrl: NavController,
    public navParams: NavParams,
    public usuarioProvider: UsuarioProvider,
    private toastCtrl: ToastController) {  }

  /**
   * Realiza o cadastro do pacote
   * no banco de dados.
   *
   * Feito por: Augusto Paiva, 10/12/2017
   */

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

  public cadastrarPacote(): void{
    var peso = this.dados.peso;
    var altura = this.dados.altura;
    var largura = this.dados.largura;
    var comprimento = this.dados.comprimento;

    if (!peso ) {
      this.presentToast('O peso é um campo obrigatório.');
      return;
    }
    if (!altura ) {
      this.presentToast('A altura é um campo obrigatório.');
      return;
    }
    if (!largura ) {
      this.presentToast('A largura é um campo obrigatório.');
      return;
    }
    if (!comprimento ) {
      this.presentToast('O comprimento é um campo obrigatório.');
      return;
    }

    let endereco = this.navParams.get('endereco');

    // let pacote: Pacote = {
    //   width: largura,
    //   height: altura,
    //   length: comprimento,
    //   weight: peso,
    //   volume: +largura * +altura * +comprimento,
    //   id_address_start: SessionProvider.getUser().Endereco.id,
    // };
    
    // this.usuarioProvider.cadastrarPacote(pacote, () => {
    //   this.navCtrl.push(HomePage);
    // });
    
  }

}
