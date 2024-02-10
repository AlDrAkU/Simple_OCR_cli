import unittest
from ocr_class import Document

class TestDocument(unittest.TestCase):

    def test_pdf_file(self):
        file = "example.pdf"
        document = Document(file)
        self.assertEqual(document.file_extension, "pdf")
        self.assertEqual(document.file_name, "example")

    def test_non_pdf_file(self):
        file = "example.png"
        document = Document(file)
        self.assertNotEqual(document.file_extension, "pdf")
        self.assertEqual(document.file_name, "example")

if __name__ == '__main__':
    unittest.main()
