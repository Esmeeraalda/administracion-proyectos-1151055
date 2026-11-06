from mcp.server import MCPServer

mcp = MCPServer("servidor-propio")


@mcp.tool()
def saludar(nombre: str) -> str:
    """Saluda a una persona por su nombre."""
    return f"Hola, {nombre}. Bienvenido a nuestro servidor MCP."


@mcp.tool()
def sumar(numero1: float, numero2: float) -> float:
    """Suma dos números."""
    return numero1 + numero2


if __name__ == "__main__":
    mcp.run()