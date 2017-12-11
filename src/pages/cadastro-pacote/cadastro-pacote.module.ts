import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { CadastroPacotePage } from './cadastro-pacote';

@NgModule({
  declarations: [
    CadastroPacotePage,
  ],
  imports: [
    IonicPageModule.forChild(CadastroPacotePage),
  ],
})
export class CadastroPacotePageModule {}
