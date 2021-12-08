import os
import img2pdf

# Global Vars
n = 3                                                    # Chunk size (number of images per PDF file)
count = 1                                                # File counter
photolist = []                                           # Declared empty list
path = 'A:\Python Projects\Image to PDF\photos'          # Images location
f_ext = '.jpg'                                           # Image file extension

os.chdir(path)

for each in os.listdir():
    if each.endswith(f_ext):
        photolist.append(each)

newlist = [photolist[i * n:(i + 1) * n] for i in range((len(photolist) + n - 1) // n)]

for each in newlist:
    converted = img2pdf.convert(each)

    name = str(count) + '.pdf'
    file = open(name, 'wb')
    file.write(converted)
    file.close()

    print('Saved {} PDF file(s)' .format(count))
    count += 1

print('All images were converted to PDF files successfully.')