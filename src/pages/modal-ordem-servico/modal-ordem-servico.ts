import { Component } from '@angular/core';
import { IonicPage, NavParams, ViewController } from 'ionic-angular';
import { ServiceProvider } from '../../providers/service/service';

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

  constructor(private viewCtrl: ViewController, private navParams: NavParams, private serviceProvider: ServiceProvider) {
    let teste = { vol: 2000, position: "", weight: 1000 }
    this.serviceProvider.listagem(teste, resposta => {
      this.ordemServico.lista = resposta.packages;
      this.ordemServico.cod = resposta.code;
      this.ordemServico.data = resposta.finalization_date;
    });
  }

  public fecharModal(ordemServico: any) {
    this.viewCtrl.dismiss({os: ordemServico});
  }

  public mandarPacotesEscolhidos() {
    let pacotesEscolhidos = this.ordemServico.lista.filter(
      pacote => { return pacote.selecionado; }
    );

    let ordemServico = {
      lista: pacotesEscolhidos,
      data: this.ordemServico.data,
      cod: this.ordemServico.cod
    };

    this.fecharModal(ordemServico);
  }

}
