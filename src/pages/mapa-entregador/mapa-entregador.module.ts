import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { MapaEntregadorPage } from './mapa-entregador';

@NgModule({
  declarations: [
    MapaEntregadorPage,
  ],
  imports: [
    IonicPageModule.forChild(MapaEntregadorPage),
  ],
})
export class MapaEntregadorPageModule {}
