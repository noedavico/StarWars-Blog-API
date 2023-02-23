from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    fecha_suscripcion =  db.Column(db.String(250), nullable=False)
    apellido =  db.Column(db.String(250), nullable=False)
    email =  db.Column(db.String(250), nullable=False)
    favoritos = db.relationship('Favoritos',backref='user', lazy=True)
    
    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "fecha_suscripcion": self.fecha_suscripcion,
            "apellido": self.apellido,
            "email": self.email,
            "favoritos": self.favoritos,
            # do not serialize the password, its a security breach
        }
        
class Personajes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    altura = db.Column(db.String(250), nullable=False)
    genero =  db.Column(db.String(250), nullable=False)
    peso =  db.Column(db.String(250), nullable=False)
    favoritos = db.relationship('Favoritos',backref='personajes', lazy=True)        
    
    def __repr__(self):
        return '<Personajes %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "altura": self.altura,
            "genero": self.genero,
            "peso": self.peso,
            "favoritos": self.favoritos,
            # do not serialize the password, its a security breach
        }
        
class Planetas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    diametro = db.Column(db.String(250), nullable=False)
    periodo_orbital =  db.Column(db.String(250), nullable=False)
    poblacion =  db.Column(db.String(250), nullable=False)
    favoritos = db.relationship('Favoritos',backref='planetas', lazy=True)  
    
    def __repr__(self):
        return '<Planetas %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "diametro": self.diametro,
            "periodo_orbital": self.periodo_orbital,
            "poblacion": self.poblacion,
            "favoritos": self.favoritos,
            }
        
class Favoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planetas_id = db.Column(db.Integer, db.ForeignKey('planetas.id'))
    personajes_id = db.Column(db.Integer, db.ForeignKey('personajes.id'))
    
    def __repr__(self):
        return '<Favoritos %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "planetas_id": self.planetas_id,
            "personajes_id": self.personajes_id,
            # do not serialize the password, its a security breach          
            }
            