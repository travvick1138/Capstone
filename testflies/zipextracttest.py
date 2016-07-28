

import zipfile
import contextlib

# fh = open('Alex And Ada Vol 1.cbz','rb')
# z = zipfile.ZipFile(fh)
# for name in z.namelist():
#     outfile = open('Comicextractions'+'/'+name, 'wb')
#     outfile.write()
#     outfile.close()
# fh.close()

with contextlib.closing(zipfile.ZipFile('Alex And Ada Vol 1.cbz', "r")) as comic:
    comic.extractall("Comicextractions\\")
#     with myzip.open('0001.jpeg') as myfile:
#     print(myfile.read())
#
# comic = open('Alex And Ada Vol 1.cbz', "rb")
# =C:\\Users\\travv\\Python\\Python35-32\\Lib\\site-packages\\UnrarDLL\\UnRAR.lib
