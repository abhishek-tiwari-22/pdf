# pip install wikipedia
# pip install reportlab

import wikipedia
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


key=input() #-> keyword
cntnt=wikipedia.page(key) #-> wikipedia page

ttle=cntnt.title #-> title
cont=cntnt.content #-> all the text available on wikipedia
# print(cont)


# text styling
styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading1']
story = []

# dynamic file name
pdf_name = f'{ttle}.pdf'

# templates
doc = SimpleDocTemplate(
    pdf_name,
    pagesize=letter,
    bottomMargin=.4 * inch,
    topMargin=.6 * inch,
    rightMargin=.8 * inch,
    leftMargin=.8 * inch)

# pdf content
H = Paragraph(ttle+"\n",styleH) #-> title of the text
story.append(H)
P = Paragraph(cont, styleN) #-> text paaragraphs
story.append(P)

# builds and save pdf file
doc.build(
    story,
)



# in case keyword doesn't work, we can run below line to find correct keyword

# print(wikipedia.suggest("Harry Potter"))
