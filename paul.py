
#var boutons

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


#Attaque callback

def callback_Attaque_1():
    global Total_Points_Attaque
    Total_Points_Attaque = Total_Points_Attaque - ( 2.0 * C)
    label_a = Label(fenetre, text = Total_Points_Attaque)
    label_a.grid(row = 2, column = 10)
    Liste_Points_Attaque.append( -2.0 * C)
    label_a2 = Label(fenetre, text = Liste_Points_Attaque)
    label_a2.grid(row = 2, column = 12)
    e = ' -- '
    if e not in Bibli_Points_Attaque :
        Bibli_Points_Attaque[e] = 1
    else :
        Bibli_Points_Attaque[e] = Bibli_Points_Attaque[e] + 1
    label_a3 = Label(fenetre, text = Bibli_Points_Attaque)
    label_a3.grid(row = 2, column = 14)
# ESCPACE MANQUANT	
def callback_Attaque_2():
    global Total_Points_Attaque
    Total_Points_Attaque = Total_Points_Attaque - ( 1.0 * C)
    label_a = Label(fenetre, text = Total_Points_Attaque)
    label_a.grid(row = 2, column = 10)
    Liste_Points_Attaque.append( -1.0 * C)
    label_a2 = Label(fenetre, text = Liste_Points_Attaque)
    label_a2.grid(row = 2, column = 12)
    e = ' - '
    if e not in Bibli_Points_Attaque :
        Bibli_Points_Attaque[e] = 1
    else :
        Bibli_Points_Attaque[e] = Bibli_Points_Attaque[e] + 1
    label_a3 = Label(fenetre, text = Bibli_Points_Attaque)
    label_a3.grid(row = 2, column = 14)
    
def callback_Attaque_3():
    global Total_Points_Attaque
    Total_Points_Attaque = Total_Points_Attaque +( 3.0 * C)
    label_a = Label(fenetre, text = Total_Points_Attaque)
    label_a.grid(row = 2, column = 10)
    Liste_Points_Attaque.append ( +3.0 * C)
    label_a2 = Label(fenetre, text = Liste_Points_Attaque)
    label_a2.grid(row = 2, column = 12)
    e = ' + '
    if e not in Bibli_Points_Attaque :
        Bibli_Points_Attaque[e] = 1
    else :
        Bibli_Points_Attaque[e] = Bibli_Points_Attaque[e] + 1
    label_a3 = Label(fenetre, text = Bibli_Points_Attaque)
    label_a3.grid(row = 2, column = 14)
# ESCPACE MANQUANT	
def callback_Attaque_4():
    global Total_Points_Attaque
    Total_Points_Attaque = Total_Points_Attaque +(4.0 * C)
    label_a = Label(fenetre, text = Total_Points_Attaque)
    label_a.grid(row = 2, column = 10)
    Liste_Points_Attaque.append( +4.0 * C)
    label_a2 = Label(fenetre, text = Liste_Points_Attaque)
    label_a2.grid(row = 2, column = 12)
    e = ' ++ '
    if e not in Bibli_Points_Attaque :
        Bibli_Points_Attaque[e] = 1
    else :
        Bibli_Points_Attaque[e] = Bibli_Points_Attaque[e] + 1
    label_a3 = Label(fenetre, text = Bibli_Points_Attaque)
    label_a3.grid(row = 2, column = 14)

#Defense callback
    
def callback_Defense_1():
    global Total_Points_Defense
    Total_Points_Defense = Total_Points_Defense - ( 3.0 * C)
    label_d = Label(fenetre, text = Total_Points_Defense)
    label_d.grid(row = 4, column = 10)
    Liste_Points_Defense.append( -3.0 * C)
    label_d2 = Label(fenetre, text = Liste_Points_Defense)
    label_d2.grid(row = 4, column = 12)
    e = ' -- '
    if e not in Bibli_Points_Defense :
        Bibli_Points_Defense[e] = 1
    else :
        Bibli_Points_Defense[e] = Bibli_Points_Defense[e] + 1
    label_d3 = Label(fenetre, text = Bibli_Points_Defense)
    label_d3.grid(row = 4, column = 14)
