import chromadb
from src import config
import uuid

class VectorStore:
    
    def __init__(self):
        self.client=chromadb.PersistentClient(path="./chroma_db")
        self.collection=self.client.get_or_create_collection(name=config.CHROMA_COLLECTION)
        #python client.get_or_create_collection("my_collection") # collection(name="my_collection", metadata={})
    
    """
        Collections add Method
        
        (method) def add(
    ids: OneOrMany[ID],
    embeddings: OneOrMany[Embedding] | OneOrMany[PyEmbedding] | None = None,
    metadatas: OneOrMany[Metadata] | None = None,
    documents: OneOrMany[Document] | None = None,
    images: OneOrMany[Image] | None = None,
    uris: OneOrMany[URI] | None = None
) -> None
Add records to the collection.
"""
    def add(self,
            chunk: str,
            embedding: list[float],
            metadata: dict
            ) -> None:
        id = str(uuid.uuid4())
        self.collection.add(id,embeddings=[embedding],metadatas=[metadata],documents=[chunk])
        
        """def search(
    searches: OneOrMany[Search],
    read_level: ReadLevel = ReadLevel.INDEX_AND_WAL
) -> SearchResult
        """
    def search(self,embeddings: list[float])->list[str]:
        results=self.collection.query(query_embeddings=embeddings,
                                       n_results=2)
        """{'ids': [['1d52d6a5-280f-490c-b3dc-81cb4fbf5598', '1b3c2242-6879-4586-9717-a7514face128', '978e609b-397d-4b27-b9d4-e44ae8adb7f4']], 'embeddings': None, 'documents': [['Python is an interpreted language.', 'Python is an interpreted language.', 'Python is an interpreted language.']], 'uris': None, 'included': ['metadatas', 'documents', 'distances'], 'data': None, 'metadatas': [[{'page': 36, 'source': 'test.pdf'}, {'source': 'test.pdf', 'page': 36}, {'source': 'test.pdf', 'page': 36}]], 'distances': [[0.0, 0.0, 0.0]]}
        """
        return results["documents"][0]
        

    
        