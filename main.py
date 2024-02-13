from image_process import ImageData
from text_process import TextData

def save_ings():
    gd = ImageData()
    gd.get_data()

def main():
    # save_ings()

    x = TextData()
    x.process_text()
    print(x.ingredient_list)
    x.tester()




if __name__ == "__main__":
    main()
