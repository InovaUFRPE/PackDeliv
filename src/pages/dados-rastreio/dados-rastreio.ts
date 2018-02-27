import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { AlertController } from 'ionic-angular';
import { NavPush } from 'ionic-angular/components/nav/nav-push';
import { LoginPage } from '../login/login';
import { MapaEntregadorPage } from '../mapa-entregador/mapa-entregador';

/**
 * Generated class for the DadosRastreioPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-dados-rastreio',
  templateUrl: 'dados-rastreio.html',
})
export class DadosRastreioPage {

  constructor(public navCtrl: NavController, public navParams: NavParams,public alertCtrl: AlertController) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad DadosRastreioPage');
  }

  public fazerConfirmacao(){
    this.showAlert();
    

  }
  showAlert() {
    let confirm = this.alertCtrl.create({
      title: 'Tem certeza que deseja confirmar este recebimento!!',
      subTitle: 'A partir do momento que a confirmação é feita, toda a responsabilidade deste pacote passa a ser exclusivamente do destinatário. Ao confirmar este recebimento implica na comprovação de que o destino final foi atingido!',
      buttons: [
        {
          text: 'CANCELAR',
          handler: () => {
            console.log('Disagree clicked');
          }
        },
        {
          text: 'CONFIRMAR',
          handler: () => {
            console.log('Agree clicked');
            this.navCtrl.push(LoginPage);
          }
        }
      ]
    });
    confirm.present();
  }

  public rastrear(){
    this.navCtrl.push(MapaEntregadorPage);


  }

}
