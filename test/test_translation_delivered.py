from . import average

def test_sample():
    for obj in average.translation_delivered_generate("testfile/teste.txt"):
        print(obj.timestamp.minute)
