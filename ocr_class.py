import os
import shutil
import fitz
from pytesseract import image_to_string


class Document:

    def __init__(self,file):
        self.file = file
        self.file_name = file.split("/")[1].split(".")[0]
        self.file_extension = file.split(".")[1]
        self.temp_page_list = []
        if not os.path.exists("temp/"):
            os.mkdir("temp/")
        if not os.path.exists("output/"):
            os.mkdir("output/")
    def write_to_file(self,name_file,string):
        text_file = open('output/{}.txt'.format(name_file), 'w')
        text_file.write(string)
        text_file.close()
    def cleanup(self):
        if os.path.exists("temp/"):
            shutil.rmtree("temp/")
    def split(self):
        mat = fitz.Matrix(200 / 72, 200 / 72)
        doc = fitz.open(self.file)
        for page in doc:

            pix = page.get_pixmap(matrix=mat)
            img_filename = "temp/page-%04i.png" % (page.number+1)
            self.temp_page_list.append(img_filename)
            pix.save(img_filename)
        return self.temp_page_list
    def run(self):
        if self.file_extension == 'pdf':
            self.split()
            for idx,p in enumerate(self.temp_page_list):
                txt = image_to_string(image=p)
                self.write_to_file(self.file_name+"_p{}".format(idx+1),txt)

        else:
            self.write_to_file(self.file_name,image_to_string(image=self.file))
        self.cleanup()