import json
import re
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="BrewMatch")


@app.get("/health")
def health():
    return {"status": "ok"}

class SearchRequest(BaseModel):
    question: str = Field(min_length=1)
    max_price_usd: float | None = Field(default=None, ge=0)
    max_width_cm: float | None = Field(default=None, gt=0)


@app.post("/search")
def search(request: SearchRequest):
    catalog_path = Path(__file__).with_name("machines.json")
    machines = json.loads(catalog_path.read_text(encoding="utf-8"))

    # W tym katalogu nazwy modeli mają postać „BrewMatch Mini”.
    model_names = {machine["name"].split()[-1].casefold() for machine in machines}
    question_words = set(re.findall(r"\w+", request.question.casefold()))
    requested_models = model_names & question_words

    matches = []
    for machine in machines:
        if request.max_price_usd is not None and machine["price_usd"] > request.max_price_usd:
            continue

        width = machine["width_cm"]
        if request.max_width_cm is not None and (width is None or width > request.max_width_cm):
            continue

        model_name = machine["name"].split()[-1].casefold()
        if requested_models and model_name not in requested_models:
            continue

        matches.append(machine)

    if matches:
        lines = []
        for machine in matches:
            name = machine["name"]
            price = machine["price_usd"]
            width = machine["width_cm"]

            if width is None:
                lines.append(f"{name} costs ${price}. Its width is unknown.")
            else:
                lines.append(f"{name} costs ${price} and is {width} cm wide.")

        answer = "\n".join(lines)
    else:
        answer = "No coffee machines in the catalog match your criteria."

    return {
        "answer": answer,
        "matches": matches,
        "source_id": catalog_path.name,
    }