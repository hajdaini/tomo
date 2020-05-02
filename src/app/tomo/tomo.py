#!/usr/bin/python3.6
#coding:utf-8
from src.app.item.food import Food
import sys

"""
Classe Tomo
- Personnage principal du jeu
"""
class Tomo:
	def __init__(self, name : str):
		assert name.isalpha(), "C'pas la bonneuh syntaxeuuh"
		assert len(name) > 3 and len(name) <= 20, "Le nom du Tomo doit être compris entre 3 et 20 caractères."

		self.name = name # nom du Tomo
		self.age = 0
		self.max_health = 100
		self.health = self.max_health # vie (TODO : faim à implémenter)
		self.inventory = []

	def __str__(self):
		return f"[Nom {self.name}, Age {self.age}, VieMax {self.max_health}, Vie {self.health}]"

	"""
	Nourrit un Tomo
	@param pts Nombre de points à ajouter aux points de vie
	"""
	def feed(self, pts : int):
		assert pts >= 0, "Le nombre de points ne doit pas être inférieur à 0"

		self.health += pts
		if self.health > self.max_health:
			self.health = self.max_health
		elif self.health <= 0:
			self.die()

	"""
	Tue le Tomo et met fin au jeu
	"""
	def die(self):
		print("Game Over !")
		print(f"Votre Tomo est mort à {self.age} an(s).")
		sys.exit(0)

	"""
	Utilise un objet (de l'inventaire)
	@param item L'objet de l'inventaire
	"""
	def use(self, item : Item):
		assert isinstance(item, Item), "Le paramètre doit être une instance d'Item"

		self.feed(item.heal)
		self.inventory.remove(item)
		item.delete()

if __name__ == '__main__':
	pass