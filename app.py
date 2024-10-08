from textual.app import App
from textual.widgets import Static

class App(App):
    def compose(self):
        yield Static("Hola mundo")
        

if __name__ == "__main__":
    App().run( )