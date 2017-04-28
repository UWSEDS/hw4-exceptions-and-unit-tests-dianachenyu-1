'''
    Exceptions and unit tests
    Data 558 HW4
    Diana Chenyu Zhang
'''


from remove_data import dataRemover
import unittest
import os

url = "https://data.seattle.gov/resource/4xy5-26gy.csv"
filename = os.path.basename(url)


class TestDataRemover(unittest.TestCase):
    def testFileExists(self):

        if os.path.exists(filename):
            print("File exists")
        else:
            print("Create a file name", filename)
            f = open(filename, "w")

        print("Testing remove file exists.")
        result = dataRemover(url)
        test = "Delete data successfully"
        self.assertEqual(result, test)

    def testFileNotExists(self):
        if os.path.exists(filename):
            os.remove(filename)

        print("Testing remove file does not exist.")
        result = dataRemover(url)
        test = "Deletion failed"
        self.assertEqual(result, test)


if __name__ == "__main__":
    unittest.main()
