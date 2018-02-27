import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { DadosRastreioPage } from '../dados-rastreio/dados-rastreio';

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

  constructor(public navCtrl: NavController, public navParams: NavParams) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad CodigoRastreioPage');
  }

  irParaDadosRastreio(){
    this.navCtrl.push(DadosRastreioPage);
  }

}
