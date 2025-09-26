# Jorge Choque PG2 TECBA - Librería de Validadores

Una librería básica de validadores para datos personales y de contacto desarrollada como parte del Parcial 3 de Programación 2. Implementa el patrón Builder para construcción fluida de objetos con validación automática.

## Características

- **Validadores Base**: Métodos fundamentales para validar números, letras y caracteres alfanuméricos
- **Validadores Especializados**: 
  - **Datos Personales**: edad, nombre, documento de identidad
  - **Datos de Contacto**: email, celular, dirección
- **Patrón Builder**: Construcción fluida de objetos Persona con validación automática
- **Manejo de Errores**: Validaciones con excepciones descriptivas
- **Documentación Completa**: Docstrings y ejemplos detallados

## Instalación

```bash
pip install -i https://test.pypi.org/simple/ jorge-choque-pg2-tecba
```

## API - Clase Persona (Módulo Core)

### Constructor
```python
Persona()
```
Crea una nueva instancia vacía de Persona. Utiliza el patrón Builder para construcción fluida.

### Métodos de Construcción (Builder Pattern)

#### `establecer_nombre(nombre: str) -> Persona`
Establece el nombre de la persona con validación.
- **Parámetro**: `nombre` (str) - Nombre de la persona
- **Retorna**: La instancia actual para encadenamiento fluido
- **Validación**: Solo letras, acentos, espacios. Entre 2-50 caracteres
- **Excepción**: `ValueError` si la validación falla

#### `establecer_edad(edad: int) -> Persona`
Establece la edad de la persona con validación.
- **Parámetro**: `edad` (int) - Edad de la persona
- **Retorna**: La instancia actual para encadenamiento fluido
- **Validación**: Número entero entre 0 y 150
- **Excepción**: `ValueError` si la validación falla

#### `establecer_documento_identidad(documento: str) -> Persona`
Establece el documento de identidad con validación.
- **Parámetro**: `documento` (str) - Documento de identidad
- **Retorna**: La instancia actual para encadenamiento fluido
- **Validación**: Solo números, entre 7-12 dígitos
- **Excepción**: `ValueError` si la validación falla

#### `establecer_email(email: str) -> Persona`
Establece el email de contacto con validación.
- **Parámetro**: `email` (str) - Dirección de email
- **Retorna**: La instancia actual para encadenamiento fluido
- **Validación**: Formato de email válido, máximo 100 caracteres
- **Excepción**: `ValueError` si la validación falla

#### `establecer_celular(celular: str) -> Persona`
Establece el número de celular con validación.
- **Parámetro**: `celular` (str) - Número de celular
- **Retorna**: La instancia actual para encadenamiento fluido
- **Validación**: Entre 8-15 dígitos (acepta formatos con espacios, guiones)
- **Excepción**: `ValueError` si la validación falla

#### `establecer_direccion(direccion: str) -> Persona`
Establece la dirección con validación.
- **Parámetro**: `direccion` (str) - Dirección completa
- **Retorna**: La instancia actual para encadenamiento fluido
- **Validación**: Entre 5-200 caracteres, formato alfanumérico con símbolos básicos
- **Excepción**: `ValueError` si la validación falla

#### `construir() -> Persona`
Finaliza la construcción de la persona.
- **Retorna**: La instancia actual completamente construida
- **Validación**: Verifica que al menos el nombre esté establecido
- **Excepción**: `ValueError` si faltan datos obligatorios

### Propiedades de Acceso (Solo Lectura)

```python
@property
def nombre(self) -> Optional[str]          # Nombre de la persona
@property  
def edad(self) -> Optional[int]            # Edad de la persona
@property
def documento_identidad(self) -> Optional[str]  # Documento de identidad
@property
def email(self) -> Optional[str]           # Email de contacto
@property
def celular(self) -> Optional[str]         # Número de celular
@property
def direccion(self) -> Optional[str]       # Dirección completa
```

### Métodos de Acceso a Datos

#### `obtener_datos_personales() -> dict`
Retorna un diccionario con los datos personales (nombre, edad, documento).

#### `obtener_datos_contacto() -> dict`
Retorna un diccionario con los datos de contacto (email, celular, dirección).

#### `obtener_todos_los_datos() -> dict`
Retorna un diccionario con todos los datos de la persona.

### Representación de Cadena

