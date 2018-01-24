### Insercao

curl -XPOST "http://127.0.0.1:5000/company/" -d '{"xalala": 1}'
# Vai retornar erro pois nao foi passado o header dizendo que esta sendo enviado um JSON
{
  "error": "Please provide a JSON"
}

curl -XPOST "http://127.0.0.1:5000/company/" -H 'Content-type: application/json' -d '{"xalala": 1}'
# Vai retornar erro pois nenhum dado da company foi passado para ser registrado
{
  "error": "Missing fields:['name', 'password', 'login', 'email', 'uci']"
}

curl -XPOST "http://127.0.0.1:5000/company/" -H 'Content-type: application/json' \
  -d '{"name": "Doni", "login": "donizette", "email": "donizette@gmail.com", "uci": "11122233344455", "password": "caleidoscópio"}'
# Vai retornar erro pois o name nao tem 6 ou mais caracteres
{
  "error": "Invalid name, please use one with at least 6 characters"
}

curl -XPOST "http://127.0.0.1:5000/company/" -H 'Content-type: application/json' \
  -d '{"name": "Donizette Delta", "login": "doni", "email": "donizette@gmail.com", "uci": "11122233344455", "password": "caleidoscópio"}'
# Vai retornar erro pois o login nao tem 6 ou mais caracteres
{
  "error": "Invalid login, please use one with at least 6 characters"
}

curl -XPOST "http://127.0.0.1:5000/company/" -H 'Content-type: application/json' \
  -d '{"name": "Donizette Delta", "login": "donizette", "email": "donizette@gmail.com", "uci": "11122233344455", "password": "calei"}'
# Vai retornar erro pois o password nao tem 6 ou mais caracteres
{
  "error": "Invalid password, please use one with at least 6 characters"
}

curl -XPOST "http://127.0.0.1:5000/company/" -H 'Content-type: application/json' \
  -d '{"name": "Donizette Delta", "login": "donizette", "email": "d@c", "uci": "11122233344455", "password": "caleidoscópio"}'
# Vai retornar erro pois o email nao tem 6 ou mais caracteres
{
  "error": "Invalid email, please use one with at least 6 characters"
}

curl -XPOST "http://127.0.0.1:5000/company/" -H 'Content-type: application/json' \
  -d '{"name": "Donizette Delta", "login": "donizette", "email": "emailinvalido", "uci": "11122233344455", "password": "caleidoscópio"}'
# Vai retornar erro pois o email nao esta num formato valido
{
  "error": "Invalid email, please use the format aaaa@bbbb.ccc"
}

curl -XPOST "http://127.0.0.1:5000/company/" -H 'Content-type: application/json' \
  -d '{"name": "Donizette Delta", "login": "donizette", "email": "donizette@gmail.com", "uci": "123", "password": "caleidoscópio"}'
# Vai retornar erro pois o cnpj nao tem 14 digitos
{
  "error": "Invalid uci, please use one with exactly 14 digits"
}

curl -XPOST "http://127.0.0.1:5000/company/" -H 'Content-type: application/json' \
  -d '{"name": "Donizette Delta", "login": "donizette", "email": "donizette@gmail.com", "uci": "b1122233344455", "password": "caleidoscópio"}'
# Vai retornar erro pois o cnpj tem caracteres que nao sao digitos
{
  "error": "Invalid uci, please use only digits"
}

curl -XPOST "http://127.0.0.1:5000/company/" -H 'Content-type: application/json' \
  -d '{"name": "Donizette Delta", "login": "donizette", "email": "donizette@gmail.com", "uci": "11122233344455", "password": "caleidoscópio", "addresses": [{"street": "Rua Xalala", "number": "350", "district": "Poço da Panela", "postal_code": "52402402", "city": "Recife", "state": "Pernambuco", "country": "Brasil", "lat": 88.13212, "long": 13.4324234}]}'
# Vai inserir e retornar o JSON do objeto apos ser atualizado com o que foi inserido no banco
{
  "id": 1
}

### Busca
curl -XGET "http://127.0.0.1:5000/company/123123"
# Vai retornar erro porque nao existe company com esse id
{
  "error": "No vehicle found with id 123123"
}

curl -XGET "http://127.0.0.1:5000/company/1"
# Vai retornar o JSON o company
{
  "uci": "11122233344455",
  "email": "donizette@gmail.com",
  "Enderecos": [],
  "Id": 1,
  "name": "Donizette Delta",
  "Tipo": null
}

### Edicao

curl -XPUT "http://127.0.0.1:5000/company/1" -H 'Content-type: application/json' \
  -d '{"name": "Doni"}'
# Vai retornar erro pois o nome tem menos que 6 caracteres
{
  "error": "Invalid name, please use one with at least 6 characters"
}

curl -XPUT "http://127.0.0.1:5000/company/1" -H 'Content-type: application/json' \
  -d '{"name": "Donizette Gama"}'
# Vai retornar o company editado
{
  "id": 1
}

curl -XPUT "http://127.0.0.1:5000/company/7" -H 'Content-type: application/json' \
  -d '{"password": "saci-perere"}'
# Vai retornar o company editado
{
  "id": 1
}

curl -XPUT "http://127.0.0.1:5000/company/123123" -H 'Content-type: application/json' \
  -d '{"name": "Doniribas"}'
# Vai retornar erro porque o id nao existe
{
  "error": "No company found with id 123123"
}

### Remocao

curl -XDELETE "http://127.0.0.1:5000/company/123123"
# Vai retornar erro porque nao existe company com esse id
{
  "error": "No company found with id 123123"
}

curl -XDELETE "http://127.0.0.1:5000/company/1"
# Vai retornar sucesso, pois o id existe
{
  "id": 1
}
