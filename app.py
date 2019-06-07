# imports
from flask import Flask, request, jsonify, send_file, render_template
import traceback
import os
# importing database created from the database.py file
from database import db

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
    functionName = str(request.form['blockName'])
    args = str(request.form['args'])
    filePath = str(request.form['filePath'])
    filePath = filePath.replace("\\", '/')
    block = {"functionName": functionName, "args": args, "filePath": filePath}
    # python way to split the data
    sect = filePath.split("/")
    c = db
    for i in range(0, len(sect)-1):
        c = c.child(sect[i])
    c = c.child(functionName)
    c.set(block)
    return render_template("successfullBlock.html", blockName=functionName)


# endpoint to show all the users
@app.route("/getBlocks", methods=["GET"])
def get_blocks():
    # specific type of data demanding code
    """
    json_ = request.json
    if(json_["type"]=="all"):
        return jsonify(data)
    """
    # current code
    allBlocks = db.child("Python").get()
    return jsonify(allBlocks.val())


# this code generates a cov_file in which the resulting code resides till now
@app.route('/giveBlock', methods=['POST', 'GET'])
def block():
    try:
        # json file with the requirements from the client side
        json_ = request.json
        # getting file paths from the database
        # getting the json files and list of filepaths from the json file
        # json_[filePaths] is the list containing the relative file paths of the files
        filePaths = [block["filePath"] for block in json_["function"]]
        # compiling the file paths from the database
        filepathMaster = os.path.join(os.getcwd(), "covFile.py")
        for i in range(len(filePaths)):
            rfilePath = filePaths[i]
            # path gen code
            filePaths[i] = os.path.join(
                os.getcwd(), "BuildCodeBlocksAPI", "Blocks", rfilePath)
        # reversing file paths for the correct order
        filePaths.reverse()
        # writing output to another file
        with open(filepathMaster, "w") as out_file:
            for filePath in filePaths:
                with open(filePath, "r") as in_file:
                    for l in in_file.readlines():
                        out_file.writelines(l)
                    out_file.writelines("\n\n")
            # Main function code for running the code generated in the recent file
            mainFunctionCode = 'if __name__ == "__main__":'
            # Combining Function Code with args
            fullFunctions = []
            # not needed but of safety purposes
            currFunctionList = []
            for i in range(len(json_["function"])):
                function = json_["function"][i]
                currFunctionList.append(function)
                functionName = function["functionName"]
                args = function["args"]
                out = function["out"]
                try:
                    inp = function["in"]
                    # can support multiple input by split function
                    # currently not supported multiple inputs
                    for i in currFunctionList:
                        if(i["functionName"] == inp):
                            inpo = i["out"]
                            break
                except:
                    inpo = None
                if(inpo == None):
                    newFunctionName = out+"="+functionName+"("+args+")"
                else:
                    newFunctionName = out+"=" + \
                        functionName+"("+args+","+inpo+")"
                fullFunctions.append(newFunctionName)

            runningCode = ""
            for functionName in fullFunctions:
                runningCode = runningCode+"\n\t"+functionName

            additional_code = mainFunctionCode+runningCode
            out_file.writelines(additional_code)
            # if file completing successfull then status 1 else status 0
        return jsonify({'fileStatus': "1"})
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
