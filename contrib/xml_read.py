from bs4 import BeautifulSoup

from data.monofasico import lista_monofasicos
from os.path import dirname, abspath, join


def read_xml(filename):
    path = join(dirname(dirname(abspath(__file__))), 'static', 'xml', f'{filename}')

    f = open(path, 'r')

    data = f.read()

    monofasico = "Não é Monofásico"

    Bs_data = BeautifulSoup(data, 'xml')
    ncm_found = Bs_data.find_all('NCM')

    for ncm in ncm_found:
        ncm_num = ncm.get_text()
        if ncm_num in lista_monofasicos:
            monofasico = "Monofásico"

    return monofasico


