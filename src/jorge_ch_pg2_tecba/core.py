"""
Módulo core con la clase Persona implementando el patrón Builder.

Este módulo contiene la clase Persona que utiliza el patrón de diseño
Builder para construir objetos de manera fluida y validada.
"""

from typing import Optional
from .validators import ValidadorDatosPersonales, ValidadorDatosContacto


class Persona:
    """
    Clase Persona que implementa el patrón Builder.
    
    Permite construir una persona estableciendo por partes los datos
    personales y de contacto, utilizando validadores especializados.
    """
    
    def __init__(self):
        """Inicializa una instancia vacía de Persona."""
        # Datos personales
        self._nombre: Optional[str] = None
        self._edad: Optional[int] = None
        self._documento_identidad: Optional[str] = None
        
        # Datos de contacto
        self._email: Optional[str] = None
        self._celular: Optional[str] = None
        self._direccion: Optional[str] = None
        
        # Validadores
        self._validador_personales = ValidadorDatosPersonales()
        self._validador_contacto = ValidadorDatosContacto()
    
    def establecer_nombre(self, nombre: str) -> 'Persona':
        """
        Establece el nombre de la persona con validación.
        
        Args:
            nombre (str): El nombre a establecer
            
        Returns:
            Persona: La instancia actual para encadenamiento fluido
            
        Raises:
            ValueError: Si el nombre no es válido
        """
        if not self._validador_personales.validar_nombre(nombre):
            raise ValueError(f"Nombre inválido: '{nombre}'. Debe contener solo letras y tener entre 2-50 caracteres.")
        
        self._nombre = nombre.strip()
        return self
    
    def establecer_edad(self, edad: int) -> 'Persona':
        """
        Establece la edad de la persona con validación.
        
        Args:
            edad (int): La edad a establecer
            
        Returns:
            Persona: La instancia actual para encadenamiento fluido
            
        Raises:
            ValueError: Si la edad no es válida
        """
        edad_str = str(edad)
        if not self._validador_personales.validar_edad(edad_str):
            raise ValueError(f"Edad inválida: {edad}. Debe ser un número entre 0 y 150.")
        
        self._edad = edad
        return self
    
    def establecer_documento_identidad(self, documento: str) -> 'Persona':
        """
        Establece el documento de identidad con validación.
        
        Args:
            documento (str): El documento a establecer
            
        Returns:
            Persona: La instancia actual para encadenamiento fluido
            
        Raises:
            ValueError: Si el documento no es válido
        """
        if not self._validador_personales.validar_documento_identidad(documento):
            raise ValueError(f"Documento inválido: '{documento}'. Debe contener solo números y tener entre 7-12 dígitos.")
        
        self._documento_identidad = documento
        return self
    
    def establecer_email(self, email: str) -> 'Persona':
        """
        Establece el email de contacto con validación.
        
        Args:
            email (str): El email a establecer
            
        Returns:
            Persona: La instancia actual para encadenamiento fluido
            
        Raises:
            ValueError: Si el email no es válido
        """
        if not self._validador_contacto.validar_email(email):
            raise ValueError(f"Email inválido: '{email}'. Debe tener un formato válido de email.")
        
        self._email = email.lower().strip()
        return self
    
    def establecer_celular(self, celular: str) -> 'Persona':
        """
        Establece el número de celular con validación.
        
        Args:
            celular (str): El celular a establecer
            
        Returns:
            Persona: La instancia actual para encadenamiento fluido
            
        Raises:
            ValueError: Si el celular no es válido
        """
        if not self._validador_contacto.validar_celular(celular):
            raise ValueError(f"Celular inválido: '{celular}'. Debe tener entre 8-15 dígitos.")
        
        self._celular = celular
        return self
    
    def establecer_direccion(self, direccion: str) -> 'Persona':
        """
        Establece la dirección con validación.
        
        Args:
            direccion (str): La dirección a establecer
            
        Returns:
            Persona: La instancia actual para encadenamiento fluido
            
        Raises:
            ValueError: Si la dirección no es válida
        """
        if not self._validador_contacto.validar_direccion(direccion):
            raise ValueError(f"Dirección inválida: '{direccion}'. Debe tener entre 5-200 caracteres y formato válido.")
        
        self._direccion = direccion.strip()
        return self
    
    def construir(self) -> 'Persona':
        """
        Finaliza la construcción de la persona.
        
        Returns:
            Persona: La instancia actual completamente construida
            
        Raises:
            ValueError: Si faltan datos obligatorios
        """
        # Validar que se hayan establecido al menos los datos básicos
        if not self._nombre:
            raise ValueError("El nombre es obligatorio para construir una persona.")
        
        return self
    
    # Propiedades para acceso a los datos
    @property
    def nombre(self) -> Optional[str]:
        """Obtiene el nombre de la persona."""
        return self._nombre
    
    @property
    def edad(self) -> Optional[int]:
        """Obtiene la edad de la persona."""
        return self._edad
    
    @property
    def documento_identidad(self) -> Optional[str]:
        """Obtiene el documento de identidad de la persona."""
        return self._documento_identidad
    
    @property
    def email(self) -> Optional[str]:
        """Obtiene el email de la persona."""
        return self._email
    
    @property
    def celular(self) -> Optional[str]:
        """Obtiene el celular de la persona."""
        return self._celular
    
    @property
    def direccion(self) -> Optional[str]:
        """Obtiene la dirección de la persona."""
        return self._direccion
    
    def obtener_datos_personales(self) -> dict:
        """
        Obtiene todos los datos personales.
        
        Returns:
            dict: Diccionario con los datos personales
        """
        return {
            'nombre': self._nombre,
            'edad': self._edad,
            'documento_identidad': self._documento_identidad
        }
    
    def obtener_datos_contacto(self) -> dict:
        """
        Obtiene todos los datos de contacto.
        
        Returns:
            dict: Diccionario con los datos de contacto
        """
        return {
            'email': self._email,
            'celular': self._celular,
            'direccion': self._direccion
        }
    
    def obtener_todos_los_datos(self) -> dict:
        """
        Obtiene todos los datos de la persona.
        
        Returns:
            dict: Diccionario con todos los datos
        """
        datos = self.obtener_datos_personales()
        datos.update(self.obtener_datos_contacto())
        return datos
    
    def __str__(self) -> str:
        """Representación en cadena de la persona."""
        datos = []
        if self._nombre:
            datos.append(f"Nombre: {self._nombre}")
        if self._edad is not None:
            datos.append(f"Edad: {self._edad}")
        if self._documento_identidad:
            datos.append(f"Documento: {self._documento_identidad}")
        if self._email:
            datos.append(f"Email: {self._email}")
        if self._celular:
            datos.append(f"Celular: {self._celular}")
        if self._direccion:
            datos.append(f"Dirección: {self._direccion}")
        
        return "Persona(" + ", ".join(datos) + ")"
    
    def __repr__(self) -> str:
        """Representación técnica de la persona."""
        return self.__str__()


