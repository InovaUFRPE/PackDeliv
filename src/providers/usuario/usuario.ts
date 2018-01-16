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

  /**
   * fazerLogin é o método responsável por fazer o login de empresa e de entregador.
   *
   * @param credenciais
   *  As credenciais do usuário (Login e Senha).
   */

  public login(credenciais: Credenciais): Observable<any> {
    return this.http.post(this.url + 'login/', credenciais, this.getRequestOptionsArgs())
    .map((response: Response) => response.json());
  }

  /** ------------ AJUDA A PARTIR DE AQUI -------------- */
  public validarCNPJ(cnpj: string, callback: any): void {
    cnpj = cnpj

    var resposta = {endereco: undefined, nome: undefined};

    this.http.get(this.url + 'cnpj/' + cnpj)
    .map((response: Response) => response.json())
    .subscribe( response => {
      if (!response.error) {
        let ender: Endereco = {
          street: response.logradouro,
          number: response.numero,
          complement: response.complemento,
          district: response.bairro,
          postal_code: response.cep,
          city: response.municipio,
          state: response.uf,
          country: 'BRASIL'
        };

        resposta.endereco = ender;
        resposta.nome = response.nome;
        callback(resposta);
      }
    }, error => {
      console.log('Erro na validação de CNPJ: ' + error);
    });
  }

  //Cadastra a empresa
  public cadastrarEmpresa(empresa: Empresa): Observable<any> {
    console.log(empresa);
    return this.http.post(this.url + 'company/', empresa, this.getRequestOptionsArgs())
      .map((response: Response) => response.json());
  }



  //Cadastra o entregador
  public cadastrarEntregador(entregador: Entregador, success: any){
    let headers = new Headers();
    headers.append('X-Auth-Token', localStorage.getItem('token'));
    headers.append('Content-Type', 'application/json');

    this.http.post(this.url+'deliveryman/', entregador,{headers: headers})
    .subscribe( (res) => {
      alert('Entregador cadastrado!');
      success();
    }, (error) => {
      throw error;
    });
  }
  //cadastrar pacote
  public cadastrarPacote(pacote: Pacote, success: any){
    let headers = new Headers();
    headers.append('X-Auth-Token', localStorage.getItem('token'));
    headers.append('Content-Type', 'application/json');

    this.http.post(this.url+"package", pacote,{headers: headers})
    .subscribe( (res) => {
      alert('Pacote cadastrado!');
      success();
    }, (error) => {
      throw error;
    });
  }

public atualizarPerfilEmpresa(usuario:Empresa,success:any){
  let headers = new Headers();
  headers.append('X-Auth-Token', localStorage.getItem('token'));
  headers.append('Content-Type', 'application/json');

  this.http.post(this.url+'edit_company', usuario,{headers: headers})
  .subscribe( (res) => {
    alert('Perfil atualizado!');
    success();
  }, (error) => {
    throw error;
  });
}

}
