CREATE USER 'test'@'192.168.43.180' IDENTIFIED BY '123456';

GRANT ALL PRIVILEGES ON *.* TO "test"@"192.168.43.180" IDENTIFIED BY "123456" WITH GRANT OPTION;
grant replication slave,reload,create user, super on *.* to 'test'@'192.168.43.180' IDENTIFIED BY '123456';  //  机器A上执行
grant replication slave,reload,create user, super on *.* to 'test'@'10.0.9.199' IDENTIFIED BY '123456';  // 机器B上执行

mysql> change master to
     master_host = '192.168.43.44',
     master_port = 3306,
     master_user = 'test',
     master_password = '123456';  //机器A上执行，A为slave
mysql> change master to
    -> master_host = '10.0.9.199',
    -> master_port = 3306,
    -> master_user = 'test',
    -> master_password = '123456'; //机器B上执行，B为slave
    
    mysql -h 192.168.43.180 -u test -p -P 3306