#### `__str__() -> str`
Retorna una representación legible de la persona con todos sus datos.

### Clase PersonaBuilder (Auxiliar)

#### `PersonaBuilder.nueva_persona() -> Persona`
Crea una nueva instancia de Persona.

#### `PersonaBuilder.con_datos_basicos(nombre: str, edad: int) -> Persona`
Crea una persona con nombre y edad establecidos.

## 📝 Ejemplos de Uso

### Ejemplo Básico - Construcción Completa de Persona

```python
from jorge_choque_pg2_tecba.core import Persona

# Crear persona con todos los datos
persona = (Persona()
    .establecer_nombre("María González")
    .establecer_edad(28)
    .establecer_documento_identidad("87654321")
    .establecer_email("maria@email.com")
    .establecer_celular("555-1234567")
    .establecer_direccion("Avenida Principal 123, Ciudad")
    .construir())

print(persona)
# Output: Persona(Nombre: María González, Edad: 28, Documento: 87654321, 
#         Email: maria@email.com, Celular: 555-1234567, 
#         Dirección: Avenida Principal 123, Ciudad)

# Acceder a datos individuales
print(f"Nombre: {persona.nombre}")           # María González
print(f"Edad: {persona.edad}")               # 28
print(f"Email: {persona.email}")             # maria@email.com
```

### Ejemplo con Datos Parciales

```python
from jorge_choque_pg2_tecba.core import PersonaBuilder

# Crear persona solo con datos básicos
persona = (PersonaBuilder.con_datos_basicos("Juan Pérez", 35)
    .establecer_email("juan.perez@empresa.com")
    .construir())

print(f"Datos personales: {persona.obtener_datos_personales()}")
# Output: {'nombre': 'Juan Pérez', 'edad': 35, 'documento_identidad': None}

print(f"Datos de contacto: {persona.obtener_datos_contacto()}")  
# Output: {'email': 'juan.perez@empresa.com', 'celular': None, 'direccion': None}
```

### Ejemplo de Validación y Manejo de Errores

```python
from jorge_choque_pg2_tecba.core import Persona

try:
    # Intentar crear persona con datos inválidos
    persona = (Persona()
        .establecer_nombre("María123")  # ❌ Contiene números
        .establecer_edad(200)           # ❌ Edad fuera del rango
        .construir())
except ValueError as e:
    print(f"Error de validación: {e}")
    # Output: Error de validación: Nombre inválido: 'María123'. 
    #         Debe contener solo letras y tener entre 2-50 caracteres.

try:
    # Email con formato incorrecto
    persona = (Persona()
        .establecer_nombre("Ana Silva")
        .establecer_email("email_sin_formato"))  # ❌ Formato inválido
except ValueError as e:
    print(f"Error: {e}")
    # Output: Error: Email inválido: 'email_sin_formato'. 
    #         Debe tener un formato válido de email.
```

### Ejemplo de Uso con Validadores Independientes

```python
from jorge_choque_pg2_tecba.validators import (
    ValidadorDatosPersonales, 
    ValidadorDatosContacto
)

# Validar datos antes de crear la persona
validador_personal = ValidadorDatosPersonales()
validador_contacto = ValidadorDatosContacto()

nombre = "Carlos Mendoza"
edad = "42"
email = "carlos.mendoza@empresa.com"

if validador_personal.validar_nombre(nombre):
    print(f"✓ Nombre '{nombre}' es válido")

if validador_personal.validar_edad(edad):
    print(f"✓ Edad '{edad}' es válida")

if validador_contacto.validar_email(email):
    print(f"✓ Email '{email}' es válido")

# Crear persona con datos pre-validados
persona = (Persona()
    .establecer_nombre(nombre)
    .establecer_edad(int(edad))
    .establecer_email(email)
    .construir())
```

### Ejemplo de Copia y Modificación

```python
from jorge_choque_pg2_tecba.core import PersonaBuilder

# Crear persona original
persona_original = (Persona()
    .establecer_nombre("Roberto Silva")
    .establecer_edad(45)
    .establecer_email("roberto@empresa.com")
    .construir())

# Crear una copia y modificarla
persona_copia = (PersonaBuilder.copia_desde(persona_original)
    .establecer_nombre("Roberto Silva Jr.")
    .establecer_edad(22)
    .construir())

print(f"Original: {persona_original.nombre}, {persona_original.edad}")
print(f"Copia: {persona_copia.nombre}, {persona_copia.edad}")
```

