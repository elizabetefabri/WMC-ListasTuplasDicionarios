'''
3. Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra.

'''
#Dictionary representing a shopping cart 
shopping_cart = {
    'yogurt': {'qty':2,'price': 5.00},
    'cheese': {'qty':3,'price': 33.00},
    'juice': {'qty':6,'price': 10.00},
    'bread': {'qty':4,'price': 5.99}
} 

#Function to calculate the total of the shopping cart will be showed:
total_price = 0
for product in shopping_cart:
    product_details = shopping_cart[product]
    product_subtotal = product_details['qty'] * product_details['price']
    total_price += product_subtotal

#Printing the total price
print(f"The total price is: R${total_price}")   
