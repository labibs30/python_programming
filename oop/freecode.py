class Book:
    def __init__(self,title,quantity,author,price,discount=None):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price
        self.__discount = discount
        self.total_price = 0
    
    # Encapsulation - start
    def set_discount(self, discount):
        self.__discount = discount    
        
    def get_price(self):
        if self.__discount:
            return self.price * (1 - self.__discount)
        return self.price
    def get_total_price(self):
        if self.quantity >= 20 and self.__discount:
            self.set_discount(self.__discount)
            price_of_book = self.price * (1 - self.__discount)
            total_price = price_of_book * self.quantity
            return total_price
        total_price = self.price * self.quantity
        return total_price
    # Encapsulation - end
    def __repr__(self):
        return f"Book({self.title}, {self.quantity}, {self.author}, Book price :{self.price})"

class Novel(Book):
    def __init__(self, title, quantity, author, price, discount, pages):
        super().__init__(title, quantity, author, price, discount)
        self.pages = pages

class Academic(Book):
    def __init__(self, title, quantity, author, price, discount, pages):
        super().__init__(title, quantity, author, price, discount)
        self.pages = pages
        
        
book1 = Book("Harry Potter", 10, "JK Rowling", 100)
book2 = Book("Lord of the Rings", 20, "Tolkien", 200)
book3 = Book("The Hobbit", 30, "Tolkien", 300)

# print(book1.price)
# print(book1.get_price())
# # print(book2.__discount)
# print(book2)
# print(book3)

# A CASE 

single_book = Book("Harry Potter", 1, "JK Rowling", 100)
bulk_books = Book("Harry Potter", 100, "JK Rowling", 100, 0.2)
print(single_book)
print(bulk_books)

print(single_book.get_price())
print(single_book.get_total_price())
print(bulk_books.get_price())
print(bulk_books.get_total_price())

# A INHERITANCE CASE

novel1 = Novel('Two States', 20, 'Chetan Bhagat', 200, 0.2 ,187)
# novel1.set_discount(0.20)
print(novel1.get_total_price())
print(novel1)