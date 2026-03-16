import time
import richWord as rw
import multiDictionary as md

class SpellChecker:

    def __init__(self):
        mult=md.MultiDictionary()
        self.dizL=mult.dizionariLingue

    def handleSentence(self, txtIn, language):
        risultato=[]
        multi =md.MultiDictionary()
        lista=txtIn.split()
        for e in lista:
            self.replaceChars(e)
        print("RICERCA NORMALE")
        for i in lista:
            risultato.append(multi.searchWord(i,language))
            check=multi.searchWord(i,language)
            if check.corretta:
                print(i)
            else:
                print(f"{i} (NOT FOUND)")
        print("="*60)
        print("RICERCA LINEARE")
        for i in lista:
            risultato.append(multi.searchWordLinear(i,language))
            check = multi.searchWordLinear(i, language)
            if check.corretta:
                print(i)
            else:
                print(f"{i} (NOT FOUND)")
        print("=" * 60)
        print("RICERCA DICOTOMICA")
        for i in lista:
            risultato.append(multi.searchWordDicotomic(i, language))
            check = multi.searchWordDicotomic(i, language)
            if check.corretta:
                print(i)
            else:
                print(f"{i} (NOT FOUND)")

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
