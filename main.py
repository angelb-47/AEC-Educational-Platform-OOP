# AIDE ECOLE CANADA - VERSION 2.0

# NOM : Kamgueu Tagne 
# PRENOM : Ange Nael
# Date : 11 novembre 2025
# DESCRIPTION : J'ai crée un jeu AEC 2.0 ou cette fois ci chaque parti  est divisé en classe. 
# Je vous remercie également pour le temps supplementaire. etant donné que je voulais bien faire j'ai pris plus de temps que prevu.
# ARCHITECTURE POO :
# ------------------
# - Configuration : Classe de constantes (couleurs, dimensions, difficultés)
# - Utilisateur : Modèle de données pour l'élève
# - JeuBase : Classe parente abstraite (héritage)
#    JeuMathematiques : Hérite de JeuBase
#    JeuComptage : Hérite de JeuBase
# - FenetreInformations : Collecte et validation des données
# - FenetrePrincipale : Orchestration et point d'entrée

import tkinter as tk
from tkinter import messagebox

from PIL import Image, ImageTk
import random as rand
import idlelib.tooltip as infobulle



# CLASSE 1 : Configuration - Gère les constantes et paramètres du programme

class Configuration:
    """
    Classe qui contient toutes les configurations de l'application.
    Propriétés : couleurs, difficultés, dimensions
    """
    # Couleurs générales
    COULEUR_TEXTE = "#001F3F"
    COULEUR_FOND = "#00FFD0"
    COULEUR_FOND_BLANC = "#fff"
    COULEUR_BOUTON = "#D9D4D4"
    COULEUR_VERT = "#108310"
    
    # Niveaux de difficulté
    niveau_diffculté12 = 10
    niveau_diffculté34 = 15
    niveau_diffculté56 = 20
    
    # Dimensions fenêtres
    TAILLE_PRINCIPALE = "1080x750"
    TAILLE_INFO = "720x510"
    TAILLE_JEU1 = "500x500"
    TAILLE_JEU2 = "500x600"



# CLASSE 2 : Utilisateur - Gère les informations de l'utilisateur

class Utilisateur:
    
    # Classe représentant un utilisateur de la plateforme.
    # Propriétés : nom, prenom, age, niveau
    # Méthodes : __init__, get_difficulte
    
    def __init__(self):
        """Initialise un utilisateur vide"""
        self.nom = ""
        self.prenom = ""
        self.age = 0
        self.niveau = 0
    
    def get_difficulte(self):
        """
        Retourne la difficulté en fonction du niveau de l'utilisateur.
        Returns: tuple (difficulte, nombre_max, nombre_max) selon le niveau
        """
        if self.niveau in [1, 2]:
            return (Configuration.niveau_diffculté12, Configuration.niveau_diffculté12, Configuration.niveau_diffculté12)
        elif self.niveau in [3, 4]:
            return (Configuration.niveau_diffculté34, Configuration.niveau_diffculté34, Configuration.niveau_diffculté34)
        elif self.niveau in [5, 6]:
            return (Configuration.niveau_diffculté56, Configuration.niveau_diffculté56, Configuration.niveau_diffculté56)
        return (Configuration.niveau_diffculté12, Configuration.niveau_diffculté12, Configuration.niveau_diffculté12)



# CLASSE 3 : FenetreInformations - Fenêtre de collecte des infos utilisateur

