from datetime import time
from domicilio import Domicilio
from typing import Optional
from paprika import *


@data
class Sucursal:
    nombre: str
    horarioApertura: time
    horarioCierre: time
    es_Casa_Matriz: bool

    domicilio: Domicilio


