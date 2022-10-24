import cv2
import pytesseract

imgSpa = cv2.imread('images/spa.jpg')
imgEngHand = cv2.imread('images/engHand.jpg')
imgEngBlack = cv2.imread('images/engBlack.jpg')
imgPol = cv2.imread('images/pol.jpg')
imgPolBlack = cv2.imread('images/polBlack.jpg')

a = pytesseract.image_to_string(imgSpa, lang='spa')
b = pytesseract.image_to_string(imgPol, lang='pol')
c = pytesseract.image_to_string(imgEngHand, lang='eng')
d = pytesseract.image_to_string(imgPolBlack, lang='pol')
e = pytesseract.image_to_string(imgEngBlack, lang='eng')
print(d)