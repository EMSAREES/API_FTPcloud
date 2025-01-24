from ftplib import FTP

FTP_HOST = '192.168.0.51'
FTP_PORT = 2221
FTP_USER = 'android'
FTP_PASS = 'android'

try:
    ftp = FTP()
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASS)
    print("Contenido de la raíz del servidor FTP:")
    ftp.retrlines('LIST')  # Lista el contenido en la raíz
    ftp.quit()
except Exception as e:
    print(f"Error: {e}")
