import logging

import fastapi
from contrib.xml_read import xml_read

router = fastapi.APIRouter()


@router.post("/read_xml")
def xml_information(filename=str):
    try:
        r = xml_read(filename)
        if r:
            return "Monofásico"
        else:
            return "Não é Monofásico"

    except Exception as e:
        return f'Erro: {e}'
