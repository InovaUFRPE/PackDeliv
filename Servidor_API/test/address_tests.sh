### Insercao

curl -XPOST "http://127.0.0.1:5000/address/" -d '{"xalala": 1}'
# Vai retornar erro pois nao foi passado o header dizendo que esta sendo enviado um JSON
{
  "error": "Please provide a JSON"
}

curl -XPOST "http://127.0.0.1:5000/address/" -H 'Content-type: application/json' -d '{"xalala": 1}'
# Vai retornar erro pois nenhum dado do address foi passado para ser registrado
{
  "error": "Missing fields:['Logradouro', 'Numero', 'Bairro', 'CEP', 'Cidade', 'Estado', 'Pais', 'Lat', 'Long', 'Empresa_Id', 'Cliente_Id']"
}

curl -XPOST "http://127.0.0.1:5000/address/" -H 'Content-type: application/json' \
  -d '{"Logradouro": "Rua Xalala", "Numero": "350", "Bairro": "Poço da Panela", "CEP": "52402402", "Cidade": "Recife", "Estado": "Pernambuco", "Pais": "Brasil", "Lat": 95.13212, "Long": 13.4324234, "Empresa_Id": 1}'
# Vai retornar erro pois a lat esta fora do range aceitavel
{
  "error": "Invalid lat, please use one within the range of -90.0 to 90.0"
}

curl -XPOST "http://127.0.0.1:5000/address/" -H 'Content-type: application/json' \
  -d '{"Logradouro": "Rua Xalala", "Numero": "350", "Bairro": "Poço da Panela", "CEP": "52402402", "Cidade": "Recife", "Estado": "Pernambuco", "Pais": "Brasil", "Lat": 88.13212, "Long": 13.4324234, "Empresa_Id": 7, "Tipo": 5}'
# Vai retornar erro pois o tipo esta invalido
{
  "error": "Invalid type, please use one of the options: [1, 2, 3]"
}

curl -XPOST "http://127.0.0.1:5000/address/" -H 'Content-type: application/json' \
  -d '{"Logradouro": "Rua Xalala", "Numero": "350", "Bairro": "Poço da Panela", "CEP": "52402402", "Cidade": "Recife", "Estado": "Pernambuco", "Pais": "Brasil", "Lat": 88.13212, "Long": 13.4324234, "Empresa_Id": 7}'
# Vai inserir e retornar o JSON do objeto apos ser atualizado com o que foi inserido no banco
{
  "id": 1
}
curl -XPOST "http://127.0.0.1:5000/address/" -H 'Content-type: application/json' \
  -d '{"Logradouro": "Rua Xalala", "Numero": "350", "Bairro": "Poço da Panela", "CEP": "52402402", "Cidade": "Recife", "Estado": "Pernambuco", "Pais": "Brasil", "Lat": 88.13212, "Long": 13.4324234, "Empresa_Id": 7, "Tipo": 1}'
{
  "id": 2
}

### Busca
curl -XGET "http://127.0.0.1:5000/address/123123"
# Vai retornar erro porque nao existe address com esse id
{
  "error": "No vehicle found with id 123123"
}

curl -XGET "http://127.0.0.1:5000/address/1"
# Vai retornar o JSON o address
{
  "Bairro": "Po\u00e7o da Panela",
  "CEP": "52402402",
  "Cidade": "Recife",
  "Cliente_Id": null,
  "Complemento": null,
  "Empresa_Id": 7,
  "Estado": "Pernambuco",
  "Id": 1,
  "Lat": 88.1321,
  "Logradouro": "Rua Xalala",
  "Long": 13.4324,
  "Numero": "350",
  "Pais": "Brasil",
  "Tipo": 1
}

### Edicao

curl -XPUT "http://127.0.0.1:5000/address/1" -H 'Content-type: application/json' \
  -d '{"Tipo": 7}'
# Vai retornar erro pois o tipo esta invalido
{
  "error": "Invalid type, please use one of the options: [1, 2, 3]"
}

curl -XPUT "http://127.0.0.1:5000/address/7" -H 'Content-type: application/json' \
  -d '{"Tipo": 3}'
# Vai retornar o address editado
{
  "id": 1
}

curl -XPUT "http://127.0.0.1:5000/address/123123" -H 'Content-type: application/json' \
  -d '{"Tipo": 3}'
# Vai retornar erro porque o id nao existe
{
  "error": "Unable to update Address with id 123123"
}

### Remocao

curl -XDELETE "http://127.0.0.1:5000/address/123123"
# Vai retornar erro porque nao existe address com esse id
{
  "error": "No address found with id 123123"
}

curl -XDELETE "http://127.0.0.1:5000/address/1"
# Vai retornar sucesso, pois o id existe
{
  "id": 1
}
