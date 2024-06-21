# 2. E-commerce Product Catalog System

# Objective: The goal of this assignment is to demonstrate a deep understanding of inheritance and method overriding in Python. Students will apply these concepts to develop an E-commerce Product Catalog System that handles various types of products with both common and unique attributes.

# Problem Statement: An e-commerce platform requires a system to manage different types of products, such as books, electronics, and clothing. Each product type shares some common characteristics but also has unique features. The system should be able to display information about each product appropriately.

# Task 1: Create Base Product Class

# Develop a base class Product with common attributes like product ID, name, price, and a method to display product information.

class Product ():
    def __init__ (self, product_id, type, name, price):
        self._product_id = product_id
        self._type = type
        self._name = name
        self._price = price

    def get_product_id(self):
        return self._product_id
    
    def get_type(self):
        return self._type

    def get_name(self):
        return self._name
    
    def get_price(self):
        return self._price
    
    def set_product_id (self, new_product_id):
        self._product_id = new_product_id

    def set_type (self, new_type):
        self._type = new_type
    
    def set_name (self, new_name):
        self._name = new_name

    def set_price (self, new_price):
        self._price = new_price

    
    def display_product_information(self):
        print(f'''
Product Information:

ID: {self.get_product_id()}
Type: {self.get_type()}
Name: {self.get_name()}
Price: {self.get_price()}''')
    


# Expected Outcome: A Product class that can hold general information about a product and display it.

tv = Product(12345, "Electronics", "Samsung TV", 500)
tv.display_product_information()


# Task 2: Implement Subclasses for Specific Products

# (ONLY BOOK SUBCLASS REQUIRED)

# Create subclasses Book, Electronic, and Clothing that inherit from Product.

# Each subclass should have additional attributes relevant to its category (e.g., author for books, specs for electronics, size for clothing).


class Book (Product):
    def __init__(self, product_id, type, name, price, author, genre, description):
        super().__init__(product_id, type, name, price)
        self.__author = author
        self.__genre = genre
        self.__description = description

    def get_author(self):
        return self.__author
    
    def get_genre(self):
        return self.__genre
    
    def get_description(self):
        return self.__description
    
    def set_author(self, new_author):
        self.__author = new_author

    def set_genre(self, new_genre):
        self.__genre = new_genre

    def set_description(self, new_description):
        self.__description = new_description

    def display_product_information(self):
        super().display_product_information()
        print(f'''Author: {self.get_author()}
Genre: {self.get_genre()}
Description: {self.get_description()}
''')

# Expected Outcome: Each subclass contains both inherited attributes from Product and new attributes specific to the product type.

book = Book(67890, "Books", "Game of Thrones", 4.99, "George R.R. Martin", "Fantasy", "A battle of thrones with dragons and stuff!")

book.display_product_information()




# Task 3: Override Display Method in Subclasses

# Override the method to display product information in each subclass to include specific attributes.
# For example, the Book class should display the author, Electronic should display specs, etc.

class Electronic (Product):
    def __init__(self, product_id, type, name, price, specs):
        super().__init__(product_id, type, name, price)
        self.__specs = specs

    def get_specs(self):
        return self.__specs
    
    def set_author(self, new_specs):
        self.__specs = new_specs

    def display_product_information(self):
        super().display_product_information()
        print(f'''Specifications: {self.get_specs()}
''')


# Expected Outcome: Calling the display method on an instance of any subclass shows both common and specific product details.


xbox = Electronic(6987, "Electronics", "Xbox Series X", 699.99, "1 TB")

xbox.display_product_information()




# Task 4: Test Product Catalog Functionality

# Instantiate objects of each subclass and call their display methods to ensure correct information is shown.
# Expected Outcome: The system should accurately display detailed information for each type of product, demonstrating inheritance and method overriding.

print("*" * 100)

book.display_product_information()
xbox.display_product_information()



