from flask import Flask, jsonify, request
import requests
from flaskext.mysql import MySQL
from flask_cors import CORS
from DB.DB_helper import INIT_API, saveCompany, getCompany

INIT_API()

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
#Json Model /company --> {"Nome_fantasia":"empresa teste", "Senha":"123213132", "Login":"adasdsada", "Email":"dansdjad", "CNPJ":"1232353", "Endereco": {"Id":"","Logradouro":"testeLog", "Numero":"1234","Complemento":"testeComplemento", "Bairro":"testeBairoo", "CEP":"54546123", "Cidade":"testeC", "Estado":"testeE","Pais":"testeP"  } }
#campos não obrigatorios podem ficar vazios ex: complemento:""

def register_company():

    if request.method == 'POST':  
        json = request.get_json()
        idCompany = saveCompany(json)
        
        if (idCompany):
            return jsonify({'response' : {"companyID":str(idCompany)}})
        else:
            return jsonify({'error' : 'Não foi possivel cadastar'})
            

@app.route('/login',methods=['POST'])
#Json Model /login --> {"login":"teste","senha":"teste"}
def login_company():
    if request.method == 'POST':
        json_login = request.get_json()
        Company = getCompany (json_login)
        if (Company):
            
            return jsonify({'response' : Company})
        else:
            return jsonify({'error' : 'Não foi possivel logar usuario'})
        
            
@app.route('/cnpj/<cnpj>',methods=['GET'])
def cnpj(cnpj):
    if request.method == 'GET':
        
        r = requests.get('https://www.receitaws.com.br/v1/cnpj/'+ str(cnpj) )

        return jsonify(r.json())
        
        
        


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
  
def logar(user):
    try:
        cur = mysql.connect().cursor()
        cur.execute('select * from usuario where Login='+user.username+' and Senha='+user.password+';' )
        cursor.close()
        return jsonify({'done':'usuario logado'})
    except:
        return jsonify({'error':'Houve um erro ao logar'})
'''    

