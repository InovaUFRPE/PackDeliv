import { Endereco } from "./endereco";

interface Veiculo {
    Placa: string,
    Ano: number,
    Modelo: string
}

export interface Entregador {
    Veiculo: Veiculo,
    Nome_fantasia: string,
    CNH: string,
    Login: string,
    CNPJ: string,
    Senha: string,
    Email: string,
    id?: number,
    Id_veiculo?: number
}