from PIL import Image

def curateImages(image1,image2):
    # If images are not RGB, convert them to RGB
    if (image1.mode != 'RGB'):
        image1 = image1.convert('RGB')
    if (image2.mode != 'RGB'):
        image2 = image2.convert('RGB')

def compareImages(image1,image2):
    #Check if the image sizes are same
    if(image1.size == image2.size):

        #lists to get image pixels in tuple form
        pixel1List = list(image1.getdata())
        pixel2List = list(image2.getdata())

        count = 0
        black = (0, 0, 0)
        white = (255, 255, 255)

        #new image to store the final result in black and white
        comparisonList = list()

        #compares colors of two images and puts white color for pixels where pixel-wise comparison gives true
        #and black color for pixels where pixel-wise comparison gives false
        for index , pixel in enumerate(pixel1List):
            if(pixel != pixel2List[index]):
                comparisonList.append(black)
                count += 1
            else:
                comparisonList.append(white)
        print "Total number of different pixels in the image: ", count
        return comparisonList
    else:
        print "Unable to compare. Ensure that the images are of the same size"
        return None

def saveImage(comparisonList):
    comparison = Image.new('RGB', image1.size)
    comparison.putdata(comparisonList)
    comparison.save("Comparison.png", 'PNG')

# map the images that you would like to compare here
image1 = Image.open('Image3.png')
image2 = Image.open('Image4.png')
curateImages(image1,image2)
comparisonList = compareImages(image1, image2)
if(comparisonList != None):
    saveImage(comparisonList)
else:
    print"Please try again with the correct images"