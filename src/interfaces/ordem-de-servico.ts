export interface OrdemDeServico {
    id?: number,
    code: number,
    shipping_date: string,
    finalization_date: string,
    status: string,
    packages: Array<Pacote>
}

export interface Pacote {
    id?: number,
    width: number,
    height: number,
    length: number,
    weight: number,
    shipped: boolean,
    received: boolean,
    volume: number,
    static_location: string,
    status: string,
    send_date?: string,
    delivery_date?: string,
    id_address_start: number,
    id_address_destiny: number,
    id_company: number,
    id_client: number,
    id_area?: number
}
