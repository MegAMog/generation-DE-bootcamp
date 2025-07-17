INSERT INTO products (product_name, price) VALUES
('espresso',3.5),
('americano',3.75),
('latte',3.75),
('cappuccino',3.25),
('flat white',3.5),
('macchiato',3.75),
('mocha',4.0);


SELECT *
FROM products;


INSERT INTO couriers (courier_first_name, courier_last_name, courier_phone_number) VALUES
('John','Lennon','07123456789'),
('Paul','McCartney','07345678923'),
('George','Harrison','07345678901'),
('Ringo','Starr','07345678456');


SELECT *
FROM couriers;


INSERT INTO order_status (status_name)
VALUES
  ('preparing'),
  ('new'),
  ('confirmed'),
  ('out for delivery'),
  ('delivered'),
  ('cancelled');


SELECT *
FROM order_status;



INSERT INTO orders 
(customer_first_name, customer_last_name, customer_address, customer_phone_number, 
courier_id, 
order_status_id,
product_ids)
VALUES
('Kate','Bush','23 King Way, London', '07364563675', 2, 2,'5');


INSERT INTO orders (customer_first_name, customer_last_name, customer_address, customer_phone_number, courier_id, product_ids)
VALUES
('Anna','Smith','46 Empire Way, London', '07264163623', 1, '1,5,2');
	


SELECT *
FROM orders;
