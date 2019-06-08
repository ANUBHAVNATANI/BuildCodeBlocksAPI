from database import db


def convertToArray(s):
    # function for converting a string to the array form
    # speration is "_" or "__"
    conv = []
    if (len(s) == 0):
        return [conv]
    b = s.split("  ")

    for i in b:
        conv.append(i.split(" "))
    return conv


def convertToDict(s):
    # function to convert in the dict
    # module for adding blocks for database
    conv = dict()
    if(len(s) == 0):
        return conv

    b = s.split(",")
    c = []
    for i in b:
        c.append(i.split("="))
    for j in c:
        conv[j[0]] = j[1]
    return conv


def addblock(blockName, args, ins, out, filePath):
    args = convertToDict(args)
    filePath = filePath.replace("\\", '/')
    # python way to split the data
    sect = filePath.split("/")
    out = convertToArray(out)
    # code change sigle array insted of multiple array
    if(len(ins) != 0):
        ins = ins.split(" ")
    else:
        ins = []
    # explicit addition of / in the file path
    block = {"blockName": blockName,
             "args": args, "filePath": filePath, "out": out, "in": ins}
    # Adding to database
    c = db
    for i in range(0, len(sect)-1):
        c = c.child(sect[i])
    c = c.child(blockName)
    c.set(block)
    return blockName
