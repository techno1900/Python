# class BookMarkPage:
#     def __init__(self):
#         self.bookmarks = {}
    
#     def add(self, bookmark):
#         self.bookmarks[bookmark] = self.bookmarks.get(bookmark, 0) + 1


# book = BookMarkPage()
# book.add('python')
# book.add('python')
# book.add('python')
# book.add('python')
# book.add('Python')

# print(book.bookmarks)




# class BookMarkPage:
#     def __init__(self):
#         self.bookmarks = {}
    
#     def add(self, bookmark):
#         self.bookmarks[bookmark.lower()] = self.bookmarks.get(bookmark.lower(), 0) +1

# book=BookMarkPage()
# book.add('PYTHON')
# book.add('pythOn')
# book.add('pYthon')
# book.add('Python')
# book.add('nimsara')



# print(book.bookmarks)


class BookMarkPage:
    def __init__(self):
        self.bookmarks = {}
    
    def add(self, bookmark):
        self.bookmarks[bookmark.lower()] = self.bookmarks.get(bookmark.lower(), 0) +1
        
    def __getitem__(self,bookmark):
        return self.bookmarks.get(bookmark.lower(), 0)

book=BookMarkPage()
book.add('PYTHON')
book.add('pythOn')
book.add('pYthon')
book.add('Python')

print(book.bookmarks)
print(book['python'])