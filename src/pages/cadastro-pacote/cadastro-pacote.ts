import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, ToastController } from 'ionic-angular';
import { UsuarioProvider } from "../../providers/usuario/usuario";
import { CadastroPacote2Page } from "../cadastro-pacote2/cadastro-pacote2"
import { Endereco, Cliente } from "../../interfaces/usuario"
import { ClienteProvider } from "../../providers/cliente/cliente";

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
    rua: '',
    numero: '',
    complemento: '',
    bairro: '',
    cep: '',
    cidade: '',
    estado: '',
    nome: '',
    cpf:''
  };

  constructor(
    public navCtrl: NavController,
    public navParams: NavParams,
    public usuarioProvider: UsuarioProvider,
    public clienteProvider: ClienteProvider,
    private toastCtrl: ToastController) {  }
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

  public cadastrarPacote(): void{
    // Pega as informações do endereço
    var rua = this.dados.rua;
    var numero = this.dados.numero;
    var complemento = this.dados.complemento;
    var bairro = this.dados.bairro;
    var cep = this.dados.cep;
    var cidade = this.dados.cidade;
    var estado = this.dados.estado;
    var nome = this.dados.nome;
    var cpf = this.dados.cpf;

    // verificação de campo vazio
    if (!rua ) {
      this.presentToast('A Rua é um campo obrigatório.');
      return;
    }
    if (!numero ) {
      this.presentToast('O Numero é um campo obrigatório.');
      return;
    }
    if (!bairro ) {
      this.presentToast('O bairro é um campo obrigatório.');
      return;
    }
    if (!cep ) {
      this.presentToast('O CEP é um campo obrigatório.');
      return;
    }
    if (!cidade ) {
      this.presentToast('A cidade é um campo obrigatório.');
      return;
    }
    if (!estado ) {
      this.presentToast('O estado é um campo obrigatório.');
      return;
    }
    if(!cpf){
      this.presentToast('O cpf é um campo obrigatório.')
    }
    if(!nome){
      this.presentToast('O nome é um campo obrigatório.')
    }

    let endereco: Endereco = {
      street: rua,
      number: numero,
      complement: complemento,
      district: bairro,
      postal_code: cep,
      city: cidade,
      state: estado,
      type:'endereco_cliente',
      country: 'BRASIL',
      lat: 0,
      long: 0
    };

     let cliente: Cliente = {
       name: nome,
       upi: cpf,
       addresses: [endereco]
     };
     console.log(cliente);

    this.clienteProvider.cadastrarCliente(cliente).subscribe( response => {
      this.navCtrl.push(CadastroPacote2Page, { cliente: cliente });
    }, error => console.log('Erro ao cadastrar cliente: ' + error));
  }

}