class PersonaBuilder:
    """
    Builder alternativo para construcción más explícita de Persona.
    
    Proporciona una interfaz alternativa para construir objetos Persona
    de manera más explícita y clara.
    """
    
    @staticmethod
    def nueva_persona() -> Persona:
        """
        Crea una nueva instancia de Persona.
        
        Returns:
            Persona: Nueva instancia de Persona
        """
        return Persona()
    
    @staticmethod
    def con_datos_basicos(nombre: str, edad: int) -> Persona:
        """
        Crea una persona con datos básicos.
        
        Args:
            nombre (str): Nombre de la persona
            edad (int): Edad de la persona
            
        Returns:
            Persona: Persona con datos básicos establecidos
        """
        return Persona().establecer_nombre(nombre).establecer_edad(edad)
    
    @staticmethod
    def copia_desde(otra_persona: Persona) -> Persona:
        """
        Crea una nueva persona copiando los datos de otra.
        
        Args:
            otra_persona (Persona): Persona a copiar
            
        Returns:
            Persona: Nueva persona con los datos copiados
        """
        nueva = Persona()
        
        if otra_persona.nombre:
            nueva.establecer_nombre(otra_persona.nombre)
        if otra_persona.edad is not None:
            nueva.establecer_edad(otra_persona.edad)
        if otra_persona.documento_identidad:
            nueva.establecer_documento_identidad(otra_persona.documento_identidad)
        if otra_persona.email:
            nueva.establecer_email(otra_persona.email)
        if otra_persona.celular:
            nueva.establecer_celular(otra_persona.celular)
        if otra_persona.direccion:
            nueva.establecer_direccion(otra_persona.direccion)
        
        return nueva