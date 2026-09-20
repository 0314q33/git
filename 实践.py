products = {
    "耳机": {"price": 199, "stock": 8},
    "音箱": {"price": 299, "stock": 0},
}
def answer_product_question(product_name, products):
   if product_name=='':
      return('请说明你要查询的商品')
   if product_name not in products:
      return('未找到商品')
   product=products[product_name]
   price=product['price']
   stock=product['stock']
   if stock==0:
      return f'商品价格为{price}，暂时无货'
   return f'{product_name}库存有{stock},价格为{price}'
print(answer_product_question("", products))
print(answer_product_question("手机", products))
print(answer_product_question("音箱", products))
print(answer_product_question("耳机", products))
