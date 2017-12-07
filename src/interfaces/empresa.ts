import { Endereco } from "./endereco";

export interface Empresa {
    id?: number,
    Id_Endereco?: number, 
    Nome_fantasia: string,
    Senha: string,
    Login: string,
    Email: string,
    CNPJ: string,
    Endereco: Endereco
}