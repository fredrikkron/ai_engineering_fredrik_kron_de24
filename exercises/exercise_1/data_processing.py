import json
from constants import DATA_PATH
from pydantic import BaseModel, Field
from pprint import pprint

def read_json_file(filename):
    with open(DATA_PATH / filename, "r") as file:
        data = json.load(file)
    
    return data

class Glossary(BaseModel):
    id: int
    word: str
    meaning: str

def glossary_data(filename):
    json_data = read_json_file(filename)
    return [Glossary.model_validate(glossary) for glossary in json_data]

if __name__=="__main__":
    glossaries = glossary_data("fastapi_glossary.json")
    pprint(glossaries)