import { SessionProvider } from './../../providers/session/session';
import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { MonitorarEntregasPage } from "../monitorar-entregas/monitorar-entregas";
import { PerfilPage } from "../perfil/perfil";
import { SolicitarEntregasPage } from "../solicitar-entregas/solicitar-entregas";
import { CadastroPacotePage } from "../cadastro-pacote/cadastro-pacote"

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
  rootPage = PerfilPage
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
<<<<<<< HEAD
    this.navCtrl.push(CadastroPacotePage);
=======
    this.navCtrl.push(SolicitarEntregasPage,{session: this.sessionProvider});
>>>>>>> 615f8f9a23c100bbdff4b26996a7f1235e4f2bf4
  }
  abrirMonitorarEntregas(){
    this.navCtrl.push(MonitorarEntregasPage,{session: this.sessionProvider});
  }
  sair(){
    this.session.closeSession();
    this.navCtrl.popToRoot();
  }
}
