import os
import tkinter as tk
   
class Volleyball(object):

    #nbInstance = 0

    def __init__(self):
        self.attaque = 0
        self.defense = 0
        self.service = 0
        self.passe = 0
        self.contre = 0
        self.coefPasse = 1
        self.attaqueList = []
        self.defenseList = []
        self.serviceList = []
        self.passeList = []
        self.contreList = []
        
#class Application(tk.Frame, Volleyball):
class Application(tk.Frame):
    
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        #Volleyball.__init__(self)
        #self.instanceVolley = Volleyball()
        
    def createWidgets(self):          
        self.instanceVolley = Volleyball()
        
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
        self.btn_attaque1 = tk.Button(self, text = "-2", command = setattr(self.instanceVolley, 'attaque', getattr(self.instanceVolley, 'attaque') + 1)).grid(row = 1, column = 1)
        #self.btn_attaque1 = tk.Button(self, text = "-2").grid(row = 1, column = 1)
        self.btn_attaque2 = tk.Button(self, text = "-1").grid(row = 1, column = 2)
        self.btn_attaque3 = tk.Button(self, text = "+3").grid(row = 1, column = 3)
        self.btn_attaque4 = tk.Button(self, text = "+4").grid(row = 1, column = 4)
        #self.lbl_attaquePtsTotal = tk.Label(self, text = str(getattr(self.instanceVolley, 'attaque'))).grid(row = 1, column = 5)
        #self.lbl_attaquePtsTotal = tk.Label(self, text = getattr(self.instanceVolley, 'attaque')).grid(row = 1, column = 5)
        self.lbl_attaquePtsTotal = tk.Label(self, text = "0").grid(row = 1, column = 5)
        self.lbl_attaquePtsCumu = tk.Label(self, text = "[...]").grid(row = 1, column = 6)

        # troisieme ligne
        self.lbl_defense = tk.Label(self, text = "Defense").grid(row = 2, column = 0)
        self.btn_defense1 = tk.Button(self, text = "-3").grid(row = 2, column = 1)
        self.btn_defense2 = tk.Button(self, text = "-1").grid(row = 2, column = 2)
        self.btn_defense3 = tk.Button(self, text = "+1").grid(row = 2, column = 3)
        self.btn_defense4 = tk.Button(self, text = "+3").grid(row = 2, column = 4)
        self.lbl_defensePtsTotal = tk.Label(self, text = "0").grid(row = 2, column = 5)
        self.lbl_defensePtsCumu = tk.Label(self, text = "[...]").grid(row = 2, column = 6)
        
        # quatrime ligne
        self.lbl_service = tk.Label(self, text = "Service").grid(row = 3, column = 0)
        self.btn_service1 = tk.Button(self, text = "-4").grid(row = 3, column = 1)
        self.btn_service2 = tk.Button(self, text = "-2").grid(row = 3, column = 2)
        self.btn_service3 = tk.Button(self, text = "+2").grid(row = 3, column = 3)
        self.btn_service4 = tk.Button(self, text = "+4").grid(row = 3, column = 4)
        self.lbl_servicePtsTotal = tk.Label(self, text = "0").grid(row = 3, column = 5)
        self.lbl_servicePtsCumu = tk.Label(self, text = "[...]").grid(row = 3, column = 6)
        
        # cinquieme ligne
        self.lbl_passe = tk.Label(self, text = "Passe").grid(row = 4, column = 0)
        self.btn_passe1 = tk.Button(self, text = "-2").grid(row = 4, column = 1)
        self.btn_passe2 = tk.Button(self, text = "-1").grid(row = 4, column = 2)
        self.btn_passe3 = tk.Button(self, text = "+1").grid(row = 4, column = 3)
        self.btn_passe4 = tk.Button(self, text = "+2").grid(row = 4, column = 4)
        self.lbl_passePtsTotal = tk.Label(self, text = "0").grid(row = 4, column = 5)
        self.lbl_passePtsCumu = tk.Label(self, text = "[...]").grid(row = 4, column = 6)
        
        # sixieme ligne
        self.lbl_contre = tk.Label(self, text = "Contre").grid(row = 5, column = 0) 
        self.btn_contre1 = tk.Button(self, text = "-2").grid(row = 5, column = 1)
        self.btn_contre2 = tk.Button(self, text = "-1").grid(row = 5, column = 2)
        self.btn_contre3 = tk.Button(self, text = "+1").grid(row = 5, column = 3)
        self.btn_contre4 = tk.Button(self, text = "+3").grid(row = 5, column = 4)
        self.lbl_contrePtsTotal = tk.Label(self, text = "0").grid(row = 5, column = 5)
        self.lbl_contrePtsCumu = tk.Label(self, text = "[...]").grid(row = 5, column = 6)        

        # saut ? peut etre un meilleur moyen
        self.lbl_saut = tk.Label(self, text = " ").grid(row = 6, column = 0) 
                
        # coefficient attaque defense passe precedente
        self.lbl_coefPasse = tk.Label(self, text = "Coef Passe\nPrécédente").grid(row = 7, column = 0) 
        self.rbtn_coefPasse1 = tk.Radiobutton(self, text = "Normale x1", value=1).grid(row = 7, column = 1) 
        self.rbtn_coefPasse2 = tk.Radiobutton(self, text = "Moyen x1.3", value=1.3).grid(row = 7, column = 2) 
        self.rbtn_coefPasse3 = tk.Radiobutton(self, text = "Difficile x2", value=2).grid(row = 7, column = 3) 


    
root = tk.Tk()
app = Application(master=root)
app.mainloop()

#instanceVolley = Volleyball()
#setattr(instanceVolley, 'attaque', getattr(instanceVolley, 'attaque') + 1)
#setattr(instanceVolley, 'attaque', getattr(instanceVolley, 'attaque') + 1)
#setattr(instanceVolley, 'attaque', getattr(instanceVolley, 'attaque') + 1)
#print ("Total %d" % getattr(instanceVolley, 'attaque'))

#os.system("pause")


