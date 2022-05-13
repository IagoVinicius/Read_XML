import logging
import os
from os.path import dirname, abspath, join
import fastapi
from contrib.xml_read import read_xml

router = fastapi.APIRouter()


@router.post("/read_one_xml")
def read_one_xml(filename=str):
    try:
        r = read_xml(filename)
        return r

    except Exception as e:
        return f'Erro: {e}'

@router.post("/read_all_xml")
def read_all_xml():
    try:
        monofasicos = {}

        path = join(dirname(dirname(abspath(__file__))), 'static', 'xml')
        for filename in os.listdir(path):
            monofasicos[f'{filename}'] = read_xml(filename)

        return monofasicos

    except Exception as e:
        return f'Erro: {e}'

if __name__ == '__main__':
    read_all_xml()
