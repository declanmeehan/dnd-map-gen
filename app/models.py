from . import db

class Map(db.Model):
    __tablename__ = "maps"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    tiles = db.relationship("Tile", backref="map", lazy="dynamic")

    def __repr__(self):
        return "<Map %r>" % self.name

class Tile(db.Model):
    __tablename__ = "tiles"

    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    image_path = db.Column(db.String(128), index=True)
    map_id = db.Column(db.Integer, db.ForeignKey("maps.id"))

    def __repr__(self)