import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, ToastController } from 'ionic-angular';
import { UsuarioProvider } from "../../providers/usuario/usuario";
import { CadastroPacote2Page } from "../cadastro-pacote2/cadastro-pacote2"
import { Endereco } from "../../interfaces/usuario"

/**
 * Generated class for the CadastrarPacotePage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-cadastro-pacote',
  templateUrl: 'cadastro-pacote.html',
})
export class CadastroPacotePage {

  public dados = {
    rua: null,
    numero: null,
    complemento: null,
    bairro: null,
    cep: null,
    cidade: null,
    estado: null
  };

  constructor(public navCtrl: NavController, public navParams: NavParams, public usuarioProvider: UsuarioProvider,private toastCtrl: ToastController) {
    console.log('cadastrar')
  }
  /**
   * Realiza o cadastro de endereço de destino para o pacote
   * no banco de dados.
   *
   * Feito por: Augusto Paiva, 08/12/2017
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

  irParaCadastrarPacote2(){
    this.navCtrl.push(CadastroPacote2Page);
  }

  public cadastrarPacote(): void{
    // Pega as informações do endereço
    var rua = this.dados.rua;
    var numero = this.dados.numero;
    var complemento = this.dados.complemento;
    var bairro = this.dados.bairro;
    var cep = this.dados.cep;
    var cidade = this.dados.cidade;
    var estado = this.dados.estado;

    // verificação de campo vazio
    if (rua==undefined ) {
      this.presentToast('A Rua é um campo obrigatório.');
      return;
    }
    if (numero==undefined ) {
      this.presentToast('O Numero é um campo obrigatório.');
      return;
    }
    if (bairro==undefined ) {
      this.presentToast('O bairro é um campo obrigatório.');
      return;
    }
    if (cep==undefined ) {
      this.presentToast('O CEP é um campo obrigatório.');
      return;
    }
    if (cidade==undefined ) {
      this.presentToast('A cidade é um campo obrigatório.');
      return;
    }
    if (estado==undefined ) {
      this.presentToast('O estado é um campo obrigatório.');
      return;
    }

    let endereco: Endereco = {
      Logradouro: rua,
      Numero: numero,
      Complemento: complemento,
      Bairro: bairro,
      CEP: cep,
      Cidade: cidade,
      Estado: estado,
      Pais: 'brasil'
    };
    console.log(endereco);
    

    this.navCtrl.push(CadastroPacote2Page, {endereco: endereco })
    //aqui deve ter uma criação de objeto para ser mandada para o usuario provider

  }





  ionViewDidLoad() {
    console.log('ionViewDidLoad CadastrarPacotePage');
  }

}
