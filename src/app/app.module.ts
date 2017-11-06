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


@NgModule({
  declarations: [
    MyApp,
    HomePage,
    LoginPage,
    CadastroPage,
    EscolhaCadastroPage,
    CadastroEntregadorPage,
    CadastroVeiculoPage
  ],
  imports: [
    BrowserModule,
    IonicModule.forRoot(MyApp)
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    HomePage,
    LoginPage,
    CadastroPage,
    EscolhaCadastroPage,
    CadastroEntregadorPage,
    CadastroVeiculoPage
  ],
  providers: [
    StatusBar,
    SplashScreen,
    {provide: ErrorHandler, useClass: IonicErrorHandler},
    UsuarioProvider
  ]
})
export class AppModule {}
