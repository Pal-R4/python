import barcode
from barcode.writer import ImageWriter
text="python programming"
text1=str(text)
code=barcode.get_barcode_class("code128")
image=code(text,writer=ImageWriter())
img=image.save("my final barcode")
