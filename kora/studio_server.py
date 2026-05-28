"""Local-only KORA Studio server skeleton."""

from __future__ import annotations

import html
import json
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any, Callable

from kora.studio_status import get_studio_status

DEFAULT_STUDIO_HOST = "127.0.0.1"
DEFAULT_STUDIO_PORT = 8765
ALLOWED_STUDIO_HOSTS = {"127.0.0.1", "localhost"}

StatusProvider = Callable[[], dict[str, Any]]
BrowserOpener = Callable[[str], bool]


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
        "cloud_sync_enabled": False,
        "browser_launch_available": True,
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
        "cloud_sync_enabled": False,
        "browser_launch_available": True,
    }


def get_studio_status_payload(host: str = DEFAULT_STUDIO_HOST, port: int = DEFAULT_STUDIO_PORT) -> dict[str, Any]:
    """Return the /status response payload."""

    return get_studio_server_status(host=host, port=port)


def get_studio_url(host: str = DEFAULT_STUDIO_HOST, port: int = DEFAULT_STUDIO_PORT) -> str:
    """Return the local KORA Studio URL."""

    return f"http://{host}:{port}/"


def open_studio_browser(url: str, browser_opener: BrowserOpener = webbrowser.open) -> bool:
    """Open the Studio URL with a mockable browser opener."""

    try:
        return bool(browser_opener(url))
    except Exception:
        return False


def render_studio_server_status_text(
    status: dict[str, Any],
    *,
    open_browser: bool = True,
    browser_opened: bool | None = None,
) -> str:
    """Render local server skeleton startup status for CLI output."""

    url = get_studio_url(str(status["host"]), int(status["port"]))
    lines = [
        "Launching KORA Studio...",
        "",
        "Local URL:",
        url,
        "",
        "Mode:",
        "Local-only",
        "Provider calls: disabled",
        "Cloud sync: disabled",
        "",
        "Press Ctrl+C to stop.",
    ]
    if open_browser and browser_opened is False:
        lines.extend(["", "Browser launch failed. Open this URL manually:", url])
    elif not open_browser:
        lines.extend(["", "Browser launch: disabled by --no-browser."])
    return "\n".join(lines) + "\n"


