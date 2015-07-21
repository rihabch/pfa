--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: competences; Type: TABLE; Schema: public; Owner: imen; Tablespace: 
--

CREATE TABLE competences (
    matricule bigint NOT NULL,
    code_op character varying(254) NOT NULL,
    competence bigint,
    allure bigint,
    taux_de_retouche bigint,
    date_aff date,
    code_util character varying(254) NOT NULL
);


ALTER TABLE competences OWNER TO imen;

--
-- Name: details_equilibrage; Type: TABLE; Schema: public; Owner: imen; Tablespace: 
--

CREATE TABLE details_equilibrage (
    matricule bigint NOT NULL,
    code_op character varying(254) NOT NULL,
    code_eq character varying(254) NOT NULL
);


ALTER TABLE details_equilibrage OWNER TO imen;

--
-- Name: details_gamme; Type: TABLE; Schema: public; Owner: imen; Tablespace: 
--

CREATE TABLE details_gamme (
    code_modele character varying(254) NOT NULL,
    code_op character varying(254) NOT NULL,
    id_gamme character varying(254) NOT NULL
);


ALTER TABLE details_gamme OWNER TO imen;

--
-- Name: details_privileges; Type: TABLE; Schema: public; Owner: imen; Tablespace: 
--

CREATE TABLE details_privileges (
    code_groupe character varying(254) NOT NULL,
    code_priv bigint NOT NULL,
    code_util character varying(254) NOT NULL,
    nom_table character varying(254)
);


ALTER TABLE details_privileges OWNER TO imen;

--
-- Name: employes; Type: TABLE; Schema: public; Owner: imen; Tablespace: 
--

CREATE TABLE employes (
    matricule bigint NOT NULL,
    cin_emp bigint,
    nom character varying(254),
    prenom character varying(254),
    presence character varying(254),
    date_naissance date,
    date_embauche date,
    code_utilisateur character varying(254) NOT NULL,
    image character varying(254)
);


ALTER TABLE employes OWNER TO imen;

--
-- Name: equilibrages; Type: TABLE; Schema: public; Owner: imen; Tablespace: 
--

CREATE TABLE equilibrages (
    code_eq character varying(254) NOT NULL,
    code_modele character varying(254) NOT NULL,
    etat_eq character varying(254),
    date_deb date,
    date_fin date,
    cadence bigint,
    nb_ouvrieres bigint,
    code_util character varying(254) NOT NULL
);


ALTER TABLE equilibrages OWNER TO imen;

--
-- Name: gammes; Type: TABLE; Schema: public; Owner: imen; Tablespace: 
--

CREATE TABLE gammes (
    code_modele character varying(254) NOT NULL,
    nom_modele character varying(254),
    marque character varying(254),
    code_util character varying(254)
);


ALTER TABLE gammes OWNER TO imen;

--
-- Name: groupe; Type: TABLE; Schema: public; Owner: imen; Tablespace: 
--

CREATE TABLE groupe (
    code_groupe character varying(254) NOT NULL,
    nom_groupe character varying(254)
);


ALTER TABLE groupe OWNER TO imen;

--
-- Name: operations; Type: TABLE; Schema: public; Owner: imen; Tablespace: 
--

CREATE TABLE operations (
    code_op character varying(254) NOT NULL,
    nom_op character varying(254),
    minutage double precision,
    machine character varying(254),
    critere_de_qualite character varying(254),
    code_util character varying(254),
    video character varying(254)
);


ALTER TABLE operations OWNER TO imen;

--
-- Name: privilege; Type: TABLE; Schema: public; Owner: imen; Tablespace: 
--

CREATE TABLE privilege (
    code_priv bigint NOT NULL,
    type_permission character varying(254)
);


ALTER TABLE privilege OWNER TO imen;

--
-- Name: utilisateur; Type: TABLE; Schema: public; Owner: imen; Tablespace: 
--

CREATE TABLE utilisateur (
    code_util character varying(254) NOT NULL,
    code_groupe character varying(254) NOT NULL,
    nom_util character varying(254),
    prenom_util character varying(254),
    poste_util character varying(254),
    mot_de_passe character varying(254)
);


ALTER TABLE utilisateur OWNER TO imen;

--
-- Data for Name: competences; Type: TABLE DATA; Schema: public; Owner: imen
--

COPY competences (matricule, code_op, competence, allure, taux_de_retouche, date_aff, code_util) FROM stdin;
\.


--
-- Data for Name: details_equilibrage; Type: TABLE DATA; Schema: public; Owner: imen
--

COPY details_equilibrage (matricule, code_op, code_eq) FROM stdin;
\.


--
-- Data for Name: details_gamme; Type: TABLE DATA; Schema: public; Owner: imen
--

