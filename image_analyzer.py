from argparse import FileType
from PIL import Image
import filetype
import sqlite3

def image_analyzer(image_path):
    if filetype.is_image(image_path):
        image = Image.open(image_path).convert('RGB')
        pixel_dictionary = {}
        image_width = image.width;
        image_height = image.height;
        image_size = image_width * image_height
        for width in range(image_width):
            for height in range(image_height):
                r,g,b = image.getpixel((width, height))
                pixel = r,g,b
                if pixel in pixel_dictionary:
                    pixel_dictionary[pixel] += 1;
                else:
                    pixel_dictionary[pixel] = 1;
        for x, y in pixel_dictionary.items():
            y = round(y * 100 / image_size)
            pixel_dictionary.update({x:y})
        return pixel_dictionary
    else:
        raise TypeError("file is not image")        

image = image_analyzer("test.png")

#results conversion to save it to db
list_for_db = []
for x, y in image.items():
    x = str(x)
    y = str(y)
    thistuple = (x,y)
    list_for_db.append(thistuple)

con = sqlite3.connect('database.db')
cur = con.cursor()

cur.execute('''DROP TABLE image''')
cur.execute('''CREATE TABLE IF NOT EXISTS image (color txt, color_value txt)''')
cur.executemany("INSERT OR IGNORE INTO image VALUES (?,?)", list_for_db)

con.commit()