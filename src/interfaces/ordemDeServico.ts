export class OrdemDeServico {
    Id: string;
    codigo: string;
    dataExpedida: string;
    dataFinal: string;
    pacotes: any;

    constructor(id: number, codigo: string, dataExpedida: string, dataFinal: string, pacotes: any){
      this.dataExpedida = dataExpedida;
      this.dataFinal = dataFinal;
      this.pacotes = pacotes;
      this.codigo = codigo;
      this.Id = id;
    }
}
