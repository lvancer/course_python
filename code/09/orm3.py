# ORM3

dbfile = "C:\\Users\\lin02\\AppData\\Roaming\\DBeaverData\\workspace6\\.metadata\\sample-database-sqlite-1\\Chinook.db"

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, Table  # 引入字段定义类

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
    ArtistId = Column(Integer, ForeignKey('Artist.ArtistId'), nullable=False)
    Artist = relationship("Artist", backref="Album")

class Track(Base):

    __tablename__ = 'Track'

    TrackId = Column(Integer, primary_key=True, nullable=False)
    Name = Column(String(200), nullable=False)
    AlbumId = Column(Integer, ForeignKey('Album.AlbumId'))
    Album = relationship("Album", backref="Track")
    Bytes = Column(Integer)


# 关联表
from sqlalchemy import Table
playlist_track = Table(
    "PlaylistTrack",        # 表名
    Base.metadata,          # 表类型
    Column("PlaylistId", Integer,
           ForeignKey("Playlist.PlaylistId"), primary_key=True),
    Column("TrackId", Integer,
           ForeignKey("Track.TrackId"), primary_key=True)
)


class Playlist(Base):

    __tablename__ = 'Playlist'

    PlaylistId = Column(Integer, primary_key=True, nullable=False)
    Name = Column(String(200), nullable=False)
    # 多对多
    Tracks = relationship("Track", backref="Playlist", secondary=playlist_track)


if __name__ == '__main__':
    Session = sessionmaker(bind=engine)

    # 查询
    # session = Session()
    # playlist = session.query(Playlist).first()
    # print(playlist.Name)
    # for track in playlist.Tracks:
    #     print('\t{} 【专辑:{}】 【作者：{}】'
    #           .format(track.Name, track.Album.Title, track.Album.Artist.Name))
    # session.close()

    # 增加
    session = Session()
    playlist = session.query(Playlist).filter_by(PlaylistId=2).first()
    track = session.query(Track).filter_by(TrackId=3503).first()
    playlist.Tracks.append(track)
    session.add(playlist)
    session.commit()
    session.close()






