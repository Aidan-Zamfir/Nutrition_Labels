import pandas as pd
import json

class DataAnalysis:
    """Imports dictionary from JSON, creates df & graphs frequency of ingredients"""

    def __init__(self):
        pass


    def pad_list(self, dict_list, padel):
        """Make all nested ingredient lists in dict. the same length"""

        lmax = 0
        for i in dict_list.keys():
            lmax = max(lmax, len(dict_list[i]))
            for i in dict_list.keys():
                ll = len(dict_list[i])
                if ll < lmax:
                    dict_list[i] += [padel] * (lmax - ll)
            return dict_list


    def get_json(self):
        """Access dict from JSON, make dict. useable for methods"""

        with open('ingredient_dictionary.json') as f:
            ingredient_dict = json.load(f)

        return ingredient_dict

    def create_df(self):
        """Take dict. from JSON, add padding, put it into a df"""

        ingredient_dict = self.get_json()
        padded_dictionary = self.pad_list(ingredient_dict, " ")
        df = pd.DataFrame(padded_dictionary)

        return df


    def graph_data(self):
        """Get actual data comparing food items etc...."""
        pass
