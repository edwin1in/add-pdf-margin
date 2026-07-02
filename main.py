from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError,
)
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader


def change_margin(
    pdfpath: str = "",
    lmargin: int = 0,
    rmargin: int = 0,
    tmargin: int = 0,
    bmargin: int = 0,
) -> None:
    try:
        images = convert_from_path("test.pdf")
    except FileNotFoundError:
        raise FileNotFoundError("PDF not found")

    if len(images) < 1:
        raise FileNotFoundError("PDF contains no pages.")

    pdf_width = images[0].width
    pdf_height = images[0].height

    lmargin, rmargin, tmargin, bmargin = [
        max(0, m) for m in (lmargin, rmargin, tmargin, bmargin)
    ]

    c = canvas.Canvas(
        "type.pdf",
        pagesize=(pdf_width + (lmargin + rmargin), pdf_height + (tmargin + bmargin)),
    )
    for img in images:
        # (0,0) origin point at the lower left corner of the page
        # Furthermore the first coordinate x goes to the right and the second coordinate y goes up, by default.
        c.drawImage(
            ImageReader(img), lmargin, bmargin, width=pdf_width, height=pdf_height
        )
        c.showPage()
    c.save()


if __name__ == "__main__":
    pass
