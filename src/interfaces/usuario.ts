export interface Credenciais {
    login: string,
    password: string
}

export interface Veiculo {
    license_plate: string,
    year: string,
    model: string,
    color: string,
    ready: boolean,
    volume: number,
    id?: number,
    id_deliveryman: number
}

export interface Entregador extends Empresa {
    vehicle?: Veiculo,
    name_deliveryman: string,
    status: boolean,
    lat: number,
    long: number,
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
    id_client?: number,
    street: string,
    number: string,
    complement: string,
    district: string,
    postal_code: string,
    city: string,
    state: string,
    country: string,
    type: string,
    lat: number,
    long: number
}

export interface Cliente {
    id?: number,
    upi: string,
    name: string,
    addresses: [Endereco]
}