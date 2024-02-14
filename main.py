from image_process import ImageData
from text_process import TextData
from use_data import DataAnalysis

def image_recognition(): #get data from image
    gd = ImageData()
    gd.get_data()

def use_text_data(): #make to text useable for dataframes
    x = TextData()

    split_text = x.string_splice('key1')  # user input food item and/or read from label (?)
    split_text


def data_analysis(): #use data to make df and graphs
    y = DataAnalysis()
    dataf = y.create_df()

    print(dataf) #for testing purposes. Delete later



def main():
    # image_recognition()
    use_text_data()
    data_analysis()



if __name__ == "__main__":
    main()
