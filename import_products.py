
import json
import mysql.connector

def load_json_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def insert_data_into_db(data, connection_params):
    connection = mysql.connector.connect(**connection_params)
    cursor = connection.cursor()
    
    insert_query = "INSERT INTO petlebi (product_url, name, barcode, price, stock, images, description, sku, category, product_id, brand) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    for item in data:
        cursor.execute(insert_query, (
            item.get('product_url'),
            item.get('name'),
            item.get('barcode'),
            item.get('price'),
            item.get('stock'),
            json.dumps(item.get('images')),
            item.get('description'),
            item.get('sku'),
            item.get('category'),
            item.get('product_id'),
            item.get('brand'),
        ))
        
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    # Before running the code, json path must be entered.
    json_filepath = 'path_json'
    data = load_json_data(json_filepath)
    # Before running the code, the necessary SQL information must be entered.
    connection_params = {
        'host': 'host',
        'database': 'database',
        'user': 'user',
        'password': 'password'
    }
    
    insert_data_into_db(data, connection_params)
