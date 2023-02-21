import zipfile
import os


files_zip = [filename for filename in os.listdir('.') if zipfile.is_zipfile(filename)]

# with zipfile.ZipFile('workbook.zip') as z_file:
#     z_file.printdir()




