from chunking import Chunking
from embeddings import Embeddings
from chrome_store import ChromaDB


class DataIngestion:
    def __init__(self, obj):
        self.obj = obj

    def ingest(self):
        try:
            chunks = Chunking().get_chuks(self.obj)
            embedding = Embeddings().get_embedding(chunks)

            ChromaDB().insert_embeddings(chunks, embedding)

        except Exception as e:
           return {"message": "Unable to ingest data"}

        return "Successfully ingested data"

    def search_query(self, query:str) -> dict:
        result = ChromaDB().search_query(query)
        return result



