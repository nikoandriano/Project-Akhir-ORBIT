import streamlit as st
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

st.set_page_config(page_title="FAQ", page_icon="media/logo.png", layout="wide")
st.sidebar.image("media/logo.png")
st.sidebar.title("EnZone")

model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

model.eval()

def generate_response(prompt, max_length=100):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    with torch.no_grad():
        output = model.generate(input_ids, max_length=max_length, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95)

    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

# FAQ data
faq_data = {
    "What is EnZone?": "EnZone is an Energy PLTB Potential Zone Application.",
    "How does EnZone work?": "EnZone utilizes advanced algorithms and data analysis to identify potential zones for PLTB (Pembangkit Listrik Tenaga Bayu) or wind power plants.",
    "What is PLTB?": "PLTB stands for Pembangkit Listrik Tenaga Bayu, which translates to Wind Power Plant in English.",
    "Is EnZone available for public use?": "Yes, EnZone is designed to be accessible for public use to promote sustainable energy practices.",
    "How can I access EnZone?": "You can access EnZone through its official website or application, which provides an intuitive interface for users to explore potential PLTB zones.",
    "What data does EnZone use for analysis?": "EnZone utilizes various data sources, including geographical data, wind patterns, and environmental factors, to analyze and identify potential PLTB zones.",
    "Are there any fees associated with using EnZone?": "The basic access to EnZone is often free, but there might be premium features or services that require a subscription or payment.",
    "Can EnZone be used globally?": "EnZone's applicability depends on the availability of relevant data for different regions. It is designed to be adaptable to various geographical locations.",
    "Is there technical support for EnZone users?": "Yes, EnZone typically provides technical support to users to ensure a smooth experience and address any issues they may encounter."
}
st.markdown(
    """
    <style>
        .reportview-container .main .block-container {
            max-width: 1200px;
            padding-top: 2rem;
            padding-right: 2rem;
            padding-left: 2rem;
            padding-bottom: 2rem;
        }
        h1 {
            text-align: center;
            color: #7ED957;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Frequently Ask Question")
st.write("Welcome to EnZoBot! Ask Me Anything About Energy PLTB Potential Zone.")

user_input = st.text_input("Type Your Question Here:", "")

if user_input:
    if user_input in faq_data:
        st.text("EnZoBot:" + faq_data[user_input])
    else:
        bot_response = generate_response(user_input)
        st.text("EnZoBot:" + bot_response)

st.sidebar.markdown(
    """
    **Informasi Kontak**\n
    **Telepon       : +628-9560-6415-240**\n
    **Instagram     : enzone_id**\n
    **Email         : support.id@enzone.com**\n


    Hak Cipta © 2023 EnZone: Energy PLTB Potential Zone Application
    """
)
