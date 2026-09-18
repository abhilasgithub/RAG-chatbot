from DataIngestion import DataIngestion
from fastapi import FastAPI,File, UploadFile
import logging
import io

app = FastAPI()
logging.basicConfig(level=logging.INFO, filename="newfile.log",
                    format='%(asctime)s %(levelname)s: %(message)s',
                    filemode='w')
logger = logging.getLogger()


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_bytes = await file.read()

    file_stream = io.BytesIO(file_bytes)
    obj1 = DataIngestion(file_stream)
    result3=obj1.ingest()
    return result3

@app.get("/")
async def getdata(query:str)-> list[dict]:
    obj2 = DataIngestion(None)
    result=obj2.search_query(query)
    return result




