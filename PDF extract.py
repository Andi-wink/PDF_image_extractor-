import io
import os
import sys
import time
import zipfile

import fitz
import PySimpleGUI as sg

print(fitz.__doc__)

if not tuple(map(int, fitz.version[0].split("."))) >= (1, 18, 18):
    raise SystemExit("require PyMuPDF v1.18.18+")

dimlimit = 0
relsize = 0
abssize = 0

def recoverpix(doc, item):
    xref = item[0]  # xref of PDF image
    smask = item[1]  # xref of its /SMask
    # the rest of the function remains unchanged
    # ...
    return doc.extract_image(xref)

# Fetch the filename
fname = None
if len(sys.argv) == 2:
    fname = sys.argv[1]
else:
    fname = sg.PopupGetFile("Select file:", title="PyMuPDF PDF Image Extraction")

if not fname:
    raise SystemExit()

# Create a directory in the same location as the PDF file
base_filename = os.path.splitext(os.path.basename(fname))[0]
imgdir = os.path.join(os.path.dirname(fname), base_filename)
if not os.path.exists(imgdir):
    os.makedirs(imgdir)

t0 = time.time()
doc = fitz.open(fname)
page_count = doc.page_count

xreflist = []
imglist = []
for pno in range(page_count):
    sg.QuickMeter(
        "Extract Images",
        pno + 1,
        page_count,
        "*** Scanning Pages ***",
    )

    il = doc.get_page_images(pno)
    imglist.extend([x[0] for x in il])

    img_counter = 0
    for img in il:
        xref = img[0]
        if xref in xreflist:
            continue

        # Additional logic to increment image counter per page and name images accordingly
        img_counter += 1
        width = img[2]
        height = img[3]
        if min(width, height) <= dimlimit:
            continue
        image = recoverpix(doc, img)
        n = image["colorspace"]
        imgdata = image["image"]

        if len(imgdata) <= abssize:
            continue
        if len(imgdata) / (width * height * n) <= relsize:
            continue

        imgfile = os.path.join(imgdir, f"{pno + 1}_{img_counter}_page_image.{image['ext']}")
        with open(imgfile, "wb") as fout:
            fout.write(imgdata)
        xreflist.append(xref)

# Create a zip file of all extracted images
zip_filename = os.path.join(os.path.dirname(fname), base_filename + "_images.zip")
with zipfile.ZipFile(zip_filename, 'w') as imgzip:
    for imgfile in os.listdir(imgdir):
        imgzip.write(os.path.join(imgdir, imgfile), arcname=imgfile)

t1 = time.time()
imglist = list(set(imglist))
print(len(set(imglist)), "images in total")
print(len(xreflist), "images extracted")
print("total time %g sec" % (t1 - t0))

