class HillCipher:
    def __init__(self, key): # key in the form of [[a, c]^T, [b, d]^T]
        self.key = key
    
    def charToInt(char):
        return (ord(char.capitalize()) - 65)
    
    def groupInts(ints): # integer list
        # adds dummy integer if odd number of letters
        if((len(ints) % 2) != 0):
            ints.append(0)

        output = []
        for i in range(0, len(ints) - 2, 2):
            output += [ints[i], ints[i + 1]]
    
    def encrypt(self, text):
        