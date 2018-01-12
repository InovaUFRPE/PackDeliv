import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs/add/operator/map';


/*
  Generated class for the SessionProvider provider.
  
  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
@Injectable()
export class SessionProvider {
  
  private static user: any
  public static status: boolean = false
  public static deliveryManStatus: string = "Inativo"
  constructor(public http: Http) {
    console.log('Hello Session Provider Provider');  
  }

  static getStatus():boolean{
    return this.status
  }

  static setStatus():void{
    if (this.status == true){
      this.status = false
    }else {
      this.status = true
    }
  }
 
  static getUser():any{
    return this.user
  }  

  static openSession(credentials: any):void{
    this.user = credentials
    this.setStatus()
  }
  
  static closeSession():void{
    this.setStatus()
    this.user = null
  }

  static getDeliveryManStatus(status: string){
    return this.deliveryManStatus
  }

  static setDeliveryAtivo():void{
    this.deliveryManStatus = "Ativo"
  }

  static setDeliveryManEmServico():void{
    this.deliveryManStatus = "Em serviço"
  }

  static setDeliveryManInativo():void{
    this.deliveryManStatus = "Inativo"
  }

}
