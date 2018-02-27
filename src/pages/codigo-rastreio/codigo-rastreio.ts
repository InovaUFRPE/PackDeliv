import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams,ToastController,AlertController } from 'ionic-angular';
import { DadosRastreioPage } from '../dados-rastreio/dados-rastreio';
import { Codigo } from '../../interfaces/usuario';
import { PacoteProvider } from "../../providers/pacote/pacote";
import { SessionProvider } from '../../providers/session/session';

/**
 * Generated class for the CodigoRastreioPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-codigo-rastreio',
  templateUrl: 'codigo-rastreio.html',
})
export class CodigoRastreioPage {

  public credenciais: Codigo = { codigo:''};

  constructor( public navCtrl: NavController,
    public navParams: NavParams,
    public toastCtrl: ToastController,
    public pacoteProvider: PacoteProvider,
    private alertCtrl: AlertController) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad CodigoRastreioPage');
  }

  rastreioPacote(){
    this.navCtrl.push(DadosRastreioPage);
  }

  public fazerRastreio(): void {
    if (!this.credenciais) {
      this.presentAlert('O campo de login é obrigatório!');
      return;
    }
    console.log(this.credenciais)
    if((this.pacoteProvider.rastrear(this.credenciais))!=undefined){
      console.log('bumbum')
    }
    
  }

  private presentAlert(message: string): void {
    let alert = this.alertCtrl.create({
      title: 'Alerta',
      subTitle: message,
      buttons: ['Ok']
    });

    alert.present();
  }

}
