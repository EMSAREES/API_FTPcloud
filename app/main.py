from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from app.ftp_utils import see_connection, list_files_in_directory, upload_file, delete_file, create_fold, download_file
from io import BytesIO

app = FastAPI()

@app.get("/")
def read_root():
    message = see_connection()
    return {"message": message}

@app.get("/files")
def list_files(directory: str):
    try:
        files = list_files_in_directory(directory)
        return{"files": files}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/upload")
async def upload_file_endpoint(directory: str, file: UploadFile = File(...)):
    try:
        content = await file.read()
        filename = file.filename
        result = upload_file(directory, filename, content)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete")
def delete_file_endpoint(directory: str, filename: str):
    try:
        result = delete_file(directory, filename)
        return result
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    

@app.post("/create_folder")
def create_file_endpoint(directory: str, folder_name: str):
    try:
        result = create_fold(directory, folder_name)
        return result
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    


@app.get("/download")
def  download_file_endpoint(directory: str, filename: str):
    try:
        filedata = download_file(directory, filename)
        return StreamingResponse(BytesIO(filedata), media_type='application/octet-stream', headers={"Content-Disposition": f"attachment; filename={filename}"})
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))