COPY details_gamme (code_modele, code_op, id_gamme) FROM stdin;
\.


--
-- Data for Name: details_privileges; Type: TABLE DATA; Schema: public; Owner: imen
--

COPY details_privileges (code_groupe, code_priv, code_util, nom_table) FROM stdin;
\.


--
-- Data for Name: employes; Type: TABLE DATA; Schema: public; Owner: imen
--

COPY employes (matricule, cin_emp, nom, prenom, presence, date_naissance, date_embauche, code_utilisateur, image) FROM stdin;
21	12036547	hellab	samira	D	1992-03-02	2012-04-03	admin_01	
3265	78054698	dellay	haroun	P	1978-02-09	1998-05-05	admin_02	
3254	98568749	lamine	zaineb	P	1993-08-09	2010-05-09	admin_01	
3596	14528963	mkhinini	meriam	A	1990-05-07	2000-11-11	admin_01	
\.


--
-- Data for Name: equilibrages; Type: TABLE DATA; Schema: public; Owner: imen
--

COPY equilibrages (code_eq, code_modele, etat_eq, date_deb, date_fin, cadence, nb_ouvrieres, code_util) FROM stdin;
\.


--
-- Data for Name: gammes; Type: TABLE DATA; Schema: public; Owner: imen
--

COPY gammes (code_modele, nom_modele, marque, code_util) FROM stdin;
\.


--
-- Data for Name: groupe; Type: TABLE DATA; Schema: public; Owner: imen
--

COPY groupe (code_groupe, nom_groupe) FROM stdin;
grp_01	administrateur
grp_02	utilisateur
\.


--
-- Data for Name: operations; Type: TABLE DATA; Schema: public; Owner: imen
--

COPY operations (code_op, nom_op, minutage, machine, critere_de_qualite, code_util, video) FROM stdin;
VPC1012	couture pince	0.849999999999999978	301		admin_01	
VPMP020	montage poche	0.520000000000000018	301		admin_02	
PNCM002	conformage poches	0.959999999999999964	fer		admin_02	
VPNH0201	nervure ouverture poches	1.01000000000000001	205		admin_01	
VCM1203	assemblage poches	1.30000000000000004	3001		admin_01	
\.


--
-- Data for Name: privilege; Type: TABLE DATA; Schema: public; Owner: imen
--

COPY privilege (code_priv, type_permission) FROM stdin;
100	read_only
\.


--
-- Data for Name: utilisateur; Type: TABLE DATA; Schema: public; Owner: imen
--

COPY utilisateur (code_util, code_groupe, nom_util, prenom_util, poste_util, mot_de_passe) FROM stdin;
utl_01	grp_02	yaaich	amine	consultant	0123
admin_01	grp_01	tounsi	imen	administrateur	imen
utl_02	grp_02	bhar	imen	directeur	hedi
admin_02	grp_01	chakchouk	rihab	developpeur	rihab
\.


--
-- Name: competences_pkey; Type: CONSTRAINT; Schema: public; Owner: imen; Tablespace: 
--

ALTER TABLE ONLY competences
    ADD CONSTRAINT competences_pkey PRIMARY KEY (matricule, code_op);


--
-- Name: employes_cin_emp_key; Type: CONSTRAINT; Schema: public; Owner: imen; Tablespace: 
--

ALTER TABLE ONLY employes
    ADD CONSTRAINT employes_cin_emp_key UNIQUE (cin_emp);


--
-- Name: employes_pkey; Type: CONSTRAINT; Schema: public; Owner: imen; Tablespace: 
--

ALTER TABLE ONLY employes
    ADD CONSTRAINT employes_pkey PRIMARY KEY (matricule);


--
-- Name: equilibrages_pkey; Type: CONSTRAINT; Schema: public; Owner: imen; Tablespace: 
--

ALTER TABLE ONLY equilibrages
    ADD CONSTRAINT equilibrages_pkey PRIMARY KEY (code_eq);


--
-- Name: gammes_pkey; Type: CONSTRAINT; Schema: public; Owner: imen; Tablespace: 
--

ALTER TABLE ONLY gammes
    ADD CONSTRAINT gammes_pkey PRIMARY KEY (code_modele);


--
-- Name: operations_pkey; Type: CONSTRAINT; Schema: public; Owner: imen; Tablespace: 
--

ALTER TABLE ONLY operations
    ADD CONSTRAINT operations_pkey PRIMARY KEY (code_op);


--
-- Name: pk_details_gamme; Type: CONSTRAINT; Schema: public; Owner: imen; Tablespace: 
--

ALTER TABLE ONLY details_gamme
    ADD CONSTRAINT pk_details_gamme PRIMARY KEY (code_modele, code_op, id_gamme);


