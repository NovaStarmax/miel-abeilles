
# Le Miel et les Abeilles

### Description du projet

_"Le miel et les abeilles"_ est un projet simulant l'évolution d'une colonie d'abeilles dans un environnement naturel. L'objectif est d'utiliser un **algorithme génétique** pour optimiser les déplacements des abeilles à travers un champ de fleurs mellifères, en améliorant leur efficacité de butinage au fil des générations. Le projet met en œuvre des concepts d'algorithmique évolutive et de simulation de comportements collectifs, avec une visualisation graphique des résultats.

### Fonctionnalités principales

- Simulation de l'évolution d'une colonie d'abeilles.
- Optimisation des chemins de butinage des abeilles dans un champ de fleurs à l'aide d'un algorithme génétique.
- Visualisation des chemins optimaux empruntés par les abeilles.
- Génération de graphiques représentant les performances des générations successives d'abeilles.

### Structure du projet

Le projet est composé des fichiers suivants :

- **`beehive.py`** : Contient les classes et fonctions relatives à la simulation de la ruche et des abeilles.
- **`main.py`** : Fichier de simulation principale exécutant l'algorithme génétique pour améliorer l'efficacité des abeilles.
- **`config.py`** : Paramètres de configuration pour ajuster les paramètres de l'algorithme (taux de mutation, reproduction, etc.).
- **`flower.json`, `flower_5.json`, `flower_10.json`, `flower_30.json`** : Données des positions des fleurs dans le champ pour différents scénarios.
  
### Algorithme génétique

L'algorithme génétique utilisé dans ce projet se base sur les principes suivants :
- **Sélection naturelle** : Les abeilles les plus rapides à butiner sont sélectionnées pour se reproduire.
- **Mutation** : Un taux de mutation permet de simuler l'exploration de nouveaux chemins dans le champ de fleurs.
- **Reproduction** : Les abeilles les plus performantes transmettent leurs connaissances à leurs descendants.

L'objectif est de minimiser le temps de parcours pour butiner toutes les fleurs et retourner à la ruche, située aux coordonnées (500, 500).

### Visualisation

Deux graphiques sont générés pour visualiser les résultats de la simulation :
1. **Chemin optimal de la meilleure abeille** : Représentation graphique des positions des fleurs et du chemin emprunté par la meilleure abeille de la dernière génération.
2. **Évolution des performances** : Graphique montrant l'évolution du temps moyen de butinage pour chaque génération d'abeilles.

### Contributeurs

- Sulivan
- Inès
- Antoine

### Comment exécuter le projet

1. Cloner le repository :
   ```bash
   git clone https://github.com/<ton-utilisateur>/miel-abeilles.git
   cd miel-abeilles
   ```

2. Installer les dépendances nécessaires :
   ```bash
   pip install -r requirements.txt
   ```

3. Lancer la simulation :
   ```bash
   python main.py
   ```

4. Visualiser les résultats graphiques.

### Conclusion

Ce projet démontre l'application pratique des algorithmes génétiques pour résoudre des problèmes d'optimisation inspirés de la nature. Grâce à une approche évolutive, la colonie d'abeilles améliore ses performances au fil du temps, offrant une solution élégante à un problème complexe.
