import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { DadosRastreioPage } from './dados-rastreio';

@NgModule({
  declarations: [
    DadosRastreioPage,
  ],
  imports: [
    IonicPageModule.forChild(DadosRastreioPage),
  ],
})
export class DadosRastreioPageModule {}
