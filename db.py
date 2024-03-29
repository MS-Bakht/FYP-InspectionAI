import sqlite3

# Define database name
db_name = "inspection_data.db"

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect(db_name)

# Create a cursor object
cursor = conn.cursor()

# Define the CREATE TABLE statement
create_table_query = """
CREATE TABLE IF NOT EXISTS inspection_data (
  ID INTEGER PRIMARY KEY AUTOINCREMENT,
  Date TEXT NOT NULL,
  Raw_Footage TEXT,
  Annotated_Footage TEXT,
  "3D_Model" TEXT
);
"""

# Execute the CREATE TABLE statement
cursor.execute(create_table_query)

# Commit changes (important to save the table creation)
conn.commit()

# Close the connection
conn.close()

print(f"Table created successfully in database: {db_name}")
