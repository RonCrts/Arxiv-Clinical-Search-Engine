# Arxiv-Clinical-Search-Engine

This is a Streamlit app that allows users to search for medical papers on Arxiv and analyze the entities using a Medical NER (Named Entity Recognition) model. The app has a sidebar where users can enter a search query and select the maximum number of results they want to see. The app then uses the Arxiv API to retrieve the results and displays them in the main section of the app.

For each result, the app displays the title, link, and a summary of the paper. The summary is analyzed using the Medical NER model, which can recognize medical entities like problem, test, treatment, etc. The app then highlights the recognized entities in the summary by wrapping them in a span tag with a color that corresponds to the type of entity. The app also displays a pie chart of the top 3 entities recognized in the summary.
