from lib.musictrack import*
"""
Start with empty list, nothing added
"""
def test_empty_list():
    musictracked = MusicTracker() 
    assert musictracked.musiclist()== []
"""
listened to one song. add song to list
"""
def test_listened_one_song():
    musictracked = MusicTracker()
    musictracked.add("Ippos song") 
    assert musictracked.musiclist() == ["Ippos song"]

"""
listened to multiple songs. add songs to list
"""
def test_listened_mutiple_songs():
    musictracked = MusicTracker()
    musictracked.add("Ippos song")
    musictracked.add("Echos sing song") 
    musictracked.add("Rengar sing song") 
    assert musictracked.musiclist() == ["Ippos song", "Echos sing song", "Rengar sing song"]
