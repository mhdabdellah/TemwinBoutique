-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Client: localhost
-- Généré le: Mar 15 Février 2022 à 17:22
-- Version du serveur: 5.6.12-log
-- Version de PHP: 5.4.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données: `django_db`
--
CREATE DATABASE IF NOT EXISTS `django_db` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `django_db`;

-- --------------------------------------------------------

--
-- Structure de la table `accounts_profile`
--

CREATE TABLE IF NOT EXISTS `accounts_profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `phone_number` varchar(12) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `manager` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Contenu de la table `accounts_profile`
--

INSERT INTO `accounts_profile` (`id`, `phone_number`, `image`, `user_id`, `manager`) VALUES
(1, '', 'default.jpg', 1, NULL),
(2, '', 'default.jpg', 2, NULL),
(3, '', 'default.jpg', 3, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Contenu de la table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$150000$PbfhFzS1pHps$1Y0QRCTUDLhJjBwepY5C4YrCJPUjPN7+KMs1SzuhJRs=', '2022-02-15 00:28:34.859293', 1, 'mohamedou', '', '', 'mohamedou@gmail.com', 1, 1, '2022-02-15 00:26:55.384168'),
(2, 'pbkdf2_sha256$150000$LEn8BVy7yJ0n$ohFKmO9RmzlkwatIozDIEFAlmcNQWYs4nhq1J7jVO1E=', '2022-02-15 00:41:12.561668', 0, 'sidigh', 'ahmed', 'sidigh', 'sidigh@gmail.com', 1, 1, '2022-02-15 00:31:04.724447'),
(3, 'pbkdf2_sha256$150000$TYlkuGXciUnG$doJr9gcoD3epzLdcrgvuR72UfvjtseVPAF5a78dVoMw=', '2022-02-15 00:43:51.784905', 0, 'sidighe', 'ahmed', 'sidigh', 'sidigh@gmail.com', 0, 1, '2022-02-15 00:33:02.095427');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `chat_message`
--

CREATE TABLE IF NOT EXISTS `chat_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seen` tinyint(1) NOT NULL,
  `date_created` datetime(6) NOT NULL,
  `receiver_id` int(11) NOT NULL,
  `sender_id` int(11) NOT NULL,
  `message` varchar(5000) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `chat_message_receiver_id_0eceddde_fk_auth_user_id` (`receiver_id`),
  KEY `chat_message_sender_id_991c686c_fk_auth_user_id` (`sender_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=43 ;

