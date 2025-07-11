from fastapi import FastAPI
import uvicorn
from first_name import first
from last_name import last
from convertor import decimal_to_roman
import random

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Graveyard Name Generator API is working"}


def generate_graveyard_name():
    first_idx = random.randint(0, len(first) - 1)
    second_idx = random.randint(0, len(last) - 1)
    number = random.randint(1, 5000)
    numeral = decimal_to_roman(number)
    return f"{first[first_idx].lower()}_{last[second_idx].lower()}_{numeral}"

@app.get("/name/")
@app.get("/name/{number}")
def generate_name(number: int = 1):
    # Generate `number` names using different seeds
    names = [generate_graveyard_name() for _ in range(number)]
    return names

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
