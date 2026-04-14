$url = "http://127.0.0.1:18099/healthz"

Write-Host "Checking $url ..."

try {
  $response = Invoke-WebRequest -UseBasicParsing -Uri $url -TimeoutSec 10
  Write-Host ""
  Write-Host "Lingxing MCP gateway is reachable."
  Write-Host $response.Content
} catch {
  Write-Host ""
  Write-Host "Lingxing MCP gateway is not reachable."
  Write-Host "Make sure 01_open_tunnel.cmd is still running."
  Write-Host $_.Exception.Message
  exit 1
}
