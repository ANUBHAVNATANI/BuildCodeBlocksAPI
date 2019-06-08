# module for the code genearation
import os
from mainFunctionCode import pythonMainFunction
from cleanup import importLineup


def argGen(args, inpv=None):
    s = ""
    if(type(args) != dict and inpv == None):
        return s
    if(type(args) != dict):
        for inputName in inpv:
            s = s+inputName+","
        s = s[:-1]
        return s
    if(inpv == None):
        for key, value in args.items():
            s = s+key+"="+value+","
            s = s[:-1]
        return s
    else:
        for inputName in inpv:
            s = s+inputName+","
        for key, value in args.items():
            s = s+key+"="+value+","
        s = s[:-1]
        return s


def outVarGen(out, number):
    s = ""
    outv = dict()
    for i in range(len(out)):
        s = s+out[i]+str(number)+","
        outv[out[i]] = out[i]+str(number)
    s = s[:-1]
    return s, outv


def inputMap(inp, currFunctionList):
    # function for searching compatible output for the inputs
    if(len(currFunctionList) != 0):
        nameList = [function["blockName"] for function in currFunctionList]
    inpv = []
    for key, value in inp.items():
        # exception handling should be done here or at the front end
        # As if not in the list then there will be an error
        if(value == "user"):
            inpv.append("user")
        else:
            index = nameList.index(value)
            inpv.append(currFunctionList[index]["outv"][key])
    return inpv


def codeGenerator(json):
    filePaths = [block["filePath"] for block in json["blocks"]]
    # compiling the file paths from the database
    filepathMaster = os.path.join(os.getcwd(), "covFile.py")

    for i in range(len(filePaths)):
        rfilePath = filePaths[i]
        # path gen code
        filePaths[i] = os.path.join(
            os.getcwd(), "Blocks", rfilePath)
    # reversing file paths for the correct order
    # reversing filepath is not necessary
    # filePaths.reverse()
    # writing output to another file
    with open(filepathMaster, "w") as out_file:
        for filePath in filePaths:
            with open(filePath, "r") as in_file:
                for l in in_file.readlines():
                    out_file.writelines(l)
                out_file.writelines("\n\n")
        # Main function code for running the code generated in the recent file
        mainFunctionCode = pythonMainFunction
        # Combining Function Code with args and input and outputs
        fullFunctions = []
        # not needed but of safety purposes
        currFunctionList = []
        for i in range(len(json["blocks"])):
            function = json["blocks"][i]
            # giving unique number to each function
            function["number"] = i

            functionName = function["blockName"]
            args = function["args"]
            out = function["out"]
            inp = function["in"]
            # can support multiple input by split function
            # can be a flaw of cheking from the back to see for the inputs as the first one is also giving the input insted
            # to be corrected with good algoithms
            # out to be taken to be selected
            # datastructure for out selection
            outs, outv = outVarGen(out, i)
            function["outv"] = outv
            # new datastructure for the input
            # selected by user that out only comes
            if(len(inp) == 0):
                newFunctionName = outs+"="+functionName+"("+argGen(args)+")"
            else:
                inpv = inputMap(inp, currFunctionList)
                newFunctionName = outs+"=" + \
                    functionName+"("+argGen(args, inpv)+")"
            currFunctionList.append(function)
            fullFunctions.append(newFunctionName)

        runningCode = ""
        for functionName in fullFunctions:
            runningCode = runningCode+"\n\t"+functionName

        additional_code = mainFunctionCode+runningCode
        out_file.writelines(additional_code)
    importLineup(filepathMaster)
    return 1
