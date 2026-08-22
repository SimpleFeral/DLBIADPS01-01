from xml.sax import parse
from xml.sax.handler import ContentHandler
from Aufgabe_4a import Book

class BookResolverHandler(ContentHandler):
    books = []
    in_title_tag = False
    in_author_tag = False
    title = ''
    author = ''
    
    def __init__(self):
        super().__init__()
        self.books.clear()
        
    def startElement(self, name, attrs):
        if name == 'book':
            self.title = ''
            self.author = ''
        if name == 'title':
            self.in_title_tag = True
        if name == 'author':
            self.in_author_tag = True
            
        print(f"BEGIN: <{name}>, {attrs.keys()}") 

    def endElement(self, name):
        if name == 'title':
            self.in_title_tag = False
        if name == 'author':
            self.in_author_tag = False
        if name == 'book':
            book = Book(self.title.strip(), self.author.strip())
            if book not in self.books:
                self.books.append(book)     
        print(f"END: </{name}>") 
        
    def characters(self, content):
        if content.strip() != '':
            if self.in_title_tag:
                self.title += content
            if self.in_author_tag:
                self.author += content
            print("CONTENT:", repr(content))
        
    def getResolvedBooks(self):
        return self.books

book_resolver_handler = BookResolverHandler()    
parse('books.xml', book_resolver_handler)
for resolved_book in book_resolver_handler.getResolvedBooks():
    print(resolved_book)