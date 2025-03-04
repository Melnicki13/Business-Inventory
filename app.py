# Importăm toate modulele necesare pentru aplicație

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, InventoryItem, BOOKS_INVENTORY
from datetime import datetime


# Inițializăm aplicația Flask
app = Flask(__name__)

# Configurăm setările aplicației
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inițializăm baza de date și sistemul de login
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Setăm pagina de login


# Funcție necesară pentru Flask-Login pentru a încărca utilizatorul
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

# Ruta pentru login.
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        # Obținem datele din formular
        username = request.form['username']
        password = request.form['password']

        # Căutăm utilizatorul în baza de date
        user = db.session.execute(db.select(User).filter_by(username=username)).scalar_one_or_none()

        # Verificăm credențialele
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid username or password')
    return render_template('login.html')

# Ruta pentru logout
@app.route('/logout')
@login_required # Necesită autentificare
def logout():
    logout_user()
    return redirect(url_for('login'))

# Ruta principală - pagina de start
@app.route('/')
@login_required
def index():

    # Obținem toate itemele din inventar
    items = db.session.execute(db.select(InventoryItem)).scalars().all()
    return render_template('index.html', items=items)

# Ruta pentru adăugarea unui item nou
@app.route('/add_item', methods=['GET', 'POST'])
@login_required
def add_item():
    if request.method == 'POST':

        # Obținem datele din formular
        inventory_number = int(request.form['inventory_number'])
        book_title = BOOKS_INVENTORY.get(inventory_number, "Unknown Book")
        personal_note = request.form.get('personal_note', '').strip()

        # Combinăm titlul cărții cu nota personală
        full_description = f"{book_title}\nNote: {personal_note}" if personal_note else book_title
        # Creăm un nou item în inventar
        new_item = InventoryItem(
            inventory_number=inventory_number,
            description=full_description,
            status=request.form['status']
        )
        # Salvăm în baza de date
        db.session.add(new_item)
        db.session.commit()
        flash('Item added successfully')
        return redirect(url_for('index'))
    return render_template('add_item.html', books=BOOKS_INVENTORY)

# Ruta pentru rezervarea/eliberarea unui item
@app.route('/book/<int:id>')
@login_required
def book_item(id):
    item = db.session.get(InventoryItem, id)
    if not item:
        flash('Item not found')
        return redirect(url_for('index'))

    # Schimbăm statusul de rezervare
    if item.booked == 'Free':
        item.booked = 'In use'
    else:
        item.booked = 'Free'
    db.session.commit()
    return redirect(url_for('index'))

# Ruta pentru editarea unui item
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_item(id):
    item = db.session.get(InventoryItem, id)
    if not item:
        flash('Item not found')
        return redirect(url_for('index'))

    if request.method == 'POST':

        # Actualizăm datele itemului
        item.inventory_number = request.form['inventory_number']
        item.description = request.form['description']
        item.status = request.form['status']
        db.session.commit()
        flash('Item updated successfully')
        return redirect(url_for('index'))
    return render_template('edit.html', item=item)

# Ruta pentru ștergerea unui item
@app.route('/delete/<int:id>')
@login_required
def delete_item(id):
    item = db.session.get(InventoryItem, id)
    if item:
        db.session.delete(item)
        db.session.commit()
        flash('Item deleted successfully')
    else:
        flash('Item not found')
    return redirect(url_for('index'))

# Funcție pentru crearea utilizatorului admin implicit
def create_default_user():
    user = db.session.execute(db.select(User).filter_by(username='admin')).scalar_one_or_none()
    if not user:
        user = User(
            username='admin',
            password=generate_password_hash('admin123')
        )
        db.session.add(user)
        db.session.commit()

# Punctul de intrare al aplicației
if __name__ == '__main__':
    with app.app_context():

        # Creăm tabelele în baza de date și utilizatorul admin
        db.create_all()
        create_default_user()
        # Pornim serverul în mod debug
    app.run(debug=True)
