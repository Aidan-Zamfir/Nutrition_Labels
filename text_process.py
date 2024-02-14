import pandas as pd
import json

PATH = 'temp_ingredients.txt'

class TextData:
    """Takes ingredients from lable, creates dict. for dataframe to use"""

    def __init__(self):
        self.ingredient_dict = {}
        self.temp_ing_list = [] #for string_splice() to add to dict



    def get_text(self): #delete later
        """Use simply to check/print text in temp_ingredients"""

        with open(PATH, "r") as f:
            text = f.readline()

        return text


    def string_splice(self, food_item): #use to make dict NOT new text file
        """Make 'key' for dict th name of product:
        should be an arg in function to input name (somewhere from main)"""

        with open(PATH, "r") as f:
            text = f.readline()

            x = text.split(',')
            for i in x[1:]: #itterate over ingreds. (skip first item) and add to local list
                self.temp_ing_list.append(i)

            self.ingredient_dict = {f"{food_item}": self.temp_ing_list}

        return self.ingredient_dict

    def make_df(self):
        df = pd.DataFrame(self.ingredient_dict)

        print(df)








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





