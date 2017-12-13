import { Endereco } from "./endereco";

export class Pacote {
    id?:number
    width:number
    height:number
    length:number
    weight:number
    shipped:boolean
    received:boolean
    
    idAdress:number
    idDestiny:number
    inicialAdress:Endereco
    destinyAdress:Endereco
}