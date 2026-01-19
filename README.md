# Lab 1 – Repo Organization

## Description
This program processes a directory of receipt images and uses the OpenAI API
to extract the receipt date, total amount, vendor name, and category.
The output is printed as a JSON object.

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY = "your_key"
```
## Run
```bash
make run
```



