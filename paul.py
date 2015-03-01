
# TABLEAU D'EVALUATION DE VOLLEY-BALL
# OUTIL D'OBSERVATION
# MIPI 23

# RAY Paul Mipi 23.2

#Python 3.4.3
#'pip install pygal' dans invite de commandes -> C:\Python34\Scripts

from tkinter import *
import json
import time
import pygal

fenetre = Tk()
fenetre.title("Tableau d'évaluation De Volley")

#var boutons et entry

Total_Points_Attaque = 0
Total_Points_Defense = 0
Total_Points_Passe = 0
Total_Points_Contre = 0
Total_Points_Service = 0

Liste_Points_Attaque = []
Liste_Points_Defense = []
Liste_Points_Passe = []
Liste_Points_Contre = []
Liste_Points_Service = []

Bibli_Points_Attaque = dict()
Bibli_Points_Defense = dict()
Bibli_Points_Passe = dict()
Bibli_Points_Contre = dict()
Bibli_Points_Service = dict()

e1     = Entry(fenetre)
Nom    = e1.get()
e2     = Entry(fenetre)
Prenom = e2.get()
e3     = Entry(fenetre)
Groupe = e3.get()

    
# Def permettant d'utiliser les coefficients avec les radiobutton

C = 1
v = IntVar()

def c():
    global C
    if v.get() == 1:
        C = 1.0
    if v.get() == 2:
        C = 1.5
    if v.get() == 3:
        C = 2.0


#Callbacks permettant de donner une commande aux boutons et de mettre a jour les données sur le tableau

#Attaque callback
def callback_Attaque(x,y):
    global Total_Points_Attaque
    Total_Points_Attaque = Total_Points_Attaque + ( x * C)
    Label(fenetre, text = Total_Points_Attaque).grid(row = 2, column = 10)
    Liste_Points_Attaque.append( x * C)
    Label(fenetre, text = Liste_Points_Attaque).grid(row = 2, column = 12)
    e = y
    if e not in Bibli_Points_Attaque :
        Bibli_Points_Attaque[e] = 1
    else :
        Bibli_Points_Attaque[e] = Bibli_Points_Attaque[e] + 1
    Label(fenetre, text = Bibli_Points_Attaque).grid(row = 14, column = 10)

#Defense callback
    
def callback_Defense(x,y):
    global Total_Points_Defense
    Total_Points_Defense = Total_Points_Defense +( x * C)
    Label(fenetre, text = Total_Points_Defense).grid(row = 4, column = 10)
    Liste_Points_Defense.append( x * C)
    Label(fenetre, text = Liste_Points_Defense).grid(row = 4, column = 12)
    e = y
    if e not in Bibli_Points_Defense :
        Bibli_Points_Defense[e] = 1
    else :
        Bibli_Points_Defense[e] = Bibli_Points_Defense[e] + 1
    Label(fenetre, text = Bibli_Points_Defense).grid(row = 16, column = 10)
	
#Passe callback
    
def callback_Passe(x,y):
    global Total_Points_Passe
    Total_Points_Passe = Total_Points_Passe +(x * C) 
    Label(fenetre, text = Total_Points_Passe).grid(row = 6, column = 10)
    Liste_Points_Passe.append( x * C)
    Label(fenetre, text = Liste_Points_Passe).grid(row = 6, column = 12)
    e = y
    if e not in Bibli_Points_Passe :
        Bibli_Points_Passe[e] = 1
    else :
        Bibli_Points_Passe[e] = Bibli_Points_Passe[e] + 1
    Label(fenetre, text = Bibli_Points_Passe).grid(row = 18, column = 10)
    
#Contre callback
    
