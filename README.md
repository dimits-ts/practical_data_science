# Practical Data Science

This repository houses three complete projects concerning Large Language Models (LLMs), data acquisition, dataset qualitative analysis and Natural Language Processing (NLP) tasks. These projects were developed during the MSc in Data Science of the Athens University Economics and Business.

[This supporting repository](https://github.com/dimits-exe/LLMs_prompting_annotation) features smaller projects connected to the ones showcased here. Their scope is more limited but they contain important exploration, code and experimentation on which these projects were based on.

The three projects contained in this repo can be found below:

## Greek Proverb LLM Annotation

Utilizing an LLM through Prompt Engineering to provide clusterings for a Greek proverb clustering task. Estimating annotator agreement, clustering cohesion and using human clusterings to pick the best LLM clusterings. [Found here](proverb_annot/proverb_analysis.ipynb).

## Scraping YouTube for Language Identification and (LLM) Toxicity Detection Tasks

[In this project](lang_toxic_scraping/lang_identification.ipynb) we attempt to achieve the following goals:

-   Creating a language dataset including Greeklish
-   Crawling YouTube videos which include both Greek and Greeklish comments
-   Training a language identification classifier
-   Training a LLM-based toxicity classifier
-   Using the LLM classifier to produce data for, and train a traditional ML toxicity classifier
-   Applying our language identification and toxicity classifiers on the crawled YouTube videos identifying interesting facts and trends


## LLM Text Detection

This project is an analysis on LLM detection based on [this Kaggle Challenge](https://www.kaggle.com/competitions/llm-detect-ai-generated-text).

We utilize different LLMs with varying prompts to generate a representative dataset of LLM generated essays. We analyze the quality of this dataset, create an optimal dataset, and train a best classifier on it. Comprised of [the notebook](llm_detection/notebooks/llm_detection.ipynb), a [README file](llm_detection/README.md) with extra information about prompting and dataset attribution and [presentation materials](llm_detection/presentation/Text%20Selection%20for%20LLM%20Detection.pptx).
