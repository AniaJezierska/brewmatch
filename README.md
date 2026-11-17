# BrewMatch — AI Coffee Machine Finder

An AI assistant designed to help users compare coffee machines based on their budget, available space, and preferences. Recommendations will include explanations and links to supporting sources.

**Status:** Planning the first version. Implementation has not started.

## About the project

Choosing a coffee machine often means switching between product pages, specifications, and manuals. I want to bring that information together so users can describe what they need, narrow down their options, and understand the differences.

The project combines structured product filtering, document retrieval, and LLM-generated responses. My main focus is whether recommendations meet the user's requirements and whether the explanations are supported by product documentation.

## Initial scope

The first version will cover around 20 coffee machines. Starting with a small catalog will let me check the source data and evaluate the answers in detail.

Planned features:

- Search by budget, dimensions, and preferences.
- Compare two products from the catalog.
- Recommend up to three matching models with explanations.
- Answer questions about features and cleaning.
- Include sources and clearly flag missing information.

Prices will come from the catalog, with a recorded collection date. Live price tracking and purchasing are outside the initial scope.

## Example questions

The application will initially support questions in Polish, such as:

- “Szukam ekspresu do 2000 zł o szerokości do 25 cm.”
- “Piję głównie czarną kawę. Które modele będą łatwe w czyszczeniu?”
- “Czym różnią się te dwa ekspresy?”
- “Czy wyjmowane części tego modelu można myć w zmywarce?”

## Technical approach

Price and dimension constraints will be checked through filtering in application code. Retrieval will provide relevant passages from product descriptions and manuals.

The LLM will use the selected products and retrieved content to generate an answer with source references. This follows a retrieval-augmented generation (RAG) approach.

This separation will let me evaluate filtering, retrieval, and answer generation independently.

## Evaluation

I will create a set of questions with expected outcomes and check whether the application:

- Respects budget and dimension constraints.
- Supports its explanations with relevant sources.
- Clearly identifies missing product data.
- Reports when no products match.
- Avoids guessing when the documentation does not contain an answer.

For example, a machine with an unknown width should not be presented as a confirmed fit for a 25 cm space. Missing cleaning instructions should not be treated as permission to put parts in a dishwasher.

## Next steps

- [ ] Build the product catalog and collect source documentation.
- [ ] Implement filtering and retrieval.
- [ ] Generate answers with source references.
- [ ] Evaluate results and investigate errors.
- [ ] Add setup instructions and a demo.
