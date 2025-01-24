# API_FTPcloud
# FTP API - FastAPI Implementation

In this project, our goal is to create a backend to manage files and folders using an FTP server. This backend can be used by web or mobile applications to upload, download, delete files, among other things. A phone is being used as an FTP server using an application.

## API Operations

### Check Connection
Check if the server is connected.

- **GET** `/`
  - Response: `{"message": "Esta conectado al servidor"}` or an error message.

---

### List Files
Retrieve the list of files in a directory.

- **GET** `/files?directory=/path/to/directory`
  - **Parameters**:
    - `directory` (string, required): The directory to list the files from.
  - **Example**: `/files?directory=/`
  - **Response**: `{"files": ["file1.txt", "file2.txt"]}`

---

### Upload File
Upload a file to a specific directory.

- **POST** `/upload?directory=/path/to/directory`
  - **Form Data**:
    - `file` (MultipartFile, required): The file to upload.
  - **Example**: `/upload?directory=/`
  - **Response**: `{"message": "Archivo subido correctamente"}`

---

### Create Folder
Create a new folder in a specified directory.

- **POST** `/create_folder?directory=/path/to/directory&folder_name=folder_name`
  - **Parameters**:
    - `directory` (string, required): The parent directory.
    - `folder_name` (string, required): The name of the folder to create.
  - **Example**: `/create_folder?directory=/&folder_name=carpeta100`
  - **Response**: `{"message": "Carpeta creada correctamente"}`

---

### Delete File or Folder
Delete a file or folder in a specified directory.

- **DELETE** `/delete?directory=/path/to/directory&filename=filename`
  - **Parameters**:
    - `directory` (string, required): The directory containing the file or folder.
    - `filename` (string, required): The name of the file or folder to delete.
  - **Example**: `/delete?directory=/&filename=carpeta100`
  - **Response**: 
    - `{"message": "Archivo eliminado correctamente"}` or
    - `{"message": "Carpeta eliminada correctamente"}`

---

### Download File
Download a file from a specified directory.

- **GET** `/download?directory=/path/to/directory&filename=filename`
  - **Parameters**:
    - `directory` (string, required): The directory containing the file.
    - `filename` (string, required): The name of the file to download.
  - **Example**: `/download?directory=/&filename=com.termux_1000.apk`
  - **Response**: File stream with `Content-Disposition` header for download.

---

## Project Structure

