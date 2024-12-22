from collections import namedtuple

# Product = namedtuple('Product', ['name', 'price'])
# Users = namedtuple('User', ['name', 'age', 'email', 'phone'])


# print(f'product: {iphone._asdict()},User:  {john._asdict()}')


class Product(namedtuple('Product', ['name', 'price'])):
    def get_name(self):
        return {self.name}


class User(namedtuple('User', ['name', 'age', 'email', 'phone'])):
    def get_info(self):
        return self._asdict()


iphone = Product('15pro max', '1000$')
john = User('john', '18', 'john@gmail.com', '+9991234321234')

print(Product.get_name(iphone))
print(User.get_info(john))
