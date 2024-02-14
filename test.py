import pandas as pd
import json

#test converting dicts to df's

def pad_list(dict_list, padel):
    lmax = 0
    for lname in dict_list.keys():
        lmax = max(lmax, len(dict_list[lname]))
        for lname in dict_list.keys():
            ll = len(dict_list[lname])
            if ll < lmax:
                dict_list[lname] += [padel] * (lmax - ll)
        return dict_list


text_dict = {
    "k1": ['WATER (759)', 'SUGARS (12%)', '(GLUCOSE (48%)', 'FRUCTOSE (40%)'],
    "k2": ['SUCROSE (2%)', 'WATER (759)', 'SUGARS (12%)'],
    "k3": ['(GLUCOSE (48%)', 'WATER (759)', 'STARCH(5%)', 'LYSINE(5%)'],
}

text_dict = pad_list(text_dict, " ")
print(text_dict)


# with open('my_dict.json', 'w') as f:
#     json.dump(my_dict, f)
#

#
# with open('my_dict.json') as f:
#     my_dict = json.load(f)
#

# df = pd.DataFrame(text_dict)
# print(df)


#  --USE LATER--
# df.to_csv('test.csv', index=False)
# df2 = pd.read_csv('test.csv')
# print(df2)