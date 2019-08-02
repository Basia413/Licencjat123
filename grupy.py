class Grupa:
    def __init__(self,strin,lis):
        self.number_binary=strin
        self.number=lis
        self.number_of_true_bits=self.bitstrue()
    def __eq__(self, other):
        return self.number_binary==other.number_binary
    def __add__(self, other):
        for i in other.number:
            self.number.append(i)
        return self
    def __str__(self):
        tym=""
        for j in self.number:
            tym+=str(j)+" "
        return tym# + ":"+ str(self.number_binary)

    def bitstrue(self):
        suma = 0
        for i in self.number_binary:
            if i == "1":
                suma += 1
        return suma


