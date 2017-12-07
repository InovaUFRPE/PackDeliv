import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams ,ToastController} from 'ionic-angular';
import { UsuarioProvider } from '../../providers/usuario/usuario';

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
    placa:null,
    ano:null,
    modelo:null,
  };
  
  constructor( public navCtrl: NavController, public navParams: NavParams,public toastCtrl:ToastController, private usuarioProvider: UsuarioProvider) {
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
  public fazerCadastroVeiculo(): void {
    // Pega as informações do usuário

    var placa = this.dados.placa;
    var ano = this.dados.ano;
    var modelo = this.dados.modelo;

    if (placa==undefined ) {
      // Faz algo caso não sejam
      this.presentToast('A placa é um campo obrigatório.');
      return;
    }
    if (placa.length !=  7 ) {
      // Faz algo caso não sejam
      this.presentToast('Placa inválida.');
      return;
    }
    if (ano==undefined ) {
      // Faz algo caso não sejam
      this.presentToast('O ano do carro é um campo obrigatório.');
      return;
    }
    if (ano.length !=  4 ) {
      // Faz algo caso não sejam
      this.presentToast('Ano inválido digite um ano com 4 digitos.');
      return;
    }
    if (modelo==undefined ) {
      // Faz algo caso não sejam
      this.presentToast('Modelo do carro é um campo obrigatório.');
      return;
    }

    var veiculo: object = {
      placa: placa,
      ano: ano,
      modelo: modelo,
    };

    var entregador = this.navParams.get('user');

    entregador.veiculo = veiculo;
  
    this.usuarioProvider.validarCNPJ(entregador, UsuarioProvider.ENTREGADOR, () => {
      this.irParaLogin();
    });
  }

  public irParaLogin(): void {
    this.navCtrl.popToRoot();
  }

}
