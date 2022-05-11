import fastapi
import shutil

from typing import List
from fastapi import UploadFile, File
from os.path import dirname, abspath, join

router = fastapi.APIRouter()


@router.post("/upload_file")
async def upload_file(files: List[UploadFile] = File(...)):
    try:
        for file in files:
            if file.content_type == 'application/vnd.rar' or file.content_type == 'application/zip':
                path = join(dirname(dirname(abspath(__file__))), 'static', 'zip', f'{file.filename}')
            elif file.content_type == 'application/xml':
                path = join(dirname(dirname(abspath(__file__))), 'static', 'xml', f'{file.filename}')
            else:
                raise Exception('Unknown file format')

            with open(f'{path}', "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

    except Exception as e:
        return f'Erro: {e}'

    return 'Success!'


if __name__ == '__main__':
    upload_file()