--
-- Name: pk_details_privileges; Type: CONSTRAINT; Schema: public; Owner: imen; Tablespace: 
--

ALTER TABLE ONLY details_privileges
    ADD CONSTRAINT pk_details_privileges PRIMARY KEY (code_groupe, code_priv);


--
-- Name: pk_detailseq; Type: CONSTRAINT; Schema: public; Owner: imen; Tablespace: 
--

ALTER TABLE ONLY details_equilibrage
    ADD CONSTRAINT pk_detailseq PRIMARY KEY (matricule, code_op, code_eq);


--
-- Name: pk_groupe; Type: CONSTRAINT; Schema: public; Owner: imen; Tablespace: 
--

ALTER TABLE ONLY groupe
    ADD CONSTRAINT pk_groupe PRIMARY KEY (code_groupe);


--
-- Name: pk_privileges; Type: CONSTRAINT; Schema: public; Owner: imen; Tablespace: 
--

ALTER TABLE ONLY privilege
    ADD CONSTRAINT pk_privileges PRIMARY KEY (code_priv);


--
-- Name: pk_utilisateur; Type: CONSTRAINT; Schema: public; Owner: imen; Tablespace: 
--

ALTER TABLE ONLY utilisateur
    ADD CONSTRAINT pk_utilisateur PRIMARY KEY (code_util);


--
-- Name: competences_code_op_fkey; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY competences
    ADD CONSTRAINT competences_code_op_fkey FOREIGN KEY (code_op) REFERENCES operations(code_op) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: competences_code_util_fkey; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY competences
    ADD CONSTRAINT competences_code_util_fkey FOREIGN KEY (code_util) REFERENCES utilisateur(code_util) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: competences_matricule_fkey; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY competences
    ADD CONSTRAINT competences_matricule_fkey FOREIGN KEY (matricule) REFERENCES employes(matricule) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: details_equilibrage_code_eq_fkey; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY details_equilibrage
    ADD CONSTRAINT details_equilibrage_code_eq_fkey FOREIGN KEY (code_eq) REFERENCES equilibrages(code_eq) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: details_equilibrage_code_op_fkey; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY details_equilibrage
    ADD CONSTRAINT details_equilibrage_code_op_fkey FOREIGN KEY (code_op) REFERENCES operations(code_op) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: details_equilibrage_matricule_fkey; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY details_equilibrage
    ADD CONSTRAINT details_equilibrage_matricule_fkey FOREIGN KEY (matricule) REFERENCES employes(matricule) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: details_gamme_code_modele_fkey; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY details_gamme
    ADD CONSTRAINT details_gamme_code_modele_fkey FOREIGN KEY (code_modele) REFERENCES gammes(code_modele) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: details_gamme_code_op_fkey; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY details_gamme
    ADD CONSTRAINT details_gamme_code_op_fkey FOREIGN KEY (code_op) REFERENCES operations(code_op) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: employes_code_utilisateur_fkey; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY employes
    ADD CONSTRAINT employes_code_utilisateur_fkey FOREIGN KEY (code_utilisateur) REFERENCES utilisateur(code_util) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: equilibrages_code_modele_fkey; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY equilibrages
    ADD CONSTRAINT equilibrages_code_modele_fkey FOREIGN KEY (code_modele) REFERENCES gammes(code_modele) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: equilibrages_code_util_fkey; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY equilibrages
    ADD CONSTRAINT equilibrages_code_util_fkey FOREIGN KEY (code_util) REFERENCES utilisateur(code_util) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fk_details__associati_groupe; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY details_privileges
    ADD CONSTRAINT fk_details__associati_groupe FOREIGN KEY (code_groupe) REFERENCES groupe(code_groupe) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fk_details__associati_privileg; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY details_privileges
    ADD CONSTRAINT fk_details__associati_privileg FOREIGN KEY (code_priv) REFERENCES privilege(code_priv) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fk_details__gerer_pri_utilisat; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY details_privileges
    ADD CONSTRAINT fk_details__gerer_pri_utilisat FOREIGN KEY (code_util) REFERENCES utilisateur(code_util) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fk_utilisat_appartien_groupe; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY utilisateur
    ADD CONSTRAINT fk_utilisat_appartien_groupe FOREIGN KEY (code_groupe) REFERENCES groupe(code_groupe) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: gammes_code_util_fkey; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY gammes
    ADD CONSTRAINT gammes_code_util_fkey FOREIGN KEY (code_util) REFERENCES utilisateur(code_util) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: operations_code_util_fkey; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY operations
    ADD CONSTRAINT operations_code_util_fkey FOREIGN KEY (code_util) REFERENCES utilisateur(code_util) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

