# ORM2

dbfile = "C:\\Users\\lin02\\AppData\\Roaming\\DBeaverData\\workspace6\\.metadata\\sample-database-sqlite-1\\Chinook.db"

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey  # 引入字段定义类

from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///' + dbfile)
Base = declarative_base()


class Artist(Base):

    __tablename__ = 'Artist'

    ArtistId = Column(Integer, primary_key=True, nullable=False)
    Name = Column(String(120))


class Album(Base):

    __tablename__ = 'Album'

    AlbumId = Column(Integer, primary_key=True, nullable=False)
    Title = Column(String(160), nullable=False)
    # ArtistId = Column(Integer, nullable=False)
    # 外键
    ArtistId = Column(Integer, ForeignKey('Artist.ArtistId'), nullable=False)
    Artist = relationship("Artist", backref="Album")

class Track(Base):

    __tablename__ = 'Track'

    TrackId = Column(Integer, primary_key=True, nullable=False)
    Name = Column(String(200), nullable=False)
    # AlbumId = Column(Integer)
    # 外键
    AlbumId = Column(Integer, ForeignKey('Album.AlbumId'))
    Album = relationship("Album", backref="Track")
    Bytes = Column(Integer)

if __name__ == '__main__':
    Session = sessionmaker(bind=engine)

    # 查询
    # session = Session()
    # artists = session.query(Artist).all()     # 查询全部
    # tracks = session.query(Track).filter_by(AlbumId=1).all()    # 条件查询
    # tracks = session.query(Track)\
    #     .with_entities(Track.TrackId, Track.Name)\
    #     .filter_by(AlbumId=1).all()    # 部分字段
    # tracks = session.query(Track)\
    #     .order_by(Track.Bytes)\
    #     .filter_by(AlbumId=1).all()    # 排序
    # session.close()

    # 外键
    # session = Session()
    # album = session.query(Album).first()
    # artist = album.Artist   # 外键实体
    # print(artist.Name)
    # session.close()

    # 外键2
    # session = Session()
    # tracks = session.query(Track).all()
    # ret = []
    # for track in tracks:
    #     ret.append((track.Name, track.Album.Title))
    # print(ret)
    # session.close()