# ESCPACE MANQUANT	
def callback_Defense_2():
    global Total_Points_Defense
    Total_Points_Defense = Total_Points_Defense -(1.0 * C)
    label_d = Label(fenetre, text = Total_Points_Defense)
    label_d.grid(row = 4, column = 10)
    Liste_Points_Defense.append( -1.0 * C)
    label_d2 = Label(fenetre, text= Liste_Points_Defense)
    label_d2.grid(row = 4, column = 12)
    e = ' - '
    if e not in Bibli_Points_Defense :
        Bibli_Points_Defense[e] = 1
    else :
        Bibli_Points_Defense[e] = Bibli_Points_Defense[e] + 1
    label_d3 = Label(fenetre, text = Bibli_Points_Defense)
    label_d3.grid(row = 4, column = 14)
# ESCPACE MANQUANT	
def callback_Defense_3():
    global Total_Points_Defense
    Total_Points_Defense = Total_Points_Defense + (1.0 * C)
    label_d=Label(fenetre, text = Total_Points_Defense)
    label_d.grid(row = 4, column = 10)
    Liste_Points_Defense.append( +1.0 * C)
    label_d2 = Label(fenetre, text = Liste_Points_Defense)
    label_d2.grid(row = 4, column = 12)
    e = ' + '
    if e not in Bibli_Points_Defense :
        Bibli_Points_Defense[e] = 1
    else :
        Bibli_Points_Defense[e] = Bibli_Points_Defense[e] + 1
    label_d3 = Label(fenetre, text = Bibli_Points_Defense)
    label_d3.grid(row = 4, column = 14)
# ESCPACE MANQUANT	
def callback_Defense_4():
    global Total_Points_Defense
    Total_Points_Defense = Total_Points_Defense + ( 3.0 * C)
    label_d = Label(fenetre, text = Total_Points_Defense)
    label_d.grid(row = 4, column = 10)
    Liste_Points_Defense.append( +3.0 * C)
    label_d2 = Label(fenetre, text = Liste_Points_Defense)
    label_d2.grid(row = 4, column = 12)
    e = ' ++ '
    if e not in Bibli_Points_Defense :
        Bibli_Points_Defense[e] = 1
    else :
        Bibli_Points_Defense[e] = Bibli_Points_Defense[e] + 1
    label_d3 = Label(fenetre, text = Bibli_Points_Defense)
    label_d3.grid(row = 4, column = 14)

#Passe callback
    
def callback_Passe_1():
    global Total_Points_Passe
    Total_Points_Passe = Total_Points_Passe - ( 4.0 * C) 
    label_p = Label(fenetre, text = Total_Points_Passe)
    label_p.grid(row = 6, column = 10)
    Liste_Points_Passe.append( -4.0 * C)
    label_p2 = Label(fenetre, text = Liste_Points_Passe)
    label_p2.grid(row = 6, column = 12)
    e = ' -- '
    if e not in Bibli_Points_Passe :
        Bibli_Points_Passe[e] = 1
    else :
        Bibli_Points_Passe[e] = Bibli_Points_Passe[e] + 1
    label_p3 = Label(fenetre, text = Bibli_Points_Passe)
    label_p3.grid(row = 6, column = 14)
# ESCPACE MANQUANT	
def callback_Passe_2():
    global Total_Points_Passe
    Total_Points_Passe = Total_Points_Passe - ( 2.0 * C)
    label_p = Label(fenetre, text = Total_Points_Passe)
    label_p.grid(row = 6, column = 10)
    Liste_Points_Passe.append( -2.0 * C )
    label_p2 = Label(fenetre, text = Liste_Points_Passe)
    label_p2.grid(row = 6, column = 12)
    e = ' - '
    if e not in Bibli_Points_Passe :
        Bibli_Points_Passe[e] = 1
    else :
        Bibli_Points_Passe[e] = Bibli_Points_Passe[e] + 1
    label_p3 = Label(fenetre, text = Bibli_Points_Passe)
    label_p3.grid(row = 6, column = 14)
