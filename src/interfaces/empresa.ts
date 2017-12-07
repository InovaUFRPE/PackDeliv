interface Endereco {
    Logradouro: string,
    Numero: string,
    Complemento: string,
    Bairro: string,
    CEP: string,
    Cidade: string,
    Estado: string,
    Pais: string
}

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