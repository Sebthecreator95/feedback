from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

bcrypt = Bcrypt()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class User(db.Model):
    """User model"""
    @property
    def full_name(self):
        """Get Full Name"""
        return f'{self.first_name} {self.last_name}'
    def __repr__(self):
        u = self
        return f'<User_id={u.id} username={u.username} first_name={u.first_name} last_name={u.last_name} email={u.email}>'

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True) 
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    feedback = db.relationship("Feedback", backref="user", cascade="all, delete-orphan")
    # start_register
    @classmethod
    def register(cls, username, password, email, first_name, last_name):
        """Register user w/hashed password & return user."""

        hashed = bcrypt.generate_password_hash(password)
        # turn bytestring into normal (unicode utf8) string
        hashed_utf8 = hashed.decode('utf8')

        # return instance of user w/username and hashed pwd
        return cls(username=username, password=hashed_utf8, email=email, first_name=first_name, last_name=last_name)

    # start_authenticate
    @classmethod
    def authenticate(cls, username, password):
        """Validate that user exists & password is correct.

        Return user if valid; else return False.
        """

        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, password):
            # return user instance
            return u
        else:
            return False


class Feedback(db.Model):
    """Feedback Model"""
    def __repr__(self):
        f = self
        return f'<Feedback_id={f.id} username={f.username} title={f.title} content={f.content}>'

    __tablename__= 'feedback'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text,nullable=False)
    username = db.Column(db.String(20), db.ForeignKey('users.username'),nullable=False)
    