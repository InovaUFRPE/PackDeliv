import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, ToastController} from 'ionic-angular';
import { UsuarioProvider } from "../../providers/usuario/usuario";
import { Pacote } from "../../interfaces/ordem-de-servico";
import { HomePage } from "../home/home";
import { SessionProvider } from '../../providers/session/session';
import { PacoteProvider } from '../../providers/pacote/pacote'
import { ClienteProvider } from '../../providers/cliente/cliente';
import { Cliente } from '../../interfaces/usuario';

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
  public id_endereco_destino;
  public cliente;
  public id_client;
  public dados = {
    altura: '',
    largura: '',
    comprimento: '',
    peso: ''
  };
  

  constructor(
    public navCtrl: NavController,
    public navParams: NavParams,
    public sessionProvider:SessionProvider,
    public usuarioProvider: UsuarioProvider,
    private toastCtrl: ToastController,
    private pacoteProvider: PacoteProvider,
    private clienteProvider: ClienteProvider) {  }

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
  ionViewDidLoad() {
    console.log(SessionProvider.idclient)
    console.log(this.clienteProvider.pegarCliente(SessionProvider.idclient).addresses);
  }

  public cadastrarPacote(): void{
    this.cliente = this.navParams.get('cliente');
    this.clienteProvider.pegarCliente(SessionProvider.idclient).subscribe(response => {
      this.id_endereco_destino = response.Client.addresses[0].id;
      this.id_client = response.Client.id;
    }, error => console.log('Erro ao pegar cliente: ' + error));

    
     this.chamarCadastroDePacote();
  }

  pass(){
    this.navCtrl.push(HomePage);
  }

  chamarCadastroDePacote(){
    setTimeout(()=>{
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

    
    let pacote: Pacote = {
      
      width: +largura,
      height: +altura,
      length: +comprimento,
      weight: +peso,
      volume: +largura * +altura * +comprimento,
      id_address_start: SessionProvider.getUser().addresses[0].id,
      id_address_destiny: this.clienteProvider.pegarCliente(SessionProvider.idclient).addresses.id,
      id_client: SessionProvider.idclient,
      shipped: false,
      received: false,
      static_location: '',
      status: 'em fila para coleta',
      id_company: SessionProvider.getUser().id
    };
    console.log(pacote);
    this.pacoteProvider.cadastrarPacote(pacote, (response) => {
      console.log(response);
      this.navCtrl.setRoot(HomePage);
      this.navCtrl.popToRoot();
    });
  }, 5000);
  }

}
