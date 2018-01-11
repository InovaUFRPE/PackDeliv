### Insercao

curl -XPOST "http://127.0.0.1:5000/vehicle/" -d '{"xalala": 1}'
# Vai retornar erro pois nao foi passado o header dizendo que esta sendo enviado um JSON
{
  "error": "Please provide a JSON"
}

curl -XPOST "http://127.0.0.1:5000/vehicle/" -H 'Content-type: application/json' -d '{"xalala": 1}'
# Vai retornar erro pois nenhum dado do veiculo foi passado para ser registrado
{
  "error": "Missing placa"
}

curl -XPOST "http://127.0.0.1:5000/vehicle/" -H 'Content-type: application/json' \
  -d '{"placa": "KL-9193", "ano": 2017, "modelo": "New Fiesta", "cor": "Prata", "volume": 5}'
# Vai retornar erro pois a placa esta no formato incorreto (so tem 2 letras antes do traco)
{
  "error": "Invalid license plate, please use the format AAA-9999"
}

curl -XPOST "http://127.0.0.1:5000/vehicle/" -H 'Content-type: application/json' \
  -d '{"placa": "KLB-9193", "ano": 2017, "modelo": "New Fiesta", "cor": "Prata", "volume": 5}'
# Vai inserir e retornar o JSON do objeto apos ser atualizado com o que foi inserido no banco
{
  "id": 1
}

curl -XPOST "http://127.0.0.1:5000/vehicle/" -H 'Content-type: application/json' \
  -d '{"placa": "KLB-9193", "ano": 2017, "modelo": "New Fiesta", "cor": "Prata", "volume": 5}'
# Vai tentar inserir e nao vai conseguir pq a placa ja existe no banco
{
  "error": "Unable to register vehicle: (pymysql.err.IntegrityError) (1062, u\"Duplicate entry 'KLB-9193' for key 'placa'\")"
}

### Busca
curl -XGET "http://127.0.0.1:5000/vehicle/123123"
# Vai retornar erro porque nao existe veiculo com esse id
{
  "error": "No vehicle found with id 123123"
}

curl -XGET "http://127.0.0.1:5000/vehicle/1"
# Vai retornar o JSON o veiculo
{
  "ano": 2017,
  "apto": false,
  "cor": "Prata",
  "id": 1,
  "modelo": "New Fiesta",
  "placa": "KLB-9193",
  "volume": 5
}

### Edicao

curl -XPUT "http://127.0.0.1:5000/vehicle/1" -H 'Content-type: application/json' \
  -d '{"placa": "KLB-9193", "ano": 2017, "modelo": "New Fiesta", "cor": "Verde", "volume": 7, "apto": false}'
# Vai retornar o veiculo editado
{
  "id": 1
}

curl -XPUT "http://127.0.0.1:5000/vehicle/123123" -H 'Content-type: application/json' \
  -d '{"ano": 2018, "modelo": "New Fiesta Sedan", "cor": "Verde"}'
# Vai retornar erro porque o id nao existe
{
  "error": "No vehicle found with id 123123"
}

### Remocao

curl -XDELETE "http://127.0.0.1:5000/vehicle/123123"
# Vai retornar erro porque nao existe veiculo com esse id
{
  "error": "No vehicle found with id 123123"
}

curl -XDELETE "http://127.0.0.1:5000/vehicle/1"
# Vai retornar sucesso, pois o id existe
{
  "id": 1
}
