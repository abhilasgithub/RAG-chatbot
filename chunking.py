import logging  # 1. Import Python's built-in logging module
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader

class Chunking:
    def __init__(self, chunk_size: int = 200, chunk_overlap: int = 100):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def get_chuks(self, fileObj):
        """
        :param fileObj:
        :return: chunks
        """

        """Directly configure and initiate the logger here"""
        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
        )
        logger = logging.getLogger(__name__)

        """reading the pdf file"""
        logger.info("reading the file from Fastapi")
        try:
            print(type(fileObj))
            reader = PdfReader(fileObj)
            full_text = ""

            for page in reader.pages:
              text = page.extract_text()
              if text:
                full_text += text + " "

             #Split the text into chunks
            splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=100)
            chunks = splitter.split_text(full_text)

            """Log the output directly to the terminal"""
            logger.info("Total chunks: %d", len(chunks))
            return chunks
        except Exception as e:
            raise Exception



