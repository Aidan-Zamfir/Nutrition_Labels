import pandas as pd
import json

PATH = 'temp_ingredients.txt'

class TextData:
    """Takes ingredients from lable, creates dict. for dataframe to use"""

    def __init__(self):
        self.ingredient_dict = {}
        self.ingredient_list = [] #for string_splice() to add to dict


    def string_splice(self, food_item): #use to make dict & JSON

        with open(PATH, "r") as f:
            text = f.readline()

            x = text.split(',')
            for i in x[1:]: #itterate over ingreds. (skip first item) and add to local list
                self.ingredient_list.append(i)

            self.ingredient_dict = {food_item: self.ingredient_list}

        with open('ingredient_dictionary.json', 'a') as f:
            json.dump(self.ingredient_dict, f)

