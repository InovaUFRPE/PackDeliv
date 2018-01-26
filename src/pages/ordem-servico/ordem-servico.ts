import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, ModalController, Modal ,AlertController} from 'ionic-angular';
import { SessionProvider } from '../../providers/session/session';
import { UsuarioProvider } from '../../providers/usuario/usuario';
import { ModalOrdemServicoPage } from "../modal-ordem-servico/modal-ordem-servico";



/**
 * Generated class for the OrdemServicoPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-ordem-servico',
  templateUrl: 'ordem-servico.html',
})
export class OrdemServicoPage {

  public ordemServico = {lista: [], cod: 0, data: ''};
  public ativo:boolean= SessionProvider.getUser().status;
  constructor(
    public usuarioProvider: UsuarioProvider,
    public navCtrl: NavController,
    public navParams: NavParams,
    public modalCtrl: ModalController,
    private alertCtrl: AlertController
  ) {  }

  public ionViewDidLoad() {
  }

  private verificarStatus(){
    this.ativo=SessionProvider.getUser().status;
    if (this.ativo==false){
      this.presentAlert('Por favor! Altere seu status na tela de configuração pra poder gerar uma ordem de serviço!!');
      return;

    }
    else{
      this.criarModal();
      SessionProvider.getUser().ready=true;
      this.usuarioProvider.atualizarStatusEntregador(SessionProvider.getUser());
      
    }
  }

  private criarModal() {
    const modal: Modal = this.modalCtrl.create(ModalOrdemServicoPage, {}, {enableBackdropDismiss: false});
    modal.present();
    modal.onDidDismiss( data => {
      this.ordemServico = data.os;
      console.log('ordemServico: ');
      console.log(this.ordemServico);
    });
  }
  private presentAlert(message: string): void {
    let alert = this.alertCtrl.create({
      title: 'Alerta',
      subTitle: message,
      buttons: ['Ok']
    });

    alert.present();
  }
  
}
