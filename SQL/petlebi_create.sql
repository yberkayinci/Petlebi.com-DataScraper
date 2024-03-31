
CREATE TABLE IF NOT EXISTS petlebi (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_url VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    barcode VARCHAR(255),
    price DECIMAL(10, 2),
    stock INT,
    images TEXT,
    description TEXT,
    sku VARCHAR(255),
    category VARCHAR(255) NOT NULL,
    product_id VARCHAR(255),
    brand VARCHAR(255) NOT NULL
);
