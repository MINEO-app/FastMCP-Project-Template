import os

from fastmcp import FastMCP
from fastmcp.server.auth.providers.jwt import StaticTokenVerifier
from src.tools import add, subtract, multiply

# Auth A (active): shared static token ? same identity for every caller.
AUTH_TOKEN = os.environ.get("MCP_AUTH_TOKEN", "default-token")
PORT = int(os.environ.get("MCP_PORT", "8000"))
auth = StaticTokenVerifier(
    tokens={AUTH_TOKEN: {"client_id": "mcp-client", "scopes": ["read", "write"]}},
    required_scopes=["read"],
)

mcp = FastMCP("Calculator", auth=auth)

# Auth B (per-user identity): uncomment to verify Mineo's signed per-user tokens against its
# public JWKS, so `whoami` returns the real caller (no secret lives here). MINEO_JWKS_URL is
# injected into every Live App pod by the platform.
#
"""
from fastmcp.server.auth.providers.jwt import JWTVerifier
from fastmcp.server.dependencies import get_access_token
auth = JWTVerifier(
    jwks_uri=os.environ["MINEO_JWKS_URL"], issuer="mineo", audience="mineo-mcp", algorithm="ES256",
)
mcp = FastMCP("Calculator", auth=auth)

@mcp.tool()
def whoami() -> dict:
    # Return the verified identity of the user who invoked this tool.
    token = get_access_token()
    return {
        "user_uuid": token.claims["sub"],
        "thread_uuid": token.claims.get("thr"),
        "project_uuid": token.claims.get("prj"),
        "organization_uuid": token.claims.get("org"),
    }
"""

for tool in [add, subtract, multiply]:
    mcp.tool()(tool)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=PORT, path="/")
