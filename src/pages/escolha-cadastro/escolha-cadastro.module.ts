import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { EscolhaCadastroPage } from './escolha-cadastro';

@NgModule({
  declarations: [
    EscolhaCadastroPage,
  ],
  imports: [
    IonicPageModule.forChild(EscolhaCadastroPage),
  ],
})
export class EscolhaCadastroPageModule {}
