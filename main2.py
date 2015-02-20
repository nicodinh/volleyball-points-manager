import os
import tkinter as tk
   
attaque = 0
defense = 0
service = 0
passe = 0
contre = 0
coefPasse = 1
attaqueList = []
defenseList = []
serviceList = []
passeList = []
contreList = []
    
class Application(tk.Frame):
    
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):          
        
        # premiere ligne
        self.lbl_qualite = tk.Label(self, text = "Qualités").grid(row = 0, column = 0)
        self.lbl_rate = tk.Label(self, text = "Raté\n--").grid(row = 0, column = 1)
        self.lbl_mauvaise = tk.Label(self, text = "Mauvaise\n-").grid(row = 0, column = 2)
        self.lbl_bonne = tk.Label(self, text = "Bonne\n+").grid(row = 0, column = 3)
        self.lbl_excellente = tk.Label(self, text = "Excellente\n++").grid(row = 0, column = 4)
        self.lbl_pointsTotal = tk.Label(self, text = "Points Total").grid(row = 0, column = 5)
        self.lbl_pointsCumules = tk.Label(self, text = "Points cumulés").grid(row = 0, column = 6)

        # deuxieme ligne
        self.lbl_attaque = tk.Label(self, text = "Attaque").grid(row = 1, column = 0)
        self.btn_attaque1 = tk.Button(self, text = "-2", command = lambda: self.updateAttaque(-2)).grid(row = 1, column = 1)
        self.btn_attaque2 = tk.Button(self, text = "-1", command = lambda: self.updateAttaque(-1)).grid(row = 1, column = 2)
        self.btn_attaque3 = tk.Button(self, text = "+3", command = lambda: self.updateAttaque(3)).grid(row = 1, column = 3)
        self.btn_attaque4 = tk.Button(self, text = "+4", command = lambda: self.updateAttaque(4)).grid(row = 1, column = 4)
        self.lbl_attaquePtsTotal = tk.Label(self, text = attaque).grid(row = 1, column = 5)
        self.lbl_attaquePtsCumu = tk.Label(self, text = "[...]").grid(row = 1, column = 6)

        # troisieme ligne
        self.lbl_defense = tk.Label(self, text = "Defense").grid(row = 2, column = 0)
        self.btn_defense1 = tk.Button(self, text = "-3", command = lambda: self.updateDefense(-3)).grid(row = 2, column = 1)
        self.btn_defense2 = tk.Button(self, text = "-1", command = lambda: self.updateDefense(-1)).grid(row = 2, column = 2)
        self.btn_defense3 = tk.Button(self, text = "+1", command = lambda: self.updateDefense(1)).grid(row = 2, column = 3)
        self.btn_defense4 = tk.Button(self, text = "+3", command = lambda: self.updateDefense(3)).grid(row = 2, column = 4)
        self.lbl_defensePtsTotal = tk.Label(self, text = defense).grid(row = 2, column = 5)
        self.lbl_defensePtsCumu = tk.Label(self, text = "[...]").grid(row = 2, column = 6)
        
        # quatrime ligne
        self.lbl_service = tk.Label(self, text = "Service").grid(row = 3, column = 0)
        self.btn_service1 = tk.Button(self, text = "-4", command = lambda: self.updateService(-4)).grid(row = 3, column = 1)
        self.btn_service2 = tk.Button(self, text = "-2", command = lambda: self.updateService(-2)).grid(row = 3, column = 2)
        self.btn_service3 = tk.Button(self, text = "+2", command = lambda: self.updateService(2)).grid(row = 3, column = 3)
        self.btn_service4 = tk.Button(self, text = "+4", command = lambda: self.updateService(4)).grid(row = 3, column = 4)
        self.lbl_servicePtsTotal = tk.Label(self, text = service).grid(row = 3, column = 5)
        self.lbl_servicePtsCumu = tk.Label(self, text = "[...]").grid(row = 3, column = 6)
        
        # cinquieme ligne
        self.lbl_passe = tk.Label(self, text = "Passe").grid(row = 4, column = 0)
        self.btn_passe1 = tk.Button(self, text = "-2", command = lambda: self.updatePasse(-2)).grid(row = 4, column = 1)
        self.btn_passe2 = tk.Button(self, text = "-1", command = lambda: self.updatePasse(-1)).grid(row = 4, column = 2)
        self.btn_passe3 = tk.Button(self, text = "+1", command = lambda: self.updatePasse(1)).grid(row = 4, column = 3)
        self.btn_passe4 = tk.Button(self, text = "+2", command = lambda: self.updatePasse(2)).grid(row = 4, column = 4)
        self.lbl_passePtsTotal = tk.Label(self, text = passe).grid(row = 4, column = 5)
        self.lbl_passePtsCumu = tk.Label(self, text = "[...]").grid(row = 4, column = 6)
        
        # sixieme ligne
        self.lbl_contre = tk.Label(self, text = "Contre").grid(row = 5, column = 0) 
        self.btn_contre1 = tk.Button(self, text = "-2", command = lambda: self.updateContre(-2)).grid(row = 5, column = 1)
        self.btn_contre2 = tk.Button(self, text = "-1", command = lambda: self.updateContre(-1)).grid(row = 5, column = 2)
        self.btn_contre3 = tk.Button(self, text = "+1", command = lambda: self.updateContre(1)).grid(row = 5, column = 3)
        self.btn_contre4 = tk.Button(self, text = "+3", command = lambda: self.updateContre(3)).grid(row = 5, column = 4)
        self.lbl_contrePtsTotal = tk.Label(self, text = contre).grid(row = 5, column = 5)
        self.lbl_contrePtsCumu = tk.Label(self, text = "[...]").grid(row = 5, column = 6)        

        # saut ? peut etre un meilleur moyen
        self.lbl_saut = tk.Label(self, text = " ").grid(row = 6, column = 0) 
                
        # coefficient attaque defense passe precedente 
        v = tk.DoubleVar()
        v.set(1)
        self.lbl_coefPasse = tk.Label(self, text = "Coef Passe\nPrécédente").grid(row = 7, column = 0) 
        self.rbtn_coefPasse1 = tk.Radiobutton(self, text = "Normale x1", value = 1, variable = v, command = lambda: self.printValueRadio(v.get())).grid(row = 7, column = 1)
        self.rbtn_coefPasse2 = tk.Radiobutton(self, text = "Moyen x1.3", value = 1.3, variable = v, command = lambda: self.printValueRadio(v.get())).grid(row = 7, column = 2) 
        self.rbtn_coefPasse3 = tk.Radiobutton(self, text = "Difficile x2", value = 2, variable = v, command = lambda: self.printValueRadio(v.get())).grid(row = 7, column = 3) 
    
    def printValueRadio(self, value):
        global coefPasse
        coefPasse = value        
        
    def updateAttaque(self, points):
        global attaque
        attaque +=  points * coefPasse
        self.lbl_attaquePtsTotal = tk.Label(self, text = format(attaque, '.1f')).grid(row = 1, column = 5)
        attaqueList.append(format(points * coefPasse, '.1f'))
        self.updateAttaqueList()

    def updateDefense(self, points):
        global defense
        defense +=  points * coefPasse
        self.lbl_defensePtsTotal = tk.Label(self, text = format(defense, '.1f')).grid(row = 2, column = 5)
        defenseList.append(format(points * coefPasse, '.1f'))
        self.updateDefenseList()
        
    def updateService(self, points):
        global service
        service +=  points
        self.lbl_servicePtsTotal = tk.Label(self, text = service).grid(row = 3, column = 5)
        serviceList.append(points)
        self.updateServiceList()
        
    def updatePasse(self, points):
        global passe
        passe +=  points * coefPasse
        self.lbl_passePtsTotal = tk.Label(self, text = format(passe, '.1f')).grid(row = 4, column = 5)
        passeList.append(format(points * coefPasse, '.1f'))
        self.updatePasseList()
        
    def updateContre(self, points):
        global contre
        contre +=  points
        self.lbl_contrePtsTotal = tk.Label(self, text = contre).grid(row = 5, column = 5)
        contreList.append(points)
        self.updateContreList()
        
    def updateAttaqueList(self):
        text = '['
        for index, item in enumerate(attaqueList):
            text += item
            if len(attaqueList) == 1:
                text += ']'
                break
            if index == len(attaqueList) - 1:    
                text += ']'
            elif index < len(attaqueList):
                text += ' ,'    
        self.lbl_attaquePtsCumu = tk.Label(self, text = text).grid(row = 1, column = 6)
        print(attaqueList)   
        
    def updateDefenseList(self):
        text = '['
        for index, item in enumerate(defenseList):
            text += item
            if len(defenseList) == 1:
                text += ']'
                break
            if index == len(defenseList) - 1:    
                text += ']'
            elif index < len(defenseList):
                text += ' ,'    
        self.lbl_defensePtsCumu = tk.Label(self, text = text).grid(row = 2, column = 6)        
        print(defenseList)    
        
    def updateServiceList(self):
        text = '['
        for index, item in enumerate(serviceList):
            text += str(item)
            if len(serviceList) == 1:
                text += ']'
                break
            if index == len(serviceList) - 1:    
                text += ']'
            elif index < len(serviceList):
                text += ' ,' 
        self.lbl_servicePtsCumu = tk.Label(self, text = text).grid(row = 3, column = 6)        
        print(serviceList)    
    
    def updatePasseList(self):
        text = '['
        for index, item in enumerate(passeList):
            text += item
            if len(passeList) == 1:
                text += ']'
                break
            if index == len(passeList) - 1:    
                text += ']'
            elif index < len(passeList):
                text += ' ,'    
        self.lbl_passePtsCumu = tk.Label(self, text = text).grid(row = 4, column = 6)        
        print(passeList)
        
    def updateContreList(self):
        text = '['
        for index, item in enumerate(contreList):
            text += str(item)
            if len(contreList) == 1:
                text += ']'
                break
            if index == len(contreList) - 1:    
                text += ']'
            elif index < len(contreList):
                text += ' ,' 
        self.lbl_contrePtsCumu = tk.Label(self, text = text).grid(row = 5, column = 6)         
        print(contreList)

    
root = tk.Tk()
app = Application(master=root)
app.mainloop()

os.system("pause")


