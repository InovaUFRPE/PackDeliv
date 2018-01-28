import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, AlertController } from 'ionic-angular';
import { GoogleMaps, GoogleMap, GoogleMapsEvent, LatLng, CameraPosition, GoogleMapOptions } from '@ionic-native/google-maps';
import { Geolocation, PositionError } from '@ionic-native/geolocation';

/**
 * Generated class for the MapaEntregadorPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-mapa-entregador',
  templateUrl: 'mapa-entregador.html',
})
export class MapaEntregadorPage {

  constructor(
    public navCtrl: NavController,
    public navParams: NavParams,
    public geolocation: Geolocation,
    public googleMaps: GoogleMaps,
    private alertCtrl: AlertController
  ) {  }

  ionViewDidLoad() {
    this.updateCoords();
  }

  private updateCoords() {
    this.geolocation.getCurrentPosition().then((resp) => {
      let position: LatLng = new LatLng(resp.coords.latitude, resp.coords.longitude);
      this.loadMap(position);
    }).catch((error: PositionError) => {
      this.showAlert('Erro', 'Erro ao pegar coordenadas: ' + error.message);
    });
  }

  private loadMap(coords: LatLng) {
    let element: HTMLElement = document.getElementById('map');
    let config: GoogleMapOptions = {
      controls: {
        myLocationButton: true,
        zoom: true
      }
    };

    let map: GoogleMap = this.googleMaps.create(element, config);

    map.one(GoogleMapsEvent.MAP_READY).then(() => {
      let curPos: LatLng = new LatLng(coords.lat, coords.lng);

      let position: CameraPosition<LatLng> = {
        target: curPos,
        zoom: 15,
        tilt: 30
      };

      map.addMarker({
        title: 'Você',
        icon: 'red',
        animation: 'DROP',
        position: {
          lat: curPos.lat,
          lng: curPos.lng
        }
      }).then(marker => {
        marker.on(GoogleMapsEvent.MARKER_CLICK).subscribe(() => {
          this.showAlert('Clicou', 'Você clicou no marcador');
        });
      });

      map.moveCamera(position);
    });
  }

  private showAlert(title: string, message: string) {
    let alert = this.alertCtrl.create({
      title: title,
      subTitle: message,
      buttons: ['OK']
    });
    alert.present();
  }

}
