from . import average

def test_sample():
    for obj in average.translation_delivered_generate("teste.txt"):
        print(obj.timestamp.minute)