class FenetreInformations:
    
    def __init__(self, parent, utilisateur, retour_validation):  #parent ici est la fenetre principale,utilisateur est l'objet utilisateur et retour_validation est la fonction a appeler apres la validation
        # fonction d'initialisation de la fenetre d'information
        self.utilisateur = utilisateur
        self.retour = retour_validation
        
        # Création de la fenêtre
        self.fenetre = tk.Toplevel(parent, background=Configuration.COULEUR_FOND_BLANC)
        self.fenetre.geometry(Configuration.TAILLE_INFO)
        self.fenetre.resizable(False, False)
        self.fenetre.title("À propos de vous")
        
        # Création des widgets
        self._creer_widgets()

    #Fonction pour creer tous les widgets
    def _creer_widgets(self):
        
        # Titre
        titre = tk.Label(self.fenetre, text="À propos de vous", 
                        font="Arial 20 bold", 
                        bg=Configuration.COULEUR_FOND_BLANC,
                        fg=Configuration.COULEUR_TEXTE)
        titre.pack(pady=10)
        
        # Champ NOM
        lbl_nom = tk.Label(self.fenetre, text="NOM : ", 
                          font="Arial 20 bold",
                          bg=Configuration.COULEUR_FOND_BLANC,
                          fg=Configuration.COULEUR_TEXTE)
        lbl_nom.place(x=50, y=100)
        
        #champ entry pour recevoir le nom
        self.entry_nom = tk.Entry(self.fenetre, font="Arial 20",
                                 bd=1, highlightthickness=1,
                                 highlightbackground="#000",
                                 fg=Configuration.COULEUR_TEXTE)
        self.entry_nom.place(x=200, y=100)
        
        # Champ PRENOM
        lbl_prenom = tk.Label(self.fenetre, text="PRÉNOM : ", 
                             font="Arial 20 bold",
                             bg=Configuration.COULEUR_FOND_BLANC,
                             fg=Configuration.COULEUR_TEXTE)
        lbl_prenom.place(x=50, y=170)
        
        #champ entry pour recevoir le prenom
        self.entry_prenom = tk.Entry(self.fenetre, font="Arial 20",
                                    bd=1, highlightthickness=1,
                                    highlightbackground="#000",
                                    fg=Configuration.COULEUR_TEXTE)
        self.entry_prenom.place(x=200, y=170)
        
        # Champ AGE
        lbl_age = tk.Label(self.fenetre, text="ÂGE : ", 
                          font="Arial 20 bold",
                          bg=Configuration.COULEUR_FOND_BLANC,
                          fg=Configuration.COULEUR_TEXTE)
        lbl_age.place(x=50, y=240)
        
        #champ entry pour recevoir l'age
        self.entry_age = tk.Entry(self.fenetre, font="Arial 20",
                                 bd=1, highlightthickness=1,
                                 highlightbackground="#000",
                                 fg=Configuration.COULEUR_TEXTE)
        self.entry_age.place(x=200, y=240)
        
        self.var_niveau = tk.StringVar(value="1")       #par defaut le niveau 1 est selectionné
        # Creation des Radiobuttons pour le niveau de l'Eleve
        niveau1 = tk.Radiobutton(self.fenetre, text="Niveau 1", variable=self.var_niveau , value="1", #creer le bouton radiobox
                                bg="#fff",
                                fg=Configuration.COULEUR_TEXTE,
                                font="Arial 15 bold",
                                selectcolor="#fff",         #la couleur du cercle
                                activebackground="#FFF",   #la couleur du background lors du cercle
                                activeforeground = Configuration.COULEUR_TEXTE, # la couleur du texte lors du clique 
                                bd=0,
                                highlightthickness=0,       
                                indicatoron=True,   #permet de rendre le cercle visible
                                )
        niveau1.place(x=200,y=300)  #afficher le bouton et place sert a modifier les positions comme le souhaite 
        niveau2 = tk.Radiobutton(self.fenetre, text="Niveau 2", variable=self.var_niveau, value="2",
                                bg="#fff",
                                fg=Configuration.COULEUR_TEXTE,
                                font="Arial 15 bold",
                                selectcolor="#fff",         #la couleur du cercle
                                activebackground="#FFF",   #la couleur du background lors du cercle
                                activeforeground = Configuration.COULEUR_TEXTE, # la couleur du texte lors du clique 
                                bd=0,
                                highlightthickness=0,       
                                indicatoron=True,   #permet de rendre le cercle visible
                                )
        niveau2.place(x=200,y=350)
        niveau3 = tk.Radiobutton(self.fenetre, text="Niveau 3", variable=self.var_niveau, value="3",
                                bg="#fff",
                                fg=Configuration.COULEUR_TEXTE,
                                font="Arial 15 bold",
                                selectcolor="#fff",         #la couleur du cercle
                                activebackground="#FFF",   #la couleur du background lors du cercle
                                activeforeground = Configuration.COULEUR_TEXTE, # la couleur du texte lors du clique 
                                bd=0,
                                highlightthickness=0,       
                                indicatoron=True,   #permet de rendre le cercle visible
                                )
        niveau3.place(x=200,y=400)
        niveau4 = tk.Radiobutton(self.fenetre, text="Niveau 4", variable=self.var_niveau, value="4",
                                bg="#fff",
                                fg=Configuration.COULEUR_TEXTE,
                                font="Arial 15 bold",
                                selectcolor="#fff",         #la couleur du cercle
                                activebackground="#FFF",   #la couleur du background lors du cercle
                                activeforeground = Configuration.COULEUR_TEXTE, # la couleur du texte lors du clique 
                                bd=0,
                                highlightthickness=0,       
                                indicatoron=True,   #permet de rendre le cercle visible
                                )
        niveau4.place(x=370,y=300)
        niveau5 = tk.Radiobutton(self.fenetre, text="Niveau 5", variable=self.var_niveau, value="5",
                                bg="#fff",
                                fg=Configuration.COULEUR_TEXTE,
                                font="Arial 15 bold",
                                selectcolor="#fff",         #la couleur du cercle
                                activebackground="#FFF",   #la couleur du background lors du cercle
                                activeforeground = Configuration.COULEUR_TEXTE, # la couleur du texte lors du clique 
                                bd=0,
                                highlightthickness=0,       
                                indicatoron=True,   #permet de rendre le cercle visible
                                )
        niveau5.place(x=370,y=350)
        niveau6 = tk.Radiobutton(self.fenetre, text="Niveau 6", variable=self.var_niveau, value="6",
                                bg="#fff",
                                fg=Configuration.COULEUR_TEXTE,
                                font="Arial 15 bold",
                                selectcolor="#fff",         #la couleur du cercle
                                activebackground="#FFF",   #la couleur du background lors du cercle
                                activeforeground = Configuration.COULEUR_TEXTE, # la couleur du texte lors du clique 
                                bd=0,
                                highlightthickness=0,       
                                indicatoron=True,   #permet de rendre le cercle visible
                                )
        niveau6.place(x=370,y=400)
            
        # Bouton soumettre
        btn_soumettre = tk.Button(self.fenetre, text="Soumettre", 
                                 font="Arial 20 bold",
                                 bg=Configuration.COULEUR_TEXTE,
                                 fg=Configuration.COULEUR_FOND_BLANC,
                                 command=self._soumettre)
        btn_soumettre.place(x=250, y=440)
    
    # Fonction qui recupere les informations et quand on clique sur soumettre ca ferme et affiche les informations
    def _soumettre(self):
       
        # Récupération des données
        self.utilisateur.nom = self.entry_nom.get()
        nom = self.entry_nom.get().strip()
        if not nom:
            messagebox.showerror("Erreur", "Veuillez entrer votre nom")
            self.entry_nom.focus()
            return
        if len(nom) < 2:
            messagebox.showerror("Erreur", "Le nom doit contenir au moins 2 caractères")
            self.entry_nom.focus()
            return
        
        # Validation du prénom
        prenom = self.entry_prenom.get().strip()
        if not prenom:
            messagebox.showerror("Erreur", "Veuillez entrer votre prénom")
            self.entry_prenom.focus()
            return
        if len(prenom) < 2:
            messagebox.showerror("Erreur", "Le prénom doit contenir au moins 2 caractères")
            self.entry_prenom.focus()
            return
        self.utilisateur.prenom = self.entry_prenom.get()
        try:
            age = int(self.entry_age.get())
            if age < 3 or age > 12:
                messagebox.showerror("Erreur", "L'âge doit être entre 3 et 12 ans")
                return
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un âge valide")
            return
        self.utilisateur.age = self.entry_age.get()
        self.utilisateur.niveau = int(self.var_niveau.get())
        
        # Affichage des informations
        self._afficher_recapitulatif()
        
        # Fermeture de la fenêtre
        self.fenetre.destroy()
        
        # Appel du retour
        self.retour()
    
    # Afficher les informations recuperées
    def _afficher_recapitulatif(self):
        
        # Utiliser self.fenetre.master au lieu de self.fenetre
        fenetre_recap = tk.Toplevel(self.fenetre.master, background=Configuration.COULEUR_FOND_BLANC)
        fenetre_recap.geometry("400x300")
        fenetre_recap.title("Vos Informations")
        fenetre_recap.resizable(False, False)
        
        tk.Label(fenetre_recap, text="Vos Informations", 
                font="Arial 20 bold", 
                bg=Configuration.COULEUR_FOND_BLANC,
                fg=Configuration.COULEUR_TEXTE).pack(pady=10)
        
        tk.Label(fenetre_recap, text=f"NOM : {self.utilisateur.nom}", 
                font="Arial 15 bold",
                bg=Configuration.COULEUR_FOND_BLANC,
                fg=Configuration.COULEUR_TEXTE).pack(pady=5)
        
        tk.Label(fenetre_recap, text=f"PRÉNOM : {self.utilisateur.prenom}", 
                font="Arial 15 bold",
                bg=Configuration.COULEUR_FOND_BLANC,
                fg=Configuration.COULEUR_TEXTE).pack(pady=5)
        
        tk.Label(fenetre_recap, text=f"ÂGE : {self.utilisateur.age} ans", 
                font="Arial 15 bold",
                bg=Configuration.COULEUR_FOND_BLANC,
                fg=Configuration.COULEUR_TEXTE).pack(pady=5)
        
        tk.Label(fenetre_recap, text=f"NIVEAU : {self.utilisateur.niveau}", 
                font="Arial 15 bold",
                bg=Configuration.COULEUR_FOND_BLANC,
                fg=Configuration.COULEUR_TEXTE).pack(pady=5)

