import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { ListaDeEntregasPage } from './lista-de-entregas';

@NgModule({
  declarations: [
    ListaDeEntregasPage,
  ],
  imports: [
    IonicPageModule.forChild(ListaDeEntregasPage),
  ],
})
export class ListaDeEntregasPageModule {}
