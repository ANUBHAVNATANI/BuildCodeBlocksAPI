from flask import Flask, request, jsonify
import traceback

# API definition
app = Flask(__name__)


@app.route("/")
def home():
    return "This is an api that provieds info about the blocks"


@app.route('/giveBlock', methods=['POST'])
def block():
    try:
        json_ = request.json
        print(json_)
        what_code_get = "Write in next lines code to get code"
        return jsonify({'code': str(what_code_get)})
    except:
        return jsonify({'trace': traceback.format_exc()})


if __name__ == '__main__':

    app.run(debug=True)
