# Practice 5: Python Regular Expressions

## Overview

This practice focuses on Python Regular Expressions (RegEx) and text parsing.

## Project Structure
Practice5/
├── receipt_parser.py
├── raw.txt
└── README.md

## Topics Covered

- Python re module
- Regular expression patterns
- Searching text with regex
- Extracting data from files
- Replacing and splitting strings

## Functions Used

### re.search()

Used to find the first matching pattern in text.

Example:
- Finding receipt date
- Finding total amount

### re.findall()

Used to find all matches.

Example:
- Extracting product prices
- Extracting product names

### re.sub()

Used to replace text patterns.

Example:
- Cleaning spaces and symbols

### re.split()

Used to split text using a pattern.

## Receipt Parser

The `receipt_parser.py` file reads `raw.txt` and extracts:

- Product names
- Product prices
- Total amount
- Date and time
- Payment method

The output is displayed in JSON format.

## Result

The project demonstrates how regular expressions can be used to process real text data and convert unstructured information into structured data.