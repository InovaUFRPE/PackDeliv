import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, ModalController, Modal } from 'ionic-angular';
import { SessionProvider} from '../../providers/session/session';
import { ModalOrdemServicoPage } from "../modal-ordem-servico/modal-ordem-servico";



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

  public ordemServico = {lista: [], cod: 0, data: ''};

  constructor(
    public navCtrl: NavController,
    public navParams: NavParams,
    public modalCtrl: ModalController
  ) {  }

  public ionViewDidLoad() {
    this.criarModal();
  }

  private criarModal() {
    const modal: Modal = this.modalCtrl.create(ModalOrdemServicoPage);
    modal.present();
    modal.onDidDismiss( data => {
      this.ordemServico = data.os;
      console.log('ordemServico: ');
      console.log(this.ordemServico);
    });
  }
  
}
