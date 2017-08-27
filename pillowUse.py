from PIL import Image

codeToRun = 3
if codeToRun is 0:
    img = Image.open("sampleImage.jpg")
    print(img.size)
    print(img.format)
    area = (100, 100, 3000, 4000)  # prepare a tuple
    croppedImg = img.crop(area)
    croppedImg.show()
    img.show()

elif codeToRun is 1:
    img1 = Image.open("12.jpg")
    img2 = Image.open("15.png")

    areaToPaste = (100, 100, 134, 134)   # calculate according to size of img2 image as isze of img2 is [34,34]
    img1.paste(img2, areaToPaste)

    img1.show()

elif codeToRun is 2:
    img = Image.open("sampleImage.jpg")

    print(img.mode)

    r, g, b = img.split()
   # r.show()
   # g.show()
   # b.show()

    newImage = Image.merge("RGB", (r, g, b))
    newImage.show()

elif codeToRun is 3:
    img = Image.open("12.jpg")
    # squareImage = img.resize((500, 500))
    # squareImage.show()
    # flipImage = img.transpose(Image.FLIP_LEFT_RIGHT)
    # flipImage.show()
    rotateImage = img.transpose(Image.ROTATE_90)
    rotateImage.show()



