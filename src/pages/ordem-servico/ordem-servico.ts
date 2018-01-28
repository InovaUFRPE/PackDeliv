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
  public ativo: boolean = SessionProvider.getUser().status;

  constructor(
    public usuarioProvider: UsuarioProvider,
    public navCtrl: NavController,
    public navParams: NavParams,
    public modalCtrl: ModalController,
    private alertCtrl: AlertController
  ) {  }

  private gerarOrdemDeServico(){
    this.criarModal();
    SessionProvider.getUser().ready=true;
    this.usuarioProvider.atualizarStatusEntregador(SessionProvider.getUser());
  }

  private criarModal() {
    const modal: Modal = this.modalCtrl.create(ModalOrdemServicoPage, {}, {enableBackdropDismiss: false});
    modal.present();
    modal.onDidDismiss( data => {
      console.log(data);
      if (data.os.lista.lenght != 0) {
          this.ordemServico = data.os;
          console.log('ordem de serviço:');
          console.log(this.ordemServico);
      }
    });
  }

  public confirmarEntrega(ordemServico) {
    this.ordemServico = {lista: [], cod: 0, data: ''};
    SessionProvider.getUser().status = false;
    this.presentAlert('Bom trabalho! Continue assim!');
  }

  private presentAlert(message: string): void {
    let alert = this.alertCtrl.create({
      title: 'Alerta',
      subTitle: message,
      buttons: ['Ok']
    });

    alert.present();
  }

  ionViewDidEnter() {
    this.ativo = SessionProvider.getUser().status;
  }

}
