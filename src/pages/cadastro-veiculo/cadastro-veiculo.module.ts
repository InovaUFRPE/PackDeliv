import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { CadastroVeiculoPage } from './cadastro-veiculo';

@NgModule({
  declarations: [
    CadastroVeiculoPage,
  ],
  imports: [
    IonicPageModule.forChild(CadastroVeiculoPage),
  ],
})
export class CadastroVeiculoPageModule {}