def render_studio_placeholder_html(status: dict[str, Any]) -> str:
    """Render the static KORA Studio preview page."""

    docs_path = html.escape(str(status["docs_path"]), quote=True)
    fixtures_path = html.escape(str(status["fixtures_path"]), quote=True)
    boost_message = html.escape(str(status["kora_boost_message"]), quote=True)
    boost_explanation = html.escape(str(status["kora_boost_technical_explanation"]), quote=True)

    return f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <title>KORA Studio</title>
  <style>
    :root {{
      color-scheme: dark;
      --bg: #071014;
      --panel: #0d1b22;
      --panel-2: #10242d;
      --panel-3: #0a171d;
      --text: #edf7fa;
      --muted: #9fb3bd;
      --cyan: #32d1e6;
      --amber: #f0b44c;
      --green: #57d68d;
      --line: #24424d;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.5;
    }}
    main {{
      width: min(1120px, calc(100% - 40px));
      margin: 0 auto;
      padding: 42px 0 34px;
    }}
    header {{
      border: 1px solid var(--line);
      background: linear-gradient(180deg, var(--panel), var(--panel-2));
      border-radius: 8px;
      padding: 28px;
    }}
    .topline {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      margin-bottom: 22px;
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      border: 1px solid var(--green);
      color: var(--green);
      border-radius: 999px;
      padding: 6px 12px;
      font-size: 13px;
      font-weight: 700;
      white-space: nowrap;
    }}
    h1 {{
      margin: 0 0 8px;
      font-size: clamp(34px, 6vw, 58px);
      letter-spacing: 0;
      line-height: 1.05;
    }}
    h2 {{
      margin: 0 0 14px;
      font-size: 20px;
      letter-spacing: 0;
    }}
    h3 {{
      margin: 0 0 6px;
      font-size: 15px;
      letter-spacing: 0;
    }}
    p {{ margin: 0; }}
    a {{ color: var(--cyan); }}
    code {{
      color: var(--amber);
      background: #071014;
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 2px 6px;
      overflow-wrap: anywhere;
    }}
    .subtitle {{
      color: var(--muted);
      font-size: 17px;
      max-width: 760px;
    }}
    .boost {{
      color: var(--cyan);
      font-size: 24px;
      font-weight: 800;
      margin-top: 18px;
    }}
    .technical {{
      color: var(--muted);
      max-width: 820px;
      margin-top: 10px;
      font-size: 16px;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 16px;
      margin-top: 18px;
    }}
    section, .card {{
      border: 1px solid var(--line);
      background: var(--panel);
      border-radius: 8px;
      padding: 18px;
    }}
    .status-card {{
      min-height: 118px;
      background: var(--panel-3);
    }}
    .status-card p {{ color: var(--muted); }}
    .status-value {{
      color: var(--green);
      font-weight: 800;
      margin-top: 8px;
    }}
    .status-value.disabled {{ color: var(--amber); }}
    .workflow {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 12px;
    }}
    .step {{
      border: 1px solid var(--line);
      background: var(--panel-3);
      border-radius: 8px;
      padding: 14px;
      min-height: 130px;
    }}
    .step-number {{
      color: var(--cyan);
      font-size: 13px;
      font-weight: 800;
      margin-bottom: 8px;
    }}
    ul {{
      margin: 0;
      padding-left: 20px;
      color: var(--muted);
    }}
    li + li {{ margin-top: 8px; }}
    .section-stack {{
      display: grid;
      gap: 18px;
      margin-top: 18px;
    }}
    .footer {{
      color: var(--muted);
      border-top: 1px solid var(--line);
      margin-top: 22px;
      padding-top: 16px;
      font-size: 14px;
    }}
    @media (max-width: 760px) {{
      main {{ width: min(100% - 24px, 1120px); padding-top: 24px; }}
      header {{ padding: 20px; }}
      .topline {{ align-items: flex-start; flex-direction: column; }}
      .workflow {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <main>
    <header>
      <div class=\"topline\">
        <strong>Local v0.1 Skeleton</strong>
        <span class=\"badge\">Preview / Local-only</span>
      </div>
      <h1>KORA Studio</h1>
      <p class=\"subtitle\">A static AI Task Execution Router prototype for deterministic-first local workflow exploration. KORA Studio routes local AI workflows, not just local models.</p>
      <p class=\"boost\">{boost_message}</p>
      <p class=\"technical\">{boost_explanation}</p>
      <p class=\"technical\">Standard Mode sends every step to the model. KORA Boost routes deterministic and structured tasks to CPU/local fast paths first, so the model becomes one execution path, not the default path.</p>
    </header>

    <section aria-label=\"Status Cards\" style=\"margin-top: 18px;\">
      <h2>Status Cards</h2>
      <div class=\"grid\">
        <div class=\"status-card card\"><h3>Server</h3><p class=\"status-value\">Server: local</p><p>Bound to the local Studio skeleton.</p></div>
        <div class=\"status-card card\"><h3>Provider Calls</h3><p class=\"status-value disabled\">Provider calls: disabled</p><p>No remote provider requests are made.</p></div>
        <div class=\"status-card card\"><h3>Model Runtime</h3><p class=\"status-value disabled\">Model/runtime integration: not connected</p><p>Future runtime work must distinguish physically runnable local models from workflow-usable models.</p></div>
        <div class=\"status-card card\"><h3>Browser Launch</h3><p class=\"status-value\">Browser launch: available</p><p>The CLI opens the local page by default; use <code>--no-browser</code> to suppress it.</p></div>
        <div class=\"status-card card\"><h3>Ollama</h3><p class=\"status-value disabled\">Ollama integration: not connected</p><p>No Ollama detection or model calls happen here.</p></div>
      </div>
    </section>

    <div class=\"section-stack\">
      <section>
        <h2>Endpoint Panel</h2>
        <div class=\"grid\">
          <div class=\"card\"><h3><a href=\"/health\">/health</a></h3><p>Returns local health status JSON for the preview server.</p></div>
          <div class=\"card\"><h3><a href=\"/status\">/status</a></h3><p>Returns local preview status, KORA Boost copy, docs paths, and fixture paths.</p></div>
        </div>
      </section>

      <section>
        <h2>Workflow Preview</h2>
        <div class=\"workflow\">
          <div class=\"step\"><p class=\"step-number\">01</p><h3>Request / System Profile</h3><p>Planned: show what this machine can physically run.</p></div>
          <div class=\"step\"><p class=\"step-number\">02</p><h3>Deterministic checks / Route Selection</h3><p>Planned: choose deterministic code, structured lookup, local model, or larger execution path only when needed.</p></div>
          <div class=\"step\"><p class=\"step-number\">03</p><h3>Local status / KORA Boost</h3><p>Planned: route deterministic and structured work to CPU/local fast paths first.</p></div>
          <div class=\"step\"><p class=\"step-number\">04</p><h3>Future runtime integration placeholder</h3><p>Placeholder only; no runtime execution occurs on this page.</p></div>
        </div>
      </section>

      <section>
        <h2>Limitations Panel</h2>
        <ul>
          <li>No full frontend yet</li>
          <li>No provider calls</li>
          <li>No model/runtime integration yet</li>
          <li>Browser launch is local-only and can be disabled with <code>--no-browser</code></li>
          <li>No Ollama integration</li>
          <li>No production/API-cost/energy claims</li>
          <li>No claim that KORA removes model memory requirements</li>
          <li>External/provider/distributed routes disabled by default</li>
        </ul>
      </section>

      <section>
        <h2>Local References</h2>
        <ul>
          <li><code>{docs_path}</code></li>
          <li><code>{fixtures_path}</code></li>
        </ul>
      </section>
    </div>

    <p class=\"footer\">Local-only skeleton. Claim-safe AI Task Execution Router preview; KORA does not make large models smaller or remove memory requirements.</p>
  </main>
</body>
</html>
"""


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


def run_studio_server(
    host: str = DEFAULT_STUDIO_HOST,
    port: int = DEFAULT_STUDIO_PORT,
    *,
    open_browser: bool = True,
    browser_opener: BrowserOpener = webbrowser.open,
) -> None:
    """Run the local-only KORA Studio preview server until interrupted."""

    if not is_allowed_studio_host(host):
        raise ValueError("KORA Studio server is local-only; use 127.0.0.1 or localhost.")

    status = get_studio_server_status(host=host, port=port)
    handler = create_studio_request_handler(lambda: get_studio_server_status(host=host, port=port))
    server = ThreadingHTTPServer((host, port), handler)
    browser_opened = open_studio_browser(get_studio_url(host, port), browser_opener) if open_browser else None
    try:
        print(
            render_studio_server_status_text(
                status,
                open_browser=open_browser,
                browser_opened=browser_opened,
            ),
            end="",
            flush=True,
        )
        server.serve_forever()
    except KeyboardInterrupt:
        print("KORA Studio local server stopped.", flush=True)
    finally:
        server.server_close()
