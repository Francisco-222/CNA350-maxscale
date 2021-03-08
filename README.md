# MariaDB MaxScale Docker image

## Requirements

- [Any Linux OS (ubuntu)](https://ubuntu.com/download)
- [Docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04)
- [Docker-compose](https://docs.docker.com/compose/install/)


## Key Commands:
```
sudo apt install docker
sudo apt install docker-compose
sudo apt install mariadb-client-core-10.1


```
## Get Directory location 
```
cd CNA350-maxscale
cd maxscale
ls (This is to make sure that you are in the righ location with you own file such as, docker-compose.yml)
```
## Start image or modify
```

docker-compose ps or docker-compose ps -a
docker-compose up -d (start/show the containers up)
docker-compose down -v (down server)

```

## You can use mysql or MariaDB:
```

There are multiples way to loggin to your database. In this case I am using MariaDB with my own ports; Keep in mind try to verify you server port where you want to run you database, In this example I will use port 4006, You can verify you ports with the sudo docker ps -a. However, one hit is that you can also run mysql with port 3306

Database:
You can specify the limit as long as it is the range of lines in the zipcodes csv
```
```
mysql -umaxuser -pmaxpwd -h 127.0.0.1 -P 4006
SELECT * FROM zipcodes_one.zipcodes_one LIMIT 7;


+---------+-------------+----------+-------+--------------+-----------+------------+-------------------+---------------+-----------------+---------------------+------------+
| Zipcode | ZipCodeType | City     | State | LocationType | Coord_Lat | Coord_Long | Location          | Decommisioned | TaxReturnsFiled | EstimatedPopulation | TotalWages |
+---------+-------------+----------+-------+--------------+-----------+------------+-------------------+---------------+-----------------+---------------------+------------+
|     705 | STANDARD    | AIBONITO | PR    | PRIMARY      | 18.14     | -66.26     | NA-US-PR-AIBONITO | FALSE         |                 |                     |            |
|     610 | STANDARD    | ANASCO   | PR    | PRIMARY      | 18.28     | -67.14     | NA-US-PR-ANASCO   | FALSE         |                 |                     |            |
|     611 | PO BOX      | ANGELES  | PR    | PRIMARY      | 18.28     | -66.79     | NA-US-PR-ANGELES  | FALSE         |                 |                     |            |
|     612 | STANDARD    | ARECIBO  | PR    | PRIMARY      | 18.45     | -66.73     | NA-US-PR-ARECIBO  | FALSE         |                 |                     |            |
|     601 | STANDARD    | ADJUNTAS | PR    | PRIMARY      | 18.16     | -66.72     | NA-US-PR-ADJUNTAS | FALSE         |                 |                     |            |
|     631 | PO BOX      | CASTANER | PR    | PRIMARY      | 18.19     | -66.82     | NA-US-PR-CASTANER | FALSE         |                 |                     |            |
|     602 | STANDARD    | AGUADA   | PR    | PRIMARY      | 18.38     | -67.18     | NA-US-PR-AGUADA   | FALSE         |                 |                     |            |
+---------+-------------+----------+-------+--------------+-----------+------------+-------------------+---------------+-----------------+---------------------+------------+
7 rows in set (0.01 sec)

```
```
MariaDB [(none)]> SELECT *  FROM zipcodes_two.zipcodes_two LIMIT 5;
+---------+-------------+-------------+-------+--------------+-----------+------------+----------------------+---------------+-----------------+---------------------+------------+
| Zipcode | ZipCodeType | City        | State | LocationType | Coord_Lat | Coord_Long | Location             | Decommisioned | TaxReturnsFiled | EstimatedPopulation | TotalWages |
+---------+-------------+-------------+-------+--------------+-----------+------------+----------------------+---------------+-----------------+---------------------+------------+
|   42040 | STANDARD    | FARMINGTON  | KY    | PRIMARY      | 36.67     | -88.53     | NA-US-KY-FARMINGTON  | FALSE         | 465             | 896                 | 11562973   |
|   41524 | STANDARD    | FEDSCREEK   | KY    | PRIMARY      | 37.4      | -82.24     | NA-US-KY-FEDSCREEK   | FALSE         |                 |                     |            |
|   42533 | STANDARD    | FERGUSON    | KY    | PRIMARY      | 37.06     | -84.59     | NA-US-KY-FERGUSON    | FALSE         | 429             | 761                 | 9555412    |
|   40022 | STANDARD    | FINCHVILLE  | KY    | PRIMARY      | 38.15     | -85.31     | NA-US-KY-FINCHVILLE  | FALSE         | 437             | 839                 | 19909942   |
|   40023 | STANDARD    | FISHERVILLE | KY    | PRIMARY      | 38.16     | -85.42     | NA-US-KY-FISHERVILLE | FALSE         | 1884            | 3733                | 113020684  |
+---------+-------------+-------------+-------+--------------+-----------+------------+----------------------+---------------+-----------------+---------------------+------------+
5 rows in set (0.01 sec)

```
# Also you can query with python:
```
- If you want to query the zipcodes result you can use the file name "Query.py". 
- However; if you want to query with python you need go to the docker-compose.yml and replace the arbitrary for the specific port that you want to use also.
- For example in This case I am using port 4006.
```

# Issues with servers:
```
sudo docker-compose start master (You can specify you server name with the address name)
```
```
Before Shard-A and B 
sudo docker-compose exec maxscale maxctrl list servers
┌─────────┬─────────┬──────┬─────────────┬─────────────────┬──────────┐
│ Server  │ Address │ Port │ Connections │ State           │ GTID     │
├─────────┼─────────┼──────┼─────────────┼─────────────────┼──────────┤
│ server1 │ master  │ 3306 │ 0           │ Master, Running │ 0-3000-5 │
├─────────┼─────────┼──────┼─────────────┼─────────────────┼──────────┤
│ server2 │ slave1  │ 3306 │ 0           │ Slave, Running  │ 0-3000-5 │
├─────────┼─────────┼──────┼─────────────┼─────────────────┼──────────┤
│ server3 │ slave2  │ 3306 │ 0           │ Slave, Running  │ 0-3000-5 │
└─────────┴─────────┴──────┴─────────────┴─────────────────┴──────────┘

```
With Shard-A and B
```
┌─────────┬───────────┬──────┬─────────────┬─────────────────┬───────────┐
│ Server  │ Address   │ Port │ Connections │ State           │ GTID      │
├─────────┼───────────┼──────┼─────────────┼─────────────────┼───────────┤
│ server1 │ master    │ 3306 │ 0           │ Master, Running │ 0-3000-32 │
├─────────┼───────────┼──────┼─────────────┼─────────────────┼───────────┤
│ server2 │ slave1    │ 3306 │ 0           │ Slave, Running  │ 0-3000-32 │
├─────────┼───────────┼──────┼─────────────┼─────────────────┼───────────┤
│ server3 │ master2   │ 3306 │ 0           │ Master, Running │ 0-3002-31 │
├─────────┼───────────┼──────┼─────────────┼─────────────────┼───────────┤
│ server4 │ slave2    │ 3306 │ 0           │ Slave, Running  │ 0-3002-31 │
├─────────┼───────────┼──────┼─────────────┼─────────────────┼───────────┤
│ Shard-A │ 127.0.0.1 │ 4006 │ 0           │ Running         │           │
├─────────┼───────────┼──────┼─────────────┼─────────────────┼───────────┤
│ Shard-B │ 127.0.0.1 │ 4007 │ 0           │ Running         │           │
└─────────┴───────────┴──────┴─────────────┴─────────────────┴───────────┘
```
```
mysql -umaxuser -pmaxpwd -h 127.0.0.1 -P 4006
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| zipcodes_one       |
+--------------------+

```
```
mysql -umaxuser -pmaxpwd -h 127.0.0.1 -P 4007
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| zipcodes_two       |
+--------------------+
```
## Start phpmyadmin:
```

There are a multiply way to start you php. However in this lab I am using PMA_ARBITRARY which is an arbitrary server which will allow to specify the server name with the port in the login screen of phpmyadmin. For example; if you clone my repo you will need to follow this options:
login screen php:

Server= maxscale 4006 (or you can use different port, even you can use diferente server name such as, master1 or you can use any adress name that exists inside of the cnf file)
Usarname= maxuser
Password= maxpwd
```
## if you want to avoid specifying the server name with port do the next step:
```
replace the arbitrary server inside of yml and use PMA_PORT to specify you login and port
Now you can use just this option to login to you php account
Usarname: maxuser
Password: maxuser
```
## Stop all services
sudo docker-compose down -v
## Reference:
I have received help from Sam Lian and CNA350 module sources

