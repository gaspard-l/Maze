import pygame
import sys

pygame.init()

LARGEUR, HAUTEUR = 700, 200
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))

pygame.display.set_caption("Acceuil")
accueil = 1

# Polices et couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
BLEU = (50, 100, 255)
ROUGE = (230, 20, 0)

font_20 = pygame.font.Font(None, 20) 
font_30 = pygame.font.Font(None, 30) 
font_40 = pygame.font.Font(None, 40)

# Joueur
joueur = pygame.Rect(15, 5, 12, 12)
vitesse = 3
position_depart = joueur.topleft

# Murs
niveau = [
    {
        "mur":[
            pygame.Rect(0, -1, LARGEUR, 1),           # Mur haut
            pygame.Rect(0, HAUTEUR, LARGEUR, 1),      # Mur bas
            pygame.Rect(-1, 0, 1, HAUTEUR),           # Mur gauche
            pygame.Rect(LARGEUR + 1, 0, 1, HAUTEUR),  # Mur droite
            pygame.Rect(50, 0, 7, 80),
            pygame.Rect(50, 115, 7, 90),
            pygame.Rect(100, 0, 7, 15),
            pygame.Rect(100, 50, 7, 110),
            pygame.Rect(150, 0, 7, 170),
            pygame.Rect(200, 30, 7, 170),
            pygame.Rect(250, 0, 7, 170),
            pygame.Rect(300, 170, 7, 30),
            pygame.Rect(250, 133, 75, 7),
            pygame.Rect(300, 90, 70, 7),
            pygame.Rect(250, 50, 70, 7),
            pygame.Rect(370, 30, 7, 170),
            pygame.Rect(470, 0, 7, 150),
            pygame.Rect(470, 185, 7, 15),
            pygame.Rect(520, 0, 7, 30),
            pygame.Rect(520, 70, 7, 130),
            pygame.Rect(570, 0, 7, 100),
            pygame.Rect(570, 140, 7, 60),
            pygame.Rect(620, 120, 7, 80)
        ],
        "mur_mobile": [
            {
                "rect" : pygame.Rect(420, 10, 7, 50),
                "vitesse": 2,
                "min": 0,
                "max": 150,
                "sens": "vertical"
            },
            {
                "rect": pygame.Rect(620, 60, 7, 10),
                "vitesse": 1.4,
                "min": 60,
                "max": 110,
                "sens": "vertical"
            }
        ],
        "fin" : pygame.Rect(627, 170, 73, 30),
        "temps": pygame.Rect(570, 53, 130, 7),
        "essais": 1
    },
    {
        "mur": [
            pygame.Rect(0, -1, LARGEUR, 1),           # Mur haut
            pygame.Rect(0, HAUTEUR, LARGEUR, 1),      # Mur bas
            pygame.Rect(-1, 0, 1, HAUTEUR),           # Mur gauche
            pygame.Rect(LARGEUR + 1, 0, 1, HAUTEUR),  # Mur droite
            pygame.Rect(50, 0, 7, 80),
            pygame.Rect(50, 115, 7, 90),
            pygame.Rect(100, 0, 7, 140),
            pygame.Rect(100, 175, 7, 90),
            pygame.Rect(150, 0, 7, 30),
            pygame.Rect(150, 65, 7, 135),
            pygame.Rect(200, 0, 7, 140),
            pygame.Rect(200, 175, 7, 45),
            pygame.Rect(250, 40, 7, 160),
            pygame.Rect(250, 40, 100, 7),
            pygame.Rect(400, 0, 7, 170),
            pygame.Rect(300, 80, 100, 7),
            pygame.Rect(250, 120, 100, 7),
            pygame.Rect(300, 163, 100, 7),
            pygame.Rect(450, 170, 200, 7),
            pygame.Rect(620, 170, 7, 30),
            pygame.Rect(450, 148, 177, 7),
            pygame.Rect(450, 0, 7, 35),
            pygame.Rect(450, 80, 7, 72),
            pygame.Rect(495, 0, 7, 120),
            pygame.Rect(535, 30, 7, 120),
            pygame.Rect(570, 0, 7, 120)
        ],
        "mur_mobile": [
            {
                "rect" : pygame.Rect(100, 10, 7, 50),
                "vitesse": 2,
                "min": 0,
                "max": 200,
                "sens": "vertical"
            },
            {
                "rect" : pygame.Rect(150, 10, 7, 85),
                "vitesse": 4,
                "min": 0,
                "max": 135,
                "sens": "vertical"
            },
            {
                "rect" : pygame.Rect(150, 100, 7, 10),
                "vitesse": 0.6,
                "min": 150,
                "max": 200,
                "sens": "horizontale"
            },
            {
                "rect" : pygame.Rect(220, 115, 7, 10),
                "vitesse": 0.6,
                "min": 200,
                "max": 250,
                "sens": "horizontale"
            },
            {
                "rect" : pygame.Rect(250, 70, 7, 10),
                "vitesse": 0.6,
                "min": 200,
                "max": 250,
                "sens": "horizontale"
            },
            {
                "rect" : pygame.Rect(343, 0, 7, 40),
                "vitesse": 0.6,
                "min": -50,
                "max": 0,
                "sens": "vertical"
            },
            {
                "rect" : pygame.Rect(250, 0, 7, 40),
                "vitesse": 1,
                "min": 0,
                "max": 80,
                "sens": "vertical"
            },
            {
                "rect" : pygame.Rect(300, 47, 7, 40),
                "vitesse": 1,
                "min": 47,
                "max": 160,
                "sens": "vertical"
            },
            {
                "rect" : pygame.Rect(535, 0, 7, 40),
                "vitesse": 1,
                "min": 0,
                "max": 130,
                "sens": "vertical"
            },
            {
                "rect" : pygame.Rect(570, 54, 165, 7),
                "vitesse": 1,
                "min": 54,
                "max": 147,
                "sens": "vertical"
            }
        ],
        "fin": pygame.Rect(627, 170, 73, 30),
        "temps": pygame.Rect(570, 53, 130, 7),
        "essais": 0
    }
]

