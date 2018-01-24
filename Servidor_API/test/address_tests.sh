### Insercao

curl -XPOST "http://127.0.0.1:5000/address/" -d '{"xalala": 1}'
# Vai retornar erro pois nao foi passado o header dizendo que esta sendo enviado um JSON
{
  "error": "Please provide a JSON"
}

curl -XPOST "http://127.0.0.1:5000/address/" -H 'Content-type: application/json' -d '{"xalala": 1}'
# Vai retornar erro pois nenhum dado do address foi passado para ser registrado
{
  "error": "Missing fields:['street', 'number', 'district', 'postal_code', 'city', 'state', 'country', 'lat', 'long', 'id_company', 'id_client']"
}

curl -XPOST "http://127.0.0.1:5000/address/" -H 'Content-type: application/json' \
  -d '{"street": "Rua Xalala", "number": "350", "district": "Poço da Panela", "postal_code": "52402402", "city": "Recife", "state": "Pernambuco", "country": "Brasil", "lat": 95.13212, "long": 13.4324234, "id_company": 1}'
# Vai retornar erro pois a lat esta fora do range aceitavel
{
  "error": "Invalid lat, please use one within the range of -90.0 to 90.0"
}

curl -XPOST "http://127.0.0.1:5000/address/" -H 'Content-type: application/json' \
  -d '{"street": "Rua Xalala", "number": "350", "district": "Poço da Panela", "postal_code": "52402402", "city": "Recife", "state": "Pernambuco", "country": "Brasil", "lat": 88.13212, "long": 13.4324234, "id_company": 7, "Tipo": 5}'
# Vai retornar erro pois o tipo esta invalido
{
  "error": "Invalid type, please use one of the options: [1, 2, 3]"
}

curl -XPOST "http://127.0.0.1:5000/address/" -H 'Content-type: application/json' \
  -d '{"street": "Rua Xalala", "number": "350", "district": "Poço da Panela", "postal_code": "52402402", "city": "Recife", "state": "Pernambuco", "country": "Brasil", "lat": 88.13212, "long": 13.4324234, "id_company": 7}'
# Vai inserir e retornar o JSON do objeto apos ser atualizado com o que foi inserido no banco
{
  "id": 1
}
curl -XPOST "http://127.0.0.1:5000/address/" -H 'Content-type: application/json' \
  -d '{"street": "Rua Xalala", "number": "350", "district": "Poço da Panela", "postal_code": "52402402", "city": "Recife", "state": "Pernambuco", "country": "Brasil", "lat": 88.13212, "long": 13.4324234, "id_company": 7, "Tipo": 1}'
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
  "district": "Po\u00e7o da Panela",
  "postal_code": "52402402",
  "city": "Recife",
  "id_client": null,
  "Complemento": null,
  "id_company": 7,
  "state": "Pernambuco",
  "Id": 1,
  "lat": 88.1321,
  "street": "Rua Xalala",
  "long": 13.4324,
  "number": "350",
  "country": "Brasil",
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
