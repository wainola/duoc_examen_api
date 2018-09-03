import flask
from flask import request, jsonify

from handlers.loginHandler import login
from handlers.userHandler import user
from handlers.creditHandler import credit
from handlers.executiveHandler import executive
from handlers.requestStatusHandler import request_status
from handlers.signupHandler import signup

data = [
  {
    "id": 1,
    "name": "nicolas riquelme"
  },
  {
    "id": 2,
    "name": "camilo riquelme"
  },
  {
    "id": 1,
    "name": "paulina curin"
  }
]

app = flask.Flask(__name__)
app.config['DEBUG'] = True

app.register_blueprint(login, url_prefix='/login')
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(credit, url_prefix='/credit')
app.register_blueprint(executive, url_prefix='/executive')
app.register_blueprint(request_status, url_prefix='/request_status')
app.register_blueprint(signup, url_prefix='/signup')

@app.route('/', methods=['GET'])
def home():
  return '<h1>Home app flask</h1>'

@app.route('/api/data', methods=['GET'])
def getData():
  return jsonify(data)

@app.route('/api/data/<int:id>', methods=['GET'])
def getByOne(id):
  req_id = id
  data_to_return = []

  for index in range(0, len(data)):
    if data[index]['id'] == req_id:
      data_to_return.append(data[index])

  if len(data_to_return) == 0:
    return jsonify({ 'msg': 'no data found' })
  
  return jsonify({ 'data': data_to_return })

if __name__ == '__main__':
  app.run()