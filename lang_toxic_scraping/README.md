# Scraping YouTube for Language Identification and Toxicity Detection Tasks

In this project we attempt to achieve the following goals:

- Creating a language dataset including Greeklish
- Crawling YouTube videos which include both Greek and Greeklish comments
- Training a language identification classifier
- Training a LLM-based toxicity classifier
- Using the LLM classifier to produce data for, and train a traditional ML toxicity classifier
- Applying our language identification and toxicity classifiers on the crawled YouTube videos and identifying interesting facts and trends

## Directory Structure

The project is structured as follows:
- lang_identification.ipynb: is the main Jupyter Notebook containing the project code
- prompts.pdf: Supplemental material containing the prompts used for the toxicity LLM classifier
- report.pdf: Supplemental material containing Figures, Tables and analysis on the results of the project

- src: a library of general functions for Data Science tasks
- tasks: task-specific modules
- data: the input data
- output: the output data (.csv)
- results: Graphs, Tables and Figures produced in the project