class Book:
    def __init__(self,title,author,year) :
        self.title= title
        self.author= author
        self.year= year
    
    
    def _str_(self):
        return "f{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
    def _del_(self):
        print (f"Deleting (title of the book)")
    