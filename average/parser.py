from .translation_delivered import TranslationDelivered

def translation_delivered_generate(file_path):
    with open(file_path) as file:
        for line in file:
            x = TranslationDelivered(line)
            yield x
