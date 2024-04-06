from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
class BitcoinToolsApp(App):
  BINDINGS = [("d", "toggle_dark", "Toggle dark mode")] 
  def compose(self) -> ComposeResult:
      yield Header()
      yield Footer()
  def action_toggle_dark(self) -> None:
      self.dark = not self.dark
if __name__ == "__main__":
  app = BitcoinToolsApp()
  app.run()