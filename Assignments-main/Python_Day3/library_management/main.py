from book import Book
from member import Member
from library import Library


def main():

    library = Library()

    book1 = Book("Python", "Ankush", "001")
    book2 = Book("OOPS", "Ayush", "002")
    book3 = Book("DSA", "Mayur", "003")
    book4 = Book("ML", "Hrishikesh", "004")
    book5 = Book("Devops", "Dhanush","005")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)

    print()

    member1 = Member("Ayush", "M101")
    member2 = Member("Rahul", "M102")
    member3 = Member("Ankush", "M103")

    library.add_member(member1)
    library.add_member(member2)
    library.add_member(member3)

    print("\n===== Borrowing Books =====")

    member1.borrow_book(book1)
    member1.borrow_book(book2)
    member1.borrow_book(book3)

    member1.borrow_book(book4)

    member2.borrow_book(book1)
    member3.borrow_book(book5)

    print("\n===== Returning Books =====")

    member1.return_book(book2)

    print("\n===== Borrow Again =====")

    member2.borrow_book(book2)

    library.display_books()
    library.display_members()


if __name__ == "__main__":
    main()