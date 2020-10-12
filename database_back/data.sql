-- MySQL dump 10.16  Distrib 10.1.26-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	10.1.26-MariaDB-0+deb9u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` varchar(0) DEFAULT NULL,
  `name` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` varchar(0) DEFAULT NULL,
  `group_id` varchar(0) DEFAULT NULL,
  `permission_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` tinyint(4) DEFAULT NULL,
  `content_type_id` tinyint(4) DEFAULT NULL,
  `codename` varchar(18) DEFAULT NULL,
  `name` varchar(23) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,1,'add_logentry','Can add log entry'),(2,1,'change_logentry','Can change log entry'),(3,1,'delete_logentry','Can delete log entry'),(4,1,'view_logentry','Can view log entry'),(5,2,'add_permission','Can add permission'),(6,2,'change_permission','Can change permission'),(7,2,'delete_permission','Can delete permission'),(8,2,'view_permission','Can view permission'),(9,3,'add_group','Can add group'),(10,3,'change_group','Can change group'),(11,3,'delete_group','Can delete group'),(12,3,'view_group','Can view group'),(13,4,'add_user','Can add user'),(14,4,'change_user','Can change user'),(15,4,'delete_user','Can delete user'),(16,4,'view_user','Can view user'),(17,5,'add_contenttype','Can add content type'),(18,5,'change_contenttype','Can change content type'),(19,5,'delete_contenttype','Can delete content type'),(20,5,'view_contenttype','Can view content type'),(21,6,'add_session','Can add session'),(22,6,'change_session','Can change session'),(23,6,'delete_session','Can delete session'),(24,6,'view_session','Can view session'),(25,7,'add_student','Can add student'),(26,7,'change_student','Can change student'),(27,7,'delete_student','Can delete student'),(28,7,'view_student','Can view student'),(29,8,'add_student','Can add student'),(30,8,'change_student','Can change student'),(31,8,'delete_student','Can delete student'),(32,8,'view_student','Can view student');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` tinyint(4) DEFAULT NULL,
  `password` varchar(78) DEFAULT NULL,
  `last_login` varchar(10) DEFAULT NULL,
  `is_superuser` tinyint(4) DEFAULT NULL,
  `username` varchar(5) DEFAULT NULL,
  `first_name` varchar(0) DEFAULT NULL,
  `email` varchar(23) DEFAULT NULL,
  `is_staff` tinyint(4) DEFAULT NULL,
  `is_active` tinyint(4) DEFAULT NULL,
  `date_joined` varchar(10) DEFAULT NULL,
  `last_name` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$180000$ZiiZaoFNkg8X$CG42aTxw7S7PQUVpQAG0Fd/rzdV4cFm72eCD9P7OeYI=','2020-10-06',1,'admin','','spriyanshu245@gmail.com',1,1,'2020-10-06','');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` varchar(0) DEFAULT NULL,
  `user_id` varchar(0) DEFAULT NULL,
  `group_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` varchar(0) DEFAULT NULL,
  `user_id` varchar(0) DEFAULT NULL,
  `permission_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department_student`
--

DROP TABLE IF EXISTS `department_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `department_student` (
  `id` tinyint(4) DEFAULT NULL,
  `name` varchar(15) DEFAULT NULL,
  `departments` varchar(16) DEFAULT NULL,
  `employer` varchar(7) DEFAULT NULL,
  `date` varchar(0) DEFAULT NULL,
  `package` mediumint(9) DEFAULT NULL,
  `ref_no` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department_student`
--

