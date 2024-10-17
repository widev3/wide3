# from flask import Flask
# from spm_reader.route import spm_reader_blueprint

# app = Flask(__name__)
# app.register_blueprint(spm_reader_blueprint)

# if __name__ == "__main__":
#     app.run(debug=True)

import psycopg2

conn_params = {
    "host": "db.eaziu.com",
    "port": "5432",
    "dbname": "core_db",
    "user": "u_eaziu",
    # "sslmode": "verify-full",  # Requires server certificate validation,
    # "init_command": "SET NAMES UTF8",
}

try:
    # Establish the connection
    conn = psycopg2.connect(**conn_params)

    # Create a cursor object
    cur = conn.cursor()

    # Set the schema
    cur.execute(f"SET search_path TO {schema};")

    print(f"Connected to database '{dbname}' and schema '{schema}' successfully!")

    # Now you can execute queries in the schema
    cur.execute("SELECT * FROM your_table;")  # Example query
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Don't forget to close the cursor and connection
    cur.close()
    conn.close()

except psycopg2.Error as e:
    print(f"Error connecting to PostgreSQL: {e}")
