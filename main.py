from text_analyze.text_analyze import grab_text_from_article, ner_with_counts, pos_with_lemma


from fastapi import FastAPI
import collections

app = FastAPI()

@app.get("/")
async def root():
    return ("Welcome to our wonderful API!")

@app.get("/analyze-text/text")
async def grab_text(url: str = None):
    return {'article_text': grab_text_from_article(url)}

@app.get("/analyze-text/ner")
async def analyze_ner(url: str = None):
    return {'Entities': collections.Counter(str(tuple(item)) for item in ner_with_counts(grab_text_from_article(url)))}

@app.get("/analyze-text/pos")
async def analyze_pos(url: str):
    return {"Parts of Speech": pos_with_lemma(grab_text_from_article(url))}