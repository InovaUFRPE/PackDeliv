import { SessionProvider } from './../../providers/session/session';
import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { MonitorarEntregasPage } from "../monitorar-entregas/monitorar-entregas";
import { PerfilPage } from "../perfil/perfil";
import { SolicitarEntregasPage } from "../solicitar-entregas/solicitar-entregas";
import { CadastroPacotePage } from "../cadastro-pacote/cadastro-pacote"
import { CadastroPacote2Page } from '../cadastro-pacote2/cadastro-pacote2';
import { ListaDeEntregasPage } from '../lista-de-entregas/lista-de-entregas';

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
  rootPage = ListaDeEntregasPage;
  constructor(public navCtrl: NavController, public navParams: NavParams,
    public sessionProvider: SessionProvider) {
  } 

  abrirPerfil(){
    this.navCtrl.push(PerfilPage);
  }
  abrirSolicitarEntregas(){
    this.navCtrl.push(CadastroPacotePage);
  }
  abrirMonitorarEntregas(){
    this.navCtrl.push(MonitorarEntregasPage);
  }
  sair(){
    SessionProvider.closeSession();
    this.navCtrl.popToRoot();
  }
}
