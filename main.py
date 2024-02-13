from image_process import ImageData
from text_process import TextData

def save_ings():
    gd = ImageData()
    gd.get_data()

def main():
    # save_ings()

    x = TextData()

    # test = x.get_text()
    # print(test)
    # print(" ")

    split_text = x.string_splice()
    split_text

    d = x.make_df()
    print(d)



if __name__ == "__main__":
    main()
