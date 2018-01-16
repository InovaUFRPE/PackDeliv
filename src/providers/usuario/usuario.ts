import { Empresa, Entregador, Veiculo, Endereco, Credenciais } from './../../interfaces/usuario';
import { Injectable } from '@angular/core';
import { Http, Headers, RequestOptionsArgs, Response } from '@angular/http';
import { Pacote } from '../../interfaces/pacote'
import { ListaDeEntregasPage } from '../../pages/lista-de-entregas/lista-de-entregas';
import { Observable } from 'rxjs/Observable';

@Injectable()
export class UsuarioProvider {

  private url: string = 'http://localhost:5000/';

  constructor (public http: Http) {  }

  /**
   * getRequestOptions configura as opções das requisições.
   */
  private getRequestOptionsArgs(): RequestOptionsArgs {
    let headers = new Headers();
    headers.append('Content-Type', 'application/json');
    headers.append('X-Auth-Token', localStorage.getItem('token'));

    let options = {headers: headers};

    return options;
  }


  public fazerLogin(credenciais: Credenciais): Observable<any> {
    return this.http.post(this.url + 'login/', credenciais, this.getRequestOptionsArgs())
    .map((response: Response) => response.json());
  }

  
  public validarCNPJ(cnpj: string, callback: any): void {
    var resposta = {endereco: undefined, nome: undefined, cnpj: undefined};

    this.http.get(this.url + 'cnpj/' + cnpj)
    .map((response: Response) => response.json())
    .subscribe( response => {
      if (!response.error) {
        let ender: Endereco = {
          Logradouro: response.logradouro,
          Numero: response.numero,
          Complemento: response.complemento,
          Bairro: response.bairro,
          CEP: response.cep,
          Cidade: response.municipio,
          Estado: response.uf,
          Pais: 'BRASIL'
        };

        resposta.endereco = ender;
        resposta.nome = response.nome;
        resposta.cnpj = cnpj;

        callback(resposta);
      }
    }, error => {
      console.log('Erro na validação de CNPJ: ' + error);
      callback(false);
    });
  }

  public cadastrarEmpresa(empresa: Empresa): Observable<any> {
    return this.http.post(this.url + 'company/', empresa, this.getRequestOptionsArgs())
      .map((response: Response) => response.json());
  }


  public cadastrarEntregador(entregador: Entregador): Observable<any> {
    return this.http.post(this.url+'deliveryman/', entregador, this.getRequestOptionsArgs())
    .map((response: Response) => response.json());
  }


  public cadastrarPacote(pacote: Pacote, callback: any){
    this.http.post(this.url+"package", pacote, this.getRequestOptionsArgs())
    .subscribe( (res) => {
      alert('Pacote cadastrado!');
      callback();
    }, (error) => {
      throw error;
    });
  }

  public atualizarPerfilEmpresa(usuario:Empresa, callback: any){
    this.http.put(this.url+'company/', usuario, this.getRequestOptionsArgs())
    .subscribe( (res) => {
      alert('Perfil atualizado!');
      callback();
    }, (error) => {
      throw error;
    });
  }

  public pegarTodosPacotes(id:any){
    this.http.get(this.url+'getPackage/'+id)
    .subscribe((response) => {
        var resp = response.json();
        console.log(resp['response']);
        ListaDeEntregasPage.listaentregas = resp['response'];
    });

  }

}
