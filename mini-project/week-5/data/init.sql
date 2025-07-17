-- Create table to store products data
CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL,
    product_name VARCHAR NOT NULL,
    price DECIMAL DEFAULT 0,
    PRIMARY KEY (product_id)
);


-- Create table to store courier data
CREATE TABLE IF NOT EXISTS couriers (
    courier_id SERIAL,
    courier_first_name VARCHAR NOT NULL,
    courier_last_name VARCHAR NOT NULL,
    courier_phone_number VARCHAR(11),
    PRIMARY KEY (courier_id)
);


-- Create type to store product snapshot
CREATE TYPE product_snapshot AS (
    product_id INT,
    product_name VARCHAR,
    price DECIMAL,
    quantity INT
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
    order_status VARCHAR(25) NOT NULL DEFAULT 'preparing',
    products_snapshot product_snapshot[],
    PRIMARY KEY (order_id),
    FOREIGN KEY (courier_id) REFERENCES couriers(courier_id)
);



