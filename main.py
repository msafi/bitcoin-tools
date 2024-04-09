from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Label, Input, Button, Static
from textual.containers import Center
class BitcoinToolsApp(App):
        BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
        CSS_PATH = "bitcoin_tools.tcss"
        def compose(self) -> ComposeResult:
            yield Header()
            with Center():
                yield Label("Welcome, human!\nwhat name be?", id="one")
            with Center():
                yield Input(placeholder="First Name")
                yield Input(placeholder="Last Name")
            yield Footer()
        def action_toggle_dark(self) -> None:
                        self.dark = not self.dark
        def on_mount(self) -> None:
                        self.title = "Open Wallet"
if __name__ == "__main__":
        app = BitcoinToolsApp()
        app.run()