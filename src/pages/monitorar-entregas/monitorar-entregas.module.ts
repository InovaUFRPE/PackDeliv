import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { MonitorarEntregasPage } from './monitorar-entregas';

@NgModule({
  declarations: [
    MonitorarEntregasPage,
  ],
  imports: [
    IonicPageModule.forChild(MonitorarEntregasPage),
  ],
})
export class MonitorarEntregasPageModule {}
