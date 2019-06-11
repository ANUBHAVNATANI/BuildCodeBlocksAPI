from database import db
# Module to get blocks from the database


def getblock(qtype):
    # specific type of data demanding code
    # lang resp need
    # can be defined more precisely
    # block returning code
    qtype = str(qtype)
    allBlocks = db.child(qtype).get()
    return allBlocks
