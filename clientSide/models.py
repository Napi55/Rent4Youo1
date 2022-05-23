from django.db import models


class Utilisateur(models.Model):

    nom = models.CharField(max_length=255)
    prénom = models.CharField(max_length=255)
    ddn = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    Password = models.TextField()

    class Meta:
        abstract = True


class Administrateur(Utilisateur):
    pass


class Agence(models.Model):
    nom_agence = models.CharField(max_length=255)
    siége_agence = models.TextField()
    Num_contact = models.TextField()
    email_agence = models.EmailField(unique=True)
    Nmbr_succursales = models.PositiveIntegerField()
    Nmbr_flotte = models.PositiveIntegerField()
    #logo_agence


class Employé_Agence(Utilisateur):
    id_agence = models.ForeignKey(Agence, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Dépot(models.Model):
    adress_dpt = models.TextField()
    capacité_dpt = models.PositiveIntegerField()
    id_agence = models.ForeignKey(Agence, on_delete=models.CASCADE)


class Véhicule(models.Model):
    etat = [('intrusion', 'intrusion'),
            ('enPanne', 'enPanne'),
            ('prochainementDisponible', 'prochainementDisponible'),
            ('enMarche', 'enMarche'),
            ('enArret', 'enArret')]
    catégorie = [('Petites', 'Petites'),
                 ('Moyennes', 'Moyennes'),
                 ('Larges', 'Larges'),
                 ('Premium', 'Premium'),
                 ('Monospaces', 'Monospaces'),
                 ('SUV', 'SUV')]
    matricule = models.PositiveIntegerField(unique=True)
    prix_heure = models.FloatField()
    prix_jour = models.FloatField()
    description = models.TextField()
    etat_véhicule = models.CharField(max_length=255, choices=etat, default='enMarche')
    disponibilité = models.BooleanField()
    catégorie_véhicule = models.CharField(max_length=255, choices=catégorie)
    id_dépot = models.ForeignKey(Dépot, on_delete=models.PROTECT)
    #img_vhl


class Locataire(Utilisateur):
    #img_loc
    pass


class Réservation(models.Model):
    date_début = models.DateField()
    date_fin = models.DateField()
    heure_début = models.TimeField()
    heure_fin = models.TimeField()
    id_locataire = models.ForeignKey(Locataire, on_delete=models.CASCADE)
    id_véhicule = models.OneToOneField(Véhicule, on_delete=models.CASCADE)
    id_locataire = models.ForeignKey(Locataire, on_delete=models.CASCADE)



class Facture(models.Model):
   prix_Original =models.FloatField()
   prix_total =models.FloatField()
   id_réservation = models.ForeignKey(Réservation, on_delete=models.CASCADE)


class Contrat_location(models.Model):
    #pdf
    id_réservation = models.ForeignKey(Réservation, on_delete=models.CASCADE)



class Secrétaire(Employé_Agence):
    pass


class Admin_agence(Utilisateur):
    id_agence = models.ForeignKey(Agence, on_delete=models.CASCADE)


class Propriétaire(Employé_Agence):
    pass


class Garagiste(Employé_Agence):
    pass


class Code_Promo(models.Model):
    code_promo =models.TextField()
    pourcentage =models.PositiveIntegerField()
    id_véhicule = models.ForeignKey(Véhicule, on_delete=models.CASCADE)


class Demanade_Partenariat(models.Model):
    nom_prop = models.CharField(max_length=255)
    prénom_prop= models.CharField(max_length=255)
    ddn_prop = models.DateField()
    email_prop = models.EmailField(unique=True)
    phone_prop = models.CharField(max_length=255)
    Password = models.TextField()
    nom_agence = models.CharField(max_length=255)
    siége_agence = models.TextField()
    Num_contact = models.TextField()
    email_agence = models.EmailField(unique=True)
    Nmbr_succursales = models.PositiveIntegerField()
    nmbr_flotte = models.PositiveIntegerField()
    id_administrateur = models.ForeignKey(Administrateur, on_delete=models.CASCADE)
    #id_visiteur = models.ForeignKey('Visteur', on_delete=models.PROTECT)


class Rapport(models.Model):
    description = models.TextField()
    id_locatairec = models.ForeignKey(Locataire, on_delete=models.CASCADE)
    id_agence = models.ForeignKey(Agence, on_delete=models.CASCADE)


class Réclamation(models.Model):
    contenu_réclamation = models.TextField()
    id_locatairec = models.ForeignKey(Locataire, on_delete=models.CASCADE)
    id_agence = models.ForeignKey(Agence, on_delete=models.CASCADE)



class Demande_Compte_Admin(models.Model):
    nom_admin = models.CharField(max_length=255)
    prénom_admin = models.CharField(max_length=255)
    ddn_admin = models.DateField()
    email_admin = models.EmailField(unique=True)
    phone_admin = models.CharField(max_length=255)
    Password_admin = models.TextField()
    id_agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    id_administrateur = models.ForeignKey(Administrateur, on_delete=models.CASCADE)




class Avis(models.Model):
    id_agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    id_locatairec = models.ForeignKey(Locataire, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()

