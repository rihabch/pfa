--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: competence; Type: TABLE; Schema: public; Owner: imen; Tablespace: 
--

CREATE TABLE competence (
    matricule bigint NOT NULL,
    code_op character varying(254) NOT NULL,
    code_util character varying(254) NOT NULL,
    allure double precision,
    taux_de_retouche double precision,
    competence double precision,
    date_affectation date
);


ALTER TABLE competence OWNER TO imen;

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
-- Name: employe; Type: TABLE; Schema: public; Owner: imen; Tablespace: 
--

CREATE TABLE employe (
    cin_emp bigint,
    matricule bigint NOT NULL,
    code_util character varying(254) NOT NULL,
    nom character varying(254),
    prenom character varying(254),
    date_embauche date,
    image character varying(254),
    presence character varying(254),
    date_naissance date
);


ALTER TABLE employe OWNER TO imen;

--
-- Name: equilibrage; Type: TABLE; Schema: public; Owner: imen; Tablespace: 
--

CREATE TABLE equilibrage (
    code_eq character varying(254) NOT NULL,
    code_util character varying(254) NOT NULL,
    code_modele character varying(254) NOT NULL,
    etat_eq character varying(254),
    date_debut date,
    date_fin date,
    cadence bigint,
    nb_ouvrieres bigint
);


ALTER TABLE equilibrage OWNER TO imen;

--
-- Name: gamme_de_modele; Type: TABLE; Schema: public; Owner: imen; Tablespace: 
--

CREATE TABLE gamme_de_modele (
    code_modele character varying(254) NOT NULL,
    code_util character varying(254) NOT NULL,
    nom_modele character varying(254),
    marque character varying(254)
);


ALTER TABLE gamme_de_modele OWNER TO imen;

--
-- Name: groupe; Type: TABLE; Schema: public; Owner: imen; Tablespace: 
--

CREATE TABLE groupe (
    code_groupe character varying(254) NOT NULL,
    nom_groupe character varying(254)
);


ALTER TABLE groupe OWNER TO imen;

--
-- Name: operation; Type: TABLE; Schema: public; Owner: imen; Tablespace: 
--

CREATE TABLE operation (
    code_op character varying(254) NOT NULL,
    code_util character varying(254) NOT NULL,
    nom_op character varying(254),
    minutage double precision,
    machine character varying(254),
    critere_de_qualite character varying(254),
    video character varying(254)
);


ALTER TABLE operation OWNER TO imen;

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
-- Data for Name: competence; Type: TABLE DATA; Schema: public; Owner: imen
--

COPY competence (matricule, code_op, code_util, allure, taux_de_retouche, competence, date_affectation) FROM stdin;
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
-- Data for Name: employe; Type: TABLE DATA; Schema: public; Owner: imen
--

COPY employe (cin_emp, matricule, code_util, nom, prenom, date_embauche, image, presence, date_naissance) FROM stdin;
12345678	123	admin_01	ftirich	haifa	2000-01-01		P	1990-08-01
2145345	125	admin_02	bouguel	amani	2010-05-07		A	1988-01-05
12369855	7894	admin_02	hellab	samira	2012-04-03		D	1992-03-02
70120345	5874	admin_01	dellay	haroun	1998-05-04		P	1978-02-09
70125836	9874	admin_01	labidi	ons	1999-02-10		P	1980-06-04
32519847	3659	admin_02	lamine	zeineb	2015-03-06		P	1992-02-02
36259841	2586	admin_01	mkhinini	meriam	2013-03-03		P	2000-01-01
89587463	1236	admin_01	helaoui	nada	2012-05-03		P	1992-05-07
\.


--
-- Data for Name: equilibrage; Type: TABLE DATA; Schema: public; Owner: imen
--

COPY equilibrage (code_eq, code_util, code_modele, etat_eq, date_debut, date_fin, cadence, nb_ouvrieres) FROM stdin;
\.


--
-- Data for Name: gamme_de_modele; Type: TABLE DATA; Schema: public; Owner: imen
--

COPY gamme_de_modele (code_modele, code_util, nom_modele, marque) FROM stdin;
\.


--
-- Data for Name: groupe; Type: TABLE DATA; Schema: public; Owner: imen
--

COPY groupe (code_groupe, nom_groupe) FROM stdin;
grp_01	administrateur
grp_02	utilisateur
\.


--
-- Data for Name: operation; Type: TABLE DATA; Schema: public; Owner: imen
--

COPY operation (code_op, code_util, nom_op, minutage, machine, critere_de_qualite, video) FROM stdin;
VPA1002	admin_01	assemblage cote	74	502		
VPC1012	admin_01	couture pince	0.849999999999999978	301		
VPMP020	admin_02	montage poche	0.520000000000000018	301		
VPNH0201	admin_02	nervure ouverture poche	1.01000000000000001	205		
PNCM002	admin_02	conformage poches	0.959999999999999964	fer		
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
-- Name: pk_competence; Type: CONSTRAINT; Schema: public; Owner: imen; Tablespace: 
--

