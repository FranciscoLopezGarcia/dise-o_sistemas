from paprika import *
from sucursal import Sucursal
from sucursal import Sucursal
from typing import Set, Optional, Any



@data
class Empresa:
    id : int
    nombre: str
    razonSocial: str
    cuit: int
    logo: str

    sucursales: set[Sucursal] = set()