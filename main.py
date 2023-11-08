import datetime
import utils.functions as func
import utils.functionsNice as funcNice

from flask import Flask, request, jsonify
from sqlalchemy.dialects.postgresql import JSON

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)

@app.route("/")
def hello():
    return "hello"

class WorkModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)    
    params = db.Column(JSON, nullable=False)
    result = db.Column(JSON, nullable=False)    
    createdat = db.Column(db.DateTime, default=datetime.datetime.now())

    @property
    def serialize(self):
        return {
            'id': self.id,
            'params': self.params,
            'result': self.result,
            'createdat': self.createdat,
        }

@app.route("/list",methods=['GET'])
def getWorks():
    # works = WorkModel.query.all()
    works = WorkModel.query.order_by(WorkModel.id.desc()).limit(25)
    return jsonify(works=[i.serialize for i in works])


        
def funcController(inJson):
    match inJson['method']:
        case "matrix-reverse":
            return func.reverse(inJson['data']['matrix'])
        case "matrix-Julia":
            return funcNice.reverse(inJson['data']['matrix'])
    

@app.route("/calc",methods=['POST'])
def index():    
    try:
        res = funcController(request.get_json())
        res =  {'data': {'result': res}}
        #return {"data": res, }, 200
        print(res)
        work = WorkModel(params=request.get_json(),result = res)
        db.session.add(work)
        db.session.commit()
        return {"data": work.serialize, }, 200
    except:
        return {"data": 'wrong params', }, 400
    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=2001)