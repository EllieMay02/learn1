def discounted(price, discount, max_discount=50):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError("Максимальная скидка не может быть больше 99%")
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return(price_with_discount) 
    
discounted(100, -50)
print(discounted(-300, 5))
discounted(231, 111,)
 if i am sosiska sosi ipipisky

          