clock = pygame.time.Clock()


def deplacements(actuel, niveau):
    touches = pygame.key.get_pressed()
    dx = 0
    dy = 0

    if touches[pygame.K_LEFT]:
        dx = -vitesse
    if touches[pygame.K_RIGHT]:
        dx = vitesse
    if touches[pygame.K_UP]:
        dy = -vitesse
    if touches[pygame.K_DOWN]:
        dy = vitesse

    # Mouvement horizontal
    joueur.x += dx
    for mur in niveau[actuel]["mur"]:
        if joueur.colliderect(mur):
            #joueur.topleft = position_depart
            niveau[actuel]["essais"] += 1

    # Mouvement vertical
    joueur.y += dy
    for mur in niveau[actuel]["mur"]:
        if joueur.colliderect(mur):
            #joueur.topleft = position_depart
            niveau[actuel]["essais"] += 1

def murs_mobiles(actuel, niveau):
    for mur_mobile in niveau[actuel]["mur_mobile"]:         
        # Mur a mouvement vertical
        if mur_mobile["sens"] == "vertical":
            mur_mobile["rect"].y += mur_mobile["vitesse"]
            if mur_mobile["rect"].y < mur_mobile["min"] or mur_mobile["rect"].y > mur_mobile["max"]:
                mur_mobile["vitesse"] *= -1
            if joueur.colliderect(mur_mobile["rect"]):
                #joueur.topleft = position_depart
                niveau[actuel]["essais"] += 1
        # Mur a mouvement horizontal 
        else:                                             
            mur_mobile["rect"].x += mur_mobile["vitesse"]
            if mur_mobile["rect"].x < mur_mobile["min"] or mur_mobile["rect"].x > mur_mobile["max"]:
                mur_mobile["vitesse"] *= -1
            if joueur.colliderect(mur_mobile["rect"]):
                #joueur.topleft = position_depart
                niveau[actuel]["essais"] += 1

