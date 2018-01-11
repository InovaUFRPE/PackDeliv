### Insercao

curl -XPOST "http://127.0.0.1:5000/delivery/" -d '{"xalala": 1}'
# Vai retornar erro pois nao foi passado o header dizendo que esta sendo enviado um JSON
{
  "error": "Please provide a JSON"
}

curl -XPOST "http://127.0.0.1:5000/delivery/" -H 'Content-type: application/json' -d '{"xalala": 1}'
# Vai retornar erro pois nenhum dado do delivery foi passado para ser registrado
{
  "error": "Missing fields:['Status', 'Tipo']"
}

curl -XPOST "http://127.0.0.1:5000/delivery/" -H 'Content-type: application/json' \
  -d '{"Status": 20, "Tipo": 1, "codigo": "ab95", "Data_expedicao": "2017-03-03 15:20:00", "Data_finalizacao": "2017-03-04 17:20:00", "Id_ordem_de_servico": 1, "Id_pacote": 1}'
# Vai retornar erro pois o status nao existe
{
  "error": "Invalid status, please use one of the options: [1, 2, 3, 4, 5, 6]"
}

curl -XPOST "http://127.0.0.1:5000/delivery/" -H 'Content-type: application/json' \
  -d '{"Status": 2, "Tipo": 1, "codigo": "ab95", "Data_expedicao": "2017-03-03 15:20:00", "Data_finalizacao": "2017-03-04 17:20:00", "Id_ordem_de_servico": 1, "Id_pacote": 1}'
# Vai inserir e retornar o JSON do objeto apos ser atualizado com o que foi inserido no banco
{
  "id": 1
}

### Busca
curl -XGET "http://127.0.0.1:5000/delivery/123123"
# Vai retornar erro porque nao existe delivery com esse id
{
  "error": "No delivery found with id 123123"
}

curl -XGET "http://127.0.0.1:5000/delivery/1"
# Vai retornar o JSON o delivery
{
  "Data_expedicao": "Fri, 03 Mar 2017 15:20:00 GMT",
  "Data_finalizacao": "Sat, 04 Mar 2017 17:20:00 GMT",
  "Id": 1,
  "Id_ordem_de_servico": 1,
  "Id_pacote": 1,
  "Status": 2,
  "Tipo": 1,
  "codigo": "ab95"
}

### Edicao

curl -XPUT "http://127.0.0.1:5000/delivery/1" -H 'Content-type: application/json' \
  -d '{"Status": 10}'
# Vai retornar erro pois o status esta invalido
{
  "error": "Invalid status, please use one of the options: [1, 2, 3, 4, 5, 6]"
}

curl -XPUT "http://127.0.0.1:5000/delivery/1" -H 'Content-type: application/json' \
  -d '{"Status": 5}'
# Vai retornar o delivery editado
{
  "id": 1
}

curl -XPUT "http://127.0.0.1:5000/delivery/123123" -H 'Content-type: application/json' \
  -d '{"Status": 3}'
# Vai retornar erro porque o id nao existe
{
  "error": "Unable to update Delivery with id 123123"
}

### Remocao

curl -XDELETE "http://127.0.0.1:5000/delivery/123123"
# Vai retornar erro porque nao existe delivery com esse id
{
  "error": "No delivery found with id 123123"
}

curl -XDELETE "http://127.0.0.1:5000/delivery/1"
# Vai retornar sucesso, pois o id existe
{
  "id": 1
}
