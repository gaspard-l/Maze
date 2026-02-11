# Maze v1.0

Maze est un jeu de labyrinthe développé en Python à l’aide de la bibliothèque Pygame. Le joueur contrôle un personnage devant traverser plusieurs niveaux en évitant des murs fixes et des obstacles mobiles. Le jeu intègre un système de tentatives, un menu principal ainsi qu’un écran de fin récapitulatif.
Ce projet m’a permis de consolider mes compétences en programmation Python, conception logique, structuration du code, gestion d’événements et en mise en œuvre d’un programme interactif temps réel.

---

## Fonctionnalités

- Menu principal simple (jouer / quitter)
- Plusieurs niveaux avec des murs fixes et des obstacles mobiles  
- Déplacement fluide du joueur avec gestion des collisions  
- Compteur de tentatives par niveau et total    
- Écran de fin affichant le nombre total de tentatives et permettant de rejouer ou quitter  
- Gestion des entrées clavier (flèches, espace, échap, A)  
- Interface graphique avec affichage dynamique des éléments et textes  

---

## Exemple d’utilisation

Appuyez sur la touche A pour commencer à jouer. Utilisez les flèches pour déplacer le joueur et éviter les obstacles. À la fin, un écran affiche le nombre total de tentatives, appuyez sur A pour rejouer ou Espace pour quitter.

---

## Structure du projet

```plaintext
maze/
├── main.py           # Script principal avec la boucle de jeu et la logique
└── README.md         # Documentation du projet
```

---

## Installation et exécution

pip install pygame    # Installer pygame si nécessaire

python main.py

---

## Améliorations possibles

- Repenser l’architecture du projet pour une meilleure modularité
- Ajouter un système de chronométrage par niveau et global
- Enrichir le jeu avec de nouveaux niveaux et mécaniques de difficulté
- Repenser l’ensemble du code en programmation orientée objet afin d’améliorer la maintenabilité, la lisibilité et l’évolutivité du projet

---

## Licence
Ce projet est libre d’utilisation et de modification.

---

## Auteur

Gaspard Lesourd
