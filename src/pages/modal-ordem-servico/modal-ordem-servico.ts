import { Component } from '@angular/core';
import { IonicPage, ViewController, NavParams } from 'ionic-angular';

/**
 * Generated class for the ModalOrdemServicoPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-modal-ordem-servico',
  templateUrl: 'modal-ordem-servico.html',
})
export class ModalOrdemServicoPage {
  public ordemServico = {cod: 0, data: '', lista: []};

  constructor(private viewCtrl: ViewController, private navParams: NavParams) {
    this.ordemServico = this.navParams.get('os');
  }

  public fecharModal() {
    this.viewCtrl.dismiss();
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad ModalOrdemServicoPage');
  }

}
