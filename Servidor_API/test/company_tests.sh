### Insercao

curl -XPOST "http://127.0.0.1:5000/company/" -d '{"xalala": 1}'
# Vai retornar erro pois nao foi passado o header dizendo que esta sendo enviado um JSON
{
  "error": "Please provide a JSON"
}

curl -XPOST "http://127.0.0.1:5000/company/" -H 'Content-type: application/json' -d '{"xalala": 1}'
# Vai retornar erro pois nenhum dado da company foi passado para ser registrado
{
  "error": "Missing fields:['Nome_fantasia', 'Senha', 'Login', 'Email', 'CNPJ']"
}

curl -XPOST "http://127.0.0.1:5000/company/" -H 'Content-type: application/json' \
  -d '{"Nome_fantasia": "Doni", "Login": "donizette", "Email": "donizette@gmail.com", "CNPJ": "11122233344455", "Senha": "caleidoscópio"}'
# Vai retornar erro pois o name nao tem 6 ou mais caracteres
{
  "error": "Invalid name, please use one with at least 6 characters"
}

curl -XPOST "http://127.0.0.1:5000/company/" -H 'Content-type: application/json' \
  -d '{"Nome_fantasia": "Donizette Delta", "Login": "doni", "Email": "donizette@gmail.com", "CNPJ": "11122233344455", "Senha": "caleidoscópio"}'
# Vai retornar erro pois o login nao tem 6 ou mais caracteres
{
  "error": "Invalid login, please use one with at least 6 characters"
}

curl -XPOST "http://127.0.0.1:5000/company/" -H 'Content-type: application/json' \
  -d '{"Nome_fantasia": "Donizette Delta", "Login": "donizette", "Email": "donizette@gmail.com", "CNPJ": "11122233344455", "Senha": "calei"}'
# Vai retornar erro pois o password nao tem 6 ou mais caracteres
{
  "error": "Invalid password, please use one with at least 6 characters"
}

curl -XPOST "http://127.0.0.1:5000/company/" -H 'Content-type: application/json' \
  -d '{"Nome_fantasia": "Donizette Delta", "Login": "donizette", "Email": "d@c", "CNPJ": "11122233344455", "Senha": "caleidoscópio"}'
# Vai retornar erro pois o email nao tem 6 ou mais caracteres
{
  "error": "Invalid email, please use one with at least 6 characters"
}

curl -XPOST "http://127.0.0.1:5000/company/" -H 'Content-type: application/json' \
  -d '{"Nome_fantasia": "Donizette Delta", "Login": "donizette", "Email": "emailinvalido", "CNPJ": "11122233344455", "Senha": "caleidoscópio"}'
# Vai retornar erro pois o email nao esta num formato valido
{
  "error": "Invalid email, please use the format aaaa@bbbb.ccc"
}

curl -XPOST "http://127.0.0.1:5000/company/" -H 'Content-type: application/json' \
  -d '{"Nome_fantasia": "Donizette Delta", "Login": "donizette", "Email": "donizette@gmail.com", "CNPJ": "123", "Senha": "caleidoscópio"}'
# Vai retornar erro pois o cnpj nao tem 14 digitos
{
  "error": "Invalid uci, please use one with exactly 14 digits"
}

curl -XPOST "http://127.0.0.1:5000/company/" -H 'Content-type: application/json' \
  -d '{"Nome_fantasia": "Donizette Delta", "Login": "donizette", "Email": "donizette@gmail.com", "CNPJ": "b1122233344455", "Senha": "caleidoscópio"}'
# Vai retornar erro pois o cnpj tem caracteres que nao sao digitos
{
  "error": "Invalid uci, please use only digits"
}

curl -XPOST "http://127.0.0.1:5000/company/" -H 'Content-type: application/json' \
  -d '{"Nome_fantasia": "Donizette Delta", "Login": "donizette", "Email": "donizette@gmail.com", "CNPJ": "11122233344455", "Senha": "caleidoscópio"}'
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
  "CNPJ": "11122233344455",
  "Email": "donizette@gmail.com",
  "Enderecos": [],
  "Id": 1,
  "Nome_fantasia": "Donizette Delta",
  "Tipo": null
}

### Edicao

curl -XPUT "http://127.0.0.1:5000/company/1" -H 'Content-type: application/json' \
  -d '{"Nome_fantasia": "Doni"}'
# Vai retornar erro pois o nome tem menos que 6 caracteres
{
  "error": "Invalid name, please use one with at least 6 characters"
}

curl -XPUT "http://127.0.0.1:5000/company/1" -H 'Content-type: application/json' \
  -d '{"Nome_fantasia": "Donizette Gama"}'
# Vai retornar o company editado
{
  "id": 1
}

curl -XPUT "http://127.0.0.1:5000/company/7" -H 'Content-type: application/json' \
  -d '{"Senha": "saci-perere"}'
# Vai retornar o company editado
{
  "id": 1
}

curl -XPUT "http://127.0.0.1:5000/company/123123" -H 'Content-type: application/json' \
  -d '{"Nome_fantasia": "Doniribas"}'
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

curl -XDELETE "http://127.0.0.1:5000/vehicle/1"
# Vai retornar sucesso, pois o id existe
{
  "id": 1
}
