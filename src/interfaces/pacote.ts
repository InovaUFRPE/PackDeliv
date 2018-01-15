import { Endereco } from "./usuario";

export class Pacote {
    id?:number
    Largura:number
    Altura:number
    Comprimento:number
    Peso:number
    Expedido:boolean
    Recebido:boolean
    
    Id_endereco_inicio:number
    Id_endereco_final:number
    Endereco_Inicio:Endereco
    Endereco_Destino:Endereco
    constructor(){
        
    }
}