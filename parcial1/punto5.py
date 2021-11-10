import hashlib
from os import listdir
from os.path import isdir, islink


for file in listdir("."):
    if not isdir(file) and not islink(file):
        try:
            f = open(file, "rb")
        except IOError as e:
            print(e)
        else:
            data = f.read()
            f.close()
            print(file + ": ")
            h = hashlib.sha1()
            h.update(data)
            try:
                hexdigest = h.hexdigest()
            except TypeError:
                hexdigest = h.hexdigest()

            print("Sha1: " + hexdigest)