
	#menu: liste employes
	self.Liste_Employes.triggered.connect(partial(self.stackedWidget.setCurrentWidget,self.liste_emp))
        #menu: liste competences
        self.Competences.triggered.connect(partial(self.stackedWidget.setCurrentWidget,self.liste_comp))
        #menu: details gamme
        self.Details_Gamme.triggered.connect(partial(self.stackedWidget.setCurrentWidget,self.details_gamme))
        #menu: details operantion
        self.Details_Operation.triggered.connect(partial(self.stackedWidget.setCurrentWidget,self.liste_op))
        #menu: creer equilibrage
        self.Creer_equilibrage.triggered.connect(partial(self.stackedWidget.setCurrentWidget,self.ajouter_equilib))
        #menu: liste equilibrages
        self.Liste_equilibrage.triggered.connect(partial(self.stackedWidget.setCurrentWidget,self.liste_equilib))
        #menu: statistiques
        #self.menuStatistiqus.activated.connect(partial(self.stackedWidget.setCurrentWidget,self.stats))
        #menu: accueil
        #self.menuHome.activated.connect(partial(self.stackedWidget.setCurrentWidget,self.welcome))
        
        #bouton ajouter: liste employes => ajouter employes
        self.ajouter_emp.clicked.connect(partial(self.stackedWidget.setCurrentWidget,self.ajouter_emp))
        #bouton annuler: ajouter employes => liste employes
        self.annuler_emp.clicked.connect(partial(self.stackedWidget.setCurrentWidget,self.liste_emp))
        #bouton ajouter: details gamme => ajouter gamme
        self.ajouter_gamme.clicked.connect(partial(self.stackedWidget.setCurrentWidget,self.ajout_gamme))
        #bouton annuler: ajouter gamme => details gamme
        self.annuler_gamme_aj.clicked.connect(partial(self.stackedWidget.setCurrentWidget,self.details_gamme))
        #bouton ajouter: liste operations => ajouter operation
        self.ajouter_op.clicked.connect(partial(self.stackedWidget.setCurrentWidget,self.ajout_op))
        #bouton annuler: ajouter operation => liste operations
        self.annuler_op_aj.clicked.connect(partial(self.stackedWidget.setCurrentWidget,self.liste_op))
        #bouton ajouter: liste competences => ajouter competence
        self.affecter_cmp.clicked.connect(partial(self.stackedWidget.setCurrentWidget,self.ajouter_comp))
        #bouton annuler: ajouter competence => liste competences
        self.annuler_cmp.clicked.connect(partial(self.stackedWidget.setCurrentWidget,self.liste_comp))
        #bouton annuler: ajouter equilibrage => accueil
        self.annuler_eq.clicked.connect(partial(self.stackedWidget.setCurrentWidget,self.welcome))
        
        from functools import partial
