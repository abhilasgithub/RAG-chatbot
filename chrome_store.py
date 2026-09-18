import chromadb
import uuid
import logging

class ChromaDB:
    def __init__(self):

        chroma_client = chromadb.Client()
        self.collection = chroma_client.get_or_create_collection(name="my_embeddings")

        logging.basicConfig(
            level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s",
        )
        self.logger = logging.getLogger(__name__)

    def insert_embeddings(self, chunks:list[str], embeddings:list[float]):
        ids = [str(uuid.uuid4()) for _ in chunks]
        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings,
        )

    def search_query(self, query:str) -> list[str]:

        results = self.collection.query(
            query_texts=[query],
            n_results=3
        )
        result_chunks = []
        for item in results['documents'][0]:
            result_chunks.append(item)
        print("result_chunks",result_chunks)
        return result_chunks


if __name__ == "__main__":
    obj = ChromaDB()
    # insert data to chroma databse
    obj.insert_embeddings(["hello world"], [1,0,0,1,0, 1])
    print(obj.search_query("hjhfjdhfjkd"))

