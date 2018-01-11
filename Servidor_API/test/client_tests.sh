### Insercao

curl -XPOST "http://127.0.0.1:5000/client/" -d '{"xalala": 1}'
# Vai retornar erro pois nao foi passado o header dizendo que esta sendo enviado um JSON
{
  "error": "Please provide a JSON"
}

curl -XPOST "http://127.0.0.1:5000/client/" -H 'Content-type: application/json' -d '{"xalala": 1}'
# Vai retornar erro pois nenhum dado da client foi passado para ser registrado
{
  "error": "Missing fields:['Nome', 'CPF']"
}

curl -XPOST "http://127.0.0.1:5000/client/" -H 'Content-type: application/json' \
  -d '{"Nome": "Mat", "CPF": "11122233344"}'
# Vai retornar erro pois o name nao tem 6 ou mais caracteres
{
  "error": "Invalid name, please use one with at least 6 characters"
}

curl -XPOST "http://127.0.0.1:5000/client/" -H 'Content-type: application/json' \
  -d '{"Nome": "Mathews", "CPF": "1112223334"}'
# Vai retornar erro pois o cpf nao tem 14 digitos
{
  "error": "Invalid upi, please use one with exactly 11 digits"
}

curl -XPOST "http://127.0.0.1:5000/client/" -H 'Content-type: application/json' \
  -d '{"Nome": "Mathews", "CPF": "a1122233344"}'
# Vai retornar erro pois o cpf tem caracteres que nao sao digitos
{
  "error": "Invalid upi, please use only digits"
}

curl -XPOST "http://127.0.0.1:5000/client/" -H 'Content-type: application/json' \
  -d '{"Nome": "Mathews", "CPF": "11122233344"}'
# Vai inserir e retornar o JSON do objeto apos ser atualizado com o que foi inserido no banco
{
  "id": 1
}

### Busca
curl -XGET "http://127.0.0.1:5000/client/123123"
# Vai retornar erro porque nao existe client com esse id
{
  "error": "No client found with id 123123"
}

curl -XGET "http://127.0.0.1:5000/client/1"
# Vai retornar o JSON o client
{
  "CPF": "11122233344",
  "Id": 1,
  "Nome": "Mathews"
}

### Edicao

curl -XPUT "http://127.0.0.1:5000/client/1" -H 'Content-type: application/json' \
  -d '{"Nome": "biri"}'
# Vai retornar erro pois o nome tem menos que 6 caracteres
{
  "error": "Invalid name, please use one with at least 6 characters"
}

curl -XPUT "http://127.0.0.1:5000/client/1" -H 'Content-type: application/json' \
  -d '{"Nome": "Rockefeller"}'
# Vai retornar o client editado
{
  "id": 1
}

curl -XPUT "http://127.0.0.1:5000/client/123123" -H 'Content-type: application/json' \
  -d '{"Nome": "Rockefeller"}'
# Vai retornar erro porque o id nao existe
{
  "error": "Unable to update Client with id 123123"
}

### Remocao

curl -XDELETE "http://127.0.0.1:5000/client/123123"
# Vai retornar erro porque nao existe client com esse id
{
  "error": "No client found with id 123123"
}

curl -XDELETE "http://127.0.0.1:5000/client/1"
# Vai retornar sucesso, pois o id existe
{
  "id": 1
}
