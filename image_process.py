import easyocr


class ImageData:
    """Text recognition from image -> used to extract ingredients from nutrition label
    and store them in a format which can be used for dataframes.
     (WORKS as intended dont change till end)"""

    def __init__(self):
        self.image_path = "Labelling_ingredients_list.jpg" # change to folder


    def get_data(self): #change to acess text directly rather than from txt file

        reader = easyocr.Reader(['en'], gpu=False)
        result = reader.readtext(self.image_path)

        for i in result:
            text = i[1]

            with open('temp_ingredients.txt', "a") as f:
                    f.write(text)
