#!/usr/bin/env python3
"""
Ejemplo de uso de la librería jorge_choque_pg2_tecba

Este archivo demuestra cómo usar los validadores y la clase Persona
con el patrón Builder para crear y validar datos personales y de contacto.
"""

from src.jorge_choque_pg2_tecba.core import Persona, PersonaBuilder
from src.jorge_choque_pg2_tecba.validators import (
    ValidadorBase, 
    ValidadorDatosPersonales, 
    ValidadorDatosContacto
)


def ejemplo_validadores():
    """Demuestra el uso de los validadores individuales."""
    print("=== EJEMPLO DE VALIDADORES ===")
    
    # Validador base
    validador_base = ValidadorBase()
    print(f"Solo números '12345': {validador_base.validar_solo_numeros('12345')}")
    print(f"Solo números 'abc123': {validador_base.validar_solo_numeros('abc123')}")
    print(f"Solo letras 'Juan Pérez': {validador_base.validar_solo_letras('Juan Pérez')}")
    print(f"Alfanumérico 'Casa123': {validador_base.validar_alfanumerico('Casa123')}")
    
    # Validador de datos personales
    validador_personal = ValidadorDatosPersonales()
    print(f"\\nNombre válido 'María González': {validador_personal.validar_nombre('María González')}")
    print(f"Nombre inválido '123': {validador_personal.validar_nombre('123')}")
    print(f"Edad válida '25': {validador_personal.validar_edad('25')}")
    print(f"Edad inválida '200': {validador_personal.validar_edad('200')}")
    print(f"Documento válido '12345678': {validador_personal.validar_documento_identidad('12345678')}")
    
    # Validador de datos de contacto
    validador_contacto = ValidadorDatosContacto()
    print(f"\\nEmail válido 'usuario@ejemplo.com': {validador_contacto.validar_email('usuario@ejemplo.com')}")
    print(f"Email inválido 'correo_invalido': {validador_contacto.validar_email('correo_invalido')}")
    print(f"Celular válido '555-123-4567': {validador_contacto.validar_celular('555-123-4567')}")
    print(f"Dirección válida 'Calle 123 #45': {validador_contacto.validar_direccion('Calle 123 #45')}")


def ejemplo_persona_builder():
    """Demuestra el uso del patrón Builder con la clase Persona."""
    print("\\n=== EJEMPLO DE PATRÓN BUILDER ===")
    
    try:
        # Crear persona usando el patrón builder
        persona1 = (Persona()
                   .establecer_nombre("Juan Carlos Pérez")
                   .establecer_edad(30)
                   .establecer_documento_identidad("12345678")
                   .establecer_email("juan.perez@email.com")
                   .establecer_celular("555-123-4567")
                   .establecer_direccion("Avenida Principal 123, Ciudad")
                   .construir())
        
        print(f"Persona creada: {persona1}")
        print(f"\\nDatos personales: {persona1.obtener_datos_personales()}")
        print(f"Datos de contacto: {persona1.obtener_datos_contacto()}")
        
        # Crear otra persona con datos básicos usando PersonaBuilder
        persona2 = PersonaBuilder.con_datos_basicos("Ana María Silva", 25)
        persona2.establecer_email("ana.silva@correo.com")
        
        print(f"\\nSegunda persona: {persona2}")
        
        # Crear una copia de la primera persona
        persona3 = PersonaBuilder.copia_desde(persona1)
        persona3.establecer_nombre("Juan Carlos Pérez Jr.")
        
        print(f"\\nPersona copiada y modificada: {persona3}")
        
    except ValueError as e:
        print(f"Error de validación: {e}")


def ejemplo_validaciones_fallidas():
    """Demuestra cómo se manejan las validaciones fallidas."""
    print("\\n=== EJEMPLO DE VALIDACIONES FALLIDAS ===")
    
    try:
        # Intentar crear persona con datos inválidos
        persona = (Persona()
                  .establecer_nombre("123 Nombre Inválido")  # Esto debería fallar
                  .establecer_edad(200))  # Esto también debería fallar
        print("Esta línea no debería ejecutarse")
        
    except ValueError as e:
        print(f"Error esperado: {e}")
    
    try:
        # Intentar crear persona con email inválido
        persona = (Persona()
                  .establecer_nombre("María Válida")
                  .establecer_email("email_sin_formato_correcto"))  # Esto debería fallar
        
    except ValueError as e:
        print(f"Error esperado: {e}")


def main():
    """Función principal que ejecuta todos los ejemplos."""
    print("Iniciando ejemplos de la librería jorge_choque_pg2_tecba\\n")
    
    ejemplo_validadores()
    ejemplo_persona_builder()
    ejemplo_validaciones_fallidas()
    
    print("\\n=== FIN DE EJEMPLOS ===")


if __name__ == "__main__":
    main()