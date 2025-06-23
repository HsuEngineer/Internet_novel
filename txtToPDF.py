import aspose.words as aw

def txt_to_pdf_aspose(txt_file_path, pdf_file_path):
    doc = aw.Document(txt_file_path)
    doc.save(pdf_file_path)

# Example usage:
txt_to_pdf_aspose("input.txt", "output_aspose.pdf")