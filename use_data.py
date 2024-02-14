import pandas as pd
import json

class DataAnalysis:
    """Imports dictionary from JSON, creates df & graphs frequency of ingredients"""

    def __init__(self):
        pass


    def pad_list(self, dict_list, padel):

        lmax = 0
        for i in dict_list.keys():
            lmax = max(lmax, len(dict_list[i]))
            for i in dict_list.keys():
                ll = len(dict_list[i])
                if ll < lmax:
                    dict_list[i] += [padel] * (lmax - ll)
            return dict_list


    def get_json(self):

        with open('ingredient_dictionary.json') as f:
            ingredient_dict = json.load(f)

        return ingredient_dict

    def create_df(self):
        ings = self.get_json()

        padded_dictionary = self.pad_list(ings, " ")

        df = pd.DataFrame(padded_dictionary)
        return df


    def graph_data(self):
        pass
