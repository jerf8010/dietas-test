# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request
import json
from db_conn import connection
import os
from dotenv import load_dotenv
from bson import ObjectId


load_dotenv()
PORT = os.getenv('PORT')
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to dietasApp backend!!!'

@app.route('/person', methods = ['GET'])
def get():
    try:
        data = connection()

        email    = str(request.args['Email'])
        password = str(request.args['Password'])

        item = data.find_one({'Email': email,
                              'Password': password})

        if item is None:
            return json.dumps({
                'Error': 'Person not found'
            }), 404
        else:
            return json.dumps({
                'Succed': 'Person found',
                'Person': {
                    'Email': item['Email'],
                    'Password': item['Password']
                }
            }), 200

    except:
        return json.dumps({
            'Error': 'Error de conexion con db'
        }), 500

@app.route('/register', methods = ['POST'])
def put():
    try:
        data = connection()

        email    = str(request.args.get('Email'))
        password = str(request.args.get('Password'))

        query = {'Email'   : email, 
                 'Password': password}
        
        item = data.find_one(query)
        print(item is None)

        if item is None:
            data.insert_one(
                {'_id'     : ObjectId(),
                 'Email'   : email, 
                 'Password': password}
            )
            return json.dumps({
                'Producto': query,
                'Succed': "New register added" 
            }), 200
        else:
            return json.dumps({
                'Error': f'This email {email} exists, register another'
            }), 404

    
    except Exception as  e:
        return json.dumps({
            'Error': f'Error with data base connection: {e}'
        }), 500
app.run(host = '192.168.100.26', port = 5050)
 
# main driver function
if __name__ == '__main__':
    app.run()
