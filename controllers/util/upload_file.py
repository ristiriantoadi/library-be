import os
import shutil

from fastapi import File, UploadFile

from config.config_firebase import bucket

FOLDER = "./image"


def save_file_to_local_folder(fileObject: File):
    if os.path.isdir(FOLDER) is False:
        os.mkdir(FOLDER)
    file_object = fileObject.file
    pathToFile = os.path.join(FOLDER, fileObject.filename)
    upload = open(pathToFile, "wb+")
    shutil.copyfileobj(file_object, upload)
    upload.close()
    return pathToFile


async def upload_file(file: UploadFile, featureFolder: str):
    path = save_file_to_local_folder(file)
    blob = bucket.blob(
        "{featureFolder}/{filename}".format(
            featureFolder=featureFolder, filename=file.filename
        )
    )
    blob.upload_from_filename(path)
    blob.make_public()
    return blob.public_url
