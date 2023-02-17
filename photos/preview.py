import os
from PIL import Image
files = os.listdir('.')
i = 0
length = len(files)
while i < length:
    if 'jpg' in files[i] or 'JPG' in files[i]:
        image = Image.open(files[i])
        image.thumbnail((200, 125))
        image.save('./preview/' + files[i])
    i = i + 1
