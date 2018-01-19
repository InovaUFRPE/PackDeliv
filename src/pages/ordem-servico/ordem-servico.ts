import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, ModalController, ViewController } from 'ionic-angular';
import { ServiceProvider } from '../../providers/service/service';
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
    public serviceProvider: ServiceProvider,
    public modalCtrl: ModalController
  ) {  }

  public ngAfterViewInit() {
    let teste = {vol:2000, position: "", weight:1000}
    this.serviceProvider.listagem(teste, (resposta) => {
      this.ordemServico.lista = resposta.pacotes;
      this.ordemServico.cod = resposta.codigo;
      this.ordemServico.data = resposta.dataFinal;
    });
  }

  private criarModal(ordemServico: any) {
    let modal = this.modalCtrl.create(ModalOrdemServicoPage, {os: ordemServico});
    modal.present();
  }

  public mandarPacotesEscolhidos() {
    let pacotesEscolhidos = this.ordemServico.lista.filter(
      pacote => {return pacote.selecionado;}
    );

    let ordemServico = {
      lista: pacotesEscolhidos,
      data: this.ordemServico.data,
      cod: this.ordemServico.cod
    };

    this.criarModal(ordemServico);
    // for (let pacote of pacotesEscolhidos) {
    //   pacote.selecionado = undefined;
    // }
  }
}