LOCK TABLES `department_student` WRITE;
/*!40000 ALTER TABLE `department_student` DISABLE KEYS */;
INSERT INTO `department_student` VALUES (1,'Priyanshu Singh','Computer Science','infosys','',600000,801),(3,'Priyanshu Singh','Mechanical','wipro','',70000,802);
/*!40000 ALTER TABLE `department_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` tinyint(4) DEFAULT NULL,
  `action_time` varchar(10) DEFAULT NULL,
  `object_id` tinyint(4) DEFAULT NULL,
  `object_repr` varchar(19) DEFAULT NULL,
  `change_message` varchar(0) DEFAULT NULL,
  `content_type_id` tinyint(4) DEFAULT NULL,
  `user_id` tinyint(4) DEFAULT NULL,
  `action_flag` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2020-10-06',44,'Student object (44)','',7,1,3),(2,'2020-10-06',43,'Student object (43)','',7,1,3),(3,'2020-10-06',42,'Student object (42)','',7,1,3),(4,'2020-10-06',41,'Student object (41)','',7,1,3),(5,'2020-10-06',40,'Student object (40)','',7,1,3),(6,'2020-10-06',39,'Student object (39)','',7,1,3),(7,'2020-10-06',38,'Student object (38)','',7,1,3),(8,'2020-10-06',37,'Student object (37)','',7,1,3),(9,'2020-10-06',36,'Student object (36)','',7,1,3),(10,'2020-10-06',35,'Student object (35)','',7,1,3),(11,'2020-10-06',34,'Student object (34)','',7,1,3),(12,'2020-10-06',33,'Student object (33)','',7,1,3),(13,'2020-10-06',32,'Student object (32)','',7,1,3),(14,'2020-10-06',31,'Student object (31)','',7,1,3),(15,'2020-10-06',30,'Student object (30)','',7,1,3),(16,'2020-10-06',29,'Student object (29)','',7,1,3),(17,'2020-10-06',28,'Student object (28)','',7,1,3),(18,'2020-10-06',27,'Student object (27)','',7,1,3),(19,'2020-10-06',26,'Student object (26)','',7,1,3),(20,'2020-10-06',25,'Student object (25)','',7,1,3),(21,'2020-10-06',24,'Student object (24)','',7,1,3),(22,'2020-10-06',23,'Student object (23)','',7,1,3),(23,'2020-10-06',22,'Student object (22)','',7,1,3),(24,'2020-10-06',21,'Student object (21)','',7,1,3),(25,'2020-10-06',20,'Student object (20)','',7,1,3),(26,'2020-10-06',19,'Student object (19)','',7,1,3),(27,'2020-10-06',18,'Student object (18)','',7,1,3),(28,'2020-10-06',17,'Student object (17)','',7,1,3),(29,'2020-10-06',16,'Student object (16)','',7,1,3),(30,'2020-10-06',15,'Student object (15)','',7,1,3),(31,'2020-10-06',14,'Student object (14)','',7,1,3),(32,'2020-10-06',13,'Student object (13)','',7,1,3),(33,'2020-10-06',12,'Student object (12)','',7,1,3),(34,'2020-10-06',11,'Student object (11)','',7,1,3),(35,'2020-10-06',10,'Student object (10)','',7,1,3),(36,'2020-10-06',9,'Student object (9)','',7,1,3),(37,'2020-10-06',8,'Student object (8)','',7,1,3),(38,'2020-10-06',7,'Student object (7)','',7,1,3),(39,'2020-10-06',6,'Student object (6)','',7,1,3),(40,'2020-10-06',5,'Student object (5)','',7,1,3),(41,'2020-10-06',4,'Student object (4)','',7,1,3),(42,'2020-10-06',3,'Student object (3)','',7,1,3),(43,'2020-10-06',2,'Student object (2)','',7,1,3),(44,'2020-10-06',1,'Student object (1)','',7,1,3),(45,'2020-10-06',64,'Student object (64)','',7,1,3),(46,'2020-10-06',63,'Student object (63)','',7,1,3),(47,'2020-10-06',62,'Student object (62)','',7,1,3),(48,'2020-10-06',61,'Student object (61)','',7,1,3),(49,'2020-10-06',60,'Student object (60)','',7,1,3),(50,'2020-10-06',59,'Student object (59)','',7,1,3),(51,'2020-10-06',58,'Student object (58)','',7,1,3),(52,'2020-10-06',57,'Student object (57)','',7,1,3),(53,'2020-10-06',56,'Student object (56)','',7,1,3),(54,'2020-10-06',55,'Student object (55)','',7,1,3),(55,'2020-10-06',54,'Student object (54)','',7,1,3),(56,'2020-10-06',53,'Student object (53)','',7,1,3),(57,'2020-10-06',52,'Student object (52)','',7,1,3),(58,'2020-10-06',51,'Student object (51)','',7,1,3),(59,'2020-10-06',50,'Student object (50)','',7,1,3),(60,'2020-10-06',49,'Student object (49)','',7,1,3),(61,'2020-10-06',48,'Student object (48)','',7,1,3),(62,'2020-10-06',47,'Student object (47)','',7,1,3),(63,'2020-10-06',46,'Student object (46)','',7,1,3),(64,'2020-10-06',45,'Student object (45)','',7,1,3);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` tinyint(4) DEFAULT NULL,
  `app_label` varchar(12) DEFAULT NULL,
  `model` varchar(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(8,'department','student'),(7,'placement','student'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` tinyint(4) DEFAULT NULL,
  `app` varchar(12) DEFAULT NULL,
  `name` varchar(40) DEFAULT NULL,
  `applied` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-10-06'),(2,'auth','0001_initial','2020-10-06'),(3,'admin','0001_initial','2020-10-06'),(4,'admin','0002_logentry_remove_auto_add','2020-10-06'),(5,'admin','0003_logentry_add_action_flag_choices','2020-10-06'),(6,'contenttypes','0002_remove_content_type_name','2020-10-06'),(7,'auth','0002_alter_permission_name_max_length','2020-10-06'),(8,'auth','0003_alter_user_email_max_length','2020-10-06'),(9,'auth','0004_alter_user_username_opts','2020-10-06'),(10,'auth','0005_alter_user_last_login_null','2020-10-06'),(11,'auth','0006_require_contenttypes_0002','2020-10-06'),(12,'auth','0007_alter_validators_add_error_messages','2020-10-06'),(13,'auth','0008_alter_user_username_max_length','2020-10-06'),(14,'auth','0009_alter_user_last_name_max_length','2020-10-06'),(15,'auth','0010_alter_group_name_max_length','2020-10-06'),(16,'auth','0011_update_proxy_permissions','2020-10-06'),(17,'placement','0001_initial','2020-10-06'),(18,'sessions','0001_initial','2020-10-06'),(19,'placement','0002_auto_20201006_2251','2020-10-06'),(20,'placement','0003_auto_20201006_2339','2020-10-06'),(21,'placement','0004_auto_20201009_0042','2020-10-08'),(22,'placement','0005_auto_20201009_0043','2020-10-08');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(32) DEFAULT NULL,
  `session_data` varchar(252) DEFAULT NULL,
  `expire_date` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('8kio8950ajm9s6vkss3a024i9qmazect','ZWJhNWMxNzA5MjUxNDI1NmRmNTNmY2Y5YWM4MWVjMmVhMGI3Yzc1ZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyOGJhOTUxMzMxZDA4ZmFlN2I2MDRiNmZiYjc1ZmI2NjZkMTFkYzhiIn0=','2020-10-20');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `placement_student`
--

DROP TABLE IF EXISTS `placement_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `placement_student` (
  `id` tinyint(4) DEFAULT NULL,
  `name` varchar(15) DEFAULT NULL,
  `employer` varchar(7) DEFAULT NULL,
  `date` varchar(0) DEFAULT NULL,
  `package` mediumint(9) DEFAULT NULL,
  `ref_no` smallint(6) DEFAULT NULL,
  `department` varchar(33) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `placement_student`
--

LOCK TABLES `placement_student` WRITE;
/*!40000 ALTER TABLE `placement_student` DISABLE KEYS */;
INSERT INTO `placement_student` VALUES (86,'Priyanshu Singh','infosys','',600000,801,'Mechanical'),(87,'Priyanshu Singh','wipro','',700000,802,'Computer Science'),(88,'Priyanshu Singh','wipro','',600000,803,'Electronics and Telecommunication');
/*!40000 ALTER TABLE `placement_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sqlite_sequence`
--

DROP TABLE IF EXISTS `sqlite_sequence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sqlite_sequence` (
  `name` varchar(19) DEFAULT NULL,
  `seq` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sqlite_sequence`
--

LOCK TABLES `sqlite_sequence` WRITE;
/*!40000 ALTER TABLE `sqlite_sequence` DISABLE KEYS */;
INSERT INTO `sqlite_sequence` VALUES ('django_migrations',22),('django_admin_log',64),('django_content_type',8),('auth_permission',32),('auth_user',1),('auth_group',0),('placement_student',88),('department_student',3);
/*!40000 ALTER TABLE `sqlite_sequence` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-22 15:20:27
