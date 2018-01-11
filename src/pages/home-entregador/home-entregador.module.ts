import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { HomeEntregadorPage } from './home-entregador';

@NgModule({
  declarations: [
    HomeEntregadorPage,
  ],
  imports: [
    IonicPageModule.forChild(HomeEntregadorPage),
  ],
})
export class HomeEntregadorPageModule {}
