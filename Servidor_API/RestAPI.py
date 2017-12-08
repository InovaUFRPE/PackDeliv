# coding=utf-8
from flask import Flask, jsonify, request
import requests

from flask_cors import CORS
from DB.DB_helper import INIT_API #aveDeliveryman, savePackage
from Rest_utils.entities_atributes_Names import *
from Models.company import *
from Models.adress import * 

INIT_API()

app = Flask(__name__)

CORS(app)




@app.route('/company', methods=['POST'])
#Json Model /company --> {"Nome_fantasia":"empresa teste", "Senha":"123213132", "Login":"adasdsada", "Email":"dansdjad", "CNPJ":"1232353", "Endereco": {"Id":"","Logradouro":"testeLog", "Numero":"1234","Complemento":"testeComplemento", "Bairro":"testeBairoo", "CEP":"54546123", "Cidade":"testeC", "Estado":"testeE","Pais":"testeP"  } }

def register_company():

    if request.method == 'POST':  
        json = request.get_json()
        
        json_adress = json[ADRESS]
        
        adress = Adress()
        adress.street=json_adress[ADRESS_STREET]
        adress.number=json_adress[ADRESS_NUMBER]
        adress.complement=json_adress[ADRESS_COMPLEMENT]
        adress.district=json_adress[ADRESS_DISTRICT]
        adress.postal_code=json_adress[ADRESS_POSTAL_CODE]
        adress.city=json_adress[ADRESS_CITY]
        adress.state=json_adress[ADRESS_STATE]
        adress.country=json_adress[ADRESS_COUNTRY]
        
        id_adress = Adress.save(adress)
        
        company = Company()
        company.id_adress = id_adress
        company.name_company = json[COMPANY_NAME]
        company.password = json[COMPANY_PASSWORD]
        company.login = json[COMPANY_LOGIN]
        company.email = json[COMPANY_EMAIL]
        company.uci = json[COMPANY_UCI]
        
        id_company = Company.save(company)
        
        if (id_company):
            return jsonify({'response' : {"companyID":str(id_company)}})
        else:
            return jsonify({'error' : 'Não foi possivel cadastrar'})
            

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


@app.route('/deliveryman', methods=['POST'])

#Json Model /login -->
#{"CNH":"12432554","Nome_fantasia":"deliveryman", "Senha":"123213132", "Login":"deliveryman", "Email":"deliveryman",
#"Endereco": {"Logradouro":"deliveryman testeLog", "Numero":"1234","Complemento":"testeComplemento",
#"Bairro":"testeBairoo", "CEP":"54546123", "Cidade":"testeC", "Estado":"testeE","Pais":"testeP"  } } 

def register_deliveryman():
    if request.method == 'POST':  
        json = request.get_json()
        idDeliveryman = saveDeliveryman(json)
        
        if (idDeliveryman):
            return jsonify({'response' : {"companyID":str(idDeliveryman)}})
        else:
            return jsonify({'error' : 'Não foi possivel cadastrar'})

@app.route('/package', methods=['POST'])

def register_package():
    if request.method == 'POST':
        json = request.get_json()
        idPackage= savePackage(json)

        if (idPackage):
            return jsonify({'response' : {"packageID":str(idPackage)}})
        else:
            return jsonify({'error' : "Não foi possível cadastrar"})        

if __name__ == '__main__' :
    app.run()