# ESCPACE MANQUANT	
def callback_Passe_3():
    global Total_Points_Passe
    Total_Points_Passe = Total_Points_Passe +( 2.0 * C)
    label_p = Label(fenetre, text = Total_Points_Passe)
    label_p.grid(row = 6, column = 10)
    Liste_Points_Passe.append( +2.0 * C)
    label_p2 = Label(fenetre, text = Liste_Points_Passe)
    label_p2.grid(row = 6, column = 12)
    e = ' + '
    if e not in Bibli_Points_Passe :
        Bibli_Points_Passe[e] = 1
    else :
        Bibli_Points_Passe[e] = Bibli_Points_Passe[e] + 1
    label_p3 = Label(fenetre, text = Bibli_Points_Passe)
    label_p3.grid(row = 6, column = 14)
# ESCPACE MANQUANT	
def callback_Passe_4():
    global Total_Points_Passe
    Total_Points_Passe = Total_Points_Passe + ( 4.0 * C)
    label_p = Label(fenetre, text = Total_Points_Passe)
    label_p.grid(row = 6, column = 10)
    Liste_Points_Passe.append( +4.0 * C)
    label_p2 = Label(fenetre, text = Liste_Points_Passe)
    label_p2.grid(row = 6, column = 12)
    e = ' ++ '
    if e not in Bibli_Points_Passe :
        Bibli_Points_Passe[e] = 1
    else :
        Bibli_Points_Passe[e] = Bibli_Points_Passe[e] + 1
    label_p3 = Label(fenetre, text = Bibli_Points_Passe)
    label_p3.grid(row = 6, column = 14)

#Contre callback
    
def callback_Contre_1():
    global Total_Points_Contre
    Total_Points_Contre = Total_Points_Contre - ( 2.0)
    label_c = Label(fenetre, text = Total_Points_Contre)
    label_c.grid(row = 8, column = 10)
    Liste_Points_Contre.append( -2.0)
    label_c2 = Label(fenetre, text = Liste_Points_Contre)
    label_c2.grid(row = 8, column = 12)
    e = ' -- '
    if e not in Bibli_Points_Contre :
        Bibli_Points_Contre[e] = 1
    else :
        Bibli_Points_Contre[e] = Bibli_Points_Contre[e] + 1
    label_c3 = Label(fenetre, text = Bibli_Points_Contre)
    label_c3.grid(row = 8, column = 14)
# ESCPACE MANQUANT	
def callback_Contre_2():
    global Total_Points_Contre
    Total_Points_Contre = Total_Points_Contre - ( 1.0)
    label_c = Label(fenetre, text = Total_Points_Contre)
    label_c.grid(row = 8, column = 10)
    Liste_Points_Contre.append( -1.0)
    label_c2=Label(fenetre, text = Liste_Points_Contre)
    label_c2.grid(row = 8, column = 12)
    e = ' - '
    if e not in Bibli_Points_Contre :
        Bibli_Points_Contre[e] = 1
    else :
        Bibli_Points_Contre[e] = Bibli_Points_Contre[e] + 1
    label_c3 = Label(fenetre, text = Bibli_Points_Contre)
    label_c3.grid(row = 8, column = 14)
# ESCPACE MANQUANT	
def callback_Contre_3():
    global Total_Points_Contre
    Total_Points_Contre = Total_Points_Contre + ( 1.0)
    label_c = Label(fenetre, text = Total_Points_Contre)
    label_c.grid(row = 8, column = 10)
    Liste_Points_Contre.append( +1.0)
    label_c2 = Label(fenetre, text = Liste_Points_Contre)
    label_c2.grid(row=8, column=12)
    e = ' + '
    if e not in Bibli_Points_Contre :
        Bibli_Points_Contre[e] = 1
    else :
        Bibli_Points_Contre[e] = Bibli_Points_Contre[e] + 1
    label_c3 = Label(fenetre, text = Bibli_Points_Contre)
    label_c3.grid(row = 8, column = 14)
# ESCPACE MANQUANT	
def callback_Contre_4():
    global Total_Points_Contre
    Total_Points_Contre = Total_Points_Contre + ( 2.0)
    label_c = Label(fenetre, text = Total_Points_Contre)
    label_c.grid(row = 8, column = 10)
    Liste_Points_Contre.append( +2.0)
    label_c2 = Label(fenetre, text = Liste_Points_Contre)
    label_c2.grid(row = 8, column = 12)
    e = ' ++ '
    if e not in Bibli_Points_Contre :
        Bibli_Points_Contre[e] = 1
    else :
        Bibli_Points_Contre[e] = Bibli_Points_Contre[e] + 1
    label_c3 = Label(fenetre, text = Bibli_Points_Contre)
    label_c3.grid(row = 8, column = 14)

