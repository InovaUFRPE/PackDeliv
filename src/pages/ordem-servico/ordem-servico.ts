import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { ServiceProvider } from '../../providers/service/service';
import { session } from '../../providers/session/SessionProvider'

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

  lista: any[];

  constructor(public navCtrl: NavController, public navParams: NavParams, public restProvider: ServiceProvider) {
    this.listagem({ "vol": 80, "weight": 100, "position": ""})
  }

  public listagem(informacoes: any){
    let headers = new Headers();
    headers.append('X-Auth-Token', localStorage.getItem('token'));
    headers.append('Content-Type', 'application/json');
    this.http.post(this.url + 'join-packages', informações, { headers: headers })
    .subscribe((response) => {
      var pacotes = response.json().response;
      var code = pacotes['code'];
      var data = pacotes['finalization_date'];
      this.lista = pacotes['deliveries']; //uma lista com cada elemento sendo um dicionario
    })

}
}
