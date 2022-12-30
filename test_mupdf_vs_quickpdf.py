
########################################################################################
# Test with MUPDF : creating a PDF file from a lot of tif images (with g4 compression) #
########################################################################################

import fitz, os, pathlib, time
from tkinter import filedialog

directory = filedialog.askdirectory(title="Test MUPDF : select images directory")
tBegin = time.perf_counter()

doc = fitz.open() 
nb = 0
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    if pathlib.Path(filepath).suffix==".tif":
        nb = nb + 1
        img = fitz.open(filepath)
        rect = img[0].rect
        pagePdf = doc.new_page(width=rect.width, height = rect.height)
        pdfbytes = img.convert_to_pdf() 
        img.close()
        imgPDF = fitz.open("pdf", pdfbytes) 
        pagePdf.show_pdf_page(rect, imgPDF, 0)
doc.save(directory + "/test_mupdf.pdf" )

tEnd = time.perf_counter()
size = pathlib.Path(directory + "/test_mupdf.pdf").stat().st_size
print(f"MUPDF : {nb:d} images in {tEnd - tBegin:0.2f} seconds - Pdf File Size = {size:d} bytes")

###########################################################################################
# Test with QUICKPDF : creating a PDF file from a lot of tif images (with g4 compression) #
###########################################################################################

import FoxitQPLDLL1611 as FoxitQuick

tBegin = time.perf_counter()

qp = FoxitQuick.PDFLibrary("C:\\Debenu\\DebenuPDFLibrary64DLL1611.dll")
licenseKey = open("quickpdf_license.txt","rt").read()
qp.UnlockKey(licenseKey)
nb = 0
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    if pathlib.Path(filepath).suffix==".tif":
        nb = nb + 1
        qp.NewPage()
        imageId = qp.AddImageFromFile(filepath,0)
        qp.DrawImage(0,qp.ImageHeight(),qp.ImageWidth(),qp.ImageHeight());
        qp.ReleaseImage(imageId)
qp.SaveToFile(directory + "/test_quickpdf.pdf")

tEnd = time.perf_counter()
size = pathlib.Path(directory + "/test_quickpdf.pdf").stat().st_size
print(f"QUICKPDF : {nb:d} images in {tEnd - tBegin:0.2f} seconds - Pdf File Size = {size:d} bytes")
