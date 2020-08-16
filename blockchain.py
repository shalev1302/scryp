from hashlib import sha256
def updatehash(*args):
    hashing_text="";h=sha256()
    for arg in args:
        hashing_text+=str(arg)
    h.update(hashing_text.encode('utf-8'))
    return  h.hexdigest()

class Block:
    data = None
    hash = None
    nonce = 0
    previeos_hash = "0" * 64
    def __init__(self,data,number=0):
        self.data=data
        self.number=number
    def hash(self):

        return ( updatehash(self.previeos_hash,self.number,self.data,self.nonce))
    def __str__(self):
        return ("#BLOCK:%s\ndata:%s\nhash:%s\nnoonce:%s\nprevieos:%s\n"%(self.number,
                                                                         self.data,self.hash(),
                                                                         self.nonce,
                                                                         self.previeos_hash))

class BlockChain():
    difficulty=5
    def __init__(self,chain=[]):
        self.chain=chain
    def add(self,block):
        self.chain.append(block)

    def __str__(self):
        ret=""
        for block in self.chain:
            ret+=str(block)+"\n"
        return ret
    def mine(self,block):
        try:
            block.previeos_hash=self.chain[-1].hash()
        except IndexError:
            pass
        while True:
            if block.hash()[:self.difficulty]=="0"*self.difficulty:
                self.add(block);break
            else:
                block.nonce+=1
    def isValid(self):
        for i in range(1,len(self.chain)):
            if i==1:
                if self.chain[0].hash()[:self.difficulty] != "0" * self.difficulty:
                    return False
            if self.chain[i].hash()[:self.difficulty]!="0"*self.difficulty:
                return False

            if self.chain[i-1].hash()!=self.chain[i].previeos_hash:
                return False
            return  True
def main():

    bc=BlockChain()
    database=["hello world","whats up","hello","bye"]
    num=0
    for data in database:
        num+=1
        bc.mine(Block(data,num))
    print(bc.isValid())

if __name__ == '__main__':
    main()