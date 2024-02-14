import pandas as pd
import json

class DataAnalysis:
    """Import JSON file with dict, creates df & graphs frequency of ingredients"""

    def __init__(self):
        pass

    #make funcs to get data from JSON, create df, etc
    def pad_list(self, dict_list, padel):

        lmax = 0
        for i in dict_list.keys():
            lmax = max(lmax, len(dict_list[i]))
            for i in dict_list.keys():
                ll = len(dict_list[i])
                if ll < lmax:
                    dict_list[i] += [padel] * (lmax - ll)
            return dict_list


    def create_df(self):
        with open('ingredient_dictionary.json') as f:
            ingredient_dict = json.load(f)

        #pad_list()
        #dict to df
        pass





