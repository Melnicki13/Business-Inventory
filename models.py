# Importăm modulele necesare pentru baza de date și autentificare.

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime #importam si modulul de datetime

# Inițializăm obiectul SQLAlchemy
db = SQLAlchemy()


# Dicționar cu cărțile predefinite și numerele lor de inventar
BOOKS_INVENTORY = {
    1001: "To Kill a Mockingbird - Harper Lee",
    1002: "1984 - George Orwell",
    1003: "Pride and Prejudice - Jane Austen",
    1004: "The Great Gatsby - F. Scott Fitzgerald",
    1005: "The Catcher in the Rye - J.D. Salinger",
    1006: "Harry Potter and the Sorcerer's Stone - J.K. Rowling",
    1007: "The Hobbit - J.R.R. Tolkien",
    1008: "The Lord of the Rings - J.R.R. Tolkien",
    1009: "Animal Farm - George Orwell",
    1010: "Brave New World - Aldous Huxley",
    1011: "The Chronicles of Narnia - C.S. Lewis",
    1012: "Jane Eyre - Charlotte Brontë",
    1013: "Wuthering Heights - Emily Brontë",
    1014: "The Da Vinci Code - Dan Brown",
    1015: "The Hunger Games - Suzanne Collins",
    1016: "The Alchemist - Paulo Coelho",
    1017: "The Little Prince - Antoine de Saint-Exupéry",
    1018: "Don Quixote - Miguel de Cervantes",
    1019: "The Odyssey - Homer",
    1020: "Crime and Punishment - Fyodor Dostoevsky",
    1021: "One Hundred Years of Solitude - Gabriel García Márquez",
    1022: "The Divine Comedy - Dante Alighieri",
    1023: "The Road - Cormac McCarthy",
    1024: "The Handmaid's Tale - Margaret Atwood",
    1025: "Fahrenheit 451 - Ray Bradbury",
    1026: "Dune - Frank Herbert",
    1027: "The Stand - Stephen King",
    1028: "The Shining - Stephen King",
    1029: "IT - Stephen King",
    1030: "American Gods - Neil Gaiman",
    1031: "Good Omens - Terry Pratchett & Neil Gaiman",
    1032: "The Color Purple - Alice Walker",
    1033: "The Bell Jar - Sylvia Plath",
    1034: "The Picture of Dorian Gray - Oscar Wilde",
    1035: "Frankenstein - Mary Shelley",
    1036: "Dracula - Bram Stoker",
    1037: "The War of the Worlds - H.G. Wells",
    1038: "The Time Machine - H.G. Wells",
    1039: "Twenty Thousand Leagues Under the Sea - Jules Verne",
    1040: "Journey to the Center of the Earth - Jules Verne",
    1041: "The Count of Monte Cristo - Alexandre Dumas",
    1042: "Les Misérables - Victor Hugo",
    1043: "The Three Musketeers - Alexandre Dumas",
    1044: "The Jungle Book - Rudyard Kipling",
    1045: "Alice's Adventures in Wonderland - Lewis Carroll",
    1046: "The Wind in the Willows - Kenneth Grahame",
    1047: "Watership Down - Richard Adams",
    1048: "The Grapes of Wrath - John Steinbeck",
    1049: "Of Mice and Men - John Steinbeck",
    1050: "The Old Man and the Sea - Ernest Hemingway"
}


# Modelul pentru utilizatori (admin și utilizatori normali)
class User(UserMixin, db.Model):

    # Definim coloanele tabelului
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


# Modelul pentru obiecte din inventar (cărți)
class InventoryItem(db.Model):

    # Definim coloanele tabelului pentru items
    id = db.Column(db.Integer, primary_key=True)
    inventory_number = db.Column(db.Integer, unique=True, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    date_registered = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='OK')  # OK, Damaged, Sent for maintenance
    booked = db.Column(db.String(10), default='Free')  # Free, In use