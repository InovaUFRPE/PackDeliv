import { Injectable } from '@angular/core';
import { Http, Headers, Response, RequestOptionsArgs } from '@angular/http';
import 'rxjs/add/operator/map';
import { Endereco } from '../../interfaces/usuario';
import { Observable } from 'rxjs/Observable';

/*
  Generated class for the EnderecoProvider provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
@Injectable()
export class EnderecoProvider {

  private url: string = 'http://localhost:5000/';

  constructor(public http: Http) {
    console.log('Hello EnderecoProvider Provider');
  }

  /**
   * getRequestOptionsArgs
   */
  private getRequestOptionsArgs(): RequestOptionsArgs {
    let headers = new Headers();
    headers.append('Content-Type', 'application/json');
    headers.append('X-Auth-Token', localStorage.getItem('token'));

    let options: RequestOptionsArgs = { headers: headers };

    return options;
  }

  public cadastrarEndereco(endereco: Endereco): Observable<any> {
    return this.http.post(this.url + 'address/', endereco, this.getRequestOptionsArgs())
    .map((response: Response) => response.json());
  }

}