ALTER TABLE ONLY competence
    ADD CONSTRAINT pk_competence PRIMARY KEY (matricule, code_op);


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
-- Name: pk_employe; Type: CONSTRAINT; Schema: public; Owner: imen; Tablespace: 
--

ALTER TABLE ONLY employe
    ADD CONSTRAINT pk_employe PRIMARY KEY (matricule);


--
-- Name: pk_equilibrage; Type: CONSTRAINT; Schema: public; Owner: imen; Tablespace: 
--

ALTER TABLE ONLY equilibrage
    ADD CONSTRAINT pk_equilibrage PRIMARY KEY (code_eq);


--
-- Name: pk_gamme_de_modele; Type: CONSTRAINT; Schema: public; Owner: imen; Tablespace: 
--

ALTER TABLE ONLY gamme_de_modele
    ADD CONSTRAINT pk_gamme_de_modele PRIMARY KEY (code_modele);


--
-- Name: pk_groupe; Type: CONSTRAINT; Schema: public; Owner: imen; Tablespace: 
--

ALTER TABLE ONLY groupe
    ADD CONSTRAINT pk_groupe PRIMARY KEY (code_groupe);


--
-- Name: pk_operation; Type: CONSTRAINT; Schema: public; Owner: imen; Tablespace: 
--

ALTER TABLE ONLY operation
    ADD CONSTRAINT pk_operation PRIMARY KEY (code_op);


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
-- Name: fk_competen_competenc_operatio; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY competence
    ADD CONSTRAINT fk_competen_competenc_operatio FOREIGN KEY (code_op) REFERENCES operation(code_op) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fk_competen_est_compe_employe; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY competence
    ADD CONSTRAINT fk_competen_est_compe_employe FOREIGN KEY (matricule) REFERENCES employe(matricule) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fk_competen_gerer_com_utilisat; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY competence
    ADD CONSTRAINT fk_competen_gerer_com_utilisat FOREIGN KEY (code_util) REFERENCES utilisateur(code_util) ON UPDATE RESTRICT ON DELETE RESTRICT;


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
-- Name: fk_details__details_g_gamme_de; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY details_gamme
    ADD CONSTRAINT fk_details__details_g_gamme_de FOREIGN KEY (code_modele) REFERENCES gamme_de_modele(code_modele) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fk_details__details_g_operatio; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY details_gamme
    ADD CONSTRAINT fk_details__details_g_operatio FOREIGN KEY (code_op) REFERENCES operation(code_op) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fk_details__gerer_pri_utilisat; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY details_privileges
    ADD CONSTRAINT fk_details__gerer_pri_utilisat FOREIGN KEY (code_util) REFERENCES utilisateur(code_util) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fk_employe__employe_d_employe; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY details_equilibrage
    ADD CONSTRAINT fk_employe__employe_d_employe FOREIGN KEY (matricule) REFERENCES employe(matricule) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fk_employe_gerer_emp_utilisat; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY employe
    ADD CONSTRAINT fk_employe_gerer_emp_utilisat FOREIGN KEY (code_util) REFERENCES utilisateur(code_util) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fk_equilibr_equilibra_equilibr; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY details_equilibrage
    ADD CONSTRAINT fk_equilibr_equilibra_equilibr FOREIGN KEY (code_eq) REFERENCES equilibrage(code_eq) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fk_equilibr_gamme_equ_gamme_de; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY equilibrage
    ADD CONSTRAINT fk_equilibr_gamme_equ_gamme_de FOREIGN KEY (code_modele) REFERENCES gamme_de_modele(code_modele) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fk_equilibr_gerer_equ_utilisat; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY equilibrage
    ADD CONSTRAINT fk_equilibr_gerer_equ_utilisat FOREIGN KEY (code_util) REFERENCES utilisateur(code_util) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fk_gamme_de_gerer_mod_utilisat; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY gamme_de_modele
    ADD CONSTRAINT fk_gamme_de_gerer_mod_utilisat FOREIGN KEY (code_util) REFERENCES utilisateur(code_util) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fk_operatio_gerer_ope_utilisat; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY operation
    ADD CONSTRAINT fk_operatio_gerer_ope_utilisat FOREIGN KEY (code_util) REFERENCES utilisateur(code_util) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fk_operatio_operation_operatio; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY details_equilibrage
    ADD CONSTRAINT fk_operatio_operation_operatio FOREIGN KEY (code_op) REFERENCES operation(code_op) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: fk_utilisat_appartien_groupe; Type: FK CONSTRAINT; Schema: public; Owner: imen
--

ALTER TABLE ONLY utilisateur
    ADD CONSTRAINT fk_utilisat_appartien_groupe FOREIGN KEY (code_groupe) REFERENCES groupe(code_groupe) ON UPDATE RESTRICT ON DELETE RESTRICT;


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

