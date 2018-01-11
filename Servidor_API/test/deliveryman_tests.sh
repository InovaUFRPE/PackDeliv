### Insercao

curl -XPOST "http://127.0.0.1:5000/deliveryman/" -d '{"xalala": 1}'
# Vai retornar erro pois nao foi passado o header dizendo que esta sendo enviado um JSON
{
  "error": "Please provide a JSON"
}

curl -XPOST "http://127.0.0.1:5000/deliveryman/" -H 'Content-type: application/json' -d '{"xalala": 1}'
# Vai retornar erro pois nenhum dado do deliveryman foi passado para ser registrado
{
  "error": "Missing fields:['Nome_fantasia', 'Senha', 'Login', 'Email', 'CNPJ', 'Nome', 'CNH', 'Status', 'Apto', 'Lat', 'Long', 'Id_veiculo']"
}

curl -XPOST "http://127.0.0.1:5000/deliveryman/" -H 'Content-type: application/json' \
  -d '{"Nome_fantasia": "Fire", "Login": "fire_and_ice", "Email": "contato@fireandice.com", "CNPJ": "22233344455566", "Senha": "winter", "Nome": "Hamilton Torres", "CNH": "123456", "Status": true, "Apto": false, "Lat": -22.3232434, "Long": 13.4324234, "Id_veiculo": 1}'
# Vai retornar erro pois o name nao tem 6 ou mais caracteres
{
  "error": "Invalid name, please use one with at least 6 characters"
}

curl -XPOST "http://127.0.0.1:5000/deliveryman/" -H 'Content-type: application/json' \
  -d '{"Nome_fantasia": "Fire & Ice", "Login": "fire_and_ice", "Email": "contato@fireandice.com", "CNPJ": "22233344455566", "Senha": "winter", "Nome": "Hamilton Torres", "CNH": "123456", "Status": true, "Apto": false, "Lat": -90.2323, "Long": 13.4324234, "Id_veiculo": 1}'
# Vai retornar erro pois a latitude está fora do range aceitavel
{
  "error": "Invalid lat, please use one within the range of -90.0 to 90.0"
}

curl -XPOST "http://127.0.0.1:5000/deliveryman/" -H 'Content-type: application/json' \
  -d '{"Nome_fantasia": "Fire & Ice", "Login": "fire_and_ice", "Email": "contato@fireandice.com", "CNPJ": "22233344455566", "Senha": "winter", "Nome": "Hamilton Torres", "CNH": "123456", "Status": true, "Apto": false, "Lat": -22.3232434, "Long": 180.3234, "Id_veiculo": 1}'
# Vai retornar erro pois a longitude está fora do range aceitavel
{
  "error": "Invalid long, please use one within the range of -180.0 to 180.0"
}

curl -XPOST "http://127.0.0.1:5000/deliveryman/" -H 'Content-type: application/json' \
  -d '{"Nome_fantasia": "Fire & Ice", "Login": "fire_and_ice", "Email": "contato@fireandice.com", "CNPJ": "22233344455566", "Senha": "winter", "Nome": "Hamilton Torres", "CNH": "123456", "Status": true, "Apto": false, "Lat": -22.3232434, "Long": 13.4324234, "Id_veiculo": 123123}'
# Vai retornar erro pois nao existe veiculo com id 123123
{
  "error": "Unable to register deliveryman: (pymysql.err.IntegrityError) (1452, 'Cannot add or update a child row: a foreign key constraint fails (`packdeliv`.`entregador`, CONSTRAINT `entregador_ibfk_2` FOREIGN KEY (`Id_veiculo`) REFERENCES `Veiculo` (`id`))') [SQL: 'INSERT INTO `Entregador` (id, `Nome`, `CNH`, `Status`, `Apto`, `Lat`, `Long`, `Id_veiculo`) VALUES (%(id)s, %(Nome)s, %(CNH)s, %(Status)s, %(Apto)s, %(Lat)s, %(Long)s, %(Id_veiculo)s)'] [parameters: {'CNH': '123456', 'Apto': 0, 'Nome': 'Hamilton Torres', 'Long': 13.4324234, 'Id_veiculo': 123123, 'Lat': -22.3232434, 'Status': 1, 'id': 9}]"
}

curl -XPOST "http://127.0.0.1:5000/deliveryman/" -H 'Content-type: application/json' \
  -d '{"Nome_fantasia": "Fire & Ice", "Login": "fire_and_ice", "Email": "contato@fireandice.com", "CNPJ": "22233344455566", "Senha": "winter", "Nome": "Hamilton Torres", "CNH": "123456", "Status": true, "Apto": false, "Lat": -22.3232434, "Long": 13.4324234, "Id_veiculo": 8}'
# Vai inserir e retornar o JSON do objeto apos ser atualizado com o que foi inserido no banco
{
  "id": 1
}

### Busca
curl -XGET "http://127.0.0.1:5000/deliveryman/123123"
# Vai retornar erro porque nao existe deliveryman com esse id
{
  "error": "No vehicle found with id 123123"
}

curl -XGET "http://127.0.0.1:5000/deliveryman/1"
# Vai retornar o JSON o deliveryman
{
  "Apto": false,
  "CNH": "contato@fireandice.com",
  "CNPJ": "22233344455566",
  "Email": "contato@fireandice.com",
  "Id_veiculo": 1,
  "Lat": -22.3232,
  "Long": 13.4324,
  "Nome": "Hamilton Torres",
  "Nome_fantasia": "Fire & Ice",
  "Status": true,
  "Tipo": null,
  "id": 1
}

### Edicao

curl -XPUT "http://127.0.0.1:5000/deliveryman/1" -H 'Content-type: application/json' \
  -d '{"Nome_fantasia": "Fire"}'
# Vai retornar erro pois o nome tem menos que 6 caracteres
{
  "error": "Invalid name, please use one with at least 6 characters"
}

curl -XPUT "http://127.0.0.1:5000/deliveryman/1" -H 'Content-type: application/json' \
  -d '{"Lat": -95.23123}'
# Vai retornar erro pois a latitude esta fora do range valido
{
  "error": "Invalid lat, please use one within the range of -90.0 to 90.0"
}

curl -XPUT "http://127.0.0.1:5000/deliveryman/1" -H 'Content-type: application/json' \
  -d '{"Lat": -13.66}'
# Vai retornar o deliveryman editado
{
  "id": 1
}

curl -XPUT "http://127.0.0.1:5000/deliveryman/123123" -H 'Content-type: application/json' \
  -d '{"Nome_fantasia": "Doniribas"}'
# Vai retornar erro porque o id nao existe
{
  "error": "Unable to update Deliveryman with id 123123"
}

### Remocao

curl -XDELETE "http://127.0.0.1:5000/deliveryman/123123"
# Vai retornar erro porque nao existe deliveryman com esse id
{
  "error": "No deliveryman found with id 123123"
}

curl -XDELETE "http://127.0.0.1:5000/deliveryman/1"
# Vai retornar sucesso, pois o id existe
{
  "id": 1
}
