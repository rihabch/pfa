/*==============================================================*/
/* Table : Competence                                           */
/*==============================================================*/
create table Competence  (
   matricule            INT8                 not null,
   code_op              INT8                 not null,
   code_util            INT8                 not null,
   allure               FLOAT8               null,
   taux_de_retouche     FLOAT8               null,
   competence           FLOAT8               null,
   date_affectation     DATE                 null,
   constraint PK_COMPETENCE primary key (matricule, code_op)
);

/*==============================================================*/
/* Table : Details_Equilibrage                                  */
/*==============================================================*/
create table Details_Equilibrage (
   matricule            INT8                 not null,
   code_op              INT8                 not null,
   code_eq              INT8                 not null,
   constraint PK_DETAILSEQ primary key (matricule, code_op, code_eq)
);

/*==============================================================*/
/* Table : Details_Gamme                                        */
/*==============================================================*/
create table Details_Gamme (
   code_modele          INT8                 not null,
   code_op              INT8                 not null,
   id_gamme             INT8                 not null,
   constraint PK_DETAILS_GAMME primary key (code_modele, code_op, id_gamme)
);

/*==============================================================*/
/* Table : Details_Privileges                                   */
/*==============================================================*/
create table Details_Privileges (
   code_groupe          INT8                 not null,
   code_prev            INT8                 not null,
   code_util            INT8                 not null,
   nom_table            VARCHAR(254)         null,
   constraint PK_DETAILS_PRIVILEGES primary key (code_groupe, code_prev)
);

/*==============================================================*/
/* Table : Employe                                              */
/*==============================================================*/
create table Employe (
   cin_emp              INT8                 not null,
   matricule            INT8                 not null,
   code_util            INT8                 not null,
   nom                  VARCHAR(254)         null,
   prenom               VARCHAR(254)         null,
   date_embauche        DATE                 null,
   image                VARCHAR(254)         null,
   presence             VARCHAR(254)         null,
   date_naissance       DATE                 null,
   constraint PK_EMPLOYE primary key (matricule)
);

/*==============================================================*/
/* Table : Equilibrage                                          */
/*==============================================================*/
create table Equilibrage (
   code_eq              INT8                 not null,
   code_util            INT8                 not null,
   code_modele          INT8                 not null,
   etat_eq              VARCHAR(254)         null,
   date_debut           DATE                 null,
   date_fin             DATE                 null,
   cadence              INT8                 null,
   nb_ouvrieres         INT8                 null,
   constraint PK_EQUILIBRAGE primary key (code_eq)
);


/*==============================================================*/
/* Table : Gamme_de_Modele                                      */
/*==============================================================*/
create table Gamme_de_Modele (
   code_modele          INT8                 not null,
   code_util            INT8                 not null,
   nom_modele           VARCHAR(254)         null,
   marque               VARCHAR(254)         null,
   constraint PK_GAMME_DE_MODELE primary key (code_modele)
);

/*==============================================================*/
/* Table : Groupe                                               */
/*==============================================================*/
create table Groupe (
   code_groupe          INT8                 not null,
   nom_groupe           VARCHAR(254)         null,
   constraint PK_GROUPE primary key (code_groupe)
);

/*==============================================================*/
/* Table : Operation                                            */
/*==============================================================*/
create table Operation (
   code_op              INT8                 not null,
   code_util            INT8                 not null,
   nom_op               VARCHAR(254)         null,
   minutage             FLOAT8               null,
   machine              VARCHAR(254)         null,
   critere_de_qualite   VARCHAR(254)         null,
   video                VARCHAR(254)         null,
   constraint PK_OPERATION primary key (code_op)
);


/*==============================================================*/
/* Table : Privileges                                           */
/*==============================================================*/
create table Privileges (
   code_prev            INT8                 not null,
   type_permission      INT8                 null,
   constraint PK_PRIVILEGES primary key (code_prev)
);

/*==============================================================*/
/* Table : Utilisateur                                          */
/*==============================================================*/
create table Utilisateur (
   code_util            INT8                 not null,
   code_groupe          INT8                 not null,
   nom_util             VARCHAR(254)         null,
   prenom_util          VARCHAR(254)         null,
   poste_util           VARCHAR(254)         null,
   mot_de_passe         VARCHAR(254)         null,
   constraint PK_UTILISATEUR primary key (code_util)
);


alter table Competence
   add constraint FK_COMPETEN_COMPETENC_OPERATIO foreign key (code_op)
      references Operation (code_op)
      on delete restrict on update restrict;

alter table Competence
   add constraint FK_COMPETEN_EST_COMPE_EMPLOYE foreign key (matricule)
      references Employe (matricule)
      on delete restrict on update restrict;

alter table Competence
   add constraint FK_COMPETEN_GERER_COM_UTILISAT foreign key (code_util)
      references Utilisateur (code_util)
      on delete restrict on update restrict;

alter table Details_Gamme
   add constraint FK_DETAILS__DETAILS_G_GAMME_DE foreign key (code_modele)
      references Gamme_de_Modele (code_modele)
      on delete restrict on update restrict;

alter table Details_Gamme
   add constraint FK_DETAILS__DETAILS_G_OPERATIO foreign key (code_op)
      references Operation (code_op)
      on delete restrict on update restrict;

alter table Details_Privileges
   add constraint FK_DETAILS__ASSOCIATI_GROUPE foreign key (code_groupe)
      references Groupe (code_groupe)
      on delete restrict on update restrict;

alter table Details_Privileges
   add constraint FK_DETAILS__ASSOCIATI_PRIVILEG foreign key (code_prev)
      references Privileges (code_prev)
      on delete restrict on update restrict;

alter table Details_Privileges
   add constraint FK_DETAILS__GERER_PRI_UTILISAT foreign key (code_util)
      references Utilisateur (code_util)
      on delete restrict on update restrict;

alter table Employe
   add constraint FK_EMPLOYE_GERER_EMP_UTILISAT foreign key (code_util)
      references Utilisateur (code_util)
      on delete restrict on update restrict;

alter table Equilibrage
   add constraint FK_EQUILIBR_GAMME_EQU_GAMME_DE foreign key (code_modele)
      references Gamme_de_Modele (code_modele)
      on delete restrict on update restrict;

alter table Equilibrage
   add constraint FK_EQUILIBR_GERER_EQU_UTILISAT foreign key (code_util)
      references Utilisateur (code_util)
      on delete restrict on update restrict;


alter table Details_Equilibrage 
   add constraint FK_EQUILIBR_EQUILIBRA_EQUILIBR foreign key (code_eq)
      references Equilibrage (code_eq)
      on delete restrict on update restrict;

alter table Gamme_de_Modele
   add constraint FK_GAMME_DE_GERER_MOD_UTILISAT foreign key (code_util)
      references Utilisateur (code_util)
      on delete restrict on update restrict;

alter table Operation
   add constraint FK_OPERATIO_GERER_OPE_UTILISAT foreign key (code_util)
      references Utilisateur (code_util)
      on delete restrict on update restrict;

alter table Details_Equilibrage 
   add constraint FK_OPERATIO_OPERATION_OPERATIO foreign key (code_op)
      references Operation (code_op)
      on delete restrict on update restrict;

alter table Utilisateur
   add constraint FK_UTILISAT_APPARTIEN_GROUPE foreign key (code_groupe)
      references Groupe (code_groupe)
      on delete restrict on update restrict;


alter table Details_Equilibrage 
   add constraint FK_EMPLOYE__EMPLOYE_D_EMPLOYE foreign key (matricule)
      references Employe (matricule)
      on delete restrict on update restrict;
