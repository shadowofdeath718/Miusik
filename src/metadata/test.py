from mp3 import MP3Format
from flac import FlacFormat
from tags import tag_data


def test_tags_pair():
    song1 = FlacFormat('D:/Movies/Christina_Perri-Lovestrong-Deluxe_Edition/02-christina_perri-arms.flac')
    song2 = MP3Format('D:/Drive E/Music/Bruno Mars - It Will Rain.mp3')
    # lst = song1._get_tag(song1._get_raw(), 'TIT2')
    # print lst
    tag_pairs1 = song1.read_all()
    tag_pairs2 = song2.read_all()
    print tag_pairs1
    print tag_pairs2


def test_tags_module():
    print tag_data['album']

if __name__ == '__main__':
    test_tags_pair()
