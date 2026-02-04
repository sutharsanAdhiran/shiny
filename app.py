from shiny import App, ui
from pathlib import Path

app_ui = ui.tags.html(
    ui.tags.head(
        ui.tags.title("My React"),
        ui.tags.link(rel="icon", href="/vite.svg", type="image/svg+xml"),
        # PLACEHOLDERS BELOW
        ui.tags.link(rel="stylesheet", href="assets/index-COcDBgFa.css"),
        ui.tags.script(type="module", src="assets/index-j_k5bXI_.js"),
    ),
    ui.tags.body(
        ui.div(id="root")  # React mounts here
    )
)

def server(input, output, session):
    pass

app = App(
    app_ui,
    server,
    static_assets=Path(__file__).parent / "www"
)