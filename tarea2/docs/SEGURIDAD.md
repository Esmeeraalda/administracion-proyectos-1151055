# Seguridad

## Riesgos de seguridad

Al conectar un modelo de inteligencia artificial con un servidor de sistema de archivos, pueden presentarse los siguientes riesgos:

- **Instrucciones escondidas:** un archivo puede contener instrucciones maliciosas que intenten manipular al modelo para realizar acciones no solicitadas.
- **Acceso fuera del directorio autorizado:** una configuración incorrecta podría permitir consultar archivos fuera de las carpetas permitidas.
- **Escritura o borrado no deseados:** el modelo podría modificar o eliminar archivos importantes al utilizar herramientas con permisos de escritura.

## Medidas de seguridad

Para reducir estos riesgos se pueden aplicar las siguientes medidas:

- **Confirmación humana:** solicitar autorización del usuario antes de realizar operaciones importantes, como modificar o eliminar archivos.
- **Alcance limitado:** permitir el acceso únicamente a los directorios necesarios para realizar las tareas.
- **Sólo lectura:** utilizar permisos de lectura cuando no sea necesario modificar archivos.
- **Revisar las herramientas del servidor:** comprobar qué herramientas expone el servidor y qué operaciones permite realizar antes de conectarlo.

## Referencias
- Se utilizo IA para agregar la informacion anterior