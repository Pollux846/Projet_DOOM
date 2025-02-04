# module pyglet principal (qu'on nenomme en pg pour plus de simplicité)
import pyglet as pg
# outils mathématiques
from math import sqrt

class Mur:
    def __init__(self, xA, yA, xB, yB):
        # un mur est un segment 2D entre deux points
        self.x1, self.y1 = xA, yA
        self.x2, self.y2 = xB, yB
        # étendue du mur (coordonnées du vecteur AB)
        self.dx = xB - xA
        self.dy = yB - yA
        # longueur du mur
        self.l = sqrt(self.dx**2+self.dy**2)
        # vecteur directeur (unitaire)
        self.u = (self.dx/self.l, self.dy/self.l)
        # vecteur orthogonal (unitaire)
        self.N = (self.u[1], -self.u[0])
        # "batch" du mur
        self.batch = pg.graphics.Batch()
        self.dessin = {}
    def equation_droite(self):
        p = (self.y1/(self.dy/self.dx))-self.x1
        m = self.dy/self.dx
        return (m, p, self.x1, self.x2)
    def tracer(self):
        # le mur comme un segment
        self.dessin['mur'] = pg.shapes.Line(self.x1,self.y1,self.x2,self.y2, batch=self.batch)
    def afficher(self):
        self.batch.draw()
    def debug(self):
        print("Mur ({},{})->({},{})".format(self.x1,self.y1,self.x2,self.y2))
        print("-> longueur l :", self.l)
        print("-> étendue dx et dy :",self.dx,",",self.dy)
        print("-> vecteur directeur u :",self.u)
        print("-> vecteur orthogonal N :",self.N)
        