import flask
from flask import request, jsonify

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