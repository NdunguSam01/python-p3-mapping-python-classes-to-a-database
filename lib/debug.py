#!/usr/bin/env python3

from config import CONN, CURSOR
from song import Song
# import ipdb;

if __name__ == '__main__':
    Song.create_table()

    CURSOR.execute("PRAGMA table_info(songs)").fetchall()

    hello=Song("Hello","25")
    hello.save()

    despacito=Song("Despacito","Vida")
    despacito.save()

    songs=CURSOR.execute('SELECT * FROM songs').fetchall()
    print("All songs:")
    for song in songs:
        print(song)