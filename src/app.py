from textual.app import App
from textual.widgets import Static
from textual.widget import Widget
from textual.containers import Container
from textual.reactive import Reactive

class Connect4(App):
    
    DEFAULT_CSS = """ 
        Screen{
            width:100%;
            height:100%;
            border: solid white;
            align: center middle;
        }
        #grid{
            width: 100%;
            align: center middle;
            height: auto;
            layout: grid;
            grid-size: 7 6;
            grid-columns: 3;
            grid-rows: 1;
            grid-gutter: 1;
            border: solid white;
            keyline: thin white;
        }
        #main{
            layout: vertical;
            width: 30%;
            height: auto;
            align: center middle;
        }
        Button{
            width: 100%;
            height: 100%;
        }

    """
    redOrYellow = Reactive(0)
    board_state = Reactive([[None for _ in range(6)] for _ in range(7)])
    
    def compose(self):
        with Container(id = "main"):
            yield Header()
            with Container(id = "grid"):
                for i in range(6):
                    for j in range(7):
                        yield Button(X=j, Y=i)
    def on_mount(self):
        print(self.board_state)
        
    def add_token(self, column):
        if self.board_state[column].count(None) <= 6:
            row = self.board_state[column].count(None) - 1
            self.board_state[column][row] = self.redOrYellow
            print(self.board_state)
            print("row:", row)
            return row
            
            
        
class Button(Widget):
    DEFAULT_CSS = """
        Static{
            content-align: center middle;
        }
    """
    def __init__(self, X: int, Y: int):
        self.X = X
        self.Y = Y
        super().__init__()
    
    icon = Reactive(" ")
    
    
    def compose(self):
        yield Static(self.icon)
        
    def on_click(self):
        self.icon = chr(9679)
        
        row = self.app.add_token(self.X)
        
        if row is not None:
            if self.app.redOrYellow == 0:
                for button in self.app.query("Button"):
                    if button.X == self.X:
                        if button.Y == row:
                            print(button.X, button.Y)
                            button.query_one(Static).styles.color = "red"
                            button.query_one(Static).update(self.icon)
                for Heade in self.app.query("Header"):
                    Heade.query_one("#turno", Static).styles.color = "yellow"
                    Heade.query_one("#turno", Static).update(self.icon)
                self.app.redOrYellow = 1
            else:
                for button in self.app.query("Button"):
                    if button.X == self.X:
                        if button.Y == row:
                            print(button.X, button.Y)
                            button.query_one(Static).styles.color = "yellow"
                            button.query_one(Static).update(self.icon)
                for Heade in self.app.query("Header"):
                    Heade.query_one("#turno", Static).styles.color = "red"
                    Heade.query_one("#turno", Static).update(self.icon)
                self.app.redOrYellow = 0
                
        print(row)
        print(self.X, self.Y)
        
        
        
class Header(Widget):
    DEFAULT_CSS = """
        Header{
            width: 100%;
            height: 1;
            layout: horizontal;
            align: center middle;
            background: $foreground 10%;
        }
        #turno{
            width: auto;
            height: auto;
        }
        #turnoTitle{
            width: auto;
            height: auto;
        }
        #title{
            width: auto;
            margin-right: 3;
            height: auto;
        }
    """
    
    def compose(self):
        yield Static("Conecta 4", id = "title")
        yield Static("Turno: ", id = "turnoTitle")
        yield Static(" ", id = "turno")

if __name__ == "__main__":
    Connect4().run()