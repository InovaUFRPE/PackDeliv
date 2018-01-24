import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams ,ToastController} from 'ionic-angular';
import { UsuarioProvider } from '../../providers/usuario/usuario';
import { Entregador, Veiculo } from '../../interfaces/usuario';
import { LoginPage } from '../login/login';

/**
 * Generated class for the CadastroVeiculoPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-cadastro-veiculo',
  templateUrl: 'cadastro-veiculo.html',
})
export class CadastroVeiculoPage {
  
  public dados = {
    placa: '',
    ano: '',
    modelo: '',
    volume: '',
    cor: '',

  };
  
  constructor(
    public navCtrl: NavController, 
    public navParams: NavParams,
    public toastCtrl:ToastController,
    private usuarioProvider: UsuarioProvider) { }
  


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
  public fazerCadastroVeiculo(): void {
    // Pega as informações do usuário

    var placa = this.dados.placa;
    var ano = this.dados.ano;
    var modelo = this.dados.modelo;
    var volume = this.dados.volume;

    if (!placa) {
      // Faz algo caso não sejam
      this.presentToast('A placa é um campo obrigatório.');
      return;
    }
    if (placa.length <  7 ) {
      // Faz algo caso não sejam
      this.presentToast('Placa inválida.');
      return;
    }
    if (!ano) {
      // Faz algo caso não sejam
      this.presentToast('O ano do carro é um campo obrigatório.');
      return;
    }
    if (!volume) {
      // Faz algo caso não sejam
      this.presentToast('O volume é um campo obrigatório.');
      return;
    }
    if (ano.length !=  4 ) {
      // Faz algo caso não sejam
      this.presentToast('Ano inválido digite um ano com 4 digitos.');
      return;
    }
    if (!modelo) {
      // Faz algo caso não sejam
      this.presentToast('Modelo do carro é um campo obrigatório.');
      return;
    }

    var veiculo: Veiculo = {
      license_plate: placa,
      year: +ano,
      model: modelo,
      color: '',
      ready: false,
      volume: +volume,
      id_deliveryman: this.navParams.get('id_deliveryman')
    };

    console.log(veiculo);

    this.usuarioProvider.cadastrarVeiculo(veiculo).subscribe( resolve => {
      console.log(resolve);
    }, reject => console.log('Erro ao cadastrar veículo: ' + reject));
  }

}
