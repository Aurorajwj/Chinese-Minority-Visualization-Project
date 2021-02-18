from . import db
class Nationmain(db.Model):
    __tablename__ = 'nationmain'
    name = db.Column(db.String(5),primary_key=True)
    comment = db.Column(db.String(50))
    overview = db.Column(db.String(400))
    badge = db.Column(db.String(50))
    clothing = db.Column(db.Integer)
class Area(db.Model):
    __tablename__='area'
    area =db.Column(db.String(255),primary_key=True)
    total =db.Column(db.Integer)
    han =db.Column(db.Integer)
    def __repr__(self):
        return 'Area %r'%self.area