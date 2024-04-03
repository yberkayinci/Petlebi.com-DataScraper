# Petlebi Product Data Extractor

## Overview
The Petlebi Product Data Extractor is a sophisticated tool designed for comprehensive data extraction and management. Utilizing Python and Scrapy for web scraping, it captures extensive product details from www.petlebi.com. The project elegantly handles JSON data manipulation and integrates smoothly with MySQL for efficient data storage and retrieval, showcasing a blend of data engineering and software development skills.

## Features
- **Automated Web Scraping:** Leverages Scrapy to navigate and extract data from pet product listings.
- **Data Serialization:** Converts scraped data into a structured JSON format for easy manipulation and storage.
- **Database Management:** Employs Python scripts for MySQL database operations, including table creation and data insertion.

## Technologies Used
- Python
- Scrapy
- MySQL
- JSON

## Project Structure
- `petlebi_scrapy.py`: Script for scraping product data using Scrapy.
- `petlebi_products.json`: JSON file with the extracted product information.
- `import_products.py`: Script for importing data from the JSON file to a MySQL database.
- `petlebi_create.sql`: SQL script to create the necessary database schema.
- `petlebi_insert.sql`: SQL script with data insertion commands for the database.

## Getting Started
1. **Initial Setup:** Ensure Python and MySQL are properly installed. Scrapy can be installed via `pip install scrapy`.
2. **Database Setup:** Execute `petlebi_create.sql` to prepare the database structure in MySQL.
3. **Data Extraction:** Run `python petlebi_scrapy.py` to scrape product data and generate the JSON output.
4. **Data Import:** Use `python import_products.py` to populate the MySQL database with the scraped data.

## About the Developer
Yunus Berkay İnci, a Junior Software Engineer, specializes in data science, web development, and AI technologies. Educated in Software Engineering at Yıldırım Beyazıt University, Yunus employs his theoretical foundation and technical acumen on projects that demonstrate significant practical applications and technological proficiency.

Explore more on [GitHub](https://github.com/yberkayinci).

## License
This project is made available under the MIT License. For more details, see the LICENSE file.
