class Retriever:

    def __init__(
        self,
        embedding_service,
        vector_store
    ):
        self.embedding_service = embedding_service
        self.vector_store = vector_store

    def retrieve(
        self,
        question: str) -> list[str]:

        embedding = self.embedding_service.embed_document(question)

        searchResults = self.vector_store.search(embedding)
        #remove duplicates and return
        return list(set(searchResults))