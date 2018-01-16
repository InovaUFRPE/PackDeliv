export interface Credenciais {
    Login: string,
    Password: string
}

export interface Veiculo {
    Placa: string,
    Ano: number,
    Modelo: string
}

export interface Entregador {
    Veiculo: Veiculo,
    Nome: string,
    CNH: string,
    Login: string,
    CNPJ: string,
    Senha: string,
    Email: string,
    id?: number,
    Id_veiculo?: number,
    status: string
}

export interface Empresa {
    id?: number,
    Id_Endereco?: number,
    Nome: string,
    Senha: string,
    Login: string,
    Email: string,
    CNPJ: string,
    Endereco: Endereco
}

export interface Endereco {
    Id?: string,
    Logradouro: string,
    Numero: string,
    Complemento: string,
    Bairro: string,
    CEP: string,
    Cidade: string,
    Estado: string,
    Pais: string
}