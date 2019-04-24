class Liczba:
    def __init__(self, number=0):
        self.number = number
        self.number_binary = bin(number)[2:]
        self.number_of_bits = bitsf(self.number_binary)

    #     self.status=0
    # @property
    # def status(self):
    #     return self.status
    # @status.setter
    # def status(self, new_one):
    #     self.status = new_one
    def __eq__(self, other):
        return self.number_of_bits == other.number_of_bits

    def __lt__(self, other):  # <
        return self.number_of_bits < other.number_of_bits

    def __str__(self):
        return str(self.number) + " (" + self.number_binary + ")" + "-" + str(self.number_of_bits)

    def __len__(self):
        return len(self.number_binary)

    def uzupelnij(self, long):
        for i in range(len(self.number_binary), long):
            self.number_binary = "0" + self.number_binary


def bitsf(binar):
    suma = 0
    for i in binar:
        if i == "1":
            suma += 1
    return suma
