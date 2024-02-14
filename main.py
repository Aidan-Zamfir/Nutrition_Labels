from image_process import ImageData
from text_process import TextData
from use_data import DataAnalysis

def image_recognition():
    gd = ImageData()
    gd.get_data()

def use_text_data():
    x = TextData()

    # test = x.get_text()
    # print(test)

    split_text = x.string_splice('key1')  # user input food item
    split_text


def data_analysis():
    y = DataAnalysis()
    dataf = y.create_df()

    print(dataf)



def main():
    # image_recognition()
    use_text_data()
    data_analysis()



if __name__ == "__main__":
    main()
