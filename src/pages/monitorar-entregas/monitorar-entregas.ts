import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { GoogleMap, GoogleMaps, GoogleMapsEvent, LatLng, CameraPosition } from '@ionic-native/google-maps';
import { Geolocation } from "@ionic-native/geolocation";

/**
 * Generated class for the MonitorarEntregasPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-monitorar-entregas',
  templateUrl: 'monitorar-entregas.html',
})
export class MonitorarEntregasPage {

  map: GoogleMap;
  constructor(public navCtrl: NavController, public navParams: NavParams, private googleMaps: GoogleMaps, private geolocation: Geolocation) {
  }

  ngAfterViewInit() {
    this.updateCoords();
  }

  updateCoords() {
    this.geolocation.getCurrentPosition().then((resp) => {
      let position: LatLng = new LatLng(resp.coords.latitude, resp.coords.longitude);
      this.loadMap(position);
    }).catch((error) => {
      throw error;
    });
  }

  loadMap(coords: LatLng) {
    let element: HTMLElement = document.getElementById('map');
    let map: GoogleMap = this.googleMaps.create(element);

    map.one(GoogleMapsEvent.MAP_READY).then(() => {
      console.log('Map is ready!');

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
          alert('clicou');
        });
      });

      map.moveCamera(position);
    });
  }
}
