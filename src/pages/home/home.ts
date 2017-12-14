import { SessionProvider } from './../../providers/session/session';
import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { MonitorarEntregasPage } from "../monitorar-entregas/monitorar-entregas";
import { PerfilPage } from "../perfil/perfil";
import { SolicitarEntregasPage } from "../solicitar-entregas/solicitar-entregas";
import { CadastroPacotePage } from "../cadastro-pacote/cadastro-pacote"
import { CadastroPacote2Page } from '../cadastro-pacote2/cadastro-pacote2';

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
  rootPage = MonitorarEntregasPage;
  session = this.navParams.get('session')
  constructor(public navCtrl: NavController, public navParams: NavParams,
    public sessionProvider: SessionProvider) {
  } 

  
  ionViewDidLoad() {
    console.log('ionViewDidLoad HomePage');
    console.log(this.session)
  }
  abrirPerfil(){
    this.navCtrl.push(PerfilPage,{session: this.sessionProvider});
  }
  abrirSolicitarEntregas(){
    this.navCtrl.push(CadastroPacotePage,{session: this.sessionProvider});
  }
  abrirMonitorarEntregas(){
    this.navCtrl.push(MonitorarEntregasPage,{session: this.sessionProvider});
  }
  sair(){
    this.session.closeSession();
    this.navCtrl.popToRoot();
  }
}
