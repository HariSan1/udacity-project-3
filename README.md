
The purpose of this project is to move music streaming data and metadata and processes to a cloud database.  The objective is:
1 - Build ETL pipeline that extracts their existing data from AWS S3
2 - Put the data into staging tables in Redshift
3 - Execute SQL statements to transform staging table data into analytical tables

The way we will do this is:
- create tables with SQL statements (staging and final tables)
- separately create a Redshift cluster with database in AWS, then connect to it
- download the metadata from S3 warehouse, copy it to staging tables
- extract and transform required information and load resulting data in the final tables created

Files:
sql_queries.py - 
- create the sql queries to create tables by first checking if they already exist and dropping (deleting) them if they do and then creating them
- create statements to copy data from AWS S3 bucket into staging tables - staging_events, staging_songs
- create sql statements to insert data into tables
- create statements to manipulate specific data to format and fit into table structure for songplay table

create_tables.py
- connect to AWS Redshift cluster database
- call SQL queries(drop_table, insert_table defined in sql_queries.py) from sql_queries.py listed above to create new tables 

etl.py
- populate tables with data - manipulate data with queries to extract only required data (insert_table queries, defined in sql_queries.py)
- copy staging_events and staging_songs data from S3 into database tables of same name in cluster db (copy_table queries, defined in sql_queries.py)

dwh.cfg
- configuration parameters for connecting to the Redshift cluster database in Amazon Cloud
- CLUSTER - defines host, db connection parameters
- S3 - defines Cloud Storage path parameters to copy data from
- AWS - authentication information, will be empty here for security reasons
- IAM_ROLE - Role identification for Identity Authentication Management (IAM) and Role with permission to perform functions in cluster
- DWH - Redshift dwh (data warehouse) parameters 

Folder: \screen-prints-of-table-counts
[screen print of count of records in artists table](artists-table-count.jpeg)
[screen print of count of records in songplay table](songplay-table-count.jpeg)
[screen print of ]