from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Label
class BitcoinToolsApp(App):
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    CSS_PATH = "bitcoin_tools.css""
    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Welcom, human!") 
        yield Footer()
    def action_toggle_dark(self) -> None:
            self.dark = not self.dark
    def on_mount(self) -> None:
            self.title = "Open Wallet"
    
if __name__ == "__main__":
    app = BitcoinToolsApp()
    app.run()