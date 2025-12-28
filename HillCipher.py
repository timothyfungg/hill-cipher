class HillCipher:
    def __init__(self, key): # key in the form of row matrix [[a, b], [c, d]]
        self.key = key
    
    def charToInt(cls, char):
        return (ord(char.capitalize()) - 65)
    
    def groupInts(cls, ints): # integer list
        # adds dummy integer if odd number of letters
        if((len(ints) % 2) != 0):
            ints.append(0)

        pairs = []
        for i in range(0, len(ints) - 2, 2):
            pairs.append([ints[i], ints[i + 1]])
        
        return pairs # pairs in the form of [[a_1, a_2], [a_3, a_4], . . .], where each list is a column vector
    
    def encrypt(self, text):
        ints = []
        for i in range(0, len(text)):
            ints.append(HillCipher.charToInt(text[i]))
        
        pairs = HillCipher.groupInts(ints)
        encryptedPairs = []
        for i in range(0, len(pairs)):
            pairs += []

        # matrix multiply key * pairs[i]
        for i in range(0, len(pairs)):
            for j in range(0, 2):
                encryptedPairs[i].append((self.key[0][0] * pairs[i][0]) + (self.key[0][1] * pairs[i][1]))
                encryptedPairs[i].append((self.key[1][0] * pairs[i][0]) + (self.key[1][1] * pairs[i][1]))

        return encryptedPairs