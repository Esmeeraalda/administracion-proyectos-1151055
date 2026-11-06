# Arquitectura de MCP

## ¿Cómo está formada la arquitectura?

MCP utiliza una arquitectura compuesta por tres elementos:

- **Host:** es la aplicación que integra el modelo de IA y administra las conexiones con los servidores MCP.
- **Cliente:** es el componente que se encuentra dentro del host y establece la comunicación con un servidor MCP. Cada cliente se comunica con un servidor.
- **Servidor:** proporciona herramientas, recursos y plantillas de instrucciones que el modelo puede utilizar.

En una instalación de un servidor MCP de archivos, el host sería la aplicación de IA utilizada, el cliente sería su componente MCP y el servidor sería el programa encargado de ofrecer las funciones para trabajar con archivos.

## Primitivas del servidor

El servidor puede ofrecer tres tipos de primitivas:

- **Tools (herramientas):** permiten ejecutar acciones, como crear, modificar o consultar información.
- **Resources (recursos):** proporcionan información y datos que el modelo puede utilizar como contexto, por ejemplo, archivos o información de una base de datos.
- **Prompts (instrucciones):** son plantillas de instrucciones previamente definidas que ayudan a realizar determinadas tareas.

## Primitivas del cliente

El cliente también puede proporcionar funciones al servidor:

- **Roots:** permiten indicar qué directorios o archivos son relevantes para el trabajo del servidor. Funcionan como una referencia de las ubicaciones de trabajo, no como un mecanismo de control de acceso. Esta función fue declarada obsoleta en la especificación del 28 de julio de 2026.
- **Elicitation:** permite que el servidor solicite información adicional al usuario mediante el cliente. Por ejemplo, puede solicitar datos faltantes o una confirmación antes de continuar una operación.

## Transportes de MCP

MCP cuenta con dos transportes principales para intercambiar mensajes:

**1. stdio**

Permite que el cliente ejecute el servidor como un proceso local. La comunicación se realiza mediante los flujos de entrada y salida estándar (`stdin` y `stdout`), utilizando mensajes JSON-RPC.

**2. Streamable HTTP**

Permite la comunicación entre el cliente y un servidor mediante HTTP. El cliente envía solicitudes POST y el servidor responde con mensajes JSON o mediante un flujo de eventos enviados por el servidor (SSE).

## Versión de la especificación consultada

- **Versión:** `2026-07-28`.
- **Fecha de publicación:** 28 de julio de 2026.
- **Fecha de consulta:** 5 de noviembre de 2026.

La especificación de MCP cambia con el tiempo, por lo que es importante indicar la versión utilizada para documentar su arquitectura y funcionamiento.

## Referencias

- [Arquitectura de MCP](https://modelcontextprotocol.io/specification/2026-07-28/architecture)
- [Primitivas del servidor](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)
- [Roots](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Elicitation](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation)
- para complementar las preguntas se utilizo IA chatgpt 