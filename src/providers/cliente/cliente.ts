import { Injectable } from '@angular/core';
import { Http, Response, RequestOptionsArgs, Headers } from '@angular/http';
import 'rxjs/add/operator/map';
import { Observable } from 'rxjs/Observable';
import { Cliente } from '../../interfaces/usuario';

/*
  Generated class for the ClienteProvider provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
@Injectable()
export class ClienteProvider {

  public url: string = 'http://localhost:5000/';

  constructor(public http: Http) {
    console.log('Hello ClienteProvider Provider');
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

  /**
   * cadastrarCliente é o método responsável por cadastrar clientes.
   */
  public cadastrarCliente(cliente: Cliente): Observable<any> {
    return this.http.post(this.url + 'client/', cliente, this.getRequestOptionsArgs())
    .map((response: Response) => response.json());
  }

  /**
   * pegarCliente
   */
  public pegarCliente(idCliente: number) {
    return this.http.get(this.url + 'client/' + idCliente, this.getRequestOptionsArgs())
    .map((response: Response) => response.json());
  }

}
