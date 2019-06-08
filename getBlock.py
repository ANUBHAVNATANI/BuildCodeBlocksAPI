from database import db
# Module to get blocks from the database


def getblock(json):
    # specific type of data demanding code
    # lang resp need
    # can be defined more precisely
    typer = json["type"]
    # block returning code
    allBlocks = db.child(typer).get()
    return allBlocks
