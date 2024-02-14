from image_process import ImageData
from text_process import TextData

def image_recognition():
    gd = ImageData()
    gd.get_data()

def use_text_data():
    x = TextData()
    # test = x.get_text()
    # print(test)

    split_text = x.string_splice('key1')  # user input food item
    split_text

    d = x.make_df()
    print(d)



def main():
    # image_recognition()
    use_text_data()


if __name__ == "__main__":
    main()
