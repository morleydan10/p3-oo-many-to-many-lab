
# # *****************************************************************AUTHOR*********************************************************************

# class Author:

#     authors_list = []

#     def __init__(self, name) -> None:
#         self.name:str = name
#         Author.authors_list.append(self)
    
#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self, name):
#         if isinstance(name, str):
#             self._name = name
#             # self.authors_list.append(name)
#         else:
#             raise Exception("Name must be a string.")

# # contracts(self): This method should return a list of related contracts.
#     def contracts(self):
#         c = [contract for contract in Contract.contract_list if contract.author == self ]
#         return c

# # books(self): This method should return a list of related books using the Contract class as an intermediary.
#     def books(self):
#         b = [contract.book for contract in self.contracts()]
#         return b

# #sign_contract(book, date, royalties): This method should create and return a new Contract object between the author and the specified book with the specified date and royalties
#     def sign_contract(book, date, royalties):
#         return Contract(book, date, royalties)

# # total_royalties(): This method should return the total amount of royalties that the author has earned from all of their contracts.
#     def total_royalties():
#         return sum([contract.royalties for contract in self.contracts()])




# # *************************************************BOOK******************************************************************

# class Book:


#     book_list = []

#     def __init__(self, title) -> None:
#         self.title:str = title
#         Book.book_list.append(self)
    
#     @property
#     def title(self):
#         return self._title
    
#     @title.setter
#     def title(self, title):
#         if isinstance(title, str):
#             self._title = title
#             # self.book_list.append(title)
#         else:
#             raise Exception("Title must be a string")
        
#         def contracts(self):
#             return [contract for contract in Contract.all if contract.book == self]

#         def authors(self):
#             return [contract.author for contract in self.contracts()]



# # ******************************************************************CONTRACT*******************************************************************

# class Contract:

#     contract_list = []

#     def __init__(self, author, book, date, royalties) -> None:
#         self.author:object = author
#         self.book:object = book
#         self.date:str = date
#         self.royalties:int = royalties
#         Contract.contract_list.append(self)

# # *****AUTHOR*******
#     @property
#     def author(self):
#         return self._author
    
#     @author.setter
#     def author(self, author):
#         if isinstance(author, Author):
#             self._author = author
#             # self.contract_list.append(author)
#         else:
#             raise Exception("author must be an Author.")

# # *****BOOK******
#     @property
#     def book(self):
#         return self._book
    
#     @book.setter
#     def book(self, book):
#         if isinstance(book, Book):
#             self._book = book
#             # self.contract_list.append(book)
#         else:
#             raise Exception("book must be a Book.")
        

# # ******DATE*******
#     @property
#     def date(self):
#         return self._date
    
#     @date.setter
#     def date(self, date):
#         if isinstance(date, str):
#             self._date = date
#             # self.contract_list.append(date)
#         else:
#             raise Exception("Date must be a string")

# # *******ROYALTIES*******
#     @property
#     def royalties(self):
#         return self._royalties
    
#     @royalties.setter
#     def royalties(self, royalties):
#         if isinstance(royalties, int):
#             self._royalties = royalties
#             # self.contract_list.append(royalties)
#         else:
#             raise Exception("Royalties must be a whole number.")

# # A class method contracts_by_date(cls, date): This method should return all contracts that have the same date as the date passed into the method.
#     def contracts_by_date(self, date): 
#         pass
    





# '''
# The author property should be an instance of the Author class, while the book property should be an instance of the Book class. The date property should be a string that represents the date when the contract was signed, while the royalties property should be a number that represents the percentage of royalties that the author will receive for the book.
# All setters should raise Exception upon failure.
# '''

# # **********************************TESTING*******************************************

# # b = Book("Plunder")
# # print(b.title)
# # b_all = Book.all[0]
# # print(b_all)


# # c = Contract(Author("Hawthorne"), Book("Plunder"), "02/22/2022", 5000)
# # c_all = Contract.all
# # print(c_all)

# print(Contract.contract_list)


class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])


class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]

class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception
        self._author = value

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception
        self._book = value

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception
        self._date = value

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]