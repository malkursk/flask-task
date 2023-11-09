import datetime
import utils.functions as func
import utils.functionsNice as funcNice

from flask import Flask, request, jsonify
from sqlalchemy.dialects.postgresql import JSON

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)

class WorkModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)    
    params = db.Column(JSON, nullable=False)
    result = db.Column(JSON)    
    createdat = db.Column(db.DateTime, default=datetime.datetime.now())

    @property
    def serialize(self):
        return {
            'id': self.id,
            'params': self.params,
            'result': self.result,
        }
    

def funcController(inJson):
    data = inJson['data'] 
    value = inJson['data']['value'] 

    match inJson['method']:
        # Nice functions section ==========================================
        case "matrix-Julia":
            return funcNice.matrixReverse(value)
        case "ceasar":
            return funcNice.caesar(value,data['offset'])
        case "sum":
            return funcNice.getSum(value)   

        # Usual functions section =========================================
        case "matrix-reverse":
            return func.matrixReverse(value)
        case "arraySum":
            return func.arraySum(value)
        case "matrix-t":
            return func.matrixTransponse(value)         
    return "method is not supported"
    
@app.route("/")
def hello():
    return "hello"

@app.route("/list",methods=['GET'])
def getWorks():
    works = WorkModel.query.order_by(WorkModel.id.desc()).limit(25)
    return jsonify(works=[i.serialize for i in works])

@app.route("/calc",methods=['POST'])
def index():    
    try:
        res = funcController(request.get_json())
        res =  {'data': {'result': res}}
        work = WorkModel(params=request.get_json(),result = res)
        db.session.add(work)
        db.session.commit()
        return {"data": work.serialize, }, 200
    except:
        return {"data": 'wrong json-params', }, 400
    
@app.route('/task/<id>', methods=['GET'])
def viewTask(id):
    return WorkModel.query.get(id).serialize

@app.route('/task/<id>', methods=['DELETE'])
def deleteTask(id):
    s = "not found"
    code = 404
    if(WorkModel.query.get(id)):
        db.session.delete(WorkModel.query.get(id))
        db.session.commit()
        code = 200 
        s = "successfully deleted"       
    return {"data": f"id={id} {s}"}, code
    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=2001)

