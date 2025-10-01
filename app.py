# ==============================================================================
# Meeting Transcript Topic Modeler & Action Item Extractor - Streamlit App
# ==============================================================================

import streamlit as st

# =======================
# 0. Streamlit Page Config
# =======================
st.set_page_config(
    page_title="Meeting Analyzer",
    layout="wide"
)

# =======================
# 1. Imports
# =======================
import pandas as pd
import joblib
import spacy
import re
import os
from collections import Counter
from gensim.corpora import Dictionary

# ==============================================================================
# 1. Load Models and Assets
# ==============================================================================
@st.cache_resource
def load_models():
    """Load all necessary models and assets from disk."""
    model_dir = 'models'
    if not os.path.exists(model_dir):
        st.error(f"Error: The 'models' directory was not found. Please run the `Meeting_Analysis_Model.ipynb` notebook first to generate the models.")
        return None, None, None

    try:
        lda_model = joblib.load(os.path.join(model_dir, 'lda_model.joblib'))
        dictionary = joblib.load(os.path.join(model_dir, 'dictionary.joblib'))
        nlp = spacy.load("en_core_web_sm")
        print("✅ Models loaded successfully.")
        return lda_model, dictionary, nlp
    except FileNotFoundError as e:
        st.error(f"Error loading a model file: {e}. Make sure all model files exist in the 'models' directory.")
        return None, None, None
    except Exception as e:
        st.error(f"An unexpected error occurred while loading models: {e}")
        return None, None, None


lda_model, dictionary, nlp = load_models()

# ==============================================================================
# 2. Core Analysis Functions
# ==============================================================================
def preprocess_for_lda(text, nlp_model):
    if not text or not isinstance(text, str):
        return []
    doc = nlp_model(text.lower().strip())
    tokens = [
        token.lemma_
        for token in doc
        if not token.is_stop and not token.is_punct and token.is_alpha
    ]
    return tokens

def predict_topics(text, lda, dic, nlp_model):
    if not all([text, lda, dic, nlp_model]):
        return "Models not loaded.", []

    processed_tokens = preprocess_for_lda(text, nlp_model)
    if not processed_tokens:
        return "Could not identify significant topics from the input text.", []

    bow_corpus = dic.doc2bow(processed_tokens)
    topic_probabilities = lda.get_document_topics(bow_corpus, minimum_probability=0.2)
    
    sorted_topics = sorted(topic_probabilities, key=lambda x: x[1], reverse=True)
    
    if not sorted_topics:
        return "No dominant topic found.", []
        
    top_topic_id, top_topic_prob = sorted_topics[0]
    topic_keywords_raw = lda.print_topic(top_topic_id)
    topic_keywords = ", ".join([word.split('*')[1].strip().strip('"') for word in topic_keywords_raw.split(' + ')])

    main_topic_str = f"**Topic {top_topic_id + 1}** (Confidence: {top_topic_prob:.2%})"
    return main_topic_str, topic_keywords

def extract_action_items(text, nlp_model):
    if not text or not nlp_model:
        return []
        
    doc = nlp_model(text)
    action_items = []
    action_keywords = ["i will", "we will", "we need to", "i'll", "let's", "next step", "action item", "to-do", "task is", "plan is", "agreed to"]
    responsibility_verbs = ["send", "create", "complete", "organize", "schedule", "follow up", "prepare", "review", "draft", "finalize"]
    modal_verbs = ["should", "must", "will", "need to"]
    
    for sent in doc.sents:
        sent_lower = sent.text.lower()
        found = False
        if any(keyword in sent_lower for keyword in action_keywords):
            found = True
        else:
            lemmas = [token.lemma_ for token in sent]
            if any(m in lemmas for m in modal_verbs) and any(v in lemmas for v in responsibility_verbs):
                found = True
        
        if found:
            action_items.append(sent.text.strip())
            
    return list(pd.Series(action_items).unique())

def extract_entities(text, nlp_model):
    if not text or not nlp_model:
        return []
    doc = nlp_model(text)
    allowed_labels = ["PERSON", "ORG", "DATE", "GPE"]
    entities = [(ent.text.strip(), ent.label_) for ent in doc.ents if ent.label_ in allowed_labels]
    return Counter(entities).most_common(10)

# ==============================================================================
# 3. Streamlit User Interface
# ==============================================================================
st.title("Meeting Transcript Analyzer")
st.markdown("This tool uses Topic Modeling and NLP to extract key insights from meeting transcripts.")

example_transcript = """
Meeting Chairman (Mark): Good morning. The main agenda today is our Q3 marketing strategy. Alice, can you start us off?
Alice Linnes: Of course. I think our biggest gap is social media engagement. Customers today expect faster, more personal interactions on platforms like Twitter and LinkedIn.
Donald Peters: I agree. Our current response time is over 24 hours. We should aim for under 4 hours.
Jennifer Miles: That’s a valid point, but speed isn't everything. We need to ensure the quality of the interaction. I will draft a proposal for a new set of engagement guidelines by next Friday.
Meeting Chairman (Mark): Excellent initiative, Jennifer. Let's make that an official action item. Donald, can you and your team review our current software tools and see if we need an upgrade?
Donald Peters: We will get on that and report back in the next meeting on October 15th. We'll check with the IT department at head office.
"""

transcript_input = st.text_area(
    "**Paste your full meeting transcript here:**",
    value=example_transcript,
    height=300,
    help="The full text of the conversation, including speaker names."
)

if st.button("Analyze Transcript", type="primary", use_container_width=True):
    if lda_model is None:
        st.stop()
        
    if not transcript_input.strip():
        st.warning("Please paste a transcript to analyze.")
    else:
        with st.spinner("Analyzing your transcript..."):
            main_topic, keywords = predict_topics(transcript_input, lda_model, dictionary, nlp)
            actions = extract_action_items(transcript_input, nlp)
            entities = extract_entities(transcript_input, nlp)

            st.divider()
            st.header("Analysis Results")
            
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Discovered Topic")
                st.markdown(f"The main theme appears to be: {main_topic}")
                st.markdown(f"**Keywords:** *{keywords}*")
                
                st.subheader("Key Entities Mentioned")
                if entities:
                    entity_df = pd.DataFrame(entities, columns=['Entity', 'Count'])
                    entity_df['Entity'] = entity_df['Entity'].apply(lambda x: f"{x[0]} ({x[1]})")
                    entity_df['Count'] = entity_df['Count']
                    st.dataframe(entity_df[['Entity', 'Count']], use_container_width=True, hide_index=True)
                else:
                    st.markdown("No significant named entities were identified.")

            with col2:
                st.subheader("Action Items")
                if actions:
                    for i, item in enumerate(actions, 1):
                        st.markdown(f"{i}. {item}")
                else:
                    st.info("No specific action items were identified in the text.")
