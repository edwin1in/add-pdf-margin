from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

images = convert_from_path("test.pdf")

width = images[0].width
height = images[0].height

c = canvas.Canvas(".pdf", pagesize=(width+3000, height))
c.drawImage(ImageReader(images[0]),0,0, width=width, height=height)
c.save()






