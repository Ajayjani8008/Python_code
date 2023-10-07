class Library:
    def __init__(self,customer_name):
        self.customer_name=customer_name
        self.nobooks=0
        customer_name
        self.books=[]

    def addbook(self,book):
        self.books.append(book)
        self.nobooks=len(self.books)
    def showInfo(self):
        print(f" The name of isuuer is {self.customer_name}the Total books are issue {self.nobooks} and the books are ")
        for books in self.books:
            print(books)
        
l1=Library("ajay")
l1.addbook("vachnamrutam")
l1.addbook("bhaktchintamani")
l1.addbook("nishkulanand kavya")
l1.addbook("shreemad bhagvatgita")
l1.addbook("ramayan")
l1.showInfo()