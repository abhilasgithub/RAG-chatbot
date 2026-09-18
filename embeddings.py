import logging
from langchain_huggingface import HuggingFaceEmbeddings
from typing import Any

class Embeddings:

    def __init__(self):
        self.embeddings_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s",
        )
        self.log = logging.getLogger(__name__)

    def get_embedding(self, chunks:Any[str]):
        try:

        # 4. Generate the vector embeddings
           self.log.info("Getting embedding")
           embeddings = self.embeddings_model.embed_documents(chunks)

        except Exception as e:
            self.log.error("Error getting embedding: %s", e)



        return embeddings


