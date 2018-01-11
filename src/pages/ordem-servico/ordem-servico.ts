import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { ServiceProvider } from '../../providers/service/service';

/**
 * Generated class for the OrdemServicoPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-ordem-servico',
  templateUrl: 'ordem-servico.html',
})
export class OrdemServicoPage {

  private url: string = 'http://localhost:8080/';

  items: any;
  lista: any;

  constructor(public navCtrl: NavController, public navParams: NavParams, public restProvider: ServiceProvider) {
  }



  ionViewDidLoad() {
    console.log('ionViewDidLoad OrdemServicoPage');
  }

}
