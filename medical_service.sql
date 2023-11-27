# HeidiSQL Dump 
#
# --------------------------------------------------------
# Host:                 127.0.0.1
# Database:             medical_service
# Server version:       5.4.3-beta-community
# Server OS:            Win32
# Target-Compatibility: Standard ANSI SQL
# HeidiSQL version:     3.1 RC1 Revision: 1064
# --------------------------------------------------------

/*!40100 SET CHARACTER SET latin1;*/
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ANSI';*/
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;*/


#
# Database structure for database 'medical_service'
#

CREATE DATABASE /*!32312 IF NOT EXISTS*/ "medical_service" /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_bin */;

USE "medical_service";


#
# Table structure for table 'approval'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "approval" (
  "id" varchar(50) DEFAULT NULL,
  "rid" varchar(50) DEFAULT NULL,
  "pname" varchar(50) DEFAULT NULL,
  "bgroup" varchar(50) DEFAULT NULL,
  "disease" varchar(50) DEFAULT NULL,
  "hname" varchar(50) DEFAULT NULL,
  "address" varchar(50) DEFAULT NULL,
  "Dname" varchar(50) DEFAULT NULL,
  "file" varchar(50) DEFAULT NULL
) /*!40100 DEFAULT CHARSET=latin1*/;



#
# Dumping data for table 'approval'
#

/*!40000 ALTER TABLE "approval" DISABLE KEYS;*/
LOCK TABLES "approval" WRITE;
REPLACE INTO "approval" ("id", "rid", "pname", "bgroup", "disease", "hname", "address", "Dname", "file") VALUES
	('gf','gdfg','dfgdf','dfg','dfgdf','gdfg','dfgdf','gdfg','c6.jpg');
UNLOCK TABLES;
/*!40000 ALTER TABLE "approval" ENABLE KEYS;*/


#
# Table structure for table 'donor'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "donor" (
  "id" varchar(50) DEFAULT NULL,
  "pname" varchar(50) DEFAULT NULL,
  "amt" varchar(50) DEFAULT NULL,
  "puname" varchar(50) DEFAULT NULL,
  "file" varchar(50) DEFAULT NULL,
  "upid" varchar(50) DEFAULT NULL,
  "remarks" varchar(50) DEFAULT NULL
) /*!40100 DEFAULT CHARSET=latin1*/;



#
# Dumping data for table 'donor'
#

/*!40000 ALTER TABLE "donor" DISABLE KEYS;*/
LOCK TABLES "donor" WRITE;
REPLACE INTO "donor" ("id", "pname", "amt", "puname", "file", "upid", "remarks") VALUES
	('1','Priya','50000','dhana','1.jpg','malar12@ybi','welcome');
UNLOCK TABLES;
/*!40000 ALTER TABLE "donor" ENABLE KEYS;*/


#
# Table structure for table 'donorregistration'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "donorregistration" (
  "name" varchar(50) DEFAULT NULL,
  "Email" varchar(50) DEFAULT NULL,
  "contact" varchar(50) DEFAULT NULL,
  "Address" varchar(50) DEFAULT NULL,
  "Username" varchar(50) DEFAULT NULL,
  "Password" varchar(50) DEFAULT NULL
) /*!40100 DEFAULT CHARSET=latin1*/;



#
# Dumping data for table 'donorregistration'
#

/*!40000 ALTER TABLE "donorregistration" DISABLE KEYS;*/
LOCK TABLES "donorregistration" WRITE;
REPLACE INTO "donorregistration" ("name", "Email", "contact", "Address", "Username", "Password") VALUES
	('priya','dhnajay15@gmail.com','97887888','cbe','001','priya');
UNLOCK TABLES;
/*!40000 ALTER TABLE "donorregistration" ENABLE KEYS;*/


#
# Table structure for table 'fund'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "fund" (
  "id" int(50) NOT NULL,
  "name" varchar(50) DEFAULT NULL,
  "patientid" varchar(50) DEFAULT NULL,
  "amt" varchar(50) DEFAULT NULL,
  "regid" varchar(50) DEFAULT NULL,
  "disease" varchar(50) DEFAULT NULL,
  "hname" varchar(50) DEFAULT NULL,
  "Priority" varchar(50) DEFAULT NULL,
  "proof" varchar(50) DEFAULT NULL,
  "proof2" varchar(50) DEFAULT NULL,
  "upi" varchar(50) DEFAULT NULL,
  "statusinfo" varchar(50) DEFAULT NULL,
  PRIMARY KEY ("id")
) /*!40100 DEFAULT CHARSET=latin1*/;



#
# Dumping data for table 'fund'
#

/*!40000 ALTER TABLE "fund" DISABLE KEYS;*/
LOCK TABLES "fund" WRITE;
REPLACE INTO "fund" ("id", "name", "patientid", "amt", "regid", "disease", "hname", "Priority", "proof", "proof2", "upi", "statusinfo") VALUES
	(1,'Priya',NULL,'50000','priya','Cancer','kmch','High','7.jpg','7.jpg','malar12@ybi','Approved');
UNLOCK TABLES;
/*!40000 ALTER TABLE "fund" ENABLE KEYS;*/


#
# Table structure for table 'registration'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "registration" (
  "name" varchar(50) DEFAULT NULL,
  "Email" varchar(50) DEFAULT NULL,
  "contact" varchar(50) DEFAULT NULL,
  "Address" varchar(50) DEFAULT NULL,
  "Username" varchar(50) DEFAULT NULL,
  "Password" varchar(50) DEFAULT NULL
) /*!40100 DEFAULT CHARSET=latin1*/;



#
# Dumping data for table 'registration'
#

/*!40000 ALTER TABLE "registration" DISABLE KEYS;*/
LOCK TABLES "registration" WRITE;
REPLACE INTO "registration" ("name", "Email", "contact", "Address", "Username", "Password") VALUES
	('Priya','dhnajay15@gmail.com','','cbe','priya','priya12');
UNLOCK TABLES;
/*!40000 ALTER TABLE "registration" ENABLE KEYS;*/
/*!40101 SET SQL_MODE=@OLD_SQL_MODE;*/
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;*/