class JeuBase:
    # Classe parente pour tous les jeux
    def __init__(self, parent, difficulte, utilisateur):
        self.utilisateur = utilisateur
        self.difficulte = difficulte
        self.score = 0
    
    def _afficher_score(self):
        # Méthode commune à tous les jeux
        pass


# CLASSE 4 : JeuMathematiques - Premier jeu (additions)

class JeuMathematiques(JeuBase):
    # Jeu qui pose des questions d<addions a l<utilisateur et plus son niveau est grand plus les questions seront difficiles    
    # parent ici reprensente tojours la fenetre principale et difficulte est un tuple qui contient (nb_questions, max_nombre1, max_nombre2)
    def __init__(self, parent, difficulte,utilisateur):
        super().__init__(parent, difficulte, utilisateur)  
        self.difficulte = difficulte   #(nb_questions, max_nombre1, max_nombre2)
        self.nb_questions = difficulte[0] #nombre de questions a poser
        self.max_nombre = difficulte[1] #nombre maximum pour les additions
        self.score = 0    #score initialisé a 0
        self.question_actuelle = 0 #compteur de questions initialisé a 0
        self.num1 = 0 #premier nombre de l'addition
        self.num2 = 0 #deuxieme nombre de l'addition
        
        # Création de la fenêtre
        self.fenetre = tk.Toplevel(parent, background=Configuration.COULEUR_FOND)
        self.fenetre.title("Jeu 1 : Quiz Mathématiques")
        self.fenetre.geometry(Configuration.TAILLE_JEU1)
        self.fenetre.resizable(False, False)
        
        # Création des widgets
        self._creer_widgets()
    
    def _creer_widgets(self):
        # Crée tous les widgets du jeu
        # Titre
        self.lbl_titre = tk.Label(self.fenetre, text="Répondez aux\nQuestions",
                                 font="Rubik 20 bold",
                                 fg=Configuration.COULEUR_TEXTE,
                                 bg=Configuration.COULEUR_FOND)
        self.lbl_titre.pack()
        
        # Score
        self.lbl_score = tk.Label(self.fenetre, text=f"SCORE : 0/{self.nb_questions}",
                                 font="Rubik 10 bold",
                                 fg=Configuration.COULEUR_TEXTE,
                                 bg=Configuration.COULEUR_FOND)
        self.lbl_score.place(x=5, y=5)
        
        # Question
        self.lbl_question = tk.Label(self.fenetre, text="",
                                     font="Arial 45",
                                     fg=Configuration.COULEUR_TEXTE,
                                     bg=Configuration.COULEUR_FOND)
        self.lbl_question.place(x=50, y=170)
        
        # Entry pour la réponse
        self.entry_reponse = tk.Entry(self.fenetre, font="Arial 40 bold",
                                      fg=Configuration.COULEUR_TEXTE,
                                      bd=1, highlightthickness=1, width=3)
        self.entry_reponse.place(x=350, y=170)
        
        # Bouton nouvelle question
        self.btn_question = tk.Button(self.fenetre, text="Question",
                                      font="Arial 25 bold",
                                      fg=Configuration.COULEUR_TEXTE,
                                      bg=Configuration.COULEUR_BOUTON,
                                      command=self._nouvelle_question)
        self.btn_question.pack(pady=10)
        infobulle.Hovertip(self.btn_question, "Cliquer pour afficher une nouvelle question") # infos bulles pour le bouton corriger
        
        # Bouton corriger
        self.btn_corriger = tk.Button(self.fenetre, text="Corriger",
                                      font="Arial 25 bold",
                                      fg=Configuration.COULEUR_TEXTE,
                                      bg=Configuration.COULEUR_BOUTON,
                                      command=self._corriger_reponse,
                                      state=tk.DISABLED)
        self.btn_corriger.place(x=170, y=250)
        infobulle.Hovertip(self.btn_corriger, "Cliquer pour corriger votre réponse") #infos bulles pour le bouton corriger
        # Label pour l'image de feedback
        self.lbl_image = tk.Label(self.fenetre, bg=Configuration.COULEUR_FOND)
    
    # Focntion pour creer une nouvelle question
    def _nouvelle_question(self):
        
        # Incrémenter le compteur de questions
        self.question_actuelle += 1
        
        # Vérifier si toutes les questions ont été posées
        if self.question_actuelle > self.nb_questions:
            self._afficher_fin()
            return
        
        # Générer deux nombres aléatoires
        self.num1 = rand.randint(0, self.max_nombre)
        self.num2 = rand.randint(0, self.max_nombre)
        
        # Afficher la question
        self.lbl_question.config(text=f"{self.num1} + {self.num2} = ")
        
        # Réinitialiser l'entry
        self.entry_reponse.delete(0, tk.END)
        self.entry_reponse.focus()
        
        # Masquer l'image précédente
        self.lbl_image.place_forget()
        
        # Gérer l'état des boutons
        self.btn_question.config(state=tk.DISABLED)
        self.btn_corriger.config(state=tk.NORMAL)
    
    # Fonction pour corriger si la reponse de l'utilisateur est correcte
    def _corriger_reponse(self):
        
        try:
            reponse = int(self.entry_reponse.get())
            reponse_correcte = self.num1 + self.num2
            
            if reponse == reponse_correcte:
                self.score += 1
                self._afficher_feedback(True)
            else:
                self._afficher_feedback(False)
            
            # Mettre à jour le score
            self.lbl_score.config(text=f"SCORE : {self.score}/{self.nb_questions}")
            
            # Gérer l'état des boutons
            self.btn_question.config(state=tk.NORMAL)
            self.btn_corriger.config(state=tk.DISABLED)
            
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide !")
            self.entry_reponse.delete(0, tk.END)
            self.entry_reponse.focus()
    
    # Focntion pour afficher les images Vrai ou Faux
    def _afficher_feedback(self, correct):
        
        try:
            fichier = "True.png" if correct else "false.png"
            img = Image.open(fichier)
            img = img.resize((160, 160))
            photo = ImageTk.PhotoImage(img)
            
            self.lbl_image.config(image=photo)
            self.lbl_image.image = photo
            self.lbl_image.place(x=175, y=335)
        except:
            pass  # Si les images ne sont pas disponibles
    
    #Affiche l'écran de fin de jeu
    def _afficher_fin(self):
        
        # Masquer les widgets du jeu
        self.lbl_question.place_forget()
        self.entry_reponse.place_forget()
        self.btn_question.pack_forget()
        self.btn_corriger.place_forget()
        self.lbl_titre.pack_forget()
        self.lbl_image.place_forget()
        
        # Afficher le résultat
        tk.Label(self.fenetre, text=f"JEU TERMINÉ !\n {self.utilisateur.prenom}",
                font="Rubik 30 bold",
                fg="#fff",
                bg=Configuration.COULEUR_FOND).pack(pady=50)
        
        tk.Label(self.fenetre, text=f"Score Final :\n{self.score}/{self.nb_questions}",
                font="Arial 30 bold",
                fg=Configuration.COULEUR_TEXTE,
                bg=Configuration.COULEUR_FOND).pack(pady=30)
        
        btn_suivant = tk.Button(self.fenetre, text="Suivant",
                               font="Arial 20 bold",
                               bg=Configuration.COULEUR_BOUTON,
                               fg=Configuration.COULEUR_TEXTE,
                               command=self._ouvrir_jeu2)
        btn_suivant.pack(pady=20)
    
    #Fonction pour ouvrir le deuxieme jeu
    def _ouvrir_jeu2(self):
        JeuComptage(self.fenetre.master, self.difficulte,self.utilisateur) #ouvre le 2eme jeux
        self.fenetre.destroy() #ferme le premier jeu



