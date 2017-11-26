import { Component } from '@angular/core';
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
      let element: HTMLElement = document.getElementById('map');

      let map: GoogleMap = GoogleMaps.create(element);

      // listen to MAP_READY event
      // You must wait for this event to fire before adding something to the map or modifying it in anyway
      map.one(GoogleMapsEvent.MAP_READY).then(() => console.log('Map is ready!'))
        .catch((error) => console.log('Erro ao criar mapa: ' + error));

      // create LatLng object
      let ionic: LatLng = new LatLng(resp.coords.latitude, resp.coords.longitude);

      // create CameraPosition
      let position: CameraPosition<LatLng> = {
        target: ionic,
        zoom: 18,
        tilt: 30
      };

      // move the map's camera to position
      map.moveCamera(position);

      // create new marker
      let markerOptions: MarkerOptions = {
        position: ionic,
        title: 'Ionic'
      };

      map.addMarker(markerOptions)
        .then((marker: Marker) => {
          marker.showInfoWindow();
        });
    }).catch((error) => {
      console.log('Erro ao pegar localização: '+error);
    });
  } 

}
