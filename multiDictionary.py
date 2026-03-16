import dictionary as d
import richWord as rw
import resources as rs


class MultiDictionary:

    def __init__(self):
        diz = d.Dictionary()
        self.dizionariLingue = {
            "italian": diz.loadDictionary("resources/Italian.txt"),
            "english": diz.loadDictionary("resources/English.txt"),
            "spanish": diz.loadDictionary("resources/Spanish.txt")
        }

    def printDic(self, language):
        if language in self.dizionariLingue:
            d.Dictionary.printAll(self.dizionariLingue[language])
        else:
            pass

    def searchWord(self, word, language):

        if word.lower() in self.dizionariLingue[language]:
            rich = rw.RichWord(word)
            rich.corretta = True
        else:
            rich = rw.RichWord(word)
            rich.corretta = False

        return rich

    def searchWordLinear(self, word, language):
        dizionarioCorrente = self.dizionariLingue[language]
        riw=rw.RichWord(word)
        for parola in dizionarioCorrente:
            if parola==word:
                riw.corretta=True
                return riw
            riw.corretta=False
        return riw

    def searchWordDicotomic(self, word, language):
        dizionarioCorrente = self.dizionariLingue[language]
        left, right=0, len(dizionarioCorrente)-1
        riw=rw.RichWord(word)
        parola=word.lower()
        while left<=right:
            mid=(left+right)//2
            mid_val=dizionarioCorrente[mid]
            if mid_val==parola:
                riw.corretta=True
                return riw
            elif mid_val<parola:
                left=mid+1
            else:right=mid-1
        riw.corretta=False
        return riw  #SE NON LA TROVO