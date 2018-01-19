import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { ModalOrdemServicoPage } from './modal-ordem-servico';

@NgModule({
  declarations: [
    ModalOrdemServicoPage,
  ],
  imports: [
    IonicPageModule.forChild(ModalOrdemServicoPage),
  ],
})
export class ModalOrdemServicoPageModule {}
