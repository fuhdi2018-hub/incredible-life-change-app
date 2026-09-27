$root = "C:\Users\NIPOST 17\Documents\incredible\incredible-life-change-app-1"
$prefix = "http://localhost:8000/"
$mime = @{
  ".html"="text/html"; ".js"="text/javascript"; ".json"="application/json";
  ".png"="image/png"; ".ttf"="font/ttf"; ".webmanifest"="application/manifest+json"
}
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add($prefix)
try { $listener.Start() } catch { Write-Output "START-FAILED: $_"; exit 1 }
Write-Output "SERVING $root on $prefix"
while ($listener.IsListening) {
  $ctx = $listener.GetContext()
  $rel = $ctx.Request.Url.LocalPath.TrimStart("/")
  if ([string]::IsNullOrEmpty($rel)) { $rel = "index.html" }
  $file = Join-Path $root $rel
  if (Test-Path $file -PathType Container) { $file = Join-Path $file "index.html" }
  if (Test-Path $file -PathType Leaf) {
    $ext = [IO.Path]::GetExtension($file).ToLower()
    $ct = if ($mime.ContainsKey($ext)) { $mime[$ext] } else { "application/octet-stream" }
    $bytes = [IO.File]::ReadAllBytes($file)
    $ctx.Response.ContentType = $ct
    $ctx.Response.ContentLength64 = $bytes.Length
    $ctx.Response.OutputStream.Write($bytes, 0, $bytes.Length)
  } else {
    $ctx.Response.StatusCode = 404
    $msg = [Text.Encoding]::UTF8.GetBytes("Not found")
    $ctx.Response.OutputStream.Write($msg, 0, $msg.Length)
  }
  $ctx.Response.OutputStream.Close()
}
