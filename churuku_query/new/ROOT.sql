
CREATE TABLE `root_denglu`(
`yonghuming` varchar(20) NOT NULL,
`mima` varchar(80) NOT NULL,
PRIMARY KEY(`yonghuming`)
);

INSERT INTO root_denglu (yonghuming,mima) VALUES('root',123);

SELECT * FROM root_denglu;