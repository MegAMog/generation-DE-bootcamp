# Create, Read, Update, Delete functions for products

# Add new product to the product list.
# Returns:
# -new updated copy of product list (doesn't modify list in place);
# -status: True - new product was successfully added, False - wasn't added (it is already in the product list).
def add_product(products: list, new_product: str) -> tuple[list, bool]:
    product = new_product.strip().lower()

    if product in products:
        return products, False 
    else:
        return products + [product], True
        


# Update existing product name by its index in product list.
# Returns:
# -new updated copy of product list (doesn't modify list in place);
# -status: True - product was successfully updated, False - wasn't updated (same product already exists in the product list).
def update_product_by_index(products: list, product_index: int, new_product: str) -> tuple[list, bool]:
    product=new_product.strip().lower() 

    if product in products:
        return products, False
    else:
        updated_products=products.copy()
        updated_products[product_index] = product
        return updated_products, True
