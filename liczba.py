class Liczba:
    def __init__(self, number=0, use=False):
        self.number = number
        self.number_binary = bin(number)[2:]
        self.number_of_true_bits = self.bitstrue()
        self.use = use

    def __eq__(self, other):
        return self.number_of_true_bits == other.number_of_true_bits

    def __lt__(self, other):  # <
        return self.number_of_true_bits < other.number_of_true_bits

    def __str__(self):
        return str(self.number)

    def wyswietl(self):
        print(str(self.number) + " (" + self.number_binary + ")" + "-> " + str(self.number_of_true_bits))

    def __hash__(self):
        return hash(self.number_binary)

    def used(self):
        self.use = True

    def uzupelnij(self, long):
        for i in range(len(self.number_binary), long):
            self.number_binary = "0" + self.number_binary
        return self

    def bitstrue(self):
        suma = 0
        for i in self.number_binary:
            if i == "1":
                suma += 1
        return suma
