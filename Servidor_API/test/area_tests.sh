### Insercao

curl -XPOST "http://127.0.0.1:5000/area/" -d '{"xalala": 1}'
# Vai retornar erro pois nao foi passado o header dizendo que esta sendo enviado um JSON
{
  "error": "Please provide a JSON"
}

curl -XPOST "http://127.0.0.1:5000/area/" -H 'Content-type: application/json' -d '{"xalala": 1}'
# Vai retornar erro pois nenhum dado da area foi passado para ser registrado
{
  "error": "Missing fields:['lat', 'long', 'area_radius', 'packages']"
}

curl -XPOST "http://127.0.0.1:5000/area/" -H 'Content-type: application/json' \
  -d '{"lat": -100.00, "long": 45.3342, "area_radius": 10, "packages": [{"width": 30, "height": 35, "length": 10, "weight": 1, "volume": 1, "shiped": true, "received": false, "static_location": "Xalala", "send_date": "2018-01-01", "delivery_date": null, "id_address_start": 1, "id_address_destiny": 2, "status": 1}]}'
# Vai retornar erro pois a lat está inválida
{
  "error": "Invalid lat, please use one within the range of -90.0 to 90.0"
}

curl -XPOST "http://127.0.0.1:5000/area/" -H 'Content-type: application/json' \
  -d '{"lat": -13.234324, "long": 45.3342, "area_radius": 5001, "packages": [{"width": 30, "height": 35, "length": 10, "weight": 1, "volume": 1, "shiped": true, "received": false, "static_location": "Xalala", "send_date": "2018-01-01", "delivery_date": null, "id_address_start": 1, "id_address_destiny": 2, "status": 1}]}'
# Vai retornar erro pois o raio não pode ser menor que 5000m
{
  "error": "Invalid area_radius, please use one within the range of 1 to 5000"
}

curl -XPOST "http://127.0.0.1:5000/area/" -H 'Content-type: application/json' \
  -d '{"lat": -13.234324, "long": 45.3342, "area_radius": 300, "packages": [{"width": 30, "height": 35, "length": 10, "weight": 1, "volume": 1, "shiped": true, "received": false, "static_location": "Xalala", "send_date": "2018-01-01", "delivery_date": null, "id_address_start": 2, "id_address_destiny": 2, "status": 1}]}'
# Vai inserir e retornar o JSON do objeto apos ser atualizado com o que foi inserido no banco
{
  "id": 1
}

### Busca
curl -XGET "http://127.0.0.1:5000/area/123123"
# Vai retornar erro porque nao existe area com esse id
{
  "error": "No area found with id 123123"
}

curl -XGET "http://127.0.0.1:5000/area/1"
# Vai retornar o JSON area
{
  "area_radius": 300,
  "id": 4,
  "lat": -13.2343,
  "long": 45.3342,
  "packages": [
    {
      "address_destiny": {
        "city": "Recife",
        "complement": null,
        "country": "Brasil",
        "district": "Po\u00e7o da Panela",
        "id": 2,
        "id_client": null,
        "id_company": 1,
        "lat": 88.1321,
        "long": 13.4324,
        "number": "350",
        "postal_code": 52402402,
        "state": "Pernambuco",
        "street": "Rua Xalala",
        "type": null
      },
      "address_start": {
        "city": "Recife",
        "complement": null,
        "country": "Brasil",
        "district": "Po\u00e7o da Panela",
        "id": 2,
        "id_client": null,
        "id_company": 1,
        "lat": 88.1321,
        "long": 13.4324,
        "number": "350",
        "postal_code": 52402402,
        "state": "Pernambuco",
        "street": "Rua Xalala",
        "type": null
      },
      "delivery_date": null,
      "height": 35,
      "id": 2,
      "id_address_destiny": 2,
      "id_address_start": 2,
      "id_area": 4,
      "id_client": null,
      "id_company": null,
      "length": 10,
      "received": false,
      "send_date": "Mon, 01 Jan 2018 00:00:00 GMT",
      "shiped": true,
      "static_location": "Xalala",
      "status": 1,
      "volume": 1,
      "weight": 1,
      "width": 30
    }
  ]
}

### Edicao

curl -XPUT "http://127.0.0.1:5000/area/1" -H 'Content-type: application/json' \
  -d '{"area_radius": 500}'
# Vai retornar erro pois o nome tem menos que 6 caracteres
{
  "id": 1
}

curl -XPUT "http://127.0.0.1:5000/area/123123" -H 'Content-type: application/json' \
  -d '{"area_radius": 500}'
# Vai retornar erro porque o id nao existe
{
  "error": "Unable to update Area with id 123123"
}

### Remocao

curl -XDELETE "http://127.0.0.1:5000/area/123123"
# Vai retornar erro porque nao existe area com esse id
{
  "error": "No area found with id 123123"
}

curl -XDELETE "http://127.0.0.1:5000/area/1"
# Vai retornar sucesso, pois o id existe
{
  "id": 1
}
