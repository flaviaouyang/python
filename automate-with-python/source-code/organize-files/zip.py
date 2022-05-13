import zipfile, send2trash

# create a ZipFile object
zip_file = zipfile.ZipFile("reading-zip.zip")
# list contents within the zip file
print(zip_file.namelist())

cat_info = zip_file.getinfo("reading-zip/cat.txt")
print(cat_info)
print(cat_info.file_size)
print(cat_info.compress_size)
zip_file.extractall()
send2trash.send2trash("./reading-zip")
zip_file.close()

new_zip = zipfile.ZipFile("create_zip.zip", "w")
new_zip.write("jules.txt", compress_type=zipfile.ZIP_DEFLATED)
new_zip.close()