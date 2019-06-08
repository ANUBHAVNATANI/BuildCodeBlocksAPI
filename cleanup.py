import os

# module to line up the imports


def importLineup(filepathMaster):
    with open(filepathMaster) as f:
        datafile = f.readlines()
    imports = []
    for line in range(len(datafile)):
        if(datafile[line][0:6] == "import" or datafile[line][0:4] == "from"):
            imports.append(datafile[line])
            datafile[line] = "\n"
    with open(filepathMaster, "w") as out_file:
        for line in imports:
            out_file.writelines(line)
        for line in datafile:
            out_file.writelines(line)