# CLASSE 5 : JeuComptage - Deuxième jeu (compter les pommes)

class JeuComptage(JeuBase):
    
    def __init__(self, parent, difficulte,utilisateur):     #parent ici reprensente tojours la fenetre principale et difficulte est un tuple qui contient (nb_questions, max_nombre1, max_nombre2)
        super().__init__(parent, difficulte, utilisateur)
        self.nb_questions = difficulte[0] #nombre de questions a poser
        self.score = 0 #score initialisé a 0
        self.questions_restantes = self.nb_questions ##compteur de questions initialisé au nombre total de questions
        self.nombre_correct = 0 #nombre correct de pommes a afficher    
        
        # Création de la fenêtre
        self.fenetre = tk.Toplevel(parent, background=Configuration.COULEUR_FOND)
        self.fenetre.title("Jeu 2 : Bon Nombre")
        self.fenetre.geometry(Configuration.TAILLE_JEU2)
        self.fenetre.resizable(False, False)
        
        # Charger l'image de la pomme
        self._charger_image_pomme()
        
        # Création des widgets
        self._creer_widgets()
    
    # Charge l'image de la pomme
    def _charger_image_pomme(self):
        
        try:
            img = Image.open("pomme.png")
            img = img.resize((100, 100))
            self.img_pomme = ImageTk.PhotoImage(img)
        except:
            self.img_pomme = None
    
    # Crée tous les widgets du jeu
    def _creer_widgets(self):
        
        # Titre
        tk.Label(self.fenetre, text="Combien de pommes\nvois-tu à l'écran ?",
                font="Rubik 25 bold",
                fg=Configuration.COULEUR_TEXTE,
                bg=Configuration.COULEUR_FOND).pack()
        
        # Questions restantes
        self.lbl_questions = tk.Label(self.fenetre,
                                      text=f"Questions restantes: {self.questions_restantes}",
                                      font="Arial 16",
                                      fg=Configuration.COULEUR_TEXTE,
                                      bg=Configuration.COULEUR_FOND)
        self.lbl_questions.pack(pady=5)
        
        # Bouton nouvelle question
        self.btn_question = tk.Button(self.fenetre, text="Nouvelle Question",
                                      font="Arial 25 bold",
                                      fg=Configuration.COULEUR_TEXTE,
                                      bg=Configuration.COULEUR_BOUTON,
                                      command=self._nouvelle_question)
        self.btn_question.pack(pady=10)
        infobulle.Hovertip(self.btn_question, "Cliquer pour afficher un nouveau nombre de pommes") # infos bulles pour le bouton nouvelle question
        
        # Zone d'affichage des pommes
        self.zone_pommes = tk.Frame(self.fenetre, width=400, height=250,
                                    bg=Configuration.COULEUR_FOND)
        self.zone_pommes.pack(pady=20)
        
        # Boutons de choix
        self.btn_choix1 = tk.Button(self.fenetre, text="?",
                                    font="Arial 35 bold",
                                    width=3, height=1,
                                    bg=Configuration.COULEUR_FOND_BLANC,
                                    fg=Configuration.COULEUR_TEXTE,
                                    state=tk.DISABLED,
                                    command=lambda: self._verifier_reponse(0))
        self.btn_choix1.place(x=50, y=470)
        infobulle.Hovertip(self.btn_choix1, "Cliquer sur le bouton correspondant") #infos bulles pour le bouton choix1
        
        self.btn_choix2 = tk.Button(self.fenetre, text="?",
                                    font="Arial 35 bold",
                                    width=3, height=1,
                                    bg=Configuration.COULEUR_FOND_BLANC,
                                    fg=Configuration.COULEUR_TEXTE,
                                    state=tk.DISABLED,
                                    command=lambda: self._verifier_reponse(1))
        self.btn_choix2.place(x=190, y=470)
        infobulle.Hovertip(self.btn_choix2, "Cliquer sur le bouton correspondant") #infos bulles pour le bouton choix2
        
        self.btn_choix3 = tk.Button(self.fenetre, text="?",
                                    font="Arial 35 bold",
                                    width=3, height=1,
                                    bg=Configuration.COULEUR_FOND_BLANC,
                                    fg=Configuration.COULEUR_TEXTE,
                                    state=tk.DISABLED,
                                    command=lambda: self._verifier_reponse(2))
        self.btn_choix3.place(x=340, y=470)
        infobulle.Hovertip(self.btn_choix3, "Cliquer sur le bouton correspondant") #infos bulles pour le bouton choix3
        
        self.boutons_choix = [self.btn_choix1, self.btn_choix2, self.btn_choix3]
        self.valeurs_choix = []
    
    # Génère une nouvelle question donc un nombre de pomme aleatoirement entre 1 et 6
    def _nouvelle_question(self):
        
        # Générer le nombre correct de pommes
        self.nombre_correct = rand.randint(1, 6)
        # J'ai choisi une liste car je peux facilement ajouter avec appen et rechercher avec in et l'ordre est tres impotant pour le shuffle
        # Créer 3 options (une correcte et deux incorrectes)
        self.valeurs_choix = [self.nombre_correct]
        # Tantque qu'on a pas 3 valeurs uniques, on en génère des fausses
        while len(self.valeurs_choix) < 3:
            faux = rand.randint(1, 6)
            if faux not in self.valeurs_choix: #grace a cette condtion on est sure que les valeurs sont uniques et qu'il n'y a  qu'une seule bonne reponse
                self.valeurs_choix.append(faux)
        
        # Mélanger les options
        rand.shuffle(self.valeurs_choix)
        
        # Mettre à jour les boutons
        for i, btn in enumerate(self.boutons_choix):
            btn.config(text=str(self.valeurs_choix[i]), state=tk.NORMAL)
        
        # Afficher les pommes
        self._afficher_pommes()
        
        # Désactiver le bouton nouvelle question
        self.btn_question.config(state=tk.DISABLED)
    
    #Affiche les pommes dans la zone
    def _afficher_pommes(self):
        
        # Effacer les anciennes pommes
        for widget in self.zone_pommes.winfo_children():
            widget.destroy()
        
        # Afficher les nouvelles pommes (si l'image existe)
        if self.img_pomme:
            for i in range(self.nombre_correct):
                row = 0 if i < 3 else 1
                col = i if i < 3 else i - 3
                
                lbl = tk.Label(self.zone_pommes, image=self.img_pomme,
                            bg=Configuration.COULEUR_FOND)
                lbl.image = self.img_pomme
                lbl.grid(row=row, column=col, padx=5, pady=5)
    
    # Fonction pour verifier si la reponse de l'utilisateur est correcte
    def _verifier_reponse(self, index_choix):
        
        reponse = self.valeurs_choix[index_choix] #Recoit la vrai reponse
        
        # si la vraie reponse est egale a la reponse entré alors un popup de reussite s'affiche sinon un popup d'erreur s'affiche
        if reponse == self.nombre_correct:
            self.score += 1
            messagebox.showinfo("Bravo!", f"Bonne réponse!\nScore: {self.score}/{self.nb_questions}")
        # Mais sinon un popup d'erreur s'affiche
        else:
            messagebox.showerror("Mauvais Choix",f"Mauvaise réponse. C'était {self.nombre_correct}\n" +
                            f"Score: {self.score}/{self.nb_questions}")
        
        # Décrémenter les questions restantes
        self.questions_restantes -= 1
        self.lbl_questions.config(text=f"Questions restantes: {self.questions_restantes}")
        
        # Désactiver les boutons de choix
        for btn in self.boutons_choix:
            btn.config(state=tk.DISABLED)
        
        # Vérifier si c'est la dernière question
        if self.questions_restantes == 0:
            self.btn_question.config(state=tk.DISABLED)
            self.fenetre.after(1000, self._afficher_fin)
        else:
            self.btn_question.config(state=tk.NORMAL)
    
    def _afficher_fin(self):
        """Affiche l'écran de fin de jeu"""
        self.fenetre.destroy()
        
        # Nouvelle fenêtre pour les résultats
        fenetre_resultat = tk.Toplevel(self.fenetre.master,
                                       background=Configuration.COULEUR_FOND)
        fenetre_resultat.title("Résultats")
        fenetre_resultat.geometry("500x500")
        fenetre_resultat.resizable(False, False)
        
        tk.Label(fenetre_resultat, text="Jeu Terminé!",
                font="Rubik 30 bold",
                fg=Configuration.COULEUR_TEXTE,
                bg=Configuration.COULEUR_FOND).pack(pady=30)
        
        tk.Label(fenetre_resultat, text=f"Ton score final:\n{self.score} / {self.nb_questions}",
                font="Arial 25 bold",
                fg=Configuration.COULEUR_TEXTE,
                bg=Configuration.COULEUR_FOND).pack(pady=20)
        
        # Message selon le score
        if self.score == self.nb_questions:
            message = f"Parfait! \nTu es litteralemt un génie {self.utilisateur.prenom}!"
        elif self.score >= self.nb_questions - 3:
            message = f"Bien joué!\n Tu as eu un score incroyable! {self.utilisateur.prenom}"
        elif self.score >= self.nb_questions // 2:
            message = f"Bon travail!\n Tu t'améliores! {self.utilisateur.prenom}"
        else:
            message = f"Continue,\n tu vas progresser! {self.utilisateur.prenom}"
        
        tk.Label(fenetre_resultat, text=message,
                font="Arial 20",
                fg=Configuration.COULEUR_TEXTE,
                bg=Configuration.COULEUR_FOND).pack(pady=10)
        
        tk.Button(fenetre_resultat, text="Fermer",
                 font="Arial 18 bold",
                 bg=Configuration.COULEUR_BOUTON,
                 fg=Configuration.COULEUR_TEXTE,
                 command=fenetre_resultat.destroy).pack(pady=20)