--
-- Contenu de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-02-15 00:11:47.256169'),
(2, 'auth', '0001_initial', '2022-02-15 00:11:49.971125'),
(3, 'accounts', '0001_initial', '2022-02-15 00:11:59.319798'),
(4, 'accounts', '0002_auto_20200910_2302', '2022-02-15 00:12:00.238405'),
(5, 'accounts', '0003_alter_profile_id', '2022-02-15 00:12:02.023287'),
(6, 'accounts', '0004_auto_20210909_2230', '2022-02-15 00:12:03.848889'),
(7, 'accounts', '0005_alter_profile_id', '2022-02-15 00:12:05.622299'),
(8, 'accounts', '0006_profile_manager', '2022-02-15 00:12:06.887128'),
(9, 'accounts', '0007_alter_profile_manager', '2022-02-15 00:12:08.769425'),
(10, 'accounts', '0008_alter_profile_manager', '2022-02-15 00:12:11.488766'),
(11, 'accounts', '0009_auto_20220214_1504', '2022-02-15 00:12:13.149330'),
(12, 'admin', '0001_initial', '2022-02-15 00:12:14.168669'),
(13, 'admin', '0002_logentry_remove_auto_add', '2022-02-15 00:12:16.378331'),
(14, 'admin', '0003_logentry_add_action_flag_choices', '2022-02-15 00:12:16.424410'),
(15, 'contenttypes', '0002_remove_content_type_name', '2022-02-15 00:12:17.968680'),
(16, 'auth', '0002_alter_permission_name_max_length', '2022-02-15 00:12:18.905380'),
(17, 'auth', '0003_alter_user_email_max_length', '2022-02-15 00:12:19.824158'),
(18, 'auth', '0004_alter_user_username_opts', '2022-02-15 00:12:19.891137'),
(19, 'auth', '0005_alter_user_last_login_null', '2022-02-15 00:12:20.644275'),
(20, 'auth', '0006_require_contenttypes_0002', '2022-02-15 00:12:20.681808'),
(21, 'auth', '0007_alter_validators_add_error_messages', '2022-02-15 00:12:20.739769'),
(22, 'auth', '0008_alter_user_username_max_length', '2022-02-15 00:12:21.680474'),
(23, 'auth', '0009_alter_user_last_name_max_length', '2022-02-15 00:12:22.676162'),
(24, 'auth', '0010_alter_group_name_max_length', '2022-02-15 00:12:24.605283'),
(25, 'auth', '0011_update_proxy_permissions', '2022-02-15 00:12:24.664875'),
(26, 'chat', '0001_initial', '2022-02-15 00:12:25.183194'),
(27, 'chat', '0002_message_message', '2022-02-15 00:12:27.876622'),
(28, 'chat', '0003_alter_message_options', '2022-02-15 00:12:27.941038'),
(29, 'chat', '0004_auto_20220214_1504', '2022-02-15 00:12:28.822361'),
(30, 'sessions', '0001_initial', '2022-02-15 00:12:29.315257'),
(31, 'stock', '0001_initial', '2022-02-15 00:12:33.826835'),
(32, 'stock', '0002_auto_20210827_2151', '2022-02-15 00:12:50.735344'),
(33, 'stock', '0003_auto_20210827_2221', '2022-02-15 00:12:58.312593'),
(34, 'stock', '0002_auto_20210827_1520', '2022-02-15 00:13:00.615521'),
(35, 'stock', '0004_merge_0002_auto_20210827_1520_0003_auto_20210827_2221', '2022-02-15 00:13:00.675476'),
(36, 'stock', '0005_auto_20210827_2229', '2022-02-15 00:13:02.719316'),
(37, 'stock', '0006_auto_20210827_2233', '2022-02-15 00:13:04.305819'),
(38, 'stock', '0007_categorie_user', '2022-02-15 00:13:04.902009'),
(39, 'stock', '0008_auto_20210828_1202', '2022-02-15 00:13:06.624623'),
(40, 'stock', '0009_article_statut', '2022-02-15 00:13:08.520508'),
(41, 'stock', '0010_alter_article_statut', '2022-02-15 00:13:08.600743'),
(42, 'stock', '0011_alter_article_statut', '2022-02-15 00:13:08.649269');

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('227ukhs8jj5s89187f5clbr1kdkttqtk', 'ZmFmODJmNmYyOTgyZmY1YjU5ZmY5NWNhYWQ1Mjc5OGIyNGQxMjcwMDp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwNjEzYTdiOWQwNzkyODllY2JmYjY3NmY5NTM4ZDhiM2VhZGI1MjkxIn0=', '2022-03-01 00:43:51.826880'),
('iy433ias14f0nfa5knqf7cmkj55lw8jy', 'MTFlMDllNDFkNTc0ZjVkNzZlOTI3ZWUxMDgxMjYyOTU5OGZhNzcyMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmZThmZDQ1YzgwNmJjOGMxNjRjYTViODQ4Y2EyMmY1ZTk1OWEwYzNiIn0=', '2022-03-01 00:28:34.919254');

-- --------------------------------------------------------

--
-- Structure de la table `stock_article`
--

