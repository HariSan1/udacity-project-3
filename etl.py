import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries

def load_staging_tables_docstring(cur, conn):
    """
    Call load_staging_tables to load data into staging files from S3 warehouse
        
    keyword arguments in load_staging_tables:
        cur:      cursor command, allows connection to conn db connection
        conn:     connection specifics for db connection
    """
    
def load_staging_tables(cur, conn):
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()

def insert_tables_docstring(cur, conn):
    """
    Call insert_tables to insert data into final tables
        
    keyword arguments in load_staging_tables:
        cur:      cursor command, allows connection to conn db connection
        conn:     connection specifics for db connection
    """
        
def insert_tables(cur, conn):
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()

def main_docstring():
    """
    Call load_staging_tables to load staging_events and staging_songs from S3
    Call insert_tables to extract and load data into final tables
        
    keyword arguments in load_staging_tables and insert_tables:
        cur:      cursor command, allows connection to conn db connection
        conn:     connection specifics for db connection
    """

def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()