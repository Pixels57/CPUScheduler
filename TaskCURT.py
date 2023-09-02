import json
import sys
from PySide6 import QtCore, QtWidgets, QtGui

##Reacding books.json
f = open ('books.json')
books = json.load(f)
f.close()


#Class Book
class Book():
    bookTitle = str
    Author = str
    Cost = int
    def __init__(self, title, author, cost):
        self.bookTitle = title
        self.Author = author
        self.Cost = cost


    #Get Book Title
    def getTitle(self):
        return str(self.bookTitle)
    
    #Get Book Author
    def getAuthor(self):
        return str(self.Author)
    
    #Get Book Cost
    def getCost(self):
        return int(self.Cost)
    


#Class Section
class Section():
    sectionTitle = str
    Books = [Book]

    def __init__(self, title):
        self.sectionTitle = title
        self.Books = []

    #Get Section Title
    def getTitle(self):
        return self.sectionTitle
    

    #Add book to section i.e. may be developed to stock the library with books through the application
    def addBook(self, Book):
        self.Books.append(Book)

    #Search for book by its name
    def searchBookByTitle(self, title):
        for i in range(len(self.Books)):
            if title == self.Books[i].getTitle():
                return self.Books[i]
            
        return "Not Found"
              

    #Search for author's books        
    def searchBookByAuthor(self, title):
        booksbyauthor = []
        for i in range(len(self.Books)):
            if title == self.Books[i].getAuthor():
                booksbyauthor.append(self.Books[i])
            
        if not booksbyauthor:
            return "Not Found."
        else:
            return booksbyauthor
        
    
    #Remove book from library
    def deleteBook(self, title):
        for i in range(len(self.Books)):
            if title == self.Books[i].getTitle():
                self.Books.remove(self.Books[i])
                return
            
        return False  
    
    
    #Shows librarie's books
    def showBooks(self):
        sectionbooks = []
        for i in range(len(self.Books)):
            sectionbooks.append(self.Books[i])
        return sectionbooks  


##Class Library
class Library():
    librayTitle = str
    sections = [Section]
    profit = 0

    #Class Library init. and loading of books.json into the classes
    def __init__(self, title):
        self.librayTitle = title
        names = books.keys()
        realnames = []
        authors = []
        prices = []
        realsections = []
        for i in names:
            realnames.append(i)

        for i in books:
            authors.append(books[i]["author"])
            prices.append(books[i]["cost"])
            if not books[i]["section"] in realsections:
                realsections.append(books[i]["section"])

        for i in range(len(realsections)):
            s1 = Section(realsections[i])
            self.sections.append(s1)
            
        for i in range(len(names)):
            b1 = Book(realnames[i], authors[i], prices[i])
            for j in range(len(self.sections)):
                if books[realnames[i]]["section"] == self.sections[j + 1].getTitle():
                    self.sections[j + 1].addBook(b1)
                    break


    
    #Add Section to library i.e. may be developed to expand the library with sections through the application
    def addSection(self, section):
        self.sections.append[section]

    #Search a book by its name
    def searchBookByTitle(self, title):
        for i in range(1, len(self.sections)):
            book1 = self.sections[i].searchBookByTitle(title)
            if isinstance(book1, Book):
                return book1
            
        return "Not Found."
            

    #Search author's books
    def searchBookByAuthor(self, title):
        for i in range(1, len(self.sections)):
            book1 = self.sections[i].searchBookByAuthor(title)
            if not isinstance(book1, str):
                return book1
            
        return "Not Found."

            

    #Sell a book and remove it from the library and calculate the profit
    def sellaBook(self, title):
        for i in range(1, len(self.sections)):
            book1 = self.sections[i].searchBookByTitle(title)
            if isinstance(book1, Book):
                price = book1.getCost()
                self.profit += price
                self.sections[i].deleteBook(book1.getTitle())
                return
            
        return "Not Found."


    #Returns total profit
    def getTotalProfit(self):
        return self.profit


