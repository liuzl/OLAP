from fastapi import FastAPI
import stanza
import jieba
import jieba.posseg as pseg
jieba.enable_paddle()

app = FastAPI()
nlp = stanza.Pipeline(lang='zh', processors='tokenize')


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/nlp")
def process(text: str):
    text = text.strip()
    if text == "":
        return {"err": "empty text"}
    ret = []
    for s in nlp(text).sentences:
        r = pseg.cut(s.text, use_paddle=True)
        ner = {'PER':set(), "LOC":set(), "ORG":set(), "TIME":set()}
        words = []
        for w, pos in r:
            if pos in ner: ner[pos].add(w)
            words.append(w)
        e = {"text": s.text, "words": words, "ner": ner}
        ret.append(e)
    return ret

