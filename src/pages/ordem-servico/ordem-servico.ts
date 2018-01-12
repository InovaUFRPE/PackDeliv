import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { ServiceProvider } from '../../providers/service/service';
import { SessionProvider} from '../../providers/session/session';



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
  lista : any[];
  constructor(public navCtrl: NavController, public navParams: NavParams, public serviceProvider: ServiceProvider) {

  }

  ionDidViewLoad() {
    let teste = {"vol":2000, "position": "", "weight":1000}
    this.serviceProvider.listagem(teste, (resposta) => {
      this.lista = resposta.pacotes;



    });
  }

  public listagem(informacoes: any){

}
}
