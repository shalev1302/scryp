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
    difficulty=4
    def __init__(self,chain=[]):
        self.chain=chain
    def add(self,block):
        self.chain.append({
            'hash':block.hash(),
            'previous':block.previeos_hash,
            'number':block.number,
            'data':block.data,
            'nonce':block.nonce
        })

    def __str__(self):
        ret=""
        for block in self.chain:
            ret+=str(block)
        return ret

def main():
    block=Block("welcome",1)
    bc=BlockChain()
    bc.add(block)
    print(bc)
if __name__ == '__main__':
    main()