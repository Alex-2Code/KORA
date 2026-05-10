"""Local-only KORA Studio server skeleton."""

from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any, Callable

from kora.studio_status import get_studio_status

DEFAULT_STUDIO_HOST = "127.0.0.1"
DEFAULT_STUDIO_PORT = 8765
ALLOWED_STUDIO_HOSTS = {"127.0.0.1", "localhost"}

StatusProvider = Callable[[], dict[str, Any]]


def is_allowed_studio_host(host: str) -> bool:
    """Return whether a Studio server host is explicitly local-only."""

    return host in ALLOWED_STUDIO_HOSTS


def get_studio_server_status(host: str = DEFAULT_STUDIO_HOST, port: int = DEFAULT_STUDIO_PORT) -> dict[str, Any]:
    """Return static local server skeleton status without starting a server."""

    studio_status = get_studio_status()
    return {
        "ok": True,
        "service": "kora-studio",
        "status": "preview",
        "implementation": "local_server_skeleton",
        "server": "local-only",
        "host": host,
        "port": port,
        "provider_calls_enabled": False,
        "browser_launch_available": False,
        "ollama_calls_enabled": False,
        "local_runtime_required": False,
        "no_server_side_provider_calls": True,
        "docs_path": studio_status["docs_path"],
        "fixtures_path": studio_status["fixtures_path"],
        "kora_boost_message": studio_status["kora_boost_message"],
        "kora_boost_technical_explanation": studio_status["kora_boost_technical_explanation"],
    }


def get_studio_health_payload() -> dict[str, Any]:
    """Return the /health response payload."""

    return {
        "ok": True,
        "service": "kora-studio",
        "status": "preview",
        "server": "local-only",
        "provider_calls_enabled": False,
        "browser_launch_available": False,
    }


def get_studio_status_payload(host: str = DEFAULT_STUDIO_HOST, port: int = DEFAULT_STUDIO_PORT) -> dict[str, Any]:
    """Return the /status response payload."""

    return get_studio_server_status(host=host, port=port)


def render_studio_server_status_text(status: dict[str, Any]) -> str:
    """Render local server skeleton startup status for CLI output."""

    lines = [
        "KORA Studio local server skeleton starting.",
        f"Local URL: http://{status['host']}:{status['port']}/",
        "Server mode: preview/local-only.",
        "Browser launch: not implemented yet.",
        "Provider calls: disabled. No provider calls are made.",
        "Ollama calls: disabled. No Ollama calls are made.",
        "API keys: not required.",
        "Endpoints: /health, /status, /",
    ]
    return "\n".join(lines) + "\n"


def render_studio_placeholder_html(status: dict[str, Any]) -> str:
    """Render a minimal placeholder page for the preview server."""

    return """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>KORA Studio Preview</title>
</head>
<body>
  <main>
    <h1>KORA Studio Preview</h1>
    <p>Less waiting. Better answers. No hardware upgrade.</p>
    <p>No provider calls. No browser launch. No Ollama calls.</p>
    <p>Docs: {docs_path}</p>
    <p>Fixtures: {fixtures_path}</p>
  </main>
</body>
</html>
""".format(
        docs_path=status["docs_path"], fixtures_path=status["fixtures_path"]
    )


def create_studio_request_handler(status_provider: StatusProvider | None = None) -> type[BaseHTTPRequestHandler]:
    """Create a request handler class for the local Studio preview server."""

    provider = status_provider or get_studio_server_status

    class StudioRequestHandler(BaseHTTPRequestHandler):
        server_version = "KORAStudioPreview/0.1"

        def log_message(self, format: str, *args: object) -> None:  # noqa: A002
            return

        def _write_json(self, payload: dict[str, Any], status_code: int = 200) -> None:
            body = json.dumps(payload, indent=2, sort_keys=True).encode("utf-8")
            self.send_response(status_code)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _write_html(self, html: str, status_code: int = 200) -> None:
            body = html.encode("utf-8")
            self.send_response(status_code)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self) -> None:
            status = provider()
            if self.path == "/health":
                self._write_json(get_studio_health_payload())
                return
            if self.path == "/status":
                self._write_json(status)
                return
            if self.path == "/":
                self._write_html(render_studio_placeholder_html(status))
                return
            self._write_json({"ok": False, "error": "not_found"}, status_code=404)

        def do_POST(self) -> None:
            self._write_json({"ok": False, "error": "post_not_supported"}, status_code=405)

    return StudioRequestHandler


def run_studio_server(host: str = DEFAULT_STUDIO_HOST, port: int = DEFAULT_STUDIO_PORT) -> None:
    """Run the local-only KORA Studio preview server until interrupted."""

    if not is_allowed_studio_host(host):
        raise ValueError("KORA Studio server is local-only; use 127.0.0.1 or localhost.")

    status = get_studio_server_status(host=host, port=port)
    handler = create_studio_request_handler(lambda: get_studio_server_status(host=host, port=port))
    server = ThreadingHTTPServer((host, port), handler)
    try:
        print(render_studio_server_status_text(status), end="", flush=True)
        server.serve_forever()
    except KeyboardInterrupt:
        print("KORA Studio local server stopped.", flush=True)
    finally:
        server.server_close()
