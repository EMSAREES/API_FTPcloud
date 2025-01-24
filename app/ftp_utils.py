from ftplib import FTP
import os
#from fastapi import FastAPI, UploadFile, File, HTTPException
from io import BytesIO

FTP_HOST = '192.168.0.51'
FTP_PORT = 2221
FTP_USER = 'android'
FTP_PASS = 'android'

#app = FastAPI()

def connection():
    ftp = FTP()
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp

def see_connection():
    try:
        ftp = connection()
        if ftp:
            message = "Esta conectado al servidor"
        else:
            message = "No esta conectado al servidor"
        return message
    except Exception as e:
        raise Exception(f"Error {str(e)}")

def list_files_in_directory(directory: str):
    try:
        ftp = connection()
        ftp.cwd(directory)
        files = ftp.nlst()
        #files = []
        ftp.quit()
        return files
    except Exception as e:
        raise Exception(f"Error al listar archivos: {str(e)}")
    
def upload_file(directory: str, filename: str, filedata: bytes):
    try:
        ftp = connection()
        ftp.cwd(directory)
        ftp.storbinary(f"STOR {filename}", BytesIO(filedata))
        ftp.quit()
        return {"message": "Archivo subido correctamente"}
    except Exception as e:
        raise Exception(f"Error al eliminar el archivo: {str(e)}")

def delete_file(directory: str, filename:str):
    try:
        ftp = connection()
        ftp.cwd(directory)
        try:
            ftp.delete(filename)
            result = {"message": "Archivo eliminado correctamente"}
        except Exception as e:
            ftp.rmd(filename)
            result = {"message": "Carpeta eliminada correctamente"}
        ftp.quit()
        return result
    except Exception as e:
        raise Exception(f"Error al eliminar el archivo: {str(e)}")

def create_fold(directory: str, foldename: str):
    try:
        ftp = connection()
        ftp.cwd(directory)
        ftp.mkd(foldename)
        ftp.quit()
        return {"message": "Carpeta creada correctamente"}
    except Exception as e:
        raise Exception(f"Error al crear la carpeta: {str(e)}")

def download_file(directory: str, filename: str):
    try:
        ftp = connection()
        ftp.cwd(directory)
        filedata = BytesIO()
        ftp.retrbinary(f"RETR {filename}", filedata.write)
        ftp.quit()
        filedata.seek(0)
        return filedata.read()
    except Exception as e:
        raise Exception(f"Error al descargar el archivo: {str(e)}")