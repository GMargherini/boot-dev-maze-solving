class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.a.x, self.a.y, self.b.x, self.b.y, fill=fill_color, width=2)