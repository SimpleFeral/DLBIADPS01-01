from xml.dom.minidom import parse, Node

class Book:
    title: str
    author: str
    
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        
    def __eq__(self, other):
        return (type(other) == Book 
                and self.title == other.title 
                and self.author == self.author)
        
    def __str__(self):
        return f'Book: (Title: {self.title}, Author: {self.author})'
     
books_xml = parse('books.xml')

def resolve_title_and_author():
    resolved_books = []
    for book_node in books_xml.getElementsByTagName('book'):
        title = ''
        author = ''
        for attributeNode in book_node.childNodes:
            if attributeNode.nodeType == Node.ELEMENT_NODE:
                if attributeNode.nodeName == "title":
                    title = attributeNode.childNodes[0].data.strip()
                if attributeNode.nodeName == "author":
                    author = attributeNode.childNodes[0].data.strip()
        book = Book(title, author)
        if book not in resolved_books:
            resolved_books.append(book)
    return resolved_books
            
for book in resolve_title_and_author():
    print(book)