# project02
I have created database in mysql on server 54.70.113.238 named cloud. 

create datbase cloud;

use cloud;

In that I have created tabel named cat

CREATE TABLE `cat` (
  `workId` varchar(255) DEFAULT NULL,
  `object_id` varchar(255) DEFAULT NULL,
  `revision_number` varchar(255) DEFAULT NULL,
  `timestamp` varchar(255) DEFAULT NULL,
  `details` varchar(2000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

To populate data from text file I have downloaded file and stored it in following location 

/home/cat.txt

LOAD DATA INFILE '/hoke/cat.txt' INTO TABLE cat;

