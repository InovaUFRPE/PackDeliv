import { BrowserModule } from '@angular/platform-browser';
import { ErrorHandler, NgModule } from '@angular/core';
import { IonicApp, IonicErrorHandler, IonicModule } from 'ionic-angular';
import { SplashScreen } from '@ionic-native/splash-screen';
import { StatusBar } from '@ionic-native/status-bar';

import { MyApp } from './app.component';
import { HomePage } from '../pages/home/home';
import { LoginPage } from "../pages/login/login";
import { CadastroPage } from "../pages/cadastro/cadastro";
import { EscolhaCadastroPage } from "../pages/escolha-cadastro/escolha-cadastro";
import { UsuarioProvider } from '../providers/usuario/usuario';
import { CadastroEntregadorPage } from "../pages/cadastro-entregador/cadastro-entregador";
import { CadastroVeiculoPage } from "../pages/cadastro-veiculo/cadastro-veiculo";
<<<<<<< HEAD

import { HttpModule } from '@angular/http';
import { RemoteProvider } from '../providers/remote/remote';
=======
import { ListaDeEntregasPage } from "../pages/lista-de-entregas/lista-de-entregas";
import { MonitorarEntregasPage } from "../pages/monitorar-entregas/monitorar-entregas";
import { PerfilPage } from "../pages/perfil/perfil";
import { SolicitarEntregasPage } from "../pages/solicitar-entregas/solicitar-entregas";
>>>>>>> 2e819f6e6d87c0ecc3469aa5d467dacfe3d03526

@NgModule({
  declarations: [
    MyApp,
    HomePage,
    LoginPage,
    CadastroPage,
    EscolhaCadastroPage,
    CadastroEntregadorPage,
    CadastroVeiculoPage,
    ListaDeEntregasPage,
    MonitorarEntregasPage,
    PerfilPage,
    SolicitarEntregasPage
  ],
  imports: [
    BrowserModule,
    IonicModule.forRoot(MyApp),
    HttpModule
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    HomePage,
    LoginPage,
    CadastroPage,
    EscolhaCadastroPage,
    CadastroEntregadorPage,
    CadastroVeiculoPage,
    ListaDeEntregasPage,
    MonitorarEntregasPage,
    PerfilPage,
    SolicitarEntregasPage
  ],
  providers: [
    StatusBar,
    SplashScreen,
    {provide: ErrorHandler, useClass: IonicErrorHandler},
    UsuarioProvider,
    RemoteProvider
  ]
})
export class AppModule {}
