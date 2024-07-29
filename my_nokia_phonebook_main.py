from flask import Flask, render_template, request, jsonify
from sqlalchemy.exc import IntegrityError
from flask_sqlalchemy import SQLAlchemy
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(
    filename='app_log.log',
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d : %(levelname)s : %(module)s - %(funcName)s : %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

# Configure the SQLAlchemy part of the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.db'
db = SQLAlchemy(app)


# Define the Contact model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    mobile_number = db.Column(db.String(15), nullable=False, unique=True)
    email_id = db.Column(db.String(120), nullable=False, unique=True)


# Route to display all contacts
@app.get("/")
def index():
    contact_list = Contact.query.all()
    return render_template('index.html', contact_list=contact_list)


# Route to add a new contact
@app.post('/add-contact')
def add_contact():
    data = request.json
    if not all(key in data for key in ['full_name', 'mobile_number', 'email_id']):
        return jsonify({'error': 'Missing required fields'}), 400

    new_contact = Contact(
        full_name=data['full_name'],
        mobile_number=data['mobile_number'],
        email_id=data['email_id']
    )

    try:
        db.session.add(new_contact)
        db.session.commit()
        return jsonify({'message': 'Contact saved successfully'}), 201
    except IntegrityError as ie:
        db.session.rollback()
        app.logger.error(str(ie))
        return jsonify({'error': 'Duplicate mobile number or email id'}), 400
    except Exception as ex:
        db.session.rollback()
        app.logger.error(str(ex))
        return jsonify({'error': str(ex)}), 500


# Route to delete a contact
@app.delete('/delete-contact/<int:cid>')
def delete_contact(cid):
    contact = Contact.query.get_or_404(cid)
    try:
        db.session.delete(contact)
        db.session.commit()
        return jsonify({'message': 'Contact deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# Route to get a contact by id
@app.get('/get-contact/<int:cid>')
def get_contact(cid):
    contact = Contact.query.get_or_404(cid)
    try:
        return jsonify({
            'id': contact.id,
            'full_name': contact.full_name,
            'mobile_number': contact.mobile_number,
            'email_id': contact.email_id
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# Route to update a contact by id
@app.put('/update-contact/<int:cid>')
def update_contact(cid):
    contact = Contact.query.get_or_404(cid)
    data = request.json

    contact.full_name = data.get('full_name', contact.full_name)
    contact.mobile_number = data.get('mobile_number', contact.mobile_number)
    contact.email_id = data.get('email_id', contact.email_id)

    try:
        db.session.commit()
        return jsonify({'message': 'Contact updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=8181, debug=True)
