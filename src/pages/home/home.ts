import { SessionProvider } from './../../providers/session/session';
import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { MonitorarEntregasPage } from "../monitorar-entregas/monitorar-entregas";
import { PerfilPage } from "../perfil/perfil";
import { CadastroPacotePage } from "../cadastro-pacote/cadastro-pacote"
import { ListaDeEntregasPage } from '../lista-de-entregas/lista-de-entregas';
import { PacoteProvider } from '../../providers/pacote/pacote';
import { Geolocation } from '@ionic-native/geolocation';
import { Position } from '../../interfaces/position';

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
  rootPage = PerfilPage;
  constructor(public navCtrl: NavController, public navParams: NavParams, public pacoteProvider: PacoteProvider, public geolocation: Geolocation) {
  }



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

  public emitirOrdemDeServico() {
    var volume: number = SessionProvider.getUser().car.volume;

    this.geolocation.getCurrentPosition().then((resp) => {
      let position: Position;
      position.lat = resp.coords.latitude;
      position.lng = resp.coords.longitude;

      return this.pacoteProvider.emitirOrdemDeServico(volume, position);

    }).catch(error => {
      throw error;
    });
  }
  sair(){
    SessionProvider.closeSession();
    this.navCtrl.popToRoot();
  }
}
