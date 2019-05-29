from flask import Flask, request, jsonify
import traceback
import os
import json
# API definition
app = Flask(__name__)


@app.route("/")
def home():
    return "This is an api that provieds info about the blocks"

# this code generates a cov_file in which the resulting code resides till now
@app.route('/giveBlock', methods=['POST', 'GET'])
def block():
    try:
        # json file with the requirements from the client side
        json_ = request.json
        # getting file paths from the database
        # getting the json files and list of filepaths from the json file
        # json_[filePaths] is the list containing the relative file paths of the files
        filePaths = json_["filePaths"]

        # compiling the file paths from the database
        basepath = os.path.dirname(__file__)
        filepath_master = os.path.abspath(
            os.path.join(basepath, "..", "..", "/covFile.py"))
        for i in range(len(filePaths)):
            rfilePath = filePaths[i]
            # path gen code
            filePaths[i] = os.path.abspath(
                os.path.join(basepath, "..", "..", rfilePath))
        filePaths.reverse()
        with open(filepath_master, "w") as out_file:
            for filePath in filePaths:
                with open(filePath, "r") as in_file:
                    for l in in_file.readlines():
                        out_file.writelines(l)
                    out_file.writelines("\n\n")
            # Main function code for running the code generated in the recent file
            mainFunctionCode = 'if __name__ == "__main__":'
            # Combining Function Code with args
            fullFunctions = []

            for i in range(len(json_["function"])):
                function = json_["function"][i]
                functionName = function["functionName"]
                args = function["args"]
                out = function["out"]
                newFunctionName = out+"="+functionName+"("+args+")"
                fullFunctions.append(newFunctionName)

            runningCode = ""
            for functionName in fullFunctions:
                runningCode = runningCode+"\n\t"+functionName

            additional_code = mainFunctionCode+runningCode
            out_file.writelines(additional_code)

        what_code_get = "Write in next lines code to get code"
        return jsonify({'code': str(what_code_get)})
    except:
        return jsonify({'trace': traceback.format_exc()})


if __name__ == '__main__':

    app.run(debug=True)