#Service callback
    
def callback_Service_1():
    global Total_Points_Service
    Total_Points_Service = Total_Points_Service - ( 4.0)
    label_s = Label(fenetre, text = Total_Points_Service)
    label_s.grid(row = 10, column = 10)
    Liste_Points_Service.append( -4.0)
    label_s2 = Label(fenetre, text = Liste_Points_Service)
    label_s2.grid(row = 10, column = 12)
    e = ' -- '
    if e not in Bibli_Points_Service :
        Bibli_Points_Service[e] = 1
    else :
        Bibli_Points_Service[e] = Bibli_Points_Service[e] + 1
    label_s3 = Label(fenetre, text = Bibli_Points_Service)
    label_s3.grid(row = 10, column = 14)
# ESCPACE MANQUANT	
def callback_Service_2():
    global Total_Points_Service
    Total_Points_Service = Total_Points_Service -( 1.0)
    label_s = Label(fenetre, text = Total_Points_Service)
    label_s.grid(row = 10, column = 10)
    Liste_Points_Service.append( -1.0)
    label_s2 = Label(fenetre, text = Liste_Points_Service)
    label_s2.grid(row = 10, column = 12)
    e = ' - '
    if e not in Bibli_Points_Service :
        Bibli_Points_Service[e] = 1
    else :
        Bibli_Points_Service[e] = Bibli_Points_Service[e] + 1
    label_s3 = Label(fenetre, text = Bibli_Points_Service)
    label_s3.grid(row = 10, column = 14)
# ESCPACE MANQUANT	
def callback_Service_3():
    global Total_Points_Service
    Total_Points_Service = Total_Points_Service + 1.0
    label_s = Label(fenetre, text = Total_Points_Service)
    label_s.grid(row = 10, column = 10)
    Liste_Points_Service.append( +1.0)
    label_s2 = Label(fenetre, text = Liste_Points_Service)
    label_s2.grid(row = 10, column = 12)
    e = ' + '
    if e not in Bibli_Points_Service :
        Bibli_Points_Service[e] = 1
    else :
        Bibli_Points_Service[e] = Bibli_Points_Service[e] + 1
    label_s3 = Label(fenetre, text = Bibli_Points_Service)
    label_s3.grid(row = 10, column = 14)
# ESCPACE MANQUANT	
def callback_Service_4():
    global Total_Points_Service
    Total_Points_Service = Total_Points_Service +( 4.0)
    label_s = Label(fenetre, text = Total_Points_Service)
    label_s.grid(row = 10, column = 10)
    Liste_Points_Service.append( +4.0)
    label_s2 = Label(fenetre, text = Liste_Points_Service)
    label_s2.grid(row = 10, column = 12)
    e = ' ++ '
    if e not in Bibli_Points_Service :
        Bibli_Points_Service[e] = 1
    else :
        Bibli_Points_Service[e] = Bibli_Points_Service[e] + 1
    label_s3 = Label(fenetre, text = Bibli_Points_Service)
    label_s3.grid(row = 10, column = 14)



# A METTRE AU DEBUT DU FICHIER
from tkinter import *

# A METTRE EN BAS DU FICHIER 
fenetre = Tk()
fenetre.title("Tableau d'évaluation De Volley")


#Qualités

# DEBUT - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE
label_q = Label(fenetre, text = "Actions/Efficacité")
label_1 = Label(fenetre, text = "Attaque")
label_2 = Label(fenetre, text = "Defense")
label_3 = Label(fenetre, text = "Passe")
label_4 = Label(fenetre, text = "Contre")
label_5 = Label(fenetre, text = "Service")
label_q.grid(row = 0)
label_1.grid(row = 2)
label_2.grid(row = 4)
label_3.grid(row = 6)
label_4.grid(row = 8)
label_5.grid(row = 10)
# FIN - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE 

#Evaluation

