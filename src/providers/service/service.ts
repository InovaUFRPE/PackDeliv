import { Injectable } from '@angular/core';
import { Http, Headers, Response, RequestOptionsArgs } from '@angular/http';
import 'rxjs/add/operator/map';
import { OrdemDeServico } from '../../interfaces/ordem-de-servico'

/*
  Generated class for the ServiceProvider provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
@Injectable()
export class ServiceProvider {

  private url: string = 'http://localhost:8080/';

  constructor(public http: Http) {
    console.log('Hello ServiceProvider Provider');
  }

  /**
   * getRequestOptions configura as opções das requisições.
   */
  private getRequestOptionsArgs(): RequestOptionsArgs {
    let headers = new Headers();
    headers.append('Content-Type', 'application/json');
    headers.append('X-Auth-Token', localStorage.getItem('token'));

    let options = { headers: headers };

    return options;
  }

  public listagem(informacoes: any, callback: any){
    this.http.post(this.url + 'join-packages', informacoes, this.getRequestOptionsArgs())
    .map((response: Response) => response.json())
    .subscribe((response) => {
      console.log(response);
      let ordemDeServico: OrdemDeServico = {
        code: response['code'],
        shipping_date: response['start_date'],
        finalization_date: response['finalization_date'],
        status: 'pendente',
        packages: response['deliveries']
      };
      
      callback(ordemDeServico);
      //uma lista com cada elemento sendo um dicionario
    }, error => console.log('Erro ao listar ordem de serviço: ' + error));
  }

}
