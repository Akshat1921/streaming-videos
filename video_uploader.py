from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from video_provider import videoConverter
import os
from os import path
import subprocess

storage_account_key = "oHy85ZoPqijCAyw8hS00Uuey5I2fjWymKOaIgmCbkJAxBqh1A5o1K0sxoFS5zgbu9qlQp+u0Wfgn+ASttZuVfw=="
storage_account_name = "videostorageforstreaming"
connection_string = "DefaultEndpointsProtocol=https;AccountName=videostorageforstreaming;AccountKey=oHy85ZoPqijCAyw8hS00Uuey5I2fjWymKOaIgmCbkJAxBqh1A5o1K0sxoFS5zgbu9qlQp+u0Wfgn+ASttZuVfw==;EndpointSuffix=core.windows.net"
container_name = "videostoragecontainer"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
def uploadToBlob(file_path,file_name):
    
    blob_client = blob_service_client.get_blob_client(container=container_name,blob=file_name)
    with open(file_path,'rb') as data:
        blob_client.upload_blob(data)
    print(f"uploaded {file_name}")

directory = os.getcwd()
file_path = ''
for filename in os.listdir(directory):
	f = os.path.join(directory, filename)
	if os.path.isdir(f) and "videos" in f:
		file_path = f



file_name = "minion.mp4"
os.path.join(file_path,file_name)
print(file_path)
file_to_open = os.path.join(file_path, file_name)


uploadToBlob(file_to_open,file_name)

def videoUploadHLSFormat(blob_service_client: BlobServiceClient, container_name, file_path: str):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob="minion.mp4")
    with open(file_path, "w") as blob:  # Open the file in read mode
        download_stream = blob_client.download_blob()
        blob.write(download_stream.readall())

folder_name = "blob_videos"
cwd = os.getcwd()
dir = os.path.join(cwd,folder_name)
print(dir)
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

videoUploadHLSFormat(blob_service_client,container_name,dir)