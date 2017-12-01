import { Component, ViewChild } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { HomePage } from '../home/home';
import { Geolocation } from "@ionic-native/geolocation";
import { GoogleMaps, GoogleMap, GoogleMapOptions, GoogleMapsEvent, Marker, MarkerOptions, CameraPosition, LatLng } from "@ionic-native/google-maps";
import { EditarPerfilPage } from '../editar-perfil/editar-perfil';

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

  @ViewChild('mapCanvas') map: GoogleMap;

  constructor(public navCtrl: NavController, 
    public navParams: NavParams,
    private geolocation: Geolocation) {
  }

  ionViewDidLoad() {
    this.loadMap();
  }

  public login() {
    this.navCtrl.push(HomePage);
  }

  public irParaEditarPerfil() {
    this.navCtrl.push(EditarPerfilPage);
  }

  public loadMap() {
    this.geolocation.getCurrentPosition().then((resp) => {

      this.map.one(GoogleMapsEvent.MAP_READY).then(() => {
        console.log('Mapa tá pronto');
      }).catch(() => {
        console.log('Erro ao gerar o mapa');
      });

      // create LatLng object
      let ionic: LatLng = new LatLng(resp.coords.latitude, resp.coords.longitude);

      // create CameraPosition
      let position: CameraPosition<LatLng> = {
        target: ionic,
        zoom: 18,
        tilt: 30
      };

      // move the map's camera to position
      this.map.moveCamera(position);

      // create new marker
      let markerOptions: MarkerOptions = {
        position: ionic,
        title: 'Ionic'
      };

      this.map.addMarker(markerOptions)
        .then((marker: Marker) => {
          marker.showInfoWindow();
        });
    }).catch((error) => {
      console.log('Erro ao pegar localização: '+error);
    });
  } 

}