def callback_Contre(x,y):
    global Total_Points_Contre
    Total_Points_Contre = Total_Points_Contre + (x)
    Label(fenetre, text = Total_Points_Contre).grid(row = 8, column = 10)
    Liste_Points_Contre.append( x )
    Label(fenetre, text = Liste_Points_Contre).grid(row = 8, column = 12)
    e = y
    if e not in Bibli_Points_Contre :
        Bibli_Points_Contre[e] = 1
    else :
        Bibli_Points_Contre[e] = Bibli_Points_Contre[e] + 1
    Label(fenetre, text = Bibli_Points_Contre).grid(row = 20, column = 10)
	
#Service callback
    
def callback_Service(x,y):
    global Total_Points_Service
    Total_Points_Service = Total_Points_Service +( x )
    Label(fenetre, text = Total_Points_Service).grid(row = 10, column = 10)
    Liste_Points_Service.append(x)
    Label(fenetre, text = Liste_Points_Service).grid(row = 10, column = 12)
    e = y
    if e not in Bibli_Points_Service :
        Bibli_Points_Service[e] = 1
    else :
        Bibli_Points_Service[e] = Bibli_Points_Service[e] + 1
    Label(fenetre, text = Bibli_Points_Service).grid(row = 22, column = 10)


#def permettant d'enregistrer et d'afficher le graphe radar a l'aide d'un navigateur web -> Emplacement Repertoire Courant ou Rechercher
#ATTENTION dans le cas ou le meme joueur est evalué le graphe précédent du joueur sera effacé -> il faut donc le renommer avant

def radar():
    radar_chart = pygal.Radar()
    radar_chart.title = 'Graphe Volley'
    radar_chart.x_labels = ['Attaque', 'Defense', 'Passe', 'Contre', 'Service']
    radar_chart.add(e1.get(), [Total_Points_Attaque, Total_Points_Defense, Total_Points_Passe, Total_Points_Contre, Total_Points_Service])
    radar_chart.render_to_file(e1.get() + '.str')
               
#Def permettant d'enregistrer les données dans un fichier json lisible en txt

def save():
    data = \
    {
        "Qualites": [
            {
                "Attaque": {"Total": Total_Points_Attaque, "Liste": Liste_Points_Attaque, "Actions": Bibli_Points_Attaque}
            },
            {
                "Defense": {"Total": Total_Points_Defense, "Liste": Liste_Points_Defense, "Actions": Bibli_Points_Defense}
            },
            {
                "Passe": {"Total": Total_Points_Passe, "Liste": Liste_Points_Passe, "Actions": Bibli_Points_Passe}
            },
            {
                "Contre": {"Total": Total_Points_Contre, "Liste": Liste_Points_Contre, "Actions": Bibli_Points_Contre}
            },
            {
                "Service": {"Total": Total_Points_Service, "Liste": Liste_Points_Service, "Actions": Bibli_Points_Service}
            }
        ],
        "CheminGraphRadar": e1.get() + '.str',
        "Nom" : e1.get(),
        "Prenom" : e2.get(),
        "Groupe" : e3.get(),
        "Date" : time.strftime("/%d/%m/%Y")
    }
    jsonData = json.dumps(data, ensure_ascii=False)
    file = filedialog.asksaveasfile(mode='w', title = "Sauvegarde", defaultextension = ".json", filetypes = (("json files","*.json"),("all files","*.*")))
    if file is None:
        return
    file.write(jsonData)
    print(data)
    
