import turtle

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def tracer_figure(self):

        # Création une nouvelle turtle pour dessiner
        t = turtle.Turtle()  

        # Définissons les couleurs des côtés
        couleurs = ["blue", "red"]  

        # Tracons les côtés du rectangle en utilidsant une boucle for sur 4 itérations
        for i in range(4):  
            # On alterne les deux couleurs
            t.color(couleurs[i % 2])  
            # Si i est paire, on trace selon la longueur
            if i % 2 == 0:
                t.forward(self.longueur)  
            # Sinon, on trace selon la largeur    
            else:
                t.forward(self.largeur)  
            
            # Ensuite on tourne de 90 degrés pour dessiner un angle droit
            t.left(90)  

        # Terminons le dessin du rectangle
        turtle.done()  

# Création du rectangle avec une longueur 200 et une largeur 100
rectangle = Rectangle(200, 100)  

# Appel de la méthode pour tracer le rectangle
rectangle.tracer_figure()  
