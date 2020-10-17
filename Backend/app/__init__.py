from app.User import bp as userBp
from flask import Flask,request, jsonify, make_response
import Utility.dbController as dbController

app = Flask(__name__)
db = dbController.connect()
app.register_blueprint(userBp, url_prefix="/")

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run()