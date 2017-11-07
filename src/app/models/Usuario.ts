interface Cliente {
    nomeCompleto: string;
    nomeUsuario: String;
    cnh?: string;
    cnpj: string;
    email: string;
    senha?: string;
}

export class Usuario implements Cliente {
    
    public get nomeCompleto() : string {
        return this.nomeCompleto;
    }

    
    public get nomeUsuario() : string {
        return this.nomeUsuario;
    }

    
    public get cnh() : string {
        return this.cnh;
    }

    
    public get cnpj() : string {
        return this.cnpj;
    }

    
    public get email() : string {
        return this.email;
    }

    
    public get senha() : string {
        return this.senha;
    }
}