def load():
    file = filedialog.askopenfile(mode='r', title = "Chargement", defaultextension = ".json", filetypes = (("json files","*.json"),("all files","*.*")))
    if file is None:
        return
    jsonData = file.read()
    data = json.loads(jsonData)
    global Total_Points_Attaque, Total_Points_Defense, Total_Points_Passe, Total_Points_Contre,Total_Points_Service
    global Liste_Points_Attaque, Liste_Points_Defense, Liste_Points_Passe, Liste_Points_Contre, Liste_Points_Service
    global Bibli_Points_Attaque, Bibli_Points_Defense, Bibli_Points_Passe, Bibli_Points_Contre, Bibli_Points_Service
    global Nom, Prenom, Groupe
    Total_Points_Attaque = data["Qualites"][0]["Attaque"]["Total"]
    Total_Points_Defense = data["Qualites"][1]["Defense"]["Total"]
    Total_Points_Passe = data["Qualites"][2]["Passe"]["Total"]
    Total_Points_Contre = data["Qualites"][3]["Contre"]["Total"]
    Total_Points_Service = data["Qualites"][4]["Service"]["Total"]
    Liste_Points_Attaque = data["Qualites"][0]["Attaque"]["Liste"]
    Liste_Points_Defense = data["Qualites"][1]["Defense"]["Liste"]
    Liste_Points_Passe = data["Qualites"][2]["Passe"]["Liste"]
    Liste_Points_Contre = data["Qualites"][3]["Contre"]["Liste"]
    Liste_Points_Service = data["Qualites"][4]["Service"]["Liste"]  
    Bibli_Points_Attaque = data["Qualites"][0]["Attaque"]["Actions"]
    Bibli_Points_Defense = data["Qualites"][1]["Defense"]["Actions"]
    Bibli_Points_Passe = data["Qualites"][2]["Passe"]["Actions"]
    Bibli_Points_Contre = data["Qualites"][3]["Contre"]["Actions"]
    Bibli_Points_Service = data["Qualites"][4]["Service"]["Actions"]
    Nom = data["Nom"]
    Prenom = data["Prenom"]
    Groupe = data["Groupe"]
    e1.insert(0, data["Nom"])
    e2.insert(0, data["Prenom"])
    e3.insert(0, data["Groupe"])
    gui()
    print(data)

# INTERFACE GRAPHIQUE

def gui():

#Qualités
    
    Label(fenetre, text = "Actions/Efficacité", font = ("Arial", 12)).grid(row = 0)
    Label(fenetre, text = "Attaque", font = ("Arial", 12)).grid(row = 2)
    Label(fenetre, text = "Defense", font = ("Arial", 12)).grid(row = 4)
    Label(fenetre, text = "Passe", font = ("Arial", 12)).grid(row = 6)
    Label(fenetre, text = "Contre", font = ("Arial", 12)).grid(row = 8)
    Label(fenetre, text = "Service", font = ("Arial", 12)).grid(row = 10)

#Evaluation

    Label(fenetre, text = "Ratée", font = ("Arial", 12)).grid(column = 2, row = 0)
    Label(fenetre, text = "Mauvaise", font = ("Arial", 12)).grid(column = 4, row = 0)
    Label(fenetre, text = "Bonne", font = ("Arial", 12)).grid(column = 6, row = 0)
    Label(fenetre, text = "Excellente", font = ("Arial", 12)).grid(column = 8, row = 0)
    Label(fenetre, text = "Points Total", font = ("Arial", 12)).grid(column = 10, row = 0)
    Label(fenetre, text = "Points Cumulés", font = ("Arial", 12)).grid(column = 12, row = 0)
    Label(fenetre, text = "Bibliothèque Actions", font = ("Arial", 12)).grid(column = 10, row = 12)

    Label(fenetre, text = "--", font = ("Arial", 20)).grid(column = 2, row = 1)
    Label(fenetre, text = "-", font = ("Arial", 20)) .grid(column = 4, row = 1)
    Label(fenetre, text = "+", font = ("Arial", 20)) .grid(column = 6, row = 1)
    Label(fenetre, text = "++", font = ("Arial", 20)).grid(column = 8, row = 1)

#Espace vide

    Label(fenetre, text = " ").grid(row = 3)
    Label(fenetre, text = " ").grid(row = 5)
    Label(fenetre, text = " ").grid(row = 7)
    Label(fenetre, text = " ").grid(row = 9)
    Label(fenetre, text = " ").grid(row = 11)
    Label(fenetre, text = " ").grid(row = 12)
    Label(fenetre, text = " ").grid(row = 14)

    Label(fenetre, text = " ").grid(column = 1)
    Label(fenetre, text = " ").grid(column = 3)
    Label(fenetre, text = " ").grid(column = 5)
    Label(fenetre, text = " ").grid(column = 7)
    Label(fenetre, text = " ").grid(column = 9)
    Label(fenetre, text = " ").grid(column = 11)
    Label(fenetre, text = " ").grid(column = 13)

