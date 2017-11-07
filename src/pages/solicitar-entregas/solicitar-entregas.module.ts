import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { SolicitarEntregasPage } from './solicitar-entregas';

@NgModule({
  declarations: [
    SolicitarEntregasPage,
  ],
  imports: [
    IonicPageModule.forChild(SolicitarEntregasPage),
  ],
})
export class SolicitarEntregasPageModule {}
