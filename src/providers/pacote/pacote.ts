import { Injectable } from '@angular/core';
import { Http, Headers } from '@angular/http';
import { Position } from '../../interfaces/position';
import 'rxjs/add/operator/map';

/*
  Generated class for the PacoteProvider provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
@Injectable()
export class PacoteProvider {

  private url: string = 'http://localhost:5000/'
  constructor(public http: Http) {
    console.log('Hello PacoteProvider Provider');
  }

  public emitirOrdemDeServico(volume: number, position: Position) {
    let headers = new Headers();
    headers.append('Content-Type', 'application/json');
    headers.append('X-Auth-Token', localStorage.getItem('token'));
    
    let body = {
      vol: volume*1000,
      position: null
    };

    this.http.post(this.url+'join-packages', body, { headers: headers })
    .subscribe(response => {
      var ordem_de_servico = response.json().response
      return ordem_de_servico
    }, error => {
      console.log(error);
    });
  }
}
