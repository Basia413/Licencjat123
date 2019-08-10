import numpy as np
class Grupa:
    def __init__(self,strin,lis, use=False):
        self.number_binary=strin
        self.number=np.reshape(lis, np.size(lis))
        self.number_of_true_bits=self.bitstrue()
        self.use=use
    def __eq__(self, other):
        return self.number_binary==other.number_binary
    def __add__(self, other):
        for i in other.number:
            self.number.append(i)
        return self
    def __hash__(self):
        return hash(self.number_binary)
    def __str__(self):
        tym=""
        for j in self.number:
            tym+=str(j)+" "
        return tym# + ":"+ str(self.number_binary)
    def __repr__(self):
        return self.number_binary
    def used(self):
        self.use=True
    def bitstrue(self):
        suma = 0
        for i in self.number_binary:
            if i == "1":
                suma += 1
        return suma


