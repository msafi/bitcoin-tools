from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Label
class BitcoinToolsApp(App):
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    CSS_PATH = "bitcoin_tools.tcss"
    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Welcome, human!                                                               \n what name be?gtrfhfghbrtfgbdf", id="one")
        #yield Label("Wasup my broskir67y8hugfygtuhgtyuhgftyuhygyftugytu?", id="two")
        #yield Label("when the text above you has a stroke ",id="funny-text")
        yield Footer()
    def action_toggle_dark(self) -> None:
            self.dark = not self.dark
    def on_mount(self) -> None:
            self.title = "Open Wallet"
if __name__ == "__main__":
    app = BitcoinToolsApp()
    app.run()