#Attaque

    Button(fenetre, text = "-2", command = lambda : callback_Attaque(-2.0,"--")).grid(row = 2, column = 2)
    Button(fenetre, text = "-1", command = lambda : callback_Attaque(-1.0,"-")).grid(row = 2, column = 4)
    Button(fenetre, text = "+3", command = lambda : callback_Attaque(+3.0,"+")).grid(row = 2, column = 6)
    Button(fenetre, text = "+4", command = lambda : callback_Attaque(+4.0,"++")).grid(row = 2, column = 8)

    Label(fenetre, text = Total_Points_Attaque).grid(row = 2, column = 10)
    Label(fenetre, text = Liste_Points_Attaque).grid(row = 2, column = 12)
    Label(fenetre, text = Bibli_Points_Attaque).grid(row = 14, column = 10)

#Defense

    Button(fenetre, text = "-3", command = lambda : callback_Defense(-3.0,"--")).grid(row = 4, column = 2)
    Button(fenetre, text = "-1", command = lambda : callback_Defense(-1.0,"-")).grid(row = 4, column = 4)
    Button(fenetre, text = "+1", command = lambda : callback_Defense(+1.0,"+")).grid(row = 4, column = 6)
    Button(fenetre, text = "+3", command = lambda : callback_Defense(+3.0,"++")).grid(row = 4, column = 8)

    Label(fenetre, text = Total_Points_Defense).grid(row = 4, column = 10)
    Label(fenetre, text = Liste_Points_Defense).grid(row = 4, column = 12)
    Label(fenetre, text = Bibli_Points_Defense).grid(row = 16, column = 10)

#Passe

    Button(fenetre, text = "-4", command = lambda : callback_Passe(-4.0,"--")).grid(row = 6, column = 2)
    Button(fenetre, text = "-2", command = lambda : callback_Passe(-2.0,"-")).grid(row = 6, column = 4)
    Button(fenetre, text = "+2", command = lambda : callback_Passe(+2.0,"+")).grid(row = 6, column = 6)
    Button(fenetre, text = "+4", command = lambda : callback_Passe(+4.0,"++")).grid(row = 6, column = 8)

    Label(fenetre, text = Total_Points_Passe).grid(row = 6, column = 10)
    Label(fenetre, text = Liste_Points_Passe).grid(row = 6, column = 12)
    Label(fenetre, text = Bibli_Points_Passe).grid(row = 18, column = 10)

#Contre

    Button(fenetre, text = "-2", command = lambda : callback_Contre(-2.0,"--")).grid(row = 8, column = 2)
    Button(fenetre, text = "-1", command = lambda : callback_Contre(-1.0,"-")).grid(row = 8, column = 4)
    Button(fenetre, text = "+1", command = lambda : callback_Contre(+1.0,"+")).grid(row = 8, column = 6)
    Button(fenetre, text = "+4", command = lambda : callback_Contre(+4.0,"++")).grid(row = 8, column = 8)

    Label(fenetre, text = Total_Points_Contre).grid(row = 8, column = 10)
    Label(fenetre, text = Liste_Points_Contre).grid(row = 8, column = 12)
    Label(fenetre, text = Bibli_Points_Contre).grid(row = 20, column = 10)

#Service

    Button(fenetre, text = "-4", command = lambda : callback_Service(-4.0,"--")).grid(row = 10, column = 2)
    Button(fenetre, text = "-1", command = lambda : callback_Service(-1.0,"-")).grid(row = 10, column = 4)
    Button(fenetre, text = "+1", command = lambda : callback_Service(+1.0,"+")).grid(row = 10, column = 6)
    Button(fenetre, text = "+4", command = lambda : callback_Service(+4.0,"++")).grid(row = 10, column = 8)

    Label(fenetre, text = Total_Points_Service).grid(row = 10, column = 10)
    Label(fenetre, text = Liste_Points_Service).grid(row = 10, column = 12)
    Label(fenetre, text = Bibli_Points_Service).grid(row = 22, column = 10)

