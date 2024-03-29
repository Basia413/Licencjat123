class Number:
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
        return str(self.number) + " : " + self.number_binary

    def wyswietl(self):
        print(str(self.number) + " (" + self.number_binary + ")" + "-> " + str(self.number_of_true_bits))

    def __hash__(self):
        return hash(self.number_binary)

    def __len__(self):
        i = 0
        for j in self.number_binary:
            if j == "0" or j == "1":
                i += 1
        return i

    def __int__(self):
        return int(self.number)

    def used(self):
        self.use = True

    def fill_with_zeros(self, long):
        for i in range(len(self.number_binary), long):
            self.number_binary = "0" + self.number_binary
        return self

    def bitstrue(self):
        sum1 = 0
        for i in self.number_binary:
            if i == "1":
                sum1 += 1
        return sum1
