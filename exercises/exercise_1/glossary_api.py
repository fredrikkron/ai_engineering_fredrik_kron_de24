from fastapi import FastAPI, Query
from data_processing import glossary_data


glossaries = glossary_data("fastapi_glossary.json")

app = FastAPI()

# Create an endpoint /glossary which will return all words and their meaning.
@app.get("/glossary")
async def read_glossaries():
    return [glossary.model_dump() for glossary in glossaries]


# Create a query parameter to filter out a specific word
@app.get("/glossary/filter")
async def filter_word(word: str = Query(
    "URL",
    description="Specific word (URL as default) for filtering glossaries")
):
    filtered_words = [glossary for glossary in glossaries
                      if word.casefold() in glossary.word.casefold() or 
                      word.casefold() in glossary.meaning.casefold()]

    return [glossary.model_dump() for glossary in filtered_words]