#Coef Passe Precedente

 #Label

    Label(fenetre, text = " Si Balle réussie -> ").grid(row = 13, column = 2)
    Label(fenetre, text = " Si Balle réussie -> ").grid(row = 14, column = 2)
    Label(fenetre, text = " Si Balle ratée -> ").grid(row = 20, column = 2)
    Label(fenetre, text = " Si Balle ratée -> ").grid(row = 19, column = 2)
    Label(fenetre, text = "  Coefficient de la balle precedente").grid(row = 16, column = 0)

#Coef

    Label(fenetre, text = "x2", font = ("Arial", 15)).grid(row = 16, column = 7)
    Label(fenetre, text = "x1.5", font = ("Arial", 15)).grid(row = 16, column = 5)
    Label(fenetre, text = "x1", font = ("Arial", 15)).grid(row = 16, column = 3)

#Si balle réussie

    Label(fenetre, text = "Sur Passe : Parfaite").grid(row = 13, column = 3)
    Label(fenetre, text = "Sur Attaque : Facile ou Raté").grid(row = 14, column = 3)
    Label(fenetre, text = "Sur Passe : Moyenne").grid(row = 13, column = 5)
    Label(fenetre, text = "Sur Attaque : Moyenne").grid(row = 14, column = 5)
    Label(fenetre, text = "Sur Passe : Dur ou Raté").grid(row = 13, column = 7)
    Label(fenetre, text = "Sur Attaque : Parfaite").grid(row = 14, column = 7)

#Si balle ratée

    Label(fenetre, text = "Sur Passe : Raté").grid(row = 19, column = 3)
    Label(fenetre, text = "Sur Attaque : Parfaite").grid(row = 20, column = 3)
    Label(fenetre, text = "Sur Passe : Moyenne").grid(row = 19, column = 5)
    Label(fenetre, text = "Sur Attaque : Moyenne").grid(row = 20, column = 5)
    Label(fenetre, text = "Sur Passe : Parfaite").grid(row = 19, column = 7)
    Label(fenetre, text = "Sur Attaque : Facile ou Raté").grid(row = 20, column = 7)

 #Checkbutton

    Radiobutton(fenetre, variable = v,value = 1,command = c).grid(row = 17,column = 3)
    Radiobutton(fenetre, variable = v,value = 2,command = c).grid(row = 17,column = 5)
    Radiobutton(fenetre, variable = v,value = 3,command = c).grid(row = 17,column = 7)

#Nom Prénom Groupe Date Joueur

    Label(fenetre, text = "Nom", font = ("Arial", 12)).grid(row = 22,column = 0)
    Label(fenetre, text = "Prénom", font = ("Arial", 12)).grid(row = 23,column = 0)
    Label(fenetre, text = "Groupe", font = ("Arial", 12)).grid(row = 24,column = 0)
    Label(fenetre, text = " ").grid(row = 21)
    Label(fenetre, text = " ").grid(row = 26)

    e1.grid(row = 22, column = 2)
    e2.grid(row = 23, column = 2)
    e3.grid(row = 24, column = 2)

#Bouton Sortie et enregistrer et charger et graphe
   
    Button(fenetre, text = "Quitter", command = fenetre.destroy).grid(row = 24,column = 6)
    Button(fenetre, text = "Enregistrer", command = lambda:save()).grid(row = 24, column = 4)
    Button(fenetre, text = "Charger", command = lambda:load()).grid(row = 24, column = 5)
    Button(fenetre, text = "Graphe", command = lambda:radar()).grid(row = 24, column = 8)
    
gui()
fenetre.mainloop()
