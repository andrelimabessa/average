from . import average

def test_sample():
    result = []
    for item in average.translation_delivered_parser("testfile/teste.txt"):
        result.append(item)
    

