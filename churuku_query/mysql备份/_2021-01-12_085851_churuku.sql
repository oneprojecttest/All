/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


CREATE DATABASE /*!32312 IF NOT EXISTS*/ `churuku` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `churuku`;
DROP TABLE IF EXISTS `cailiao`;
CREATE TABLE `cailiao` (
  `id` varchar(30) NOT NULL,
  `name` varchar(40) DEFAULT NULL,
  `guige` varchar(20) DEFAULT NULL,
  `danwei` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `chuku`;
CREATE TABLE `chuku` (
  `id` varchar(30) NOT NULL,
  `time` datetime DEFAULT NULL,
  `cailiao_id` varchar(30) DEFAULT NULL,
  `shuliang` int DEFAULT NULL,
  `fuzeren_name` varchar(10) DEFAULT NULL,
  `yongtu` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cailiao_id` (`cailiao_id`),
  KEY `fuzeren_name` (`fuzeren_name`),
  CONSTRAINT `chuku_ibfk_1` FOREIGN KEY (`cailiao_id`) REFERENCES `cailiao` (`id`),
  CONSTRAINT `chuku_ibfk_2` FOREIGN KEY (`fuzeren_name`) REFERENCES `fuzeren` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `denglu`;
CREATE TABLE `denglu` (
  `yonghuming` varchar(20) NOT NULL,
  `mima` varchar(80) NOT NULL,
  PRIMARY KEY (`yonghuming`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `denglu_record`;
CREATE TABLE `denglu_record` (
  `time` datetime NOT NULL,
  `yonghuming` varchar(20) NOT NULL,
  `status` varchar(5) NOT NULL,
  PRIMARY KEY (`time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `fuzeren`;
CREATE TABLE `fuzeren` (
  `name` varchar(10) NOT NULL,
  `dianhua` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `fuzhang`;
CREATE TABLE `fuzhang` (
  `id` varchar(30) NOT NULL,
  `time` datetime DEFAULT NULL,
  `gonghuodanwei_id` varchar(30) DEFAULT NULL,
  `fuzhang` float(15,2) DEFAULT NULL,
  `fangshi` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `gonghuodanwei_id` (`gonghuodanwei_id`),
  CONSTRAINT `fuzhang_ibfk_1` FOREIGN KEY (`gonghuodanwei_id`) REFERENCES `gonghuodanwei` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `gonghuodanwei`;
CREATE TABLE `gonghuodanwei` (
  `id` varchar(30) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `lianxiren` varchar(10) DEFAULT NULL,
  `dianhua` varchar(20) DEFAULT NULL,
  `dizhi` varchar(50) DEFAULT NULL,
  `isoid` varchar(20) DEFAULT NULL,
  `hege` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `kucun`;
CREATE TABLE `kucun` (
  `cailiao_id` varchar(30) NOT NULL,
  `shuliang` int DEFAULT NULL,
  KEY `cailiao_id` (`cailiao_id`),
  CONSTRAINT `kucun_ibfk_1` FOREIGN KEY (`cailiao_id`) REFERENCES `cailiao` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `root_denglu`;
CREATE TABLE `root_denglu` (
  `yonghuming` varchar(20) NOT NULL,
  `mima` varchar(80) NOT NULL,
  PRIMARY KEY (`yonghuming`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `ruku`;
CREATE TABLE `ruku` (
  `id` varchar(30) NOT NULL,
  `time` datetime DEFAULT NULL,
  `cailiao_id` varchar(30) DEFAULT NULL,
  `shuliang` int DEFAULT NULL,
  `danjia` float(15,2) DEFAULT NULL,
  `jine` float(15,2) DEFAULT NULL,
  `fuzeren_name` varchar(10) DEFAULT NULL,
  `gonghuodanwei_id` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cailiao_id` (`cailiao_id`),
  KEY `fuzeren_name` (`fuzeren_name`),
  KEY `gonghuodanwei_id` (`gonghuodanwei_id`),
  CONSTRAINT `ruku_ibfk_1` FOREIGN KEY (`cailiao_id`) REFERENCES `cailiao` (`id`),
  CONSTRAINT `ruku_ibfk_2` FOREIGN KEY (`fuzeren_name`) REFERENCES `fuzeren` (`name`),
  CONSTRAINT `ruku_ibfk_3` FOREIGN KEY (`gonghuodanwei_id`) REFERENCES `gonghuodanwei` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `weifu`;
CREATE TABLE `weifu` (
  `gonghuodanwei_id` varchar(30) NOT NULL,
  `jine` float(15,2) DEFAULT NULL,
  `yifu` float(15,2) DEFAULT NULL,
  `weifu` float(15,2) DEFAULT NULL,
  KEY `gonghuodanwei_id` (`gonghuodanwei_id`),
  CONSTRAINT `weifu_ibfk_1` FOREIGN KEY (`gonghuodanwei_id`) REFERENCES `gonghuodanwei` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `cailiao` (`id`,`name`,`guige`,`danwei`) VALUES ('123','123','123','1321'),('234','2432','2432','2432'),('tycyjv','iopjhpokj','iojopkl','klp');


INSERT INTO `denglu` (`yonghuming`,`mima`) VALUES ('czq','202cb962ac59075b964b07152d234b70'),('xyy','202cb962ac59075b964b07152d234b70');

INSERT INTO `denglu_record` (`time`,`yonghuming`,`status`) VALUES ('2021-01-05 15:50:01','xyy','成功'),('2021-01-05 15:59:41','xyy','成功'),('2021-01-05 16:03:30','xyy','成功'),('2021-01-09 18:19:07','xyy','失败'),('2021-01-09 18:19:11','xyy','成功'),('2021-01-09 18:22:08','xyy','成功'),('2021-01-10 19:39:25','xyy','成功'),('2021-01-10 19:56:09','xyy','成功'),('2021-01-11 11:44:30','xyy','成功'),('2021-01-11 11:54:51','xyy','成功'),('2021-01-11 11:56:46','xyy','成功'),('2021-01-11 11:58:26','xyy','成功'),('2021-01-11 12:01:44','root','成功'),('2021-01-11 12:03:01','root','成功'),('2021-01-11 12:06:35','czq','成功'),('2021-01-11 12:09:43','czq','成功'),('2021-01-11 12:10:26','czq','成功'),('2021-01-11 12:21:09','czq','成功'),('2021-01-11 12:26:57','root','成功');

INSERT INTO `fuzeren` (`name`,`dianhua`) VALUES ('xyy','1234545q23');


INSERT INTO `gonghuodanwei` (`id`,`name`,`lianxiren`,`dianhua`,`dizhi`,`isoid`,`hege`) VALUES ('0001','123','123123','12313','13123','312313','是'),('0002','123232','123123','12313','1312332131','3123132131','是');

INSERT INTO `kucun` (`cailiao_id`,`shuliang`) VALUES ('123',0),('234',0),('tycyjv',0);

INSERT INTO `root_denglu` (`yonghuming`,`mima`) VALUES ('root','123');


INSERT INTO `weifu` (`gonghuodanwei_id`,`jine`,`yifu`,`weifu`) VALUES ('0001',0.00,0.00,0.00),('0002',0.00,0.00,0.00);

/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
