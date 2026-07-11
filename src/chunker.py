from .pdf_loader import PDFPage
from dataclasses import dataclass

@dataclass
class Chunk:
    text: str
    page_number: int
    chunk_number: int
    
class Chunker:

    def __init__(
        self,
        chunk_size: int = 1000):
        self.chunk_size = chunk_size
        
    def chunk1(self,pdf_pages: list[PDFPage]) -> list[Chunk]:
        print("chunk is called!")
        chunk_list : list[Chunk] = []
        #join all the texts
        
        #for pdf_page in pdf_pages:
           
        all_text_length=len(all_texts)
        print(f"size of the document in chars: {all_text_length}")
        pos=0
        rest_text=all_texts
        while len(rest_text) > 0:
            next_chunk=rest_text[pos:self.chunk_size]
            chunk_list.append(next_chunk)
            pos=pos+self.chunk_size
            print(f"position in the document: {pos}")
            rest_text=rest_text[pos:all_text_length]
        
        #print(f"chunked list is: {chunk_list}")
        return chunk_list
            
       
    def chunk(self,pdf_pages: list[PDFPage]) -> list[Chunk]:
        print("chunk is called!")
        chunk_list : list[Chunk] = []
        
        
        for pdf_page in pdf_pages:
            page_number=pdf_page.page_number
            all_chunk_text=pdf_page.text
            pos_start=0
            pos_end=self.chunk_size
            processed=0
            chunk_no=0
            while processed<len(all_chunk_text):
                next_text=all_chunk_text[pos_start:pos_end]
                print(f"Next chunk in page {page_number, next_text}")
                chunk_no=chunk_no+1
                chunk=Chunk(next_text,page_number,chunk_no)
                chunk_list.append(chunk)
                pos_start=pos_start+self.chunk_size
                pos_end=pos_start+self.chunk_size
                processed=processed+self.chunk_size
            
        return chunk_list       