# DEBUT - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE
label_e1 = Label(fenetre, text = "Ratée")
label_e1.grid(column = 2, row = 0)
label_e2 = Label(fenetre, text = "Mauvaise")
label_e2.grid(column = 4, row = 0)
label_e3 = Label(fenetre, text = "Bonne")
label_e3.grid(column = 6, row = 0)
label_e4 = Label(fenetre, text = "Excellente")
label_e4.grid(column = 8, row = 0)
label_e5 = Label(fenetre, text = "Points Total")
label_e5.grid(column = 10, row = 0)
label_e6 = Label(fenetre, text = "Points Cumulés")
label_e6.grid(column = 12, row = 0)
label_e7 = Label(fenetre, text = "Bibliothèque Actions")
label_e7.grid(column = 14, row = 0)

label_n1 = Label(fenetre, text = "--")
label_n1.grid(column = 2, row = 1)
label_n2 = Label(fenetre, text = "-")
label_n2.grid(column = 4, row = 1)
label_n3 = Label(fenetre, text = "+")
label_n3.grid(column = 6, row = 1)
label_n4 = Label(fenetre, text = "++")
label_n4.grid(column = 8, row = 1)
# FIN - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE 


#Espace vide
# DEBUT - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE
label_vide1 = Label(fenetre, text = " ")
label_vide2 = Label(fenetre, text = " ")
label_vide3 = Label(fenetre, text = " ")
label_vide4 = Label(fenetre, text = " ")
label_vide5 = Label(fenetre, text = " ")
label_vide6 = Label(fenetre, text = " ")
label_vide7 = Label(fenetre, text = " ")
label_vide8 = Label(fenetre, text = " ")
label_vide9 = Label(fenetre, text = " ")
label_vide10 = Label(fenetre, text = " ")
label_vide11 = Label(fenetre, text = " ")
label_vide12 = Label(fenetre, text = " ")
label_vide13 = Label(fenetre, text = " ")

label_vide1.grid(row = 3)
label_vide2.grid(row = 5)
label_vide3.grid(row = 7)
label_vide4.grid(row = 9)
label_vide12.grid(row = 11)
label_vide11.grid(row = 12)
label_vide5.grid(column = 1)
label_vide6.grid(column = 3)
label_vide7.grid(column = 5)
label_vide8.grid(column = 7)
label_vide9.grid(column = 9)
label_vide10.grid(column = 11)
label_vide13.grid(column = 13)
# FIN - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE 




#Attaque

# DEBUT - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE
bouton_a1 = Button(fenetre, text = "-2", command = callback_Attaque_1)
bouton_a1.grid(row = 2, column = 2)
bouton_a2 = Button(fenetre, text = "-1", command = callback_Attaque_2)
bouton_a2.grid(row = 2, column = 4)
bouton_a3 = Button(fenetre, text = "+3", command = callback_Attaque_3)
bouton_a3.grid(row = 2, column = 6)
bouton_a4 = Button(fenetre, text = "+4", command = callback_Attaque_4)
bouton_a4.grid(row = 2, column = 8)
label_a = Label(fenetre, text = Total_Points_Attaque)
label_a.grid(row = 2, column = 10)
label_a2 = Label(fenetre, text = Liste_Points_Attaque)
label_a2.grid(row = 2, column = 12)
label_a3 = Label(fenetre, text = Bibli_Points_Attaque)
label_a3.grid(row = 2, column = 14)
# FIN - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE 

#Defense

# DEBUT - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE
bouton_d1 = Button(fenetre, text = "-3", command = callback_Defense_1)
bouton_d1.grid(row = 4, column = 2)
bouton_d2 = Button(fenetre, text = "-1", command = callback_Defense_2)
bouton_d2.grid(row = 4, column = 4)
bouton_d3 = Button(fenetre, text = "+1", command = callback_Defense_3)
bouton_d3.grid(row = 4, column = 6)
bouton_d4 = Button(fenetre, text = "+3", command = callback_Defense_4)
bouton_d4.grid(row = 4, column = 8)
label_d = Label(fenetre, text = Total_Points_Defense)
label_d.grid(row = 4, column = 10)
label_d2 = Label(fenetre, text = Liste_Points_Defense)
label_d2.grid(row = 4, column = 12)
label_d3 = Label(fenetre, text = Bibli_Points_Defense)
label_d3.grid(row = 4 , column = 14)
# FIN - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE 

#Passe

