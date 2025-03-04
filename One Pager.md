Sistem de Gestiune a Inventarului Bibliotecă
Descriere Proiect

Aplicație web dezvoltată în Flask pentru gestionarea inventarului unei biblioteci. Permite urmărirea cărților, statusul lor și gestionarea împrumuturilor.
Caracteristici Principale

    Sistem de Autentificare
        Login securizat
        Parolă criptată
        Cont administrator predefinit

    Gestionare Inventar
        Adăugare cărți noi
        Editare detalii cărți
        Ștergere cărți
        Vizualizare listă completă

    Sistem de Împrumut
        Marcare cărți ca împrumutate/disponibile
        Status actualizat în timp real
        Note personale pentru fiecare împrumut

    Listă Predefinită
        50 de cărți predefinite
        Numere de inventar unice
        Descrieri detaliate

Tehnologii Utilizate

    Backend: Python/Flask
    Bază de Date: SQLite/SQLAlchemy
    Frontend: HTML/CSS
    Securitate: Werkzeug pentru criptare

Structura Proiectului

    
Business Inventory/
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       └── library_background.jpg
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── index.html
│   ├── add_item.html
│   └── edit.html
├── app.py
└── models.py

    

Instalare și Rulare

    Cerințe preliminare

        
    pip install flask flask-sqlalchemy flask-login werkzeug

        

Configurare

    Clonează repository-ul
    Creează mediul virtual (opțional)
    Instalează dependențele

Rulare

    
python app.py

    

    Acces
        Deschide browser: http://localhost:5000
        Login:
            Username: admin
            Password: admin123

Funcționalități Detaliate
1. Management Utilizatori

    Autentificare securizată
    Sesiuni persistente
    Logout automat la închidere browser

2. Management Cărți

    Adăugare cu număr inventar
    Editare detalii
    Ștergere din sistem
    Note personalizate

3. Sistem de Status

    OK
    Damaged
    Sent for maintenance

4. Sistem de Rezervare

    Free
    In use

Securitate

    Autentificare
        Parole hash-uite
        Protecție împotriva SQL injection
        Sesiuni securizate

    Validare
        Validare input
        Verificări de permisiuni
        Protecție rute

Interfață Utilizator

    Design responsive
    Interfață intuitivă
    Feedback vizual pentru acțiuni
    Mesaje de confirmare/eroare

Bază de Date

    SQLite pentru stocare
    Relații definite clar
    Backup automat (opțional)
    Migrări simple

Dezvoltări Viitoare Posibile

    Funcționalități Noi
        Sistem de rezervări
        Istoric împrumuturi
        Rapoarte statistice

    Îmbunătățiri
        Interfață admin avansată
        Sistem de notificări
        Export date în CSV/PDF

Mentenanță

    Backup regulat bază de date
    Verificare log-uri erori
    Update dependințe

Troubleshooting

    Probleme Comune
        Erori de conectare
        Probleme de permisiuni
        Conflicte bază de date

    Soluții
        Verificare credențiale
        Resetare bază de date
        Curățare cache

Contact și Suport

    Documentație detaliată
    Ghid de utilizare
    Asistență tehnică

Licență

    Open Source
    Utilizare liberă
    Modificări permise

Note Importante

    Backup regulat recomandat
    Păstrare credențiale securizate
    Actualizare periodică

Acest README oferă o privire de ansamblu asupra proiectului și poate fi extins în funcție de necesități specifice sau dezvoltări viitoare.