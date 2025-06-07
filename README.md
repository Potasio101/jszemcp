# MCP Server

This project provides a minimal MCP server implementation built with FastAPI.
It defines a simple API for managing devices and uses an OpenAPI specification
stored in `mcp_server/openapi.yaml`.

## Requirements

- Python 3.11+
- `fastapi`, `uvicorn`

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Server

```bash
python -m mcp_server.main
```

The API will be available at `http://localhost:8000`. OpenAPI documentation is
served at `http://localhost:8000/docs`.
