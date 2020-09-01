import fitz
doc = fitz.open("test.pdf")
page = doc[0]
text = page.getText()
print(text)
print ("hello world")
#currently on hold to inspect more of how pdf functions