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
  
  private user: any

  constructor(public http: Http,public status: boolean = false) {
    console.log('Hello SessionProvider Provider');  
  }

  getStatus():boolean{
    return this.status
  }

  setStatus():void{
    if (this.status == true){
      this.status = false
    }else {
      this.status = true
    }
  }
 
  getUser():any{
    return this.user
  }

  openSession(credentials: any):void{
    this.user = credentials
    this.setStatus()
  }
  
  closeSession():void{
    this.setStatus()
    this.user = null
  }

}
