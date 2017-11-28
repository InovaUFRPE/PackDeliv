import { Injectable } from '@angular/core';
import { Http, Headers } from '@angular/http';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/do';
import { List } from 'ionic-angular/components/list/list';

/*
  Generated class for the UsuarioProvider provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
@Injectable()
export class UsuarioProvider {

  private url: string = 'http://localhost:5000/';

  constructor(public http: Http) {
  }

  /**
   * Return an object finalUser according to his credentials.
   * 
   * Made by: Matheus Campos da Silva, 13/11/2017
   * @param credentials 
   * An object that contains the user login and password.
   */
  public getUsuario(credentials: any, callback) {
    var finalUser: object = null;
    
    // Implements request to API
    this.http.get(this.url+'getAllUsers')
    .subscribe((response) => {
      // Treat response
      let users = response.json().response;
      let array = [];
      for (var u in users) {
        array.push(users[u]);
      }
      array.forEach(user => {
        if (user.Login == credentials.username && user.Senha == credentials.password) {
          finalUser = {
            username: user.Login,
            password: user.Senha,
            email: user.Email,
            cnpj: user.cnpj
          };
        }
      });
      callback(finalUser);      
    }, (error) => {
      throw error;
    });
  }

  public cadastrarEmpresa(usuario: any) {
    let cnpj: string = usuario.CNPJ
      .split('.')
      .join('')
      .replace('/','')
      .replace('-','');

    this.http.get(this.url+'cnpj/'+cnpj)
    .subscribe((response) => {
      var resp = response.json();
      usuario['Endereco']={};
      if (resp.status !== "ERROR"){
        usuario['id'] = ""
        usuario['Id_endereco'] = "";
        usuario['Nome_fantasia'] = resp.fantasia
        usuario['Endereco']['Logradouro'] = resp.logradouro
        usuario['Endereco']['Numero'] = resp.numero
        usuario['Endereco']['Complemento'] = resp.complemento
        usuario['Endereco']['Bairro'] = resp.bairro
        usuario['Endereco']['CEP'] = resp.cep
        usuario['Endereco']['Cidade'] = resp.municipio
        usuario['Endereco']['Estado'] = resp.uf
        usuario['Endereco']['Pais'] = ""
        console.log(usuario)
        this.inserirEmpresa(usuario);
      }
      else{
        alert(response.json().message);
      }
    }, (error) => {
      throw error;
    });
    }
//Cadastra a empresa
  public inserirEmpresa(empresa: any) {
    let headers = new Headers();
    headers.append('X-Auth-Token', localStorage.getItem('token'));
    this.http.post(this.url + 'company', empresa, { headers: headers })
      .subscribe((res) => {
        alert('Usuário cadastrado!');
      }, (error) => {
        throw error;
      });
  }

  public cadastrarentregador(entregador: any){
    let headers = new Headers();
    headers.append('X-Auth-Token', localStorage.getItem('token'));
    this.http.post(this.url+'entregador', entregador,{headers: headers})
    .subscribe( (res) => {
      alert('Entregador cadastrado!');
      alert('Cadastre o veículo!');
    }, (error) => {
      throw error;
    });
  }
}
