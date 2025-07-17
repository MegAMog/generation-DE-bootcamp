#Data model for orders

#Order statuses list (enum - ?, change to order status id)
order_status=['new', 'confirmed', 'preparing', 'ready for delivery', 'out for delivery', 'delivered', 'cancelled', 'delivery failed', 'refunded']
default_order_status=order_status[2]

#Original list of orders
original_orders=[{'customer_first_name': 'Anna', 'customer_last_name': 'Smith', 'customer_address': '45 Olympic Way, London', 'customer_phone_number': '07288363637'}]

#Customer attributes structure
customer_attributes={
    'customer_first_name':'', 
    'customer_last_name':'', 
    'customer_address':'', 
    'customer_phone_number':''}

