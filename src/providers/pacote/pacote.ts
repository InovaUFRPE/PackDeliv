import { Injectable } from '@angular/core';
import { Http, Headers, RequestOptionsArgs, Response } from '@angular/http';
import { Pacote } from "../../interfaces/ordem-de-servico";
import 'rxjs/add/operator/map';

/*
  Generated class for the PacoteProvider provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
@Injectable()
export class PacoteProvider {

  private url: string = 'http://localhost:5000/';

  constructor(public http: Http) {
    console.log('Hello PacoteProvider Provider');
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

  public emitirOrdemDeServico(volume: number) {
    let body = {
      vol: volume*1000,
      position: null
    };

    this.http.post(this.url+'join-packages', body, this.getRequestOptionsArgs())
    .map((response: Response) => response.json())
    .subscribe(response => {
      return response.response;
    }, error => {
      console.log('Erro ao combinar pacotes: ' + error);
    });
  }

  public cadastrarPacote(pacote: Pacote, callback: any) {
    this.http.post(this.url + "package/", pacote, this.getRequestOptionsArgs())
    .map((response: Response) => response.json())
      .subscribe((res) => {
        alert('Pacote cadastrado!');
        callback();
      }, (error) => {
        console.log('Erro ao cadastrar pacote: ' + error);
      });
  }
}
