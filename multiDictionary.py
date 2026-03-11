import dictionary as d
import richWord as rw
import resources as rs


class MultiDictionary:

    def __init__(self):
        diz=d.Dictionary()
        self.dizionariLingue= {
            "Italian":diz.loadDictionary("resources/Italian.txt"),
            "English": diz.loadDictionary("resources/English.txt"),
            "Spanish": diz.loadDictionary("resources/Spanish.txt")
        }


    def printDic(self, language):
        if language in self.dizionariLingue:
            d.Dictionary.printAll(self.dizionariLingue[language])
        else: pass





    def searchWord(self, word, language):

        if word in self.dizionariLingue[language]:
            rich=rw.RichWord(word)
            rich.corretta(True)
        else:
            rich = rw.RichWord(word)
            rich.corretta(False)

        return rich






