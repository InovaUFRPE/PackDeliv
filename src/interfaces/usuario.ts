export interface Credenciais {
    login: string,
    password: string
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
    id_adress?: number,
    name: string,
    password: string,
    login: string,
    email: string,
    uci: string,
    addresses: [Endereco]
}

export interface Endereco {
    id?: string,
    street: string,
    number: string,
    complement: string,
    district: string,
    postal_code: string,
    city: string,
    state: string,
    country: string
}