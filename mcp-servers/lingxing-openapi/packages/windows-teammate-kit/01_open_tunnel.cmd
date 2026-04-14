@echo off
setlocal

set GATEWAY_USER=replace-with-gateway-user
set GATEWAY_HOST=replace-with-gateway-host
set LOCAL_PORT=18099
set REMOTE_PORT=8099

echo Starting Lingxing MCP tunnel...
echo.
echo Local:  http://127.0.0.1:%LOCAL_PORT%/mcp
echo Remote: %GATEWAY_USER%@%GATEWAY_HOST% -> 127.0.0.1:%REMOTE_PORT%
echo.
echo Keep this window open while using Lingxing MCP.
echo.

ssh -N -L %LOCAL_PORT%:127.0.0.1:%REMOTE_PORT% %GATEWAY_USER%@%GATEWAY_HOST%
