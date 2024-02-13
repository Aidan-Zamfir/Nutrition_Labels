import easyocr


class ImageData:
    """Image recognition software used to extract text from nutrition label
     (WORKS as intended, make changes in text_process.py file)"""

    def __init__(self):
        self.image_path = "Labelling_ingredients_list.jpg" # change to folder


    def get_data(self):

        reader = easyocr.Reader(['en'], gpu=False)
        result = reader.readtext(self.image_path)

        for i in result:
            text = i[1]


            with open('temp_ingredients.txt', "a") as f:
                    f.write(text)

