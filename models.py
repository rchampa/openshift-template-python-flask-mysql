from flask.ext.sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()

from werkzeug import generate_password_hash, check_password_hash

class Administrador(db.Model):
  __tablename__ = 'administradores'
  email = db.Column(db.String(15), primary_key = True)
  password_hash = db.Column(db.String(54))
  registrado_en = db.Column(db.DateTime)
  actualizado_en = db.Column(db.DateTime)
  ultima_conexion = db.Column(db.DateTime)

   
  def __init__(self, email, new_password):
    self.email = email.title()
    self.set_password(new_password)
     
  def set_password(self, new_password):
    self.password_hash = generate_password_hash(new_password)
   
  def check_password(self, new_password):
    return check_password_hash(self.password_hash, new_password)