#GUI Implementation
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        #Opening Library
        super().__init__()
        self.setWindowTitle("Book Store")
        self.setLayout(QtWidgets.QVBoxLayout())
        my_label = QtWidgets.QLabel("Enter Library Name", alignment=QtCore.Qt.AlignCenter) 
        my_label.setFont(QtGui.QFont('Helvetica', 20))
        self.layout().addWidget(my_label)
        

        my_entry = QtWidgets.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        my_button = QtWidgets.QPushButton("Enter.", clicked = lambda: press_it())



        self.layout().addWidget(my_button)
        
        library = Library(my_entry.text())


        self.show

        
        def press_it():
            
            my_label.setText(my_entry.text() + " Library")
            my_entry.setText("")
            my_button.hide()
            my_entry.hide()
            my_label.move(50, 50)
            my_label.clear()
            allbooksbutton = QtWidgets.QPushButton("Show Books.", clicked = lambda: show())
            searchforbooktitle = QtWidgets.QPushButton("Search For Book By Title.", clicked = lambda: searchbytitle())
            searchforbookauthor = QtWidgets.QPushButton("Get Authors' Books.", clicked = lambda: searchbyauthor())
            buybook = QtWidgets.QPushButton("Buy A Book.", clicked = lambda: buyBook())
            self.layout().addWidget(searchforbooktitle)
            self.layout().addWidget(searchforbookauthor)
            self.layout().addWidget(allbooksbutton)
            self.layout().addWidget(buybook)
             
            #Shows all books in library in a window
            def show():
                allbooks = [Book]
                for i in range(len(library.sections) - 1):
                    allbooks = allbooks + library.sections[i + 1].showBooks()

                layout = QtWidgets.QGridLayout()
                self.setLayout(layout)
                self.listwidget = QtWidgets.QListWidget()
                for i in range(len(allbooks) - 1):
                    bookt = allbooks[i + 1].getTitle()
                    bookcost = str(allbooks[i + 1].getCost())
                    bookauthor =  allbooks[i + 1].getAuthor()
                    details = "Name: " + bookt + ",      " + "Cost: " + bookcost + ",     " + bookauthor
                    self.listwidget.insertItem(i, details)

                layout.addWidget(self.listwidget)
                self.listwidget.show()

            #Search for a book by its name and display its details
            def searchbytitle():
                booktitle_entry = QtWidgets.QLineEdit()
                booktitle_entry.setObjectName("title_field")
                booktitle_entry.setText("")
                self.layout().addWidget(booktitle_entry)
                search_button = QtWidgets.QPushButton("Search.", clicked = lambda: searchtitle())
                self.layout().addWidget(search_button)
                exitSearch_button = QtWidgets.QPushButton("Exit Search.", clicked = lambda: exitsearch())
                self.layout().addWidget(exitSearch_button)

                def searchtitle():
                    title = booktitle_entry.text()
                    answer = library.searchBookByTitle(title)
                    if isinstance(answer, Book):
                        bookt = answer.getTitle()
                        bookcost = str(answer.getCost())
                        bookauthor = answer.getAuthor()
                        details = "Name: " + bookt + ", " + "Cost: " + bookcost + ", " + bookauthor
                        book_details = QtWidgets.QLabel(details, alignment=QtCore.Qt.AlignCenter) 
                        my_label.setFont(QtGui.QFont('Helvetica', 18))
                        self.layout().addWidget(book_details)
                    else:
                        book_details = QtWidgets.QLabel("Book Not Found", alignment=QtCore.Qt.AlignCenter) 
                        my_label.setFont(QtGui.QFont('Helvetica', 18))
                        self.layout().addWidget(book_details)


                    clear_button = QtWidgets.QPushButton("Clear.", clicked = lambda: housekeeping())
                    self.layout().addWidget(clear_button)

                    def housekeeping():
                        book_details.hide()
                        clear_button.hide()

                def exitsearch():
                    search_button.hide()
                    booktitle_entry.hide()
                    exitSearch_button.hide()

            #List author's books and display their details
            def searchbyauthor():
                author_entry = QtWidgets.QLineEdit()
                author_entry.setObjectName("title_field")
                author_entry.setText("")
                self.layout().addWidget(author_entry)
                search_button1 = QtWidgets.QPushButton("Search.", clicked = lambda: searchauthor())
                self.layout().addWidget(search_button1)     
                exitSearch1_button = QtWidgets.QPushButton("Exit Search.", clicked = lambda: exitsearch())
                self.layout().addWidget(exitSearch1_button)  


                def searchauthor():
                    author = author_entry.text()
                    answer = library.searchBookByAuthor(author)
                    if not isinstance(answer, str):
                        layout = QtWidgets.QGridLayout()
                        self.setLayout(layout)
                        self.listwidget = QtWidgets.QListWidget()
                        for i in range(len(answer)):
                            bookt = answer[i].getTitle()
                            bookcost = str(answer[i].getCost())
                            details = "Name: " + bookt + ",      " + "Cost: " + bookcost
                            self.listwidget.insertItem(i, details)

                        layout.addWidget(self.listwidget)
                        self.listwidget.show()
                        
                    else:
                        book_details = QtWidgets.QLabel("No Books", alignment=QtCore.Qt.AlignCenter) 
                        my_label.setFont(QtGui.QFont('Helvetica', 18))
                        self.layout().addWidget(book_details)
                        clear2_button = QtWidgets.QPushButton("Clear.", clicked = lambda: housekeeping2())
                        self.layout().addWidget(clear2_button)


                    def housekeeping2():
                        book_details.hide()
                        clear2_button.hide()

                def exitsearch():
                    search_button1.hide()
                    author_entry.hide()
                    exitSearch1_button.hide()

            #Selling a book
            def buyBook():
                booktitle_entry = QtWidgets.QLineEdit()
                booktitle_entry.setObjectName("title_field")
                booktitle_entry.setText("")
                self.layout().addWidget(booktitle_entry)
                buy_button = QtWidgets.QPushButton("Buy", clicked = lambda: searchbook())
                self.layout().addWidget(buy_button)
                exitBuy_button = QtWidgets.QPushButton("Exit.", clicked = lambda: exitBuy())
                self.layout().addWidget(exitBuy_button)

                def searchbook():
                    title = booktitle_entry.text()
                    booktitle_entry.setText("")
                    answer = library.searchBookByTitle(title)
                    if isinstance(answer, Book):
                        library.sellaBook(title)
                        book_details = QtWidgets.QLabel("Purchase Done Successfully.", alignment=QtCore.Qt.AlignCenter) 
                        my_label.setFont(QtGui.QFont('Helvetica', 18))
                        self.layout().addWidget(book_details)
                    else:
                        book_details = QtWidgets.QLabel("Book Not Found", alignment=QtCore.Qt.AlignCenter) 
                        my_label.setFont(QtGui.QFont('Helvetica', 18))
                        self.layout().addWidget(book_details)


                    clear1_button = QtWidgets.QPushButton("Clear.", clicked = lambda: housekeeping1())
                    self.layout().addWidget(clear1_button)

                    def housekeeping1():
                        book_details.hide()
                        clear1_button.hide()

                def exitBuy():
                    buy_button.hide()
                    booktitle_entry.hide()
                    exitBuy_button.hide()





                    
#Main Function 
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MainWindow()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
