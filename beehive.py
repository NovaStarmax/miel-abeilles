import random

class Beehive:
    def __init__(self):
        self.nb_bee = 100
        self.hive_position = (500, 500)
        # Proposer un input pour gamifier notre programme
        self.selected_bees = 0.2
        self.mutation_rate = 0.1
        self.mutation_frequency = 0.2

    def create_bees(self, flowers):
        bees = []
        for _ in range (self.nb_bee):
            bees.append(self.create_bee(flowers))
        return bees

    def create_bee(self, flowers):
        bee = random.sample(flowers,len(flowers))
        bee.insert(0, self.hive_position)
        bee.insert(-1, self.hive_position)
        return bee 
         

    #def mutate_bees(self, bees):
        #for i in range(len(bees)):
            #if random.random < self.mutation_frequency:
                #return 
            
    def cross_bees():
        pass
    
    def reproduce_bees():
        pass
        #for bee in self.bees:
            
        #self.bees[:10]
        
        
# def tournamentSelection(generation, Ntour):
#     """
#     Permet le choix aléatoire de meilleurs individus de la génération.
 
#     @parameters:
#         generation: une liste de tuples (individu, fitnessValue)
#         Ntour: un entier (integer)
 
#     @return:
#         populationSelection: une liste
#     """
 
#     populationSelection = [] # Création de notre variable de sortie
 
#     for i in range(len(generation)):
#         populationRandom = [] # Création de notre liste de sélection aléatoire
 
#         for j in range(Ntour):
#             populationRandom.append(generation[random.randrange(len(generation))]) # On choisit aléatoirement des 
# # individus de la génération
         
#         populationRandom = sorted(populationRandom, key=lambda x: x[1]) # Trier en fonction de la valeur du fitness
#         populationSelection.append(populationRandom[0]) # Ajouter à notre variable de sortie l'individu ayant le 
# # meilleur fitness
 
#     populationSelection = sorted(populationSelection, key=lambda x: x[1]) # Trier en fonction du fitness
#     a = populationSelection[:] # Faire une copie de la variable de sortie
#     for i in range(len(a)):
#         populationSelection[i] = a[i][0] # On choisit l'individu sans le fitness
 
#     return populationSelection