def fin_niveau(actuel, niveau, jeu_en_cours):
    if joueur.colliderect(niveau[actuel]["fin"]):
        actuel += 1
        if actuel >= len(niveau):
            jeu_en_cours = 0
        else:
            # Réinitialiser position joueur
            joueur.x, joueur.y = 50, 50
        pygame.display.set_caption(f"Niveau {actuel+1}")
    return actuel, jeu_en_cours

def affichages(actuel, niveau):
    # Affichage murs
    ecran.fill(BLANC)
    pygame.draw.rect(ecran, BLEU, joueur)
    for mur in niveau[actuel]["mur"]:
        pygame.draw.rect(ecran, NOIR, mur)
    for mur_mobile in niveau[actuel]["mur_mobile"]:
        pygame.draw.rect(ecran, NOIR, mur_mobile["rect"])

    # Affichage arrivee
    pygame.draw.rect(ecran, ROUGE, niveau[actuel]["fin"])
    texte = font_30.render("FIN", True, BLANC)
    ecran.blit(texte, (647, 177))
    pygame.draw.rect(ecran, NOIR, niveau[actuel]["temps"])
    nombre_essai = font_20.render(f"Tentatives : {niveau[actuel]["essais"]}", True, NOIR)
    ecran.blit(nombre_essai, (585, 20))

def ecran_accueil():
    ecran.fill(BLANC)
    # Texte principal
    titre = font_40.render("Bienvenue", True, NOIR)
    titre_rect = titre.get_rect(center=(350, 80))
    ecran.blit(titre, titre_rect)

    # Rejouer ou quitter
    quitte = font_20.render("Espace - quitter", True, NOIR)
    quitte_rect = quitte.get_rect(bottomleft=(10, 190))
    ecran.blit(quitte, quitte_rect)

    start = font_20.render("A - jouer", True, NOIR)
    start_rect = start.get_rect(bottomleft=(10, 170))
    ecran.blit(start,start_rect)

def ecran_de_fin():
    ecran.fill(BLANC)
    # Texte principal
    titre = font_40.render("Merci d'avoir joué !", True, NOIR)
    titre_rect = titre.get_rect(center=(350, 60))
    ecran.blit(titre, titre_rect)

    # Tentatives
    total_essais = niveau[0]["essais"] + niveau[1]["essais"]
    tentatives = font_30.render(f"Tentatives : {total_essais}", True, NOIR)
    tentatives_rect = tentatives.get_rect(center=(350, 115))
    ecran.blit(tentatives, tentatives_rect)

    # Crédit
    credit = font_20.render("Réalisé par Gaspard LESOURD", True, NOIR)
    credit_rect = credit.get_rect(bottomright=(690, 190))
    ecran.blit(credit, credit_rect)

    # Rejouer ou quitter
    quitte = font_20.render("Espace - quitter", True, NOIR)
    quitte_rect = quitte.get_rect(bottomleft=(10, 190))
    ecran.blit(quitte, quitte_rect)

    restart = font_20.render("A - rejouer", True, NOIR)
    restart_rect = restart.get_rect(bottomleft=(10, 170))
    ecran.blit(restart, restart_rect)

while True:
    jeu_en_cours = 1
    actuel = 0 # Niveau actuel

    while accueil:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit() 
                if event.key == pygame.K_a:   
                    actuel = 0
                    joueur.topleft = position_depart
                    accueil = 0
        ecran_accueil()
        
        pygame.display.flip()
        clock.tick(60)

    pygame.display.set_caption("Niveau 1")

    while jeu_en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        deplacements(actuel, niveau)

        murs_mobiles(actuel, niveau)

        actuel, jeu_en_cours = fin_niveau(actuel, niveau, jeu_en_cours)
        
        if jeu_en_cours != 0:
            affichages(actuel, niveau)
        
        pygame.display.flip()
        clock.tick(60)

    fin_de_jeu = 1
    pygame.display.set_caption("Fin de jeu")

    while fin_de_jeu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit() 
                if event.key == pygame.K_a:   
                    actuel = 0
                    joueur.topleft = position_depart
                    fin_de_jeu = 0
                    for element in range(len(niveau)):
                        niveau[element]["essais"] = 1
        
        ecran_de_fin()
        
        pygame.display.flip()
        clock.tick(60)

