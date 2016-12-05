# project02
I have created database in mysql on server 54.70.113.238 named cloud. 

create datbase cloud;

use cloud;

In that I have created table named cat

CREATE TABLE `cat` (
  `workId` varchar(255) DEFAULT NULL,
  `object_id` varchar(255) DEFAULT NULL,
  `revision_number` varchar(255) DEFAULT NULL,
  `timestamp` varchar(255) DEFAULT NULL,
  `details` varchar(2000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

To populate data from text file I have downloaded file and stored it in following location 

/home/cat.txt

LOAD DATA INFILE '/home/cat.txt' INTO TABLE cat;

After that run the project02.py file and go to following address

http://54.70.113.238:5001/work/OL509195W
(where OL509195W is the work id)

This gives the output in json format 

{"Timestamp": "2011-01-21T06:52:39.888650", "Author Name": "Laurie Halse Anderson", "details": {"title": "Homeless (Wild at Heart)", "created": {"type": "/type/datetime", "value": "2009-12-08T04:05:48.420565"}, "covers": [1319510], "last_modified": {"type": "/type/datetime", "value": "2011-01-21T06:52:39.888650"}, "latest_revision": 3, "key": "/works/OL509195W", "authors": [{"type": {"key": "/type/author_role"}, "author": {"key": "/authors/OL33825A"}}], "type": {"key": "/type/work"}, "subjects": ["Cats", "Veterinarians", "Juvenile fiction", "Feral cats", "Animal rescue", "Fiction", "Accessible book", "Protected DAISY"], "revision": 3}}

for 2nd webservice 

http://54.70.113.238:5001/search/Homeless
(where Homeless is the search keyword)

output: 
{"works": ["http://54.70.113.238:5001/work/OL509209W", "http://54.70.113.238:5001/work/OL4134102W", "http://54.70.113.238:5001/work/OL1633998W", "http://54.70.113.238:5001/work/OL4966066W", "http://54.70.113.238:5001/work/OL17311133W", "http://54.70.113.238:5001/work/OL15440006W", "http://54.70.113.238:5001/work/OL509195W"]}

