from image_process import ImageData
from text_process import TextData

def save_ings():
    gd = ImageData()
    gd.get_data()

def main():
    save_ings()

    x = TextData()
    test = x.get_text()
    split_text = x.string_splice()
    print(test)
    print(" ")
    split_text



if __name__ == "__main__":
    main()
