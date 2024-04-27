from textual import on
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
                yield Input(placeholder="First Name Ex=Jhopsion")
                yield Input(placeholder="Last Name")
                yield Button("Primary!", variant="primary")
            yield Footer()
        def action_toggle_dark(self) -> None:
                        self.dark = not self.dark
        def on_mount(self) -> None:
                        self.title = "Open Wallet"
        @on(Button.Pressed)
        def are_there_set_thing_on_what_to_call_this_thing(self):
          yield Button("Primary!", variant="primary"),
if __name__ == "__main__":
        app = BitcoinToolsApp()
        app.run()