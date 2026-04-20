# FastMCP Project Template

A FastMCP server template with clean architecture, ready for both MINEO and local development.

## Project Structure

```
FastMCP-ProjectTemplate/
├── src/
│   └── tools.py        # Tool functions for the MCP server
├── app.py              # Main entrypoint of the FastMCP application
├── docker/
│   ├── Dockerfile     # Dockerfile for local development (can also build MINEO Worker Images)
│   └── requirements.txt  # Python dependencies
├── docker-compose.yml # Docker Compose configuration for local development
├── .gitignore
├── LICENSE
└── README.md
```

## Requirements

- Python 3.12 or higher
- Dependencies listed in `requirements.txt`

## Quick Start

### Local Development

1. Clone this repository:
   ```
   git clone <repository-url>
   cd FastMCP-ProjectTemplate
   ```

2. Install dependencies:
   ```
   pip install -r docker/requirements.txt
   ```

3. Run the MCP server:
   ```
   python app.py
   ```

The server will start on `http://localhost:8000` by default.

### Using Docker Compose

Build and run the application with Docker:
```
docker compose build
docker compose up -d
```

To run an interactive shell in your container:
```
docker compose exec mcp-project bash
```

## Configuration

Environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `MCP_PORT` | Port for the MCP server | `8000` |
| `MCP_AUTH_TOKEN` | JWT token for authentication | `default-token` |

### Security

Set a strong `MCP_AUTH_TOKEN` in production:
```bash
export MCP_AUTH_TOKEN=$(openssl rand -hex 32)
```

### Authentication

The server uses JWT authentication via the `StaticTokenVerifier`. The token is configured via the `MCP_AUTH_TOKEN` environment variable.

By default, the client must include a Bearer token in the Authorization header:
```
Authorization: Bearer <MCP_AUTH_TOKEN>
```

## Available Tools

- `add(a, b)`: Add two numbers together
- `subtract(a, b)`: Subtract the second number from the first
- `multiply(a, b)`: Multiply two numbers together

## Docker Support

### Building for MINEO Platform

The Dockerfile in the `docker/` directory can be used to build images compatible with the MINEO platform. Refer to MINEO documentation for specific deployment instructions.

---

**This is a template repository for FastMCP projects designed for development in both local environments and the MINEO platform. Modify this README to fit your specific project needs.**

---

## About

A FastMCP template with clean architecture, ready for both MINEO and local development.

### Resources

- [FastMCP Documentation](https://fastmcp.readthedocs.io/)
- [MINEO Documentation](https://docs.mineo.app/)

### License

MIT license - see [LICENSE](LICENSE) file for details.