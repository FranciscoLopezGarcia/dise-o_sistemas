from paprika import *
from localidad import Localidad
from typing import Optional


@data
class Domicilio:
    calle: str
    numero: int
    cp: int

    localidad: Localidad

