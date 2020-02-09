book = "The Hitchhiker's Guide to the Galaxy"
booklist = list(book)
print(booklist)
article = "".join(booklist[0:3])
print(article)
lastword = "".join(booklist[-6:])
print(lastword)
backwards = "".join(booklist[::-1])
print(backwards)