# CLASSE 6 : FenetrePrincipale - Fenêtre principale de l'application

class FenetrePrincipale:
    # Classe représentant la fenêtre principale de l'application.
    def __init__(self):
        # Initialisation de l'utilisateur
        self.utilisateur = Utilisateur()
        
        # Création de la fenêtre
        self.fenetre = tk.Tk()
        self.fenetre.title("Aide École Canada")
        self.fenetre.geometry(Configuration.TAILLE_PRINCIPALE)
        self.fenetre.resizable(False, False)
        self.fenetre.config(background=Configuration.COULEUR_FOND_BLANC)
        
        # Charger l'image de fond
        self._charger_fond()
        
        # Créer les widgets
        self._creer_widgets()
    
    # Fonction pour charger l'image de fonc
    def _charger_fond(self):
        
        try:
            img = Image.open("dessin_salle_classe.jpg")
            img = img.resize((1080, 750))
            self.img_fond = ImageTk.PhotoImage(img)
            
            lbl_fond = tk.Label(self.fenetre, image=self.img_fond)
            lbl_fond.image = self.img_fond
            lbl_fond.place(x=0, y=0)
        except:
            # Si l'image n'existe pas, utiliser un fond de couleur
            self.fenetre.config(background=Configuration.COULEUR_FOND)
    
    def _creer_widgets(self):
        """Crée tous les widgets de la fenêtre principale"""
        # Message de bienvenue
        lbl_bienvenue = tk.Label(self.fenetre, text="Bienvenue sur\nAEC",
                                font="Rubik 59 bold",
                                fg=Configuration.COULEUR_FOND_BLANC,
                                bg=Configuration.COULEUR_VERT,
                                width=14, height=3)
        lbl_bienvenue.place(x=188, y=54)
        
        # Bouton Infos
        self.btn_infos = tk.Button(self.fenetre, text=" Infos ",
                                   font="Arial 20 bold",
                                   bg=Configuration.COULEUR_FOND_BLANC,
                                   fg=Configuration.COULEUR_TEXTE,
                                   command=self._ouvrir_fenetre_infos)
        infobulle.Hovertip(self.btn_infos, 
                          "Cliquer sur le bouton Infos pour\ndonnez vos informations")
        self.btn_infos.place(x=480, y=430)
        
        # Bouton Commencer (désactivé au départ)
        self.btn_commencer = tk.Button(self.fenetre, text="Commencer",
                                       font="Rubik 20 bold",
                                       bg=Configuration.COULEUR_FOND_BLANC,
                                       fg=Configuration.COULEUR_TEXTE,
                                       state=tk.DISABLED,
                                       command=self._commencer_jeu)
        infobulle.Hovertip(self.btn_commencer,
                          "Cliquer sur le bouton Commencer\npour commencer les jeux")
        self.btn_commencer.place(x=437, y=530)
    
    def _ouvrir_fenetre_infos(self):
        """
        Ouvre la fenêtre de collecte d'informations.
        Événement : appelé lors du clic sur le bouton Infos
        """
        FenetreInformations(self.fenetre, self.utilisateur, self._activer_bouton_commencer)
    
    def _activer_bouton_commencer(self):
        """
        Active le bouton Commencer après validation des infos.
        retour : appelé par FenetreInformations après validation
        """
        self.btn_commencer.config(state=tk.NORMAL)
    
    def _commencer_jeu(self):
        """
        Lance le premier jeu avec la difficulté appropriée.
        Événement : appelé lors du clic sur le bouton Commencer
        """
        difficulte = self.utilisateur.get_difficulte()
        JeuMathematiques(self.fenetre, difficulte,self.utilisateur)
    
    def demarrer(self):
        """Lance la boucle principale de l'application"""
        self.fenetre.mainloop()
# Lancement de l'application
app = FenetrePrincipale()
app.demarrer()
