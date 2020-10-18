from app.User import bp as userBp
from app.Engine import bp as engineBp
from app.Org import bp as orgBp
from flask import Flask,request, jsonify, make_response
import Utility.dbController as dbController
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
db = dbController.connect()
app.register_blueprint(userBp, url_prefix="/")
app.register_blueprint(engineBp, url_prefix="/")
app.register_blueprint(orgBp, url_prefix="/")

@app.errorhandler(404)
@cross_origin()
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(debug=True)