### Ejemplo de Aplicación Real

```python
def registrar_empleado():
    """Ejemplo de función que registra un nuevo empleado."""
    print("=== Registro de Nuevo Empleado ===")
    
    try:
        empleado = (Persona()
            .establecer_nombre(input("Nombre completo: "))
            .establecer_edad(int(input("Edad: ")))
            .establecer_documento_identidad(input("Documento: "))
            .establecer_email(input("Email corporativo: "))
            .establecer_celular(input("Celular: "))
            .establecer_direccion(input("Dirección: "))
            .construir())
        
        print("\\n✓ Empleado registrado exitosamente:")
        print(empleado)
        
        # Guardar en base de datos (ejemplo conceptual)
        datos = empleado.obtener_todos_los_datos()
        # save_to_database(datos)
        
        return empleado
        
    except ValueError as e:
        print(f"\\n❌ Error en los datos: {e}")
        ## 🔧 Referencia de Validadores

### ValidadorBase

```python
from jorge_choque_pg2_tecba.validators import ValidadorBase

validador = ValidadorBase()
print(validador.validar_solo_numeros("12345"))      # True
print(validador.validar_solo_letras("Juan Pérez"))  # True
print(validador.validar_alfanumerico("Casa123"))    # True
```

### ValidadorDatosPersonales

```python
from jorge_choque_pg2_tecba.validators import ValidadorDatosPersonales

validador_personal = ValidadorDatosPersonales()
print(validador_personal.validar_nombre("María González"))  # True
print(validador_personal.validar_edad("25"))                # True
print(validador_personal.validar_documento_identidad("12345678"))  # True
```

### ValidadorDatosContacto

```python
from jorge_choque_pg2_tecba.validators import ValidadorDatosContacto

validador_contacto = ValidadorDatosContacto()
print(validador_contacto.validar_email("usuario@ejemplo.com"))    # True
print(validador_contacto.validar_celular("555-123-4567"))         # True
print(validador_contacto.validar_direccion("Calle 123 #45-67"))   # True
```

## 📋 Validaciones Implementadas

### ValidadorBase
- **`validar_solo_numeros(valor)`**: Valida que contenga solo números
- **`validar_solo_letras(valor)`**: Valida que contenga solo letras (incluye acentos)
- **`validar_alfanumerico(valor)`**: Valida caracteres alfanuméricos

### ValidadorDatosPersonales
- **`validar_edad(edad)`**: Valida edad entre 0-150 años
- **`validar_nombre(nombre)`**: Valida nombre de 2-50 caracteres, solo letras
- **`validar_documento_identidad(documento)`**: Valida documento de 7-12 dígitos

### ValidadorDatosContacto
- **`validar_email(email)`**: Valida formato de email estándar
- **`validar_celular(celular)`**: Valida número de celular de 8-15 dígitos
- **`validar_direccion(direccion)`**: Valida dirección de 5-200 caracteres

## 📁 Estructura del Proyecto

```
jorge_ch_pg2_tecba/
├── validators.py      # Módulo de validadores
├── core.py           # Módulo core con clase Persona
└── __init__.py       # Archivo de inicialización del paquete
```

## 🚀 Publicación en TestPyPI

### Paso 1: Registrarse en TestPyPI

1. **Crear cuenta en TestPyPI**:
   - Ir a [https://test.pypi.org/account/register/](https://test.pypi.org/account/register/)
   - Completar el formulario de registro
   - Verificar email

2. **Generar Token de API**:
   - Ir a [https://test.pypi.org/manage/account/](https://test.pypi.org/manage/account/)
   - Navegar a "API tokens"
   - Crear nuevo token con scope "Entire account"
   - **Guardar el token de forma segura** (solo se muestra una vez)

### Paso 2: Configurar Credenciales

Crear archivo `~/.pypirc` (Windows: `%USERPROFILE%\.pypirc`):

```ini
[distutils]
index-servers =
    testpypi

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-TU_TOKEN_AQUI
```

### Paso 3: Construir y Publicar

```bash
# 1. Instalar herramientas de construcción
pip install build twine

# 2. Construir el paquete
python -m build

