-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: dados_eventos
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `dados_eventos`
--

DROP TABLE IF EXISTS `dados_eventos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dados_eventos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `evento` varchar(100) NOT NULL,
  `data_evento` date NOT NULL,
  `horário` time(6) NOT NULL,
  `local` varchar(50) NOT NULL,
  `entrada` varchar(50) NOT NULL,
  `quantidade_de_ingressos` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `dados_eventos_chk_1` CHECK ((`quantidade_de_ingressos` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dados_eventos`
--

LOCK TABLES `dados_eventos` WRITE;
/*!40000 ALTER TABLE `dados_eventos` DISABLE KEYS */;
INSERT INTO `dados_eventos` VALUES (1,'SHOW','2024-08-29','00:44:00.000000','AVENIDA_OSMAR_BASTOS','INTEIRA',3),(2,'SHOW','2024-08-26','01:47:00.000000','AVENIDA_OSMAR_BASTOS','GRATUITA',4),(3,'PAGODE','2024-08-25','01:57:00.000000','PRAÇA_DO_JAURO','GRATUITA',4),(4,'RODEIO','2024-09-02','08:12:00.000000','LOTEAMENTO_ALTA_VISTA','MEIA',1);
/*!40000 ALTER TABLE `dados_eventos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-14 21:19:47