# DEBUT - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE
bouton_p1 = Button(fenetre, text = "-4", command = callback_Passe_1)
bouton_p1.grid(row = 6, column = 2)
bouton_p2 = Button(fenetre, text = "-2", command = callback_Passe_2)
bouton_p2.grid(row = 6, column = 4)
bouton_p3 = Button(fenetre, text = "+2", command = callback_Passe_3)
bouton_p3.grid(row = 6, column = 6)
bouton_p4 = Button(fenetre, text = "+4", command = callback_Passe_4)
bouton_p4.grid(row = 6, column = 8)
label_p = Label(fenetre, text = Total_Points_Passe)
label_p.grid(row = 6, column = 10)
label_p2 = Label(fenetre, text = Liste_Points_Passe)
label_p2.grid(row = 6, column = 12)
label_p3 = Label(fenetre, text = Bibli_Points_Passe)
label_p3.grid(row = 6 , column = 14)
# FIN - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE 

#Contre

# DEBUT - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE
bouton_c1 = Button(fenetre, text = "-2", command = callback_Contre_1)
bouton_c1.grid(row = 8, column = 2)
bouton_c2 = Button(fenetre, text = "-1", command = callback_Contre_2)
bouton_c2.grid(row = 8, column = 4)
bouton_c3 = Button(fenetre, text = "+1", command = callback_Contre_3)
bouton_c3.grid(row = 8, column = 6)
bouton_c4 = Button(fenetre, text = "+2", command = callback_Contre_4)
bouton_c4.grid(row = 8, column = 8)
label_c = Label(fenetre, text = Total_Points_Contre)
label_c.grid(row = 8, column = 10)
label_c2 = Label(fenetre, text = Liste_Points_Contre)
label_c2.grid(row = 8, column = 12)
label_c3 = Label(fenetre, text = Bibli_Points_Contre)
label_c3.grid(row = 8 , column = 14)
# FIN - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE 

#Service

# DEBUT - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE
bouton_s1 = Button(fenetre, text = "-4", command = callback_Service_1)
bouton_s1.grid(row = 10, column = 2)
bouton_s2 = Button(fenetre, text = "-1", command = callback_Service_2)
bouton_s2.grid(row = 10, column = 4)
bouton_s3 = Button(fenetre, text = "+1", command = callback_Service_3)
bouton_s3.grid(row = 10, column = 6)
bouton_s4 = Button(fenetre, text = "+4", command = callback_Service_4)
bouton_s4.grid(row = 10, column = 8)
label_s = Label(fenetre, text = Total_Points_Service)
label_s.grid(row = 10, column = 10)
label_s2 = Label(fenetre, text = Liste_Points_Service)
label_s2.grid(row = 10, column = 12)
label_s3 = Label(fenetre, text = Bibli_Points_Service)
label_s3.grid(row = 10, column = 14)
# FIN - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE 

#Coef Passe Precedente

 #Label
# DEBUT - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE
label_coef_réussie=Label(fenetre, text = " Si Balle réussie -> ")
label_coef_réussie.grid(row=13,column=2)
label_coef_réussie=Label(fenetre, text = " Si Balle réussie -> ")
label_coef_réussie.grid(row=14,column=2)
label_coef_ratée=Label(fenetre, text = " Si Balle ratée -> ")
label_coef_ratée.grid(row=20,column=2)
label_coef_ratée=Label(fenetre, text = " Si Balle ratée -> ")
label_coef_ratée.grid(row=19,column=2)
label_coef = Label(fenetre, text = "  Coefficient de la balle precedente")
label_coef.grid(row = 16,column = 0)
# FIN - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE 

#Si balle réussie
# DEBUT - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE
label_coef1 = Label(fenetre, text = "Sur Passe : Parfaite")
label_coef1.grid(row = 13, column = 3)
label_coef2 = Label(fenetre, text = "Sur Attaque : Facile ou Raté")
label_coef2.grid(row = 14, column = 3)
label_coef3 = Label(fenetre, text = "x1")
label_coef3.grid(row = 16, column = 3)
label_coef4 = Label(fenetre, text = "Sur Passe : Moyenne")
label_coef4.grid(row = 13, column = 5)
label_coef5 = Label(fenetre, text = "Sur Attaque : Moyenne")
label_coef5.grid(row = 14, column = 5)
label_coef6 = Label(fenetre, text = "x1.5")
label_coef6.grid(row = 16, column = 5)
label_coef7 = Label(fenetre, text = "Sur Passe : Dur ou Raté")
label_coef7.grid(row = 13, column = 7)
label_coef8 = Label(fenetre, text = "Sur Attaque : Parfaite")
label_coef8.grid(row = 14, column = 7)
label_coef9 = Label(fenetre, text = "x2")
label_coef9.grid(row = 16, column = 7)
# FIN - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE 

