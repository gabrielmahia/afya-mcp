# AI-KungFU East Africa MCP Server
# Glama-compatible Dockerfile for afya-mcp
FROM python:3.12-slim

LABEL org.opencontainers.image.source="https://github.com/gabrielmahia/afya-mcp"
LABEL org.opencontainers.image.description="afya-mcp — East Africa AI Coordination Infrastructure"
LABEL org.opencontainers.image.licenses="MIT"

RUN pip install --no-cache-dir afya-mcp

CMD ["afya-mcp"]
