'''
	Exceptions and unit tests
	Data 558 HW4
	Diana Chenyu Zhang
'''

import urllib3
import unittest
import os
from get_data import dataGetter



url = "https://data.seattle.gov/resource/4xy5-26gy.csv"
filename = os.path.basename(url)

class TestDataGetter(unittest.TestCase):
	def testFileExist(self):
		if os.path.exists(filename):
			print("File exists")
		else:
			print("Create a file", filename)
			f = open(filename, "w")

		result = dataGetter(url)
		test = "File exists"
		self.assertEqual(result, test)
	def testFileNotExist(self):
		result = dataGetter(url)
		test = "Download successfully"
		self.assertEqual(result, test)

	def testUrlInvalid(self):
		fakeurl = "https://ata.seattle.gov/resource/aaaa.csv"
		result = dataGetter(fakeurl)
		test = "invalid url"
		self.assertEqual(result, test)

if __name__ == '__main__':
	unittest.main()