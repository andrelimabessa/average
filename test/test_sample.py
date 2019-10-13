from . import translation_delivered_generate

def test_sample():
    for obj in translation_delivered_generate("teste.txt"):
        print(obj.timestamp.minute)
