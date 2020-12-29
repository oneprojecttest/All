DROP DATABASE churuku;

CREATE DATABASE churuku;

USE churuku;

CREATE TABLE `cailiao` (
  `id` varchar(30) NOT NULL,
  `name` varchar(40) DEFAULT NULL,
  `guige` varchar(20) DEFAULT NULL,
  `danwei` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `gonghuodanwei` (
  `id` varchar(30) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `lianxiren` varchar(10) DEFAULT NULL,
  `dianhua` varchar(20) DEFAULT NULL,
  `dizhi` varchar(50) DEFAULT NULL,
  `isoid` varchar(20) DEFAULT NULL,
  `hege` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `fuzeren` (
  `name` varchar(10) NOT NULL,
  `dianhua` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`name`)
);

CREATE TABLE `ruku` (
  `id` varchar(30) NOT NULL,
  `time` datetime,
  `cailiao_id` varchar(30) DEFAULT NULL,
  `shuliang` int(20) DEFAULT NULL,
  `danjia` float(15,2) DEFAULT NULL,
  `jine` float(15,2) DEFAULT NULL,
  `fuzeren_name` varchar(10) DEFAULT NULL,
  `gonghuodanwei_id` varchar(30) DEFAULT NULL,
  FOREIGN KEY (`cailiao_id`) REFERENCES `cailiao`(`id`),
  FOREIGN KEY (`fuzeren_name`) REFERENCES `fuzeren`(`name`),
  FOREIGN KEY (`gonghuodanwei_id`) REFERENCES `gonghuodanwei`(`id`),
  PRIMARY KEY (`id`)
);

CREATE TABLE `chuku` (
  `id` varchar(30) NOT NULL,
  `time` datetime,
  `cailiao_id` varchar(30) DEFAULT NULL,
  `shuliang` int(20) DEFAULT NULL,
  `fuzeren_name` varchar(10) DEFAULT NULL,
  `yongtu` varchar(50) DEFAULT NULL,
  FOREIGN KEY (`cailiao_id`) REFERENCES `cailiao`(`id`),
  FOREIGN KEY (`fuzeren_name`) REFERENCES `fuzeren`(`name`),
  PRIMARY KEY (`id`)
);

CREATE TABLE `fuzhang` (
  `id` varchar(30) NOT NULL,
  `time` datetime,
  `gonghuodanwei_id` varchar(30) DEFAULT NULL,
  `fuzhang` float(15,2) DEFAULT NULL,
  `fangshi` varchar(10) DEFAULT NULL,
  FOREIGN KEY (`gonghuodanwei_id`) REFERENCES `gonghuodanwei`(`id`),
  PRIMARY KEY (`id`)
);

CREATE TABLE `kucun` (
  `cailiao_id` varchar(30) NOT NULL,
  `shuliang` int(20) DEFAULT NULL,
  FOREIGN KEY (`cailiao_id`) REFERENCES `cailiao`(`id`)
);

CREATE TABLE `weifu` (
  `gonghuodanwei_id` varchar(30) NOT NULL,
  `jine` float(15,2) DEFAULT NULL,
  `yifu` float(15,2) DEFAULT NULL,
  `weifu` float(15,2) DEFAULT NULL,
  FOREIGN KEY (`gonghuodanwei_id`) REFERENCES `gonghuodanwei`(`id`)
);

CREATE TABLE `denglu`(
`yonghuming` varchar(20) NOT NULL,
`mima` varchar(80) NOT NULL,
PRIMARY KEY(`yonghuming`)
);

CREATE TABLE `root_denglu`(
`yonghuming` varchar(20) NOT NULL,
`mima` varchar(80) NOT NULL,
PRIMARY KEY(`yonghuming`)
);

CREATE TABLE `denglu_record`(
`time` datetime NOT NULL,
`yonghuming` varchar(20) NOT NULL,
`status` varchar(5) NOT NULL,
PRIMARY KEY(`time`)
);

