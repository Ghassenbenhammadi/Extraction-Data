from pdf2image import convert_from_path

# This library is for extract the data from image using easyocr
import matplotlib.pyplot as plt
import cv2
import easyocr
from pylab import rcParams
from IPython.display import Image

def converterPDFToImage(urlPDF):
    # Store Pdf with convert_from_path function
    images = convert_from_path(urlPDF,500,poppler_path=r'C:\Program Files\poppler-22.04.0\Library\bin')
    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save('Images/ImagesFromFrontEnd/Image.jpg', 'JPEG')
        # images.save('Images/ImagesFromFrontEnd/Image.jpg', 'JPEG')

    return 'Images/ImagesFromFrontEnd/Image.jpg'

def getDataFromImage(imageData):
    rcParams['figure.figsize'] = 8, 16
    reader = easyocr.Reader(['fr'])
    output = reader.readtext(imageData)
    cord = output[-8][0]
    x_min, y_min = [int(min(idx)) for idx in zip(*cord)]
    x_max, y_max = [int(max(idx)) for idx in zip(*cord)]
    image = cv2.imread(imageData)
    cv2.rectangle(image,(x_min,y_min),(x_max,y_max),(0,0,255),2)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.savefig('Images/ImagesAfterExtraction/image.png')

# converterPDFToImage("C:\\Users\\asus\\Desktop\\Nouveau dossier\\PFE\\Backend-Pfe\\authUsers\\Uploaded Files\\file (5).pdf")