import fitz, os, pathlib, time
from tkinter import filedialog
import FoxitQPLDLL1611 as FoxitQuick

directory = filedialog.askdirectory(title="Test MUPDF : select images directory")

bMuPDF = True
bQuickPDF = True

###########################################################################################################################
# Test with MUPDF (convert_to_pdf and show_pdf_page) : creating a PDF file from a lot of tif images (with g4 compression) #
###########################################################################################################################

if bMuPDF:
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
    pdf_filepath = directory + "/test_mupdf_convert_to_pdf.pdf" 
    doc.save(pdf_filepath)

    tEnd = time.perf_counter()
    size = pathlib.Path(pdf_filepath).stat().st_size
    print(f"MUPDF (convert_to_pdf and show_pdf_page) : {nb:d} images in {tEnd - tBegin:0.2f} seconds - Pdf File Size = {size:d} bytes")

#######################################################################################################
# Test with MUPDF (insert_image) : creating a PDF file from a lot of tif images (with g4 compression) #
#######################################################################################################

if bMuPDF:
    tBegin = time.perf_counter()

    doc = fitz.open() 
    nb = 0
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if pathlib.Path(filepath).suffix==".tif":
            imgbytes = pathlib.Path(filepath).read_bytes()
            prof = fitz.image_profile(imgbytes)
            nb = nb + 1
            pagePdf = doc.new_page(width=prof["width"], height=prof["height"])
            pagePdf.insert_image(pagePdf.rect, stream=imgbytes)
    pdf_filepath = directory + "/test_mupdf_insert_image.pdf" 
    doc.save(pdf_filepath )

    tEnd = time.perf_counter()
    size = pathlib.Path(pdf_filepath).stat().st_size
    print(f"MUPDF (insert_image) : {nb:d} images in {tEnd - tBegin:0.2f} seconds - Pdf File Size = {size:d} bytes")

###########################################################################################
# Test with QUICKPDF : creating a PDF file from a lot of tif images (with g4 compression) #
###########################################################################################

if bQuickPDF:
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
            image_width = qp.ImageWidth()
            image_height = qp.ImageHeight()
            qp.SetPageDimensions(image_width, image_height)
            qp.DrawImage(0,image_height,image_width,image_height)
            qp.ReleaseImage(imageId)
    pdf_filepath = directory + "/test_quickpdf.pdf" 
    qp.SaveToFile(pdf_filepath)

    tEnd = time.perf_counter()
    size = pathlib.Path(pdf_filepath).stat().st_size
    print(f"QUICKPDF : {nb:d} images in {tEnd - tBegin:0.2f} seconds - Pdf File Size = {size:d} bytes")
