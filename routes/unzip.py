import logging
import zipfile
from os.path import dirname, abspath, join

import fastapi

router = fastapi.APIRouter()


@router.post("/unzip")
def unzip(filename=str):
    try:
        origin_path = join(dirname(dirname(abspath(__file__))), 'static', 'zip', f'{filename}')
        destiny_path = join(dirname(dirname(abspath(__file__))), 'static', 'xml')

        with zipfile.ZipFile(origin_path) as zip_file:
            for item in zip_file.namelist():
                if item.endswith('.xml'):
                    zip_file.extract(item, destiny_path)

    except Exception as e:
        return f'Error: {e}'

    return 'Success!'