#Si balle ratée

# DEBUT - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE
label_coefa = Label(fenetre, text = "Sur Passe : Raté")
label_coefa.grid(row = 19, column = 3)
label_coefb = Label(fenetre, text = "Sur Attaque : Parfaite")
label_coefb.grid(row = 20, column = 3)
label_coefc = Label(fenetre, text = "Sur Passe : Moyenne")
label_coefc.grid(row = 19, column = 5)
label_coefd = Label(fenetre, text = "Sur Attaque : Moyenne")
label_coefd.grid(row = 20, column = 5)
label_coefe = Label(fenetre, text = "Sur Passe : Parfaite")
label_coefe.grid(row = 19, column = 7)
label_coeff = Label(fenetre, text = "Sur Attaque : Facile ou Raté")
label_coeff.grid(row = 20, column = 7)
# FIN - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE 

 #Checkbutton


 # A RANGER AVEC LES AUTRES FONCTIONS
C = 1

def c():
    global C
    if v.get() == 1:
        C = 1.0
    if v.get() == 2:
        C = 1.5
    if v.get() == 3:
        C = 2.0
        
v = IntVar()

# AUCUN INTERET ICI
global value

# DEBUT - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE
C1 = Radiobutton(fenetre, variable = v,value = 1,command = c)
C2 = Radiobutton(fenetre, variable = v,value = 2,command = c)
C3 = Radiobutton(fenetre, variable = v,value = 3,command = c)
C1.grid(row = 17,column = 3)
C2.grid(row = 17,column = 5)
C3.grid(row = 17,column = 7)
C4 = Label(fenetre, text = " ")
C4.grid(row = 14)
# FIN - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE 


#Nom joueur

# DEBUT - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE
n1 = Label(fenetre, text = "Nom")
n2 = Label(fenetre, text = "Prénom")
n3 = Label(fenetre, text = "Groupe")
n6 = Label(fenetre, text = "Date")
n4 = Label(fenetre, text = " ")
n5 = Label(fenetre, text = " ")
n1.grid(row = 22,column = 0)
n2.grid(row = 23,column = 0)
n3.grid(row = 24,column = 0)
n4.grid(row = 26)
n5.grid(row = 21)
n6.grid(row=25, column=0)
# DEBUT - A OPTIMISER BEAUCOUP TROP DE LIGNE INUTILE


# A DECLARER EN DEBUT DE FICHIER
e1 = Entry(fenetre)
Nom = e1.get()
e2 = Entry(fenetre)
Prénom = e2.get()
e3 = Entry(fenetre)
Groupe = e3.get()
e4 = Entry(fenetre)
Date = e4.get()

e1.grid(row = 22, column = 2)
e2.grid(row = 23, column = 2)
e3.grid(row = 24, column = 2)
e4.grid(row = 25, column = 2)



