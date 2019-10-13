from .translation_delivered import Translation_Delivered

def translation_delivered_generate(file_path):
    with open(file_path) as file:
        for line in file:
            x = Translation_Delivered(line)
            yield x
