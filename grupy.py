class Grupa:
    def __init__(self,strin,lis):
        self.kombinacja_bina=strin
        self.lista=lis
    def __eq__(self, other):
        return self.kombinacja_bina==other.kombinacja_bina
    def __add__(self, other):
        self.lista=self.lista+other.nowe_liczby
    @property.setter
    def kombinacja_bina(self, nowa):
        self.kombinacja_bina=nowa