# 3. Verificar la distribución
twine check dist/*

# 4. Subir a TestPyPI
twine upload --repository testpypi dist/*

# 5. Instalar desde TestPyPI para probar
pip install -i https://test.pypi.org/simple/ jorge-choque-pg2-tecba
```

### Paso 4: Verificar Instalación

```python
import jorge_choque_pg2_tecba
from jorge_choque_pg2_tecba.core import Persona

# Crear persona de prueba
persona = (Persona()
    .establecer_nombre("Test User")
    .establecer_edad(25)
    .construir())

print(f"Librería instalada correctamente: {persona.nombre}")
```

##  Información del Proyecto

- **Versión**: 0.0.1
- **Autor**: Jorge Choque Ferrufino
- **Email**: jorgechoque.sis24ch@tecba.edu.bo
- **Licencia**: MIT License
- **Python**: >=3.8
- **Repositorio**: https://github.com/jorge-ch/pg2_parcial3

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio
2. Crear branch para feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push al branch (`git push origin feature/nueva-funcionalidad`)
5. Crear Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo [LICENSE](LICENSE) para más detalles.

## 🔧 Uso Básico

```python
from jorge_choque_pg2_tecba.validators import ValidadorDatosPersonales, ValidadorDatosContacto

# Validador de datos personales
validador_personal = ValidadorDatosPersonales()
print(validador_personal.validar_nombre("Juan Pérez"))  # True
print(validador_personal.validar_edad("25"))            # True
print(validador_personal.validar_documento_identidad("12345678"))  # True

# Validador de datos de contacto
validador_contacto = ValidadorDatosContacto()
print(validador_contacto.validar_email("usuario@ejemplo.com"))    # True
print(validador_contacto.validar_celular("1234567890"))          # True
print(validador_contacto.validar_direccion("Calle 123 #45-67"))  # True
```

### Clase Persona con Patrón Builder

```python
from jorge_choque_pg2_tecba.core import Persona

# Construcción fluida de una persona
persona = (Persona()
    .establecer_nombre("María González")
    .establecer_edad(28)
    .establecer_documento_identidad("87654321")
    .establecer_email("maria@email.com")
    .establecer_celular("555-1234567")
    .establecer_direccion("Avenida Principal 123")
    .construir())

print(persona)
# Output: Persona(Nombre: María González, Edad: 28, Documento: 87654321, Email: maria@email.com, Celular: 555-1234567, Dirección: Avenida Principal 123)

# Acceso a los datos
print(f"Nombre: {persona.nombre}")
print(f"Edad: {persona.edad}")
print(f"Email: {persona.email}")

# Obtener todos los datos como diccionario
datos = persona.obtener_todos_los_datos()
print(datos)
```

### Builder Alternativo

```python
from jorge_choque_pg2_tecba.core import PersonaBuilder

# Crear persona con datos básicos
persona = PersonaBuilder.con_datos_basicos("Carlos Silva", 35)

# Agregar más datos
persona.establecer_email("carlos@email.com").establecer_celular("555-9876543")

print(persona)
```

## Estructura del Proyecto

```
jorge_ch_pg2_tecba/
├── validators.py      # Módulo de validadores
├── core.py           # Módulo core con clase Persona
└── __init__.py       # Archivo de inicialización del paquete
```

## Validaciones Implementadas

### ValidadorBase
- `validar_solo_numeros(valor)`: Valida que contenga solo números
- `validar_solo_letras(valor)`: Valida que contenga solo letras (incluye acentos)
- `validar_alfanumerico(valor)`: Valida caracteres alfanuméricos

### ValidadorDatosPersonales
- `validar_edad(edad)`: Valida edad entre 0-150 años
- `validar_nombre(nombre)`: Valida nombre de 2-50 caracteres, solo letras
- `validar_documento_identidad(documento)`: Valida documento de 7-12 dígitos

### ValidadorDatosContacto
- `validar_email(email)`: Valida formato de email estándar
- `validar_celular(celular)`: Valida número de celular de 8-15 dígitos
- `validar_direccion(direccion)`: Valida dirección de 5-200 caracteres

## 📊 Información del Proyecto

- **Versión**: 0.0.1
- **Autor**: Jorge Daniel Choque Ferrufino
- **Email**: jorgechoque.sis24ch@tecba.edu.bo
- **Licencia**: MIT License
- **Python**: >=3.8
- **Repositorio**: https://github.com/CubeFreaKLab/pg2_parcial3

## Licencia

MIT License