import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, ToastController } from 'ionic-angular';
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

  constructor(public navCtrl: NavController, public navParams: NavParams, private emailComposer: EmailComposer, private toastCtrl: ToastController) {
  }

  public sendEmail() {
    console.log(this.inputEmail)
    this.emailComposer.isAvailable().then((available: boolean) => {
      if (available) {
        let options: EmailComposerOptions = {
          to: this.inputEmail,
          body: 'Consegui pelo email composer porra!',
          isHtml: true,
          cc: 'silva.campos.matheus@gmail.com',
          subject: 'Email composer'
        };

        this.emailComposer.open(options);
      } else {
        this.presentToast('Email Composer não disponível');
      }
    }).catch((error) => {
      throw error;
    });
  }

  ionViewDidLoad() {
  }

  presentToast(message: string) {
    let toast = this.toastCtrl.create({
      position: 'bottom',
      duration: 3000,
      message: message,
      showCloseButton: true
    });

    toast.present();
  }

  public irParaLogin(): void {
    this.navCtrl.popToRoot();
  }

}
