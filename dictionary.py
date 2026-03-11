class Dictionary:
    def __init__(self):

        self.parole = []


    def loadDictionary(self,path:str):

        with open(path, "r", encoding="utf-8") as fileInput:
            for parola in fileInput:
                self.parole.append(parola.strip())
        return self.parole


    def printAll(self):
        for parola in self.parole:
            print(parola)



    @property
    def dict(self):
        return self._dict