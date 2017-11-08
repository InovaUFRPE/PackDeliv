from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from user import *

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'packdeliv'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

#https://www.techiediaries.com/ionic-3-http-module-rxjs/

'''@app.route('/register_company', methods=['POST'])
@app.route('/edit_company', methods=['POST'])
@app.route('/delete_company', methods=['POST'])
@app.route('/update_company', methods=['POST'])

@app.route('/register_deliveryman', methods=['POST'])
@app.route('/edit_deliveryman', methods=['POST'])
@app.route('/delete_deliveryman', methods=['POST'])
@app.route('/update_deliveryman', methods=['POST'])

@app.route('/register_vehicle', methods=['POST'])
@app.route('/edit_vehicle', methods=['POST'])
@app.route('/delete_vehicle', methods=['POST'])
@app.route('/update_vehicle', methods=['POST'])

@app.route('/register_user', methods=['POST'])
@app.route('/edit_user', methods=['POST'])
@app.route('/delete_user', methods=['POST'])
@app.route('/update_user', methods=['POST'])

@app.route('/register_profile', methods=['POST'])
@app.route('/edit_profile', methods=['POST'])
@app.route('/delete_profile', methods=['POST'])
@app.route('/update_profile', methods=['POST'])

@app.route()'''

@app.route('/getAllUsers')
def getAllUsers():
    cur = mysql.connect().cursor()
    cur.execute('select * from usuario')

    '''fetchRows=  cur.fetchall()
    print(fetchRows)
    
    for row in fetchRows:
        print(row)
       
        for i, value in enumerate(row):
            print(cur.description[i][0], value)'''
    
    r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
    r = dict(enumerate(r))
    return jsonify({'response' : r})


@app.route('/user', methods=['POST'])
def post():
    json = request.get_json(silent=True)
    print(json)
    checkList=['username', 'password','email']
    if all(i in checkList for i in json):
        user = User(json['username'], json['password'],json['email'])
        if saveUserToDb(user):
            return jsonify({'done' : 'esta salvo'})
        else:
            return jsonify({'error' : 'não foi possivel salvar no banco'})
    else:
        return jsonify({'error' : 'falta campos obrigatorios'})
    

def saveUserToDb(user):
    
    connection = mysql.connect()
    cursor=connection.cursor()
    testevar="insert into usuario(Login,Email, Senha) values ('"+ user.username +"', '" + user.email + "', '" + user.password + "');"
    print(testevar)
    cursor.execute(testevar)
    try:
        connection.commit()
        cursor.close()
        return True
    except:
        return False

if __name__ == '__main__':
    app.run()
    

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

