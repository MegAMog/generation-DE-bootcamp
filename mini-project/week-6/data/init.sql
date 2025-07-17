--UNIQUE: -- https://neon.com/postgresql/postgresql-tutorial/postgresql-unique-constraint

-- Create table to store products data
CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL,
    product_name VARCHAR NOT NULL,
    price DECIMAL DEFAULT 0,
    PRIMARY KEY (product_id),
    UNIQUE(product_name)
);


-- Create table to store courier data
CREATE TABLE IF NOT EXISTS couriers (
    courier_id SERIAL,
    courier_first_name VARCHAR NOT NULL,
    courier_last_name VARCHAR NOT NULL,
    courier_phone_number VARCHAR(11),
    PRIMARY KEY (courier_id)
);


-- Create table to store order statuses list
CREATE TABLE IF NOT EXISTS order_status (
    status_id SERIAL,
    status_name VARCHAR NOT NULL,
    PRIMARY KEY (status_id),
    UNIQUE(status_name)
);


-- Create table to store order history
CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL,
    order_date DATE DEFAULT CURRENT_DATE,
    customer_first_name VARCHAR NOT NULL,
    customer_last_name VARCHAR NOT NULL,
    customer_address TEXT NOT NULL,
    customer_phone_number VARCHAR(11) NOT NULL,
    courier_id INT,
    order_status_id INT NOT NULL DEFAULT 1,
    product_ids VARCHAR NOT NULL,
    PRIMARY KEY (order_id),
    FOREIGN KEY (courier_id) REFERENCES couriers(courier_id),
    FOREIGN KEY (order_status_id) REFERENCES order_status(status_id)
);