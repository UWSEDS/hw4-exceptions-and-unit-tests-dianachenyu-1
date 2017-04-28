'''
	Exceptions and unit tests
	Data 558 HW4
	Diana Chenyu Zhang
'''
import os
import urllib3


def dataGetter(url):
	http = urllib3.PoolManager()
	filename = os.path.basename(url)
	try: 
		if os.path.exists(filename):
			print ("File exists")
			test = "File exists"
		else: 
			file = http.request('GET', url)
			with open(filename, 'wb') as f:
				f.write(file.data)
				f.close()
			print("Download successfully")
			test = "Download successfully"
	except:
		print("invalid url")
		test = "invalid url"
	return test
