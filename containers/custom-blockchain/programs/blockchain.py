import datetime as d
import hashlib as h

class block:
    def __init__(self,index,timestamp,data,prevhash):
        self.index = index
        self.timestamp = timestamp
        self.data = data 
        self.prevhash = prevhash 
        self.hash = self.hashblock()

    def hashblock(self):
        unhash_content = str(self.index) + str(self.timestamp) + str(self.data) + str(self.prevhash)
        block_enc = h.sha256(unhash_content.encode('utf-8'))
        return block_enc.hexdigest()

    @staticmethod
    def genesisblock():
        return block(0,d.datetime.now(),"genesis block"," ")
    
    @staticmethod
    def newblock(lastblock,entry):
        index = lastblock.index+1
        timestamp = d.datetime.now()
        hashblock = lastblock.hash
        data = entry
        return block(index,timestamp,data,hashblock)


blockchain = [block.genesisblock()]
prev = blockchain[0]

while True:
    entry = input("enter the data to be in blockchain : ") 
    addblock = block.newblock(prev,entry) #  the block to be added to our chain 
    blockchain.append(addblock) # we add that block to our chain of blocks
    prev = addblock #now the previous block becomes the last block so we can add another one if needed

    print("Block ID #{} ".format(addblock.index)) # show the block id
    print("Timestamp:{}".format(addblock.timestamp))# show the block timestamp
    print("Hash of the block:{}".format(addblock.hash))# show the hash of the added block
    print("Previous Block Hash:{}".format(addblock.prevhash))# show the previous block hash
    print("data:{}\n".format(addblock.data))# show the transactions or data contained in that block

