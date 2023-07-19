import psycopg2

#seting up the database

def setup_db():
    conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='anything')
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS user_logins(
    user_id varchar(128),
    device_type varchar(32),
    masked_ip varchar(256),
    masked_device_id varchar(256),
    locale varchar(32),
    app_version integer,
    create_date date
    );
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_db()
