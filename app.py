# imports
from flask import Flask, request, jsonify, send_file, render_template
import traceback
import os
# importing database created from the database.py file
from database import db
from getBlock import getblock
from addBlock import addblock
from codeGen import codeGenerator
# API definition
app = Flask(__name__)

# Webpage to be made for this route
@app.route("/")
def home():
    return render_template('index.html')

# webpage for adding a block to the database


@app.route("/addBlock")
def addBlockPage():
    return render_template("addBlock.html")

# endpoint for creating a block entry in the database
@app.route("/addblockrequest", methods=["POST"])
def addBlock():
    blockName = str(request.form['blockName'])
    args = str(request.form['args'])
    filePath = str(request.form['filePath'])
    out = str(request.form['out'])
    ins = str(request.form['in'])
    requestComp = addblock(blockName, args, ins, out, filePath)
    return render_template("successfullBlock.html", blockName=requestComp)


# endpoint to show all the users
@app.route("/getBlocks", methods=["GET"])
def get_blocks():
    qtype = request.args.get('type')
    if(qtype == None):
        return jsonify({"message": "inavlied query string"})
    allBlocks = getblock(qtype)
    return jsonify({"Blocks": [allBlocks.val()]})


# this code generates a cov_file in which the resulting code resides till now
@app.route('/generateCode', methods=['POST', 'GET'])
def block():
    try:
        # json file with the requirements from the client side
        json_ = request.json
        # getting file paths from the database
        # getting the json files and list of filepaths from the json file
        # json_[filePaths] is the list containing the relative file paths of the files
        fileStatus = codeGenerator(json_)
        return jsonify({'fileStatus': fileStatus})
    except:
        return jsonify({'trace': traceback.format_exc()})


@app.route("/convertedFile")
def DownloadLogFile():
    try:
        filepathMaster = os.path.join(os.getcwd(), "covFile.py")
        return send_file(filepathMaster, as_attachment=True)
    except:
        return jsonify({'trace': traceback.format_exc()})


if __name__ == '__main__':
    app.run(debug=True)
