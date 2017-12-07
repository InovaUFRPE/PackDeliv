import { Injectable } from '@angular/core';
import { Http, Headers } from '@angular/http';
import { Empresa } from "../../interfaces/empresa";
import { Entregador } from '../../interfaces/entregador';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/do';

/*
  Generated class for the UsuarioProvider provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
@Injectable()
export class UsuarioProvider {

  private url: string = 'http://localhost:5000/';

  public static EMPRESA = true;
  public static ENTREGADOR = false;

  constructor(public http: Http) {
  }

  /**
   * Return an object finalUser according to his credentials.
   * 
   * Made by: Matheus Campos da Silva, 13/11/2017
   * @param credentials 
   * An object that contains the user login and password.
   */
  public logar(credentials: any, callback) {
    let headers = new Headers();
    headers.append('X-Auth-Token', localStorage.getItem('token'));
    headers.append('Content-Type', 'application/json');
    
    // Implements request to API
    this.http.post(this.url + 'login', credentials, { headers: headers })
    .subscribe((response) => {
      // Treat response
      var user = response.json().response;
      if (user !== undefined){
        callback(true);
      } else {
        callback(false);
      }
    }, (error) => {
      throw error;
    });
  }

  public validarCNPJ(usuario: any, tipo: boolean, success: any) {
    let cnpj: string = usuario.CNPJ
      .split('.')
      .join('')
      .replace('/','')
      .replace('-','');

    this.http.get(this.url+'cnpj/'+cnpj)
    .subscribe((response) => {
        var resp = response.json();
        usuario['Endereco'] = {};
        
        if (resp.status !== "ERROR"){
          usuario['id'] = "";
          usuario['Id_endereco'] = "";
          usuario['Nome_fantasia'] = resp.fantasia;
          usuario['Endereco']['Logradouro'] = resp.logradouro;
          usuario['Endereco']['Numero'] = resp.numero;
          usuario['Endereco']['Complemento'] = resp.complemento;
          usuario['Endereco']['Bairro'] = resp.bairro;
          usuario['Endereco']['CEP'] = resp.cep;
          usuario['Endereco']['Cidade'] = resp.municipio;
          usuario['Endereco']['Estado'] = resp.uf;
          usuario['Endereco']['Pais'] = "";

          if (tipo) {
            this.inserirEmpresa(usuario, success);
          } else {
            this.cadastrarEntregador(usuario, success);
          }
        }
        else{
          alert(response.json().message);
        }
      }, (error) => {
      throw error;
      });
    }

  //Cadastra a empresa
  public inserirEmpresa(empresa: Empresa, success: any) {
    let headers = new Headers();
    headers.append('X-Auth-Token', localStorage.getItem('token'));
    headers.append('Content-Type', 'application/json');

    this.http.post(this.url + 'company', empresa, { headers: headers })
      .subscribe((res) => {
        alert('Usuário cadastrado!');
        success();
      }, (error) => {
        throw error;
      });
  }

  //Cadastra o entregador
  public cadastrarEntregador(entregador: Entregador, success: any){
    let headers = new Headers();
    headers.append('X-Auth-Token', localStorage.getItem('token'));
    headers.append('Content-Type', 'application/json');

    this.http.post(this.url+'deliveryman', entregador,{headers: headers})
    .subscribe( (res) => {
      alert('Entregador cadastrado!');
      success();
    }, (error) => {
      throw error;
    });
  }
}
