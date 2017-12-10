import { EmailComposer } from '@ionic-native/email-composer';
import { Empresa } from './../../interfaces/empresa';
import { Endereco } from './../../interfaces/endereco';
import { Injectable } from '@angular/core';
import { Http, Headers } from '@angular/http';
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
  constructor(
    public http: Http
  ) {
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
    let empresa= new Empresa();
    let endereco = new Endereco();
    headers.append('X-Auth-Token', localStorage.getItem('token'));
    headers.append('Content-Type', 'application/json');
    // Implements request to API
    this.http.post(this.url + 'login', credentials, { headers: headers })
    .subscribe((response) => {
      // Treat response
      var user = response.json().response;
      console.log(user)
      var userEndereco = user.Endereco
      console.log(userEndereco)
      console.log(empresa)
      console.log(user.Senha)
      if (user !== undefined){
        //passando as informações de endereço para um objeto endereço
        endereco.Bairro = userEndereco.Bairro
        endereco.CEP = userEndereco.CEP
        endereco.Cidade = userEndereco.Cidade
        endereco.Complemento = userEndereco.Complemento
        endereco.Estado = userEndereco.Estado
        endereco.Logradouro = userEndereco.Logradouro
        endereco.Numero = userEndereco.Numero
        endereco.Pais = userEndereco.Pais
      
        if (user.CNH) {
          //não sei como funciona o 
          //callback(this.objetos.entregador);
        }
        else {
          //passando as informações do usuário para um Objeto empresa
          empresa.Id_Endereco = userEndereco.Id
          empresa.CNPJ = user.CNPJ
          empresa.Email = user.Email
          empresa.Endereco = endereco
          empresa.Login = user.Login
          empresa.Nome_fantasia = user.Nome_fantasia
          empresa.Senha = user.Senha
          callback(user);
        }
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
