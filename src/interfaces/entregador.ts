import { Endereco } from "./endereco";

export class Veiculo {
    Placa: string
    Ano: number
    Modelo: string
    constructor() {

    }
}

export class Entregador {
    Veiculo: Veiculo
    Nome_fantasia: string
    CNH: string
    Login: string
    CNPJ: string
    Senha: string
    Email: string
    id?: number
    Id_veiculo?: number
    status: boolean
    constructor(){

    }
}
