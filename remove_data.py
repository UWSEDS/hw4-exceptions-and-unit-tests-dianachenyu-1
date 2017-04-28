'''
    Exceptions and unit tests
    Data 558 HW4
    Diana Chenyu Zhang
'''

import os

def dataRemover(url):
    filename = os.path.basename(url)
    if os.path.exists(filename):
        os.remove(filename)
        print("Delete data successfully")
        test = "Delete data successfully"
    else:
        print("Can't find the file to delete")
        test = "Deletion failed"
    return test