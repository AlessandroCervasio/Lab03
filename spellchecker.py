import time
import richWord as rw
import multiDictionary as md

class SpellChecker:

    def __init__(self):
        mult=md.MultiDictionary()
        self.dizL=mult.dizionariLingue

    def handleSentence(self, txtIn, language):
        risultato=[]
        lista=txtIn.split()
        for e in lista:
            self.replaceChars(e)

        for i in lista:
            md.searchWord

        return risultato



    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


    def replaceChars(self,text):
        chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
        for c in chars:
            text = text.replace(c, "")
        return text
