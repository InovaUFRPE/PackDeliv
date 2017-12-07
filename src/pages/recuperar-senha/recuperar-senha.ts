import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, ToastController, AlertController } from 'ionic-angular';
import { EmailComposer, EmailComposerOptions } from "@ionic-native/email-composer";

/**
 * Generated class for the RecuperarSenhaPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-recuperar-senha',
  templateUrl: 'recuperar-senha.html',
})
export class RecuperarSenhaPage {

  public inputEmail: string;

  constructor(public navCtrl: NavController, public navParams: NavParams, private emailComposer: EmailComposer, private toastCtrl: ToastController, public alertCtrl: AlertController) {
  }

  public checkEmailPermission() {
    this.emailComposer.hasPermission().then((permission) => {
      if (permission) {
        this.sendEmail();
      } else {
        this.emailComposer.requestPermission().then((hasPermission) => {
          if (hasPermission) {
            this.sendEmail();
          } else {
            this.showAlert('Permissão negada', 'Você deve dar permissão para envio de e-mails para poder recuperar sua senha.');
          }
        }).catch((error) => {
          this.showAlert('Erro', 'Erro ao solicitar permissão');
        });
      }
    }).catch((error) => {
      this.showAlert('Erro', 'Erro ao verificar permissão');
    });
  }

  public sendEmail() {
    this.presentToast(this.inputEmail);
    this.emailComposer.isAvailable().then((available: boolean) => {
      if (available) {
        let options: EmailComposerOptions = {
          to: this.inputEmail,
          body: 'Consegui pelo email composer porra!',
          isHtml: true,
          cc: 'silva.campos.matheus@gmail.com',
          subject: 'Email composer'
        };

        this.emailComposer.open(options).then((resp) => {
          this.presentToast('E-mail enviado');
        }).catch((error) => {
          this.presentToast('Erro ao enviar e-mail');
        });
      } else {
        this.presentToast('Email Composer não disponível');
      }
    }).catch((error) => {
      this.showAlert('Erro', 'Erro ao verificar serviço de e-mail');
    });
  }

  presentToast(message: string) {
    let toast = this.toastCtrl.create({
      position: 'bottom',
      duration: 3000,
      message: message
    });

    toast.present();
  }

  showAlert(title: string, message: string) {
    let alert = this.alertCtrl.create({
      title: title,
      subTitle: message,
      buttons: ['OK']
    });
    alert.present();
  }

  public irParaLogin(): void {
    this.navCtrl.popToRoot();
  }

}
