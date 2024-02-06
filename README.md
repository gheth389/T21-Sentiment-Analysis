# Project Name: Sentiment Analysis and Text Cleaning

## Table of Contents
1. [Overview](#overview)
2. [Requirements](#requirements)
    - [Installation](#installation)
    - [Dataset](#dataset)
3. [Usage](#usage)
    - [Sentiment Analysis of Specific Review (Criteria 4 Part 1)](#sentiment-analysis-of-specific-review-criteria-4-part-1)
    - [Similarity Analysis between Two Reviews (Criteria 4 Part 2)](#similarity-analysis-between-two-reviews-criteria-4-part-2)
4. [Notes](#notes)
5. [Disclaimer](#disclaimer)
6. [Credits](#credits)

## Overview
This Python script is designed to perform sentiment analysis on a dataset of Amazon product reviews obtained from Kaggle. It utilizes the spaCy library for natural language processing and incorporates the spacytextblob extension for sentiment analysis. Additionally, the script includes functions for cleaning and processing individual reviews, allowing for the analysis of specific entries. The script also demonstrates the calculation of sentiment similarity between two predefined reviews.

## Requirements
- Python 3.x
- pandas
- spacy
- spacytextblob

### Installation
Ensure you have the required libraries installed by running:
```bash
pip install pandas spacy spacytextblob
python -m spacy download en_core_web_sm
```

### Dataset
1. Download the dataset from Kaggle using the following link: [Consumer Reviews of Amazon Products](https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products).
2. Place the downloaded CSV file (e.g., "amazon_product_reviews.csv") in the same directory as the script.

## Usage

### Sentiment Analysis of Specific Review (Criteria 4 Part 1)
1. Execute the script.
2. Input the row number of the review you want to analyze.
3. The script will display the sentiment analysis results for the selected review.

### Similarity Analysis between Two Reviews (Criteria 4 Part 2)
1. Uncomment and set the values for `compare_1` and `compare_2` to the row numbers of the reviews you want to compare.
2. Execute the script.
3. The script will display the similarity score between the two selected reviews.

## Notes
- The script reads the dataset from the file "amazon_product_reviews.csv" (Criteria 1).
- Cleaning and processing of all reviews are performed, creating a new column with the processed results (Criteria 2).
- The `clean_text` function allows the cleaning of individual reviews, making it unnecessary to analyze the entire dataset for certain criteria (Criteria 3).

## Disclaimer
This script assumes that the required dataset ("amazon_product_reviews.csv") is available and follows the expected structure. Ensure that the file is present in the same directory as the script before running. Additionally, the script is designed for educational purposes and may require modifications for specific use cases.

## Credits
- Author: Geoffrey Hetherington
- Date: 06/02/2024
- Contributions: Dataset from Kaggle using the following link: [Consumer Reviews of Amazon Products](https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products)
