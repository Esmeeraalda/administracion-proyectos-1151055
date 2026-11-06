# Servidor de Sistema de Archivos

## ¿Qué es el servidor de sistema de archivos?

El servidor de sistema de archivos es una implementación de referencia de MCP que permite a una aplicación de inteligencia artificial interactuar con archivos y directorios mediante herramientas.

No forma parte del protocolo MCP, sino que es uno de los servidores que utiliza este protocolo para ofrecer funciones de acceso al sistema de archivos.

## ¿Qué herramientas expone?

Entre sus principales herramientas se encuentran:

| Herramienta | Función |
|---|---|
| `read_file` | Leer el contenido de un archivo. |
| `write_file` | Crear o escribir contenido en un archivo. |
| `edit_file` | Modificar el contenido de un archivo. |
| `list_directory` | Mostrar los archivos y carpetas de un directorio. |
| `create_directory` | Crear un directorio. |
| `move_file` | Mover o renombrar archivos. |
| `search_files` | Buscar archivos y directorios por nombre o patrón. |
| `get_file_info` | Consultar información de un archivo o directorio. |
| `delete_file` | Eliminar un archivo. |
| `list_allowed_directories` | Mostrar los directorios a los que tiene acceso el servidor. |

## Directorios permitidos y control de acceso

Al iniciar el servidor se especifican los directorios a los que puede acceder. Esto limita sus operaciones únicamente a las ubicaciones autorizadas y evita que pueda consultar o modificar archivos fuera de ellas.

Por ejemplo, si se permite el acceso únicamente a la carpeta `Documentos/Proyecto`, el servidor podrá trabajar con los archivos y subdirectorios que se encuentren dentro de esa ubicación, pero no con otras carpetas de la computadora.

## ¿Qué pasaría si no existiera este límite?

Sin una restricción de directorios, el servidor podría tener acceso a archivos fuera del área de trabajo prevista, aumentando el riesgo de consultar información privada, modificar documentos importantes o eliminar archivos que no deberían estar disponibles.

Por eso, establecer directorios permitidos es una medida importante para limitar el alcance de las operaciones del servidor.

## Referencia

- [Servidor MCP de sistema de archivos - Repositorio oficial](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)
- para complementar las preguntas se utilizo IA Chatgpt