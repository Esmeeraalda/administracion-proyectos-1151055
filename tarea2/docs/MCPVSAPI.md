# MCP frente a una API

## ¿Qué es una API?

Una API (Interfaz de Programación de Aplicaciones) es un mecanismo de comunicación entre programas. Define las funciones disponibles, los datos que se deben enviar y las respuestas que se pueden recibir. El programador decide previamente qué operaciones se pueden utilizar y cómo invocarlas.

## ¿Qué es MCP?

El Model Context Protocol (MCP) es un protocolo abierto que permite conectar aplicaciones de inteligencia artificial con herramientas y fuentes de información externas. Utiliza JSON-RPC 2.0 para intercambiar mensajes entre el cliente y el servidor.

Mediante MCP, un servidor publica un catálogo de herramientas disponibles para que la aplicación pueda descubrirlas y el modelo pueda seleccionar cuál utilizar según la solicitud del usuario.

## Tabla comparativa

| Aspecto | API | MCP |
|---|---|---|
| **¿Quién decide qué se invoca?** | El programador define qué operación se ejecuta. | El modelo puede seleccionar la herramienta según la solicitud del usuario. |
| **Descubrimiento de capacidades** | Generalmente se consultan mediante documentación o especificaciones. | El cliente puede consultar al servidor qué herramientas ofrece. |
| **Acoplamiento** | El programa debe conocer previamente los endpoints y sus parámetros. | El cliente utiliza una estructura estandarizada para comunicarse con distintos servidores MCP. |
| **Formato de los mensajes** | Depende de la API; puede utilizar JSON, XML u otros formatos. | Utiliza mensajes JSON-RPC 2.0. |
| **Autenticación y consentimiento** | Depende del mecanismo de autenticación y los permisos definidos por la API. | Puede utilizar mecanismos como OAuth y permitir confirmaciones del usuario antes de ejecutar herramientas. |
| **Reutilización entre aplicaciones** | Cada aplicación debe implementar la integración correspondiente. | Un mismo servidor MCP puede conectarse con diferentes aplicaciones compatibles con el protocolo. |

## Relación entre MCP y las APIs

MCP no sustituye a las APIs. Su función es facilitar la conexión entre los modelos de inteligencia artificial y las herramientas externas. En muchos casos, un servidor MCP utiliza APIs existentes y las presenta como herramientas que el modelo puede descubrir y utilizar.Una API permite que los programas se comuniquen mediante operaciones previamente definidas, mientras que MCP estandariza la forma en que una aplicación de IA descubre y utiliza herramientas externas.

## Referencias

- [Documentación oficial de MCP](https://modelcontextprotocol.io/docs/getting-started/intro)
- [Arquitectura de MCP](https://modelcontextprotocol.io/docs/learn/architecture)
- para complementar las preguntas se utilizo IA chatgpt
