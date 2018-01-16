import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { HomePage } from '../home/home';
import { EditarPerfilPage } from '../editar-perfil/editar-perfil';
import { SessionProvider } from '../../providers/session/session';
import { Empresa } from '../../interfaces/usuario';


/**
 * Generated class for the PerfilPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-perfil',
  templateUrl: 'perfil.html',
})
export class PerfilPage {
  user =SessionProvider.getUser();
  
  
  constructor(public navCtrl: NavController, 
    public navParams: NavParams,
    public sessionProvider: SessionProvider) {
    console.log(this.user);
    
  }

  
  public login() {
    this.navCtrl.push(HomePage);
  }

  public irParaEditarPerfil() {
    this.navCtrl.push(EditarPerfilPage);
  } 

  

}
