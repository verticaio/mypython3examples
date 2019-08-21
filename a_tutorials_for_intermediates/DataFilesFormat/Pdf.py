import PyPDF2

pdf_file = open('Babak_Mammadov_CV.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)

print(read_pdf)

pdf_doc_info = read_pdf.getDocumentInfo()
print(pdf_doc_info)


pdf_fields = read_pdf.getFields()
print(pdf_fields)

#Check Number of Pages
num_of_pages = read_pdf.getNumPages()
print(num_of_pages)


#Take page and work on over this
page = read_pdf.getPage(1)
page_number = read_pdf.getPageNumber(page)
print(page_number)

page_mode = read_pdf.getPageMode()
print(page_mode)


#Extract text
page_content = page.extractText()
#print(page_content)


#Linkf for detail information
# https://www.blog.pythonlibrary.org/tag/python-pdf-series
# https://www.blog.pythonlibrary.org/2010/03/08/a-simple-step-by-step-reportlab-tutorial/
# https://medium.com/@vonkunesnewton/generating-pdfs-with-reportlab-ced3b04aedef