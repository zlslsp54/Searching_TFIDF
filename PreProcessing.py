import re

# '[Music, Applause, ...]' <- 전처리 and remove tuple

def preprocessing(captions):
    clean_captions = []

    for caption in captions:
        caption = re.sub("[^a-zA-Z]", " ", str(caption)).strip()
        words = caption.lower().split()
        clean_caption = ' '.join(words)
        clean_captions.append(clean_caption)
    return clean_captions
