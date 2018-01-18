export interface Credenciais {
    login: string,
    password: string
}

export interface Veiculo {
    license_plate: string,
    year: number,
    model: string,
    color: string,
    ready: boolean,
    volume: number,
    id?: number
}

export interface Entregador extends Empresa {
    vehicle?: Veiculo,
    name_deliveryman: string,
    id_vehicle?: number,
    status: boolean,
    lat?: number,
    long?: number,
    ready: boolean,
    dui: string,
    type?: string
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
    country: string,
    type: string,
    lat?: number,
    long?: number
}