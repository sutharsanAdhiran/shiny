

from pathlib import Path
from shiny import App, ui, render

static_dir = Path(__file__).parent / "www"

app_ui = ui.page_fluid(
    ui.tags.head(
        # Disable Bootstrap styles inside iframe
        ui.tags.style("""
        body, html { margin:0; padding:0; }
        .container-fluid { padding:0; margin:0; display:flex; }
        """)
    ),
    ui.tags.iframe(
        src="index.html",
        style="width:100%; height:100vh; border:none;"
    )
)

def server(input, output, session):
    pass

app = App(app_ui, server, static_assets=str(static_dir))
