from transformers import pipeline

pipe = pipeline("image-classification", model="trpakov/vit-face-expression")
def query(filename):
    return pipe(filename)