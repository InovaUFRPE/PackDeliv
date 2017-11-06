import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { CadastroEntregadorPage } from './cadastro-entregador';

@NgModule({
  declarations: [
    CadastroEntregadorPage,
  ],
  imports: [
    IonicPageModule.forChild(CadastroEntregadorPage),
  ],
})
export class CadastroEntregadorPageModule {}