#Bouton de sortie, enregistre
    
    
# A RANGER AVEC LES AUTRES FONCTIONS
def enregistrer():

    # echo ${PWD##*/} -> a taper dans la console pour trouver le dossier courant
    
    print ("Nom :", e1.get())
    print ("Prénom :", e2.get())
    print ("Groupe :", e3.get())
    print ("Date :", e4.get())
    print (" ")
    print ("Total Points Attaque :", Total_Points_Attaque)
    print ("Points cumulés d'Attaque : ", Liste_Points_Attaque)
    print ("Bibliothèque Actions d'Attaque : ", Bibli_Points_Attaque)
    print (" ")
    print ("Total Points Defense :", Total_Points_Defense)
    print ("Points cumulés de Défense : ", Liste_Points_Defense)
    print ("Bibliothèque Actions de Defense : ", Bibli_Points_Defense)
    print (" ")
    print ("Total Points Passe :", Total_Points_Passe)
    print ("Points cumulés de Passe : ", Liste_Points_Passe)
    print ("Bibliothèque Actions de Passe : ", Bibli_Points_Passe)
    print (" ")
    print ("Total Points Contre :", Total_Points_Contre)
    print ("Points cumulés de Contre : ", Liste_Points_Contre)
    print ("Bibliothèque Actions de Contre : ", Bibli_Points_Contre)
    print (" ")
    print ("Total Points Service :", Total_Points_Service)
    print ("Points cumulés de Service : ", Liste_Points_Service)
    print ("Bibliothèque Actions de Service : ", Bibli_Points_Service)
    
    
    obFichier = open('Liste de Données Volley.txt','a')
    obFichier.write ("\n")
    obFichier.write ("Nom : ")
    obFichier.write (e1.get())
    obFichier.write ("\n")
    obFichier.write ("Prénom :")
    obFichier.write (e2.get())
    obFichier.write ("\n")
    obFichier.write ("Groupe :")
    obFichier.write (e3.get())
    obFichier.write ("\n")
    obFichier.write ("Date :")
    obFichier.write (e4.get())
    obFichier.write ("\n")
    obFichier.write (" ")
    obFichier.write ("\n")
    obFichier.write ("Total Points Attaque :")
    obFichier.write (str(Total_Points_Attaque))
    obFichier.write ("\n")
    obFichier.write ("Points cumulés d'Attaque : ")
    obFichier.write (str(Liste_Points_Attaque))
    obFichier.write ("\n")
    obFichier.write ("Bibliothèque Actions d'Attaque : ")
    obFichier.write (str(Bibli_Points_Attaque))
    obFichier.write ("\n")
    obFichier.write (" ")
    obFichier.write ("\n")
    obFichier.write ("Total Points Defense :")
    obFichier.write (str(Total_Points_Defense))
    obFichier.write ("\n")
    obFichier.write ("Points cumulés de Défense : ")
    obFichier.write (str(Liste_Points_Defense))
    obFichier.write ("\n")
    obFichier.write ("Bibliothèque Actions de Defense : ")
    obFichier.write (str(Bibli_Points_Defense))
    obFichier.write ("\n")
    obFichier.write (" ")
    obFichier.write ("\n")
    obFichier.write ("Total Points Passe :")
    obFichier.write (str(Total_Points_Passe))
    obFichier.write ("\n")
    obFichier.write ("Points cumulés de Passe : ")
    obFichier.write (str(Liste_Points_Passe))
    obFichier.write ("\n")
    obFichier.write ("Bibliothèque Actions de Passe : ")
    obFichier.write (str(Bibli_Points_Passe))
    obFichier.write ("\n")
    obFichier.write (" ")
    obFichier.write ("\n")
    obFichier.write ("Total Points Contre :")
    obFichier.write (str(Total_Points_Contre))
    obFichier.write ("\n")
    obFichier.write ("Points cumulés de Contre : ")
    obFichier.write (str(Liste_Points_Contre))
    obFichier.write ("\n")
    obFichier.write ("Bibliothèque Actions de Contre : ")
    obFichier.write (str(Bibli_Points_Contre))
    obFichier.write ("\n")
    obFichier.write (" ")
    obFichier.write ("\n")
    obFichier.write ("Total Points Service :")
    obFichier.write (str(Total_Points_Service))
    obFichier.write ("\n")
    obFichier.write ("Points cumulés de Service : ")
    obFichier.write (str(Liste_Points_Service))
    obFichier.write ("\n")
    obFichier.write ("Bibliothèque Actions de Service : ")
    obFichier.write (str(Bibli_Points_Service))
    obFichier.write ("\n")
    obFichier.write ("\n")
    obFichier.write ("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    obFichier.close()
    
    
# TROP DE LIGNE AUSSI ICI    
bouton_sortir = Button(fenetre,text = "Quitter",command = fenetre.destroy)
bouton_sortir.grid(row = 24,column = 14)
bouton_enregistrer = Button(fenetre,text = "Enregistrer",command = enregistrer)
bouton_enregistrer.grid(row = 24,column = 12)

fenetre.mainloop()


