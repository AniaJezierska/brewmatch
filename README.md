# BrewMatch — AI Coffee Machine Finder

BrewMatch helps people find a coffee machine that fits their budget and counter space. Next, I want to use product manuals to help people compare models and answer practical questions, such as whether a particular part is dishwasher-safe.

**Status:** The local FastAPI demo searches a sample catalog of three fictional machines. It returns matching models, a short answer in English, and the name of the catalog it searched.

## About the project

Choosing a coffee machine often means switching between product pages, specifications, and manuals. I want to bring that information together so users can describe what they need, narrow down their options, and understand the differences.

I started with a practical question: if a machine’s width is missing, can I recommend it for a 25 cm space? BrewMatch excludes that machine when a width limit is set. You can still look it up by name and see that its width is unknown.

## Run the demo locally

From the repository root on macOS or Linux, run:

```bash
python3.11 -m venv .venv
.venv/bin/python -m pip install fastapi uvicorn
.venv/bin/python -m uvicorn main:app --reload
```

Open [the interactive API docs](http://127.0.0.1:8000/docs), expand `POST /search`, and select **Try it out**. Enter this request and select **Execute**:

```json
{
  "question": "Which coffee machine fits on my counter?",
  "max_price_usd": 200,
  "max_width_cm": 25
}
```

The demo returns:

```json
{
  "answer": "BrewMatch Mini costs $129 and is 19 cm wide.",
  "matches": [
    { "name": "BrewMatch Mini", "price_usd": 129, "width_cm": 19 }
  ],
  "source_id": "machines.json"
}
```

## Five searches to try

The demo recognizes model names in the question. Use the optional `max_price_usd` and `max_width_cm` fields to set numeric limits.

| Question | Request filters | Expected result |
| --- | --- | --- |
| Which coffee machine fits on my counter? | `max_price_usd: 200`, `max_width_cm: 25` | BrewMatch Mini |
| Which machines fit my budget? | `max_price_usd: 100` | An empty list and a message explaining that no machines match |
| Can you show me the Home model? | None | BrewMatch Home, $229, 28 cm wide |
| How wide is the Pro model? | None | BrewMatch Pro, with its width reported as unknown |
| Will the Pro model fit on my counter? | `max_width_cm: 25` | An empty list because the catalog has no width for Pro |

## Technical approach

FastAPI validates each request before searching the catalog. A negative budget returns a validation error (HTTP 422). A valid budget below the cheapest model returns HTTP 200 with an empty list. In both successful searches and searches with no matches, `source_id` identifies the catalog used.

For the next version, I plan to collect specifications and manuals for around 20 models and record when each price was collected. After filtering the catalog, the application will retrieve relevant passages for the remaining products. An LLM will use those passages to explain differences and cite the supporting documents.

## Evaluation

I’ve manually checked four cases: a product that fits the requested limits, a search with no matches, a model-name lookup, and a negative budget. As the catalog grows, I’ll turn these examples into regression tests.

For questions about features and cleaning, I’ll also check whether each cited passage supports the answer for that exact model. For example, a manual might say that a drip tray is removable. Before recommending that it go in the dishwasher, the assistant needs a passage confirming that it is dishwasher-safe.

## Next steps

- Expand the sample catalog and record product sources and price collection dates.
- Retrieve relevant passages from specifications and manuals.
- Compare two models and explain up to three recommendations using cited passages.
- Build an evaluation set and document cases where the system gets an answer wrong.
- Record a short walkthrough of the working assistant.

Live price tracking and purchasing are outside the initial scope.