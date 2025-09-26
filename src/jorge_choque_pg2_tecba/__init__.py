"""
Jorge Ch PG2 TECBA - Librería de Validadores

Una librería básica de validadores para datos personales y de contacto.

Módulos:
    - validators: Clases de validación (ValidadorBase, ValidadorDatosPersonales, ValidadorDatosContacto)
    - core: Clase Persona con patrón Builder

Ejemplo de uso:
    >>> from jorge_ch_pg2_tecba.core import Persona
    >>> from jorge_ch_pg2_tecba.validators import ValidadorDatosPersonales
    
    >>> persona = (Persona()
    ...     .establecer_nombre("Juan Pérez")
    ...     .establecer_edad(30)
    ...     .establecer_email("juan@email.com")
    ...     .construir())
    
    >>> print(persona.nombre)
    Juan Pérez
"""

__version__ = "0.0.1"
__author__ = "Jorge Daniel Choque Ferrufino"
__email__ = "jorgechoque.sis24ch@tecba.edu.bo"

# Importar las clases principales para facilitar el acceso
from .validators import (
    ValidadorBase,
    ValidadorDatosPersonales,
    ValidadorDatosContacto
)
from .core import Persona, PersonaBuilder

__all__ = [
    "ValidadorBase",
    "ValidadorDatosPersonales", 
    "ValidadorDatosContacto",
    "Persona",
    "PersonaBuilder",
    "__version__",
    "__author__",
    "__email__"
]