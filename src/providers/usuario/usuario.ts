import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
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

  constructor(public http: Http) {
  }

  /**
   * Retorna um objeto usuário de acordo com suas credenciais.
   * 
   * Feito por: Matheus Campos da Silva, 02/11/2017
   * @param credenciais 
   * Um objeto contendo o login e a senha do usuário.
   */
  public getUsuario(credenciais: any) {
    var usuario;

    // Implementa a requisição à API
    this.http.get(this.url+'/usuarios', {
      body: {
        username: credenciais.nomeUsuario,
        passwd: credenciais.senha
      }
    }).subscribe((response) => {
      // Em caso de sucesso, retorna o JSON para o objeto usuario
      usuario = response.json();
      return usuario;
    }, (error) => {
      // Em caso de erro, jogue o erro
      throw error;
    });

    return usuario;
  }

  /**
   * Cadastrar um usuário na base de dados do sistema.
   * 
   * Feito por: Matheus Campos da Silva, 02/11/2017
   * @param usuario 
   * Um objeto contendo todos os dados do usuário.
   */
  public cadastrar(usuario: object) {
    this.http.post(this.url, usuario)
    .do(res => alert(res));
  }

}
