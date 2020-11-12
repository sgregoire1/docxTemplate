from docxtpl import DocxTemplate

doc = DocxTemplate("./template/cv2.docx")
context = { 'NAME' : "World company" }
doc.render(context)
doc.save("./output/generated_doc.docx")