import { SessionProvider } from './../../providers/session/session';
import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { MonitorarEntregasPage } from "../monitorar-entregas/monitorar-entregas";
import { PerfilPage } from "../perfil/perfil";
import { CadastroPacotePage } from "../cadastro-pacote/cadastro-pacote"
import { ListaDeEntregasPage } from '../lista-de-entregas/lista-de-entregas';
import { PacoteProvider } from '../../providers/pacote/pacote';

/**
 * Generated class for the HomePage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-home',
  templateUrl: 'home.html',
})
export class HomePage {
  
  public rootPage = PerfilPage;

  constructor(
    public navCtrl: NavController, 
    public navParams: NavParams, 
    public pacoteProvider: PacoteProvider) {  }



  public abrirPerfil() {
    this.navCtrl.push(PerfilPage);
  }

  public abrirSolicitarEntregas() {
    this.navCtrl.push(CadastroPacotePage);
  }

  public abrirMonitorarEntregas() {
    this.navCtrl.push(MonitorarEntregasPage);
  }

  public listarEntregas() {
    this.navCtrl.push(ListaDeEntregasPage);
  }

  sair(){
    SessionProvider.closeSession();
    this.navCtrl.popToRoot();
  }
}
