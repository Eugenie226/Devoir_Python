import turtle

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def draw(self):
        t = turtle.Turtle()
        t.penup()

        # Positionnons le coin inférieur gauche
        t.setpos(-self.longueur / 2, -self.largeur / 2)  
        t.pendown()

        # Couleur de la bordure
        t.color("red")

        # Début du remplissage  
        t.begin_fill()  

        # Couleur de remplissage
        t.fillcolor("black")  
        for _ in range(2):
            t.forward(self.longueur)
            t.left(90)
            t.forward(self.largeur)
            t.left(90)

        # Fin du remplissage
        t.end_fill()  
        turtle.done()

class Square(Rectangle): 
    def __init__(self, cote):
        super().__init__(cote, cote)

# Création du rectangle avec une longueur 200 et une largeur 100
rectangle = Rectangle(200, 100)
rectangle.draw()

# Création du carré avec les cotés 150 
square = Square(150)
square.draw()
