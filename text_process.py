# import nltk
import pandas as pd

PATH = 'temp_ingredients.txt'
ING_PATH = 'ingr_text.txt'
class TextData:

    def __init__(self):
        self.ingredient_list = []



    def get_text(self):
        """Use simply to check/print text in temp_ingredients"""

        with open(PATH, "r") as f:
            text = f.readline()

        return text


    def string_splice(self): #use to make dict NOT new text file
        with open(PATH, "r") as f:
            text = f.readline()

            x = text.split(',')
            for i in x:
                with open(ING_PATH, "a") as nf:
                    nf.write(i)






    # NOT GOING TO USE NLP FOR THIS

    # def process_text(self):
    #     text = self.get_text()
    #
    #     tokens = nltk.word_tokenize(text) # --> tokens are type list
    #
    #     for i in tokens: # --> i is type str
    #         if len(i) > 3:
    #             self.ingredient_list.append(i) #appends each string to a local list (self.ingredients_list)
    #
    #     return tokens

    # def tester(self):
    #     """NOT WORTH HARD-CODING CHEMICAL NAMES IN...
    #     FIND NLP UNIT WHICH HAS CHEM. DICT"""
    #
    #     x = self.ingredient_list
    #
    #     for i, item in enumerate(x):
    #         if item == "ACID" or item == "ACIDS":
    #             word = f"{x[i-1]}" + " " + "ACID"
    #             # print(word)
    #             x[i] = word
    #             if item == x[i-1]:
    #                 x.pop(item[i])
    #
    #
    #
    #
    #             # print(x[i-1])
    #     print(x)





