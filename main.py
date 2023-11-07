import datetime
import json
import utils.functionMatrix as mtr

from flask import Flask, request, jsonify
from sqlalchemy.dialects.postgresql import JSON

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)


class WorkModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)    
    params = db.Column(JSON, nullable=False)
    result = db.Column(JSON, nullable=False)    
    createAt = db.Column(db.DateTime, default=datetime.datetime.now())

    @property
    def serialize(self):
        return {
            'id': self.id,
            'params': self.params,
            'result': self.result,
            'createAt': self.createAt,
        }

@app.route("/")
def hello():
    return "hello"

@app.route("/works",methods=['GET'])        
def getWorks():
    # works = WorkModel.query.all()
    works = WorkModel.query.order_by(WorkModel.id.desc()).limit(25)
    return jsonify(works=[i.serialize for i in works])
    
@app.route("/math/matrInverse",methods=['POST'])
def matrInverse():    
    try:
        inJson = request.get_json()
        res = mtr.reverse(inJson['matrix'])
        work = WorkModel(params=inJson,result = res)
        db.session.add(work)
        db.session.commit()
        return {"data": work.serialize, }, 200
    except:
        return {"result": 'неверные параметры', }, 400
    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=2001)