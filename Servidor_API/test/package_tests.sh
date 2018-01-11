### Insercao

curl -XPOST "http://127.0.0.1:5000/package/" -d '{"xalala": 1}'
# Vai retornar erro pois nao foi passado o header dizendo que esta sendo enviado um JSON
{
  "error": "Please provide a JSON"
}

curl -XPOST "http://127.0.0.1:5000/package/" -H 'Content-type: application/json' -d '{"xalala": 1}'
# Vai retornar erro pois nenhum dado do package foi passado para ser registrado
{
  "error": "Missing fields:['Largura', 'Altura', 'Comprimento', 'Peso', 'volume', 'Id_endereco_inicio', 'Id_endereco_destino']"
}

curl -XPOST "http://127.0.0.1:5000/package/" -H 'Content-type: application/json' \
  -d '{"Largura": 30, "Altura": 35, "Comprimento": 10, "Peso": 1, "volume": 1, "Id_endereco_inicio": 2, "Id_endereco_destino": 3, "Status": 10}'
# Vai retornar erro pois o status nao existe
{
  "error": "Invalid status, please use one of the options: [1, 2, 3, 4, 5, 6]"
}

curl -XPOST "http://127.0.0.1:5000/package/" -H 'Content-type: application/json' \
  -d '{"Largura": 30, "Altura": 35, "Comprimento": 10, "Peso": 1, "volume": 1, "Id_endereco_inicio": 2, "Id_endereco_destino": 3, "Status": 1}'
# Vai inserir e retornar o JSON do objeto apos ser atualizado com o que foi inserido no banco
{
  "id": 1
}

### Busca
curl -XGET "http://127.0.0.1:5000/package/123123"
# Vai retornar erro porque nao existe package com esse id
{
  "error": "No package found with id 123123"
}

curl -XGET "http://127.0.0.1:5000/package/1"
# Vai retornar o JSON o package
{
  "Altura": 35,
  "Comprimento": 10,
  "Expedido": false,
  "Id": 1,
  "Id_endereco_destino": 3,
  "Id_endereco_inicio": 2,
  "Largura": 30,
  "Local_atual_estatico": null,
  "Peso": 1,
  "Recebido": false,
  "Status": 1,
  "volume": 1
}

### Edicao

curl -XPUT "http://127.0.0.1:5000/package/1" -H 'Content-type: application/json' \
  -d '{"Status": 10}'
# Vai retornar erro pois o status esta invalido
{
  "error": "Invalid status, please use one of the options: [1, 2, 3, 4, 5, 6]"
}

curl -XPUT "http://127.0.0.1:5000/package/1" -H 'Content-type: application/json' \
  -d '{"Status": 2}'
# Vai retornar o package editado
{
  "id": 1
}

curl -XPUT "http://127.0.0.1:5000/package/123123" -H 'Content-type: application/json' \
  -d '{"Status": 3}'
# Vai retornar erro porque o id nao existe
{
  "error": "Unable to update Package with id 123123"
}

### Remocao

curl -XDELETE "http://127.0.0.1:5000/package/123123"
# Vai retornar erro porque nao existe package com esse id
{
  "error": "No package found with id 123123"
}

curl -XDELETE "http://127.0.0.1:5000/package/1"
# Vai retornar sucesso, pois o id existe
{
  "id": 1
}
