import os
import requests
import mysql.connector

# Function to send a request to the API and return the user data
def get_user_data():
    api_url = "https://jsonplaceholder.typicode.com/posts?userId=1"
    response = requests.get(api_url)
    data = response.json()
    return data

# Function to insert user data into the MySQL table
def insert_into_mysql(data):
    try:
        connection = mysql.connector.connect(
            host=os.environ.get("DB_HOST"),
            user=os.environ.get("DB_USERNAME"),
            password=os.environ.get("DB_PASSWORD"),
            database=os.environ.get("DB_NAME"),
            port=os.environ.get("DB_PORT")
        )
        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                userId INT,
                title VARCHAR(255),
                body TEXT
            )
            """
        )

        for item in data:
            sql = "INSERT INTO data (userId, title, body) VALUES (%s, %s, %s)"
            val = (item['userId'], item['title'], item['body'])
            cursor.execute(sql, val)

        connection.commit()
        print("Data inserted successfully into MySQL")

        cursor.close()
        connection.close()

    except mysql.connector.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    data = get_user_data()

    if data:
        item_info_to_insert = [
            {
                "userId": item['userId'],
                "title": item['title'],
                "body": item['body'],
            }
            for item in data
        ]
        insert_into_mysql(item_info_to_insert)
    else:
        print("No data to insert")