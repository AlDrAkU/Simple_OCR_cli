from ocr_class import Document
import sys

def main():

    for arg in sys.argv:
        if not "ocr.py" in arg:
            print(arg)
            doc = Document(arg)
            doc.run()


if __name__ == "__main__":

    main()