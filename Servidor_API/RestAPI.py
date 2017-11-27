from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from flask_cors import CORS
from DB.DB_helper import INIT_API, saveCompany


app = Flask(__name__)
mysql = MySQL()
CORS(app)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'packdeliv'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)



@app.route('/company', methods=['POST'])
#Json Model /company --> {"id": 1 , "Id_endereco": ufrpe street , "Nome_fantasia":"empresa teste", "Senha":"123213132", "Login":"adasdsada", "Email":"dansdjad", "CNPJ":"1232353", "Endereco": {"Logradouro":"testeLog", "Numero":"1234","Complemento":"testeComplemento", "Bairro":"testeBairoo", "CEP":"54546123", "Cidade":"testeC", "Estado":"testeE","Pais":"testeP"  } }
#campos não obrigatorios podem ficar em branco ex: id:""
def register_company():
    checkList=['Endereco']
    if request.method == 'POST':  
        json = request.get_json()
        #if any(i in checkList for i in json): (fazer modulo de checagem json)
        idCompany=saveCompany(json)
        return jsonify({'response' : {"companyID":str(idCompany)}})
    else:
        return jsonify({'error' : 'não foi possivel salvar no banco'})
            


    
    


if __name__ == '__main__':
    app.run()


'''

@app.route('/deliveryman/<id_deliveryman>', methods=['GET'])
def get_deliveryman(id_deliveryman):
    connection = mysql.connect()
    cursor=connection.cursor()
    query='select * from entregador where id='+id_deliveryman
    print(query)
    cursor.execute(query)
    r = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
    r = dict(enumerate(r))
    return jsonify({'response' : r})
@app.route()

@app.route('/getAllUsers')
def getAllUsers():
    cur = mysql.connect().cursor()
    cur.execute('select * from usuario')    
    r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
    r = dict(enumerate(r))
    return jsonify({'response' : r})


@app.route('/user', methods=['POST'])
def post():
    json = request.get_json(silent=True)
    print(json)
    checkList=['username', 'password','email','cnpj']
    if all(i in checkList for i in json):
        user = User(json['username'], json['password'],json['email'],json['cnpj'])
        if saveUserToDb(user):
            return jsonify({'done' : 'esta salvo'})
        else:
            return jsonify({'error' : 'não foi possivel salvar no banco'})
    else:
        return jsonify({'error' : 'falta campos obrigatorios'})
    

def saveUserToDb(user):
    
    connection = mysql.connect()
    cursor=connection.cursor()
    testevar="insert into usuario(Login,Email, Senha,cnpj) values ('"+ user.username +"', '" + user.email + "', '" + user.password + "', '" + user.cnpj + "');"
    print(testevar)
    cursor.execute(testevar)
    try:
        connection.commit()
        cursor.close()
        return True
    except:
        return False

if __name__ == '__main__':
    app.run(host='192.168.0.20')
    

'''
@app.route('/teste2', methods=['GET','POST'])
def teste():
    if request.method == 'POST':
        json = request.get_json()
        user = User(json['username'], json['password'])
        return logar(user)
    else:
        return 'POST METHOD PLZ'
    
def logar(user):
    try:
        cur = mysql.connect().cursor()
        cur.execute('select * from usuario where Login='+user.username+' and Senha='+user.password+';' )
        cursor.close()
        return jsonify({'done':'usuario logado'})
    except:
        return jsonify({'error':'Houve um erro ao logar'})
'''    

