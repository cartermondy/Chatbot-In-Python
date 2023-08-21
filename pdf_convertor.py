from PyPDF2 import PdfReader

class PDF_Reader:
    
    def read_pdf(input_file):
        try:
            pdf_reader = PdfReader(input_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            return f"Error reading PDF: {str(e)}"
        
    #sample_text = read_pdf("Sample Text.pdf")
    #print(sample_text)
