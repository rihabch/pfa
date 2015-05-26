import psycopg2
import sys
import connexion

class employe():
	
	def _init_(self,matricule,cin,code_util=1,nom,prenom,date_emb,image,date_naiss)
		c = connexion()		
		self.matricule = matricule
		self.cin=cin
		self.code_util=code_util
		self.nom=nom
		self.prenom=prenom
		self.date_emb=date_emb
		self.image=image
		self.date_naiss=date_naiss
		
	def ajouter(self):
		connex = c.connect()

		# conn.cursor will return a cursor object, you can use this cursor to perform queries
		cursor = connex.cursor()
		
		# Pass data to fill a query placeholders and let Psycopg perform
		# the correct conversion (no more SQL injections!)
		cursor.execute("INSERT INTO  employe (matricule, cin_emp, code_util, nom, prenom, date_embauche, image, presence, 	date_naissance) VALUES ("+self.matricule","self.cin+","+self.code_util+",'"+self.nom+"','"+self.prenom+"','"+self.date_emb+"','"+self.image+"','"+self.date_naiss')")
	
		# Make the changes to the database persistent
		connex.commit()

		# Close communication with the database
		cursor.close()
		connex.close()		
