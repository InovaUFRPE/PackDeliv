import { Injectable } from '@angular/core';
import { Http, Headers } from '@angular/http';
import 'rxjs/add/operator/map';
import { OrdemDeServico } from '../../interfaces/ordemDeServico'

/*
  Generated class for the ServiceProvider provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
@Injectable()
export class ServiceProvider {

  private url: string = 'http://localhost:8080/';
  lista: any[];

  constructor(public http: Http) {
    console.log('Hello ServiceProvider Provider');
  }

  public listagem(informacoes: any, callback: any){
    let headers = new Headers();
    headers.append('X-Auth-Token', localStorage.getItem('token'));
    headers.append('Content-Type', 'application/json');

    this.http.post(this.url + 'join-packages', informacoes, { headers: headers })
    .subscribe((response) => {
      let json = response.json().response;
      let code = json['code'];
      let pacotes = json['deliveries'];
      let dataFinal = json['finalization_date'];
      let dataExpedida = json['start_date'];
      let id = json['id'];
      let ordemDeServico = new OrdemDeServico(id, code, dataExpedida, dataFinal, pacotes);
      callback(ordemDeServico);
      //uma lista com cada elemento sendo um dicionario
    });
}


}