CREATE TABLE IF NOT EXISTS `stock_article` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `numero` int(11) NOT NULL,
  `nom` varchar(20) NOT NULL,
  `categorie_id` bigint(20) NOT NULL,
  `quantity` int(11) DEFAULT NULL,
  `date_entree` date DEFAULT NULL,
  `prix_achat` int(11) DEFAULT NULL,
  `statut` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `stock_article_categorie_id_a4fef38e_fk_stock_categorie_id` (`categorie_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `stock_categorie`
--

CREATE TABLE IF NOT EXISTS `stock_categorie` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `categorie` varchar(20) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `stock_categorie_user_id_87bfb1b8_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `stock_commande`
--

CREATE TABLE IF NOT EXISTS `stock_commande` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stock_commande_user_id_d8ba806b_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `stock_entrer`
--

CREATE TABLE IF NOT EXISTS `stock_entrer` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `qte` int(11) NOT NULL,
  `prix_entree` int(11) NOT NULL,
  `date_entree` date NOT NULL,
  `article_id` bigint(20) NOT NULL,
  `stock_id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stock_entrer_article_id_330cc620_fk_stock_article_id` (`article_id`),
  KEY `stock_entrer_stock_id_9cf83725_fk_stock_stock_id` (`stock_id`),
  KEY `stock_entrer_user_id_87cb76aa_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `stock_facture`
--

CREATE TABLE IF NOT EXISTS `stock_facture` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `dateFacture` date NOT NULL,
  `qte` int(11) NOT NULL,
  `User_id` int(11) NOT NULL,
  `article_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stock_facture_User_id_10723e3f_fk_auth_user_id` (`User_id`),
  KEY `stock_facture_article_id_627f585b_fk_stock_article_id` (`article_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `stock_panier`
--

CREATE TABLE IF NOT EXISTS `stock_panier` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `qte` int(11) NOT NULL,
  `article_id` bigint(20) NOT NULL,
  `commande_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stock_panier_article_id_b2464f8f_fk_stock_article_id` (`article_id`),
  KEY `stock_panier_commande_id_b6f54eda_fk_stock_commande_id` (`commande_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `stock_sortir`
--

CREATE TABLE IF NOT EXISTS `stock_sortir` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `qte` int(11) NOT NULL,
  `prix_sortie` int(11) NOT NULL,
  `date_sortie` date NOT NULL,
  `article_id` bigint(20) NOT NULL,
  `stock_id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stock_sortir_article_id_81c4a177_fk_stock_article_id` (`article_id`),
  KEY `stock_sortir_stock_id_60090be2_fk_stock_stock_id` (`stock_id`),
  KEY `stock_sortir_user_id_422d4636_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `stock_stock`
--

CREATE TABLE IF NOT EXISTS `stock_stock` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `qtStock` int(11) NOT NULL,
  `categorie_id` bigint(20) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `stock_stock_categorie_id_efdeb464_fk_stock_categorie_id` (`categorie_id`),
  KEY `stock_stock_user_id_92e04fd3_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `stock_stock_article`
--

CREATE TABLE IF NOT EXISTS `stock_stock_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stock_id` bigint(20) NOT NULL,
  `article_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `stock_stock_article_stock_id_article_id_b2e55038_uniq` (`stock_id`,`article_id`),
  KEY `stock_stock_article_article_id_df80c323_fk_stock_article_id` (`article_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `accounts_profile`
--
ALTER TABLE `accounts_profile`
  ADD CONSTRAINT `accounts_profile_user_id_49a85d32_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Contraintes pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Contraintes pour la table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `chat_message`
--
ALTER TABLE `chat_message`
  ADD CONSTRAINT `chat_message_receiver_id_0eceddde_fk_auth_user_id` FOREIGN KEY (`receiver_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `chat_message_sender_id_991c686c_fk_auth_user_id` FOREIGN KEY (`sender_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Contraintes pour la table `stock_article`
--
ALTER TABLE `stock_article`
  ADD CONSTRAINT `stock_article_categorie_id_a4fef38e_fk_stock_categorie_id` FOREIGN KEY (`categorie_id`) REFERENCES `stock_categorie` (`id`);

--
-- Contraintes pour la table `stock_categorie`
--
ALTER TABLE `stock_categorie`
  ADD CONSTRAINT `stock_categorie_user_id_87bfb1b8_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `stock_commande`
--
ALTER TABLE `stock_commande`
  ADD CONSTRAINT `stock_commande_user_id_d8ba806b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `stock_entrer`
--
ALTER TABLE `stock_entrer`
  ADD CONSTRAINT `stock_entrer_user_id_87cb76aa_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `stock_entrer_article_id_330cc620_fk_stock_article_id` FOREIGN KEY (`article_id`) REFERENCES `stock_article` (`id`),
  ADD CONSTRAINT `stock_entrer_stock_id_9cf83725_fk_stock_stock_id` FOREIGN KEY (`stock_id`) REFERENCES `stock_stock` (`id`);

--
-- Contraintes pour la table `stock_facture`
--
ALTER TABLE `stock_facture`
  ADD CONSTRAINT `stock_facture_article_id_627f585b_fk_stock_article_id` FOREIGN KEY (`article_id`) REFERENCES `stock_article` (`id`),
  ADD CONSTRAINT `stock_facture_User_id_10723e3f_fk_auth_user_id` FOREIGN KEY (`User_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `stock_panier`
--
ALTER TABLE `stock_panier`
  ADD CONSTRAINT `stock_panier_commande_id_b6f54eda_fk_stock_commande_id` FOREIGN KEY (`commande_id`) REFERENCES `stock_commande` (`id`),
  ADD CONSTRAINT `stock_panier_article_id_b2464f8f_fk_stock_article_id` FOREIGN KEY (`article_id`) REFERENCES `stock_article` (`id`);

--
-- Contraintes pour la table `stock_sortir`
--
ALTER TABLE `stock_sortir`
  ADD CONSTRAINT `stock_sortir_user_id_422d4636_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `stock_sortir_article_id_81c4a177_fk_stock_article_id` FOREIGN KEY (`article_id`) REFERENCES `stock_article` (`id`),
  ADD CONSTRAINT `stock_sortir_stock_id_60090be2_fk_stock_stock_id` FOREIGN KEY (`stock_id`) REFERENCES `stock_stock` (`id`);

--
-- Contraintes pour la table `stock_stock`
--
ALTER TABLE `stock_stock`
  ADD CONSTRAINT `stock_stock_user_id_92e04fd3_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `stock_stock_article`
--
ALTER TABLE `stock_stock_article`
  ADD CONSTRAINT `stock_stock_article_article_id_df80c323_fk_stock_article_id` FOREIGN KEY (`article_id`) REFERENCES `stock_article` (`id`),
  ADD CONSTRAINT `stock_stock_article_stock_id_79f23860_fk_stock_stock_id` FOREIGN KEY (`stock_id`) REFERENCES `stock_stock` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
