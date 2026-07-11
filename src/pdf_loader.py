from dataclasses import dataclass
from pypdf import PdfReader
from pathlib import Path

@dataclass
class PDFPage:
    page_number: int
    text: str

class PDFLoader:
    def __init__(self,pdfs_directory: str):
        self.pdfs_directory=pdfs_directory
        
    def load_my_version(self,filename: str)->list[PDFPage]:
        #pdf_path=f"{self.pdfs_directory}/{filename}"
        pdf_path = Path(self.pdfs_directory) / filename
        print(f"PDF Path is: {pdf_path}")
        reader = PdfReader(pdf_path)
        #page_size=reader.get_num_pages() will be depricated
        page_count = len(reader.pages)
        #list_pdf_pages=list[PDFPage]
        list_pdf_pages: list[PDFPage] = []
        for i in range(page_count):
            page=reader.pages[i]
            pdfpage=PDFPage(i+1,page.extract_text() or "")
            list_pdf_pages.append(pdfpage)
        return list_pdf_pages  
    
    
    #The version of chatgpt
    def load(self, filename: str) -> list[PDFPage]:

        pdf_path = Path(self.pdfs_directory) / filename

        reader = PdfReader(pdf_path)

        pages: list[PDFPage] = []

        for index, page in enumerate(reader.pages):
            #Whenever you need both the index and the object, enumerate() is the Pythonic way to do it.We have

            text = page.extract_text() or ""

            pages.append(
                PDFPage(
                    page_number=index + 1,
                    text=text
                )
            )

        return pages  
        
        
      
    
    