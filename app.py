import logging
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.jwt import StaticTokenVerifier

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
)

from src.tools import add, subtract, multiply

AUTH_TOKEN = os.environ.get("MCP_AUTH_TOKEN", "default-token")
PORT = int(os.environ.get("MCP_PORT", "8000"))

logging.info(f"***** Using auth token: {AUTH_TOKEN}")

verifier = StaticTokenVerifier(
    tokens={AUTH_TOKEN: {"client_id": "mcp-client", "scopes": ["read", "write"]}},
    required_scopes=["read"],
)

mcp = FastMCP("Calculator", auth=verifier)

for tool in [add, subtract, multiply]:
    mcp.tool()(tool)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=PORT, path="/")
