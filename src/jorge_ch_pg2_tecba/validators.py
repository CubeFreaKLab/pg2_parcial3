"""
Módulo de validadores para datos personales y de contacto.

Este módulo contiene clases para validar diferentes tipos de datos:
- ValidadorBase: Clase base con validaciones básicas
- ValidadorDatosPersonales: Validaciones para datos personales
- ValidadorDatosContacto: Validaciones para datos de contacto
"""

import re


class ValidadorBase:
    """
    Clase base para validaciones básicas.
    
    Contiene métodos fundamentales para validar tipos de caracteres
    que son utilizados por las clases especializadas.
    """
    
    @staticmethod
    def validar_solo_numeros(valor: str) -> bool:
        """
        Valida que el valor contenga solo números.
        
        Args:
            valor (str): El valor a validar
            
        Returns:
            bool: True si contiene solo números, False en caso contrario
        """
        if not valor:
            return False
        return valor.isdigit()
    
    @staticmethod
    def validar_solo_letras(valor: str) -> bool:
        """
        Valida que el valor contenga solo letras (incluye espacios y acentos).
        
        Args:
            valor (str): El valor a validar
            
        Returns:
            bool: True si contiene solo letras, False en caso contrario
        """
        if not valor:
            return False
        # Permite letras, espacios, acentos y caracteres especiales del español
        patron = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$'
        return bool(re.match(patron, valor))
    
    @staticmethod
    def validar_alfanumerico(valor: str) -> bool:
        """
        Valida que el valor contenga solo caracteres alfanuméricos.
        
        Args:
            valor (str): El valor a validar
            
        Returns:
            bool: True si es alfanumérico, False en caso contrario
        """
        if not valor:
            return False
        # Permite letras, números, espacios y algunos caracteres especiales
        patron = r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑüÜ\s]+$'
        return bool(re.match(patron, valor))


class ValidadorDatosPersonales(ValidadorBase):
    """
    Validador especializado para datos personales.
    
    Utiliza los métodos de ValidadorBase para realizar validaciones
    específicas de datos personales como edad, nombre y documento.
    """
    
    def validar_edad(self, edad: str) -> bool:
        """
        Valida que la edad sea un número válido entre 0 y 150.
        
        Args:
            edad (str): La edad a validar
            
        Returns:
            bool: True si la edad es válida, False en caso contrario
        """
        if not self.validar_solo_numeros(edad):
            return False
        
        edad_num = int(edad)
        return 0 <= edad_num <= 150
    
    def validar_nombre(self, nombre: str) -> bool:
        """
        Valida que el nombre contenga solo letras y tenga longitud adecuada.
        
        Args:
            nombre (str): El nombre a validar
            
        Returns:
            bool: True si el nombre es válido, False en caso contrario
        """
        if not nombre or len(nombre.strip()) < 2:
            return False
        
        # Remover espacios extra y validar
        nombre_limpio = ' '.join(nombre.split())
        return (self.validar_solo_letras(nombre_limpio) and 
                2 <= len(nombre_limpio) <= 50)
    
    def validar_documento_identidad(self, documento: str) -> bool:
        """
        Valida que el documento de identidad tenga formato válido.
        
        Args:
            documento (str): El documento a validar
            
        Returns:
            bool: True si el documento es válido, False en caso contrario
        """
        if not documento:
            return False
        
        # Remover espacios y guiones
        documento_limpio = documento.replace(' ', '').replace('-', '')
        
        # Debe contener solo números y tener entre 7 y 12 dígitos
        return (self.validar_solo_numeros(documento_limpio) and 
                7 <= len(documento_limpio) <= 12)


class ValidadorDatosContacto(ValidadorBase):
    """
    Validador especializado para datos de contacto.
    
    Utiliza los métodos de ValidadorBase para realizar validaciones
    específicas de datos de contacto como email, celular y dirección.
    """
    
    def validar_email(self, email: str) -> bool:
        """
        Valida que el email tenga un formato válido.
        
        Args:
            email (str): El email a validar
            
        Returns:
            bool: True si el email es válido, False en caso contrario
        """
        if not email:
            return False
        
        # Patrón básico para email
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        # Validar patrón y longitud
        return bool(re.match(patron, email)) and len(email) <= 100
    
    def validar_celular(self, celular: str) -> bool:
        """
        Valida que el número de celular tenga formato válido.
        
        Args:
            celular (str): El celular a validar
            
        Returns:
            bool: True si el celular es válido, False en caso contrario
        """
        if not celular:
            return False
        
        # Remover espacios, guiones y paréntesis
        celular_limpio = (celular.replace(' ', '')
                         .replace('-', '')
                         .replace('(', '')
                         .replace(')', '')
                         .replace('+', ''))
        
        # Debe contener solo números y tener entre 8 y 15 dígitos
        return (self.validar_solo_numeros(celular_limpio) and 
                8 <= len(celular_limpio) <= 15)
    
    def validar_direccion(self, direccion: str) -> bool:
        """
        Valida que la dirección tenga formato válido.
        
        Args:
            direccion (str): La dirección a validar
            
        Returns:
            bool: True si la dirección es válida, False en caso contrario
        """
        if not direccion or len(direccion.strip()) < 5:
            return False
        
        # Remover espacios extra
        direccion_limpia = ' '.join(direccion.split())
        
        # Debe ser alfanumérica y permitir algunos caracteres especiales
        patron = r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑüÜ\s.,#-]+$'
        
        return (bool(re.match(patron, direccion_limpia)) and 
                5 <= len(direccion_limpia) <= 200)