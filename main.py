from medical_ner import MedicalNER
from arxiv_api import arxiv_clinical_api
import streamlit as st
import plotly.express as px


st.title('Arxiv Clinical Search Engine')
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/ArXiv_web.svg/1280px-ArXiv_web.svg.png")
st.title('Medical NER model')
st.info('This project uses Medical documents NER model by fine tuning BERT, it can recognize medical entities like problem, test, treatment, etc.')
st.sidebar.title('Search Engine')
st.sidebar.markdown('Search for medical papers on Arxiv and analyze the entities using medical NER model.')
search_query = st.sidebar.text_input('Search Query', 'covid-19')
max_results = st.sidebar.slider('Max Results', 1, 10, 5)
api = arxiv_clinical_api(search_query, max_results)
results = api.get_results()
ner = MedicalNER()
st.info('Showing {} results for: {}'.format(max_results, search_query))
for result in results[:max_results]:
    st.write('---')
    st.title(result['title'])
    st.write(result['link'])
    ner_df = ner.predict(result['summary'])
    tokens = ner_df['Token'].tolist()
    entities = ner_df['Entity'].tolist()
    colors = ner_df['Color'].tolist()
    summary_tokens = result['summary'].split()
    summary_with_entities = []
    for token in summary_tokens:
        if token in tokens:
            entity = entities[tokens.index(token)]
            color = colors[tokens.index(token)]
            summary_with_entities.append(f"<span style='color:{color}'>{token} ({entity})</span>")
        else:
            summary_with_entities.append(token)
    summary_paragraph = ' '.join(summary_with_entities)
    st.write(summary_paragraph, unsafe_allow_html=True)
    st.title('Top 3 Entities')
    fig = px.pie(ner_df['Entity'].value_counts()[:3], values=ner_df['Entity'].value_counts()[:3], names=ner_df['Entity'].value_counts()[:3].index)
    st.plotly_chart(fig)
    st.write(result['link'])
    st.write('---')
