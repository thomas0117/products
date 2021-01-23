import os

products = []

# 讀檔
if os.path.isfile('products.csv'):
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格'in line:
				continue
			name, price = line.strip().split(',')
			products.append([name,price])
	print(products)

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	products.append([name,price])
print(products)

# 印出所有購買紀錄:
for product in products:
	print(product)

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')