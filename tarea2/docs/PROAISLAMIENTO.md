# Problema de aislamiento
## ¿Por qué un LLM no puede acceder directamente a los archivos?
El LLM procesa la información que recibe y genera una respuesta en forma de texto. Por sí solo, no puede abrir, leer, modificar ni eliminar archivos de una computadora, porque no tiene acceso directo al sistema de archivos ni cuenta automáticamente con herramientas para realizar esas acciones.

Para que un modelo pueda trabajar con archivos, necesita otro componente que le proporcione el acceso y ejecute las operaciones necesarias.

Este problema se explica desde dos perspectivas: la arquitectura del sistema y la seguridad.

## 1. Razones de arquitectura
El modelo no obtiene automáticamente acceso al disco duro, las carpetas o los documentos de la computadora desde la que se realiza la consulta, trabaja con la información que se le proporciona en su contexto. De manera similar para modificarlo, algún componente externo debe ejecutar la operación de escritura.
Por ejemplo, si se le pide a un LLM que corrija el archivo, pero no tiene herramientas conectadas, puede sugerir el código corregido, aunque no puede guardar los cambios directamente en ese archivo. 

## 2. Razones de seguridad
La falta de acceso directo también ayuda a establecer límites de seguridad. Si una aplicación conecta un modelo con herramientas externas, debe decidir qué operaciones puede realizar, a qué archivos puede acceder y cuándo necesita autorización del usuario.

Acceso no autorizado: una herramienta podría leer archivos que contienen información privada, contraseñas o datos confidenciales.

Modificaciones no deseadas: si tiene permisos de escritura, podría sobrescribir o eliminar archivos importantes.

Inyección de instrucciones: un archivo, una página web u otro contenido externo podría incluir instrucciones maliciosas que intenten manipular al modelo para que realice acciones distintas de las solicitadas por el usuario.

Una solución consiste en utilizar herramientas externas mediante un protocolo como el Model Context Protocol (MCP). Este permite que una aplicación conecte un modelo con servidores que ofrecen funciones específicas.
