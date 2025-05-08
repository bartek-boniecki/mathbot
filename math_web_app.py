import streamlit as st
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
import os
import re

load_dotenv()

st.title("🧠 Generator zadań matematycznych Bartka")

klasa = st.sidebar.selectbox("🧮 Klasa ucznia, gdzie 1-8 to klasy szkoły podstawowej, 9-12 to klasy szkół ponadpodstawowych, a 13-17 to roczniki studiów wyższych", [str(i) for i in range(1, 18)])
dzial = st.sidebar.text_input("Wskaż z jakiego działu potrzebujesz zadań, np.: arytmetyka (ułamki, potęgi i pierwiastki), algebra (wyrażenia algebraiczne, równania i nierówności), geometria (figury płaskie, figury przestrzenne, geometria analityczna), statystyka opisowa, rachunek prawdopodobieństwa, funkcje, ciągi, kombinatoryka, analiza matematyczna:  ", "pierwiastki")
licznik = st.sidebar.slider("📊 Ile zadań chcesz wygenerować?", 1, 20, 3)

def enforce_latex_blocks(text):
    text = re.sub(r'\\\((.*?)\\\)', r'$$\1$$', text)  # replace \( ... \)
    text = re.sub(r'\(([^()]*[=][^()]*)\)', r'$$\1$$', text)  # wrap equations inside (...) with $$
    return text

if st.button("🎲 Wygeneruj zadania"):
    agent = Agent(
        model=OpenAIChat(id="gpt-3.5-turbo"),
        description="Jesteś nauczycielem matematyki w szkole podstawowej, ponadpodstawowej, oraz wykładowcą na wydziale matematyki renomowanej uczelni, który wszystkim uczniom lub studentom daje na sprawdzianach własne zadania dodatkowe na ocenę celującą, które poziomem trudności wykraczają poza materiał, są na poziomie podstawy programowej o 2 lata wyżej niż poziom danej klasy/rocznika studiów (np. gdy uczeń jest w 6 klasie szkoły podstawowej, to Ty korzystasz z podstawy programowej dla 8 ósmej klasy, a gdy jest na 9 poziomie czyli w pierwszej klasie szkoły ponadpodstawowej, to korzystasz z zadań jak dla 3 klasy szkoły ponadpodstawowej itd.). Są zadaniami-zagadkami matematycznymi, których rozwiązanie wymaga pomyślenia, i nie wystarczy samo podstawienie do wzoru i wykonanie prostych obliczeń.",
        markdown=True
    )

    for i in range(1, licznik + 1):
        prompt = (
            f"Zaproponuj jedno zadanie-zagadkę z matematyki z działu {dzial}, dla ucznia z klasy {klasa}, które wykracza poza podstawę programową, jest powiązane z życiem codziennym."
            "Ważne: wszystkie wyrażenia matematyczne zapisz tylko jako LaTeX ujęty w `$$ ... $$`. Nie używaj nawiasów `(...)`, `\\(...\\)` ani pojedynczych `$...$`."
        )
        st.markdown(f"### 🧩 Zadanie {i}")
        with st.spinner("Myślę..."):
           response = agent.run(prompt)
           content = response.content if hasattr(response, 'content') else str(response)
           cleaned = enforce_latex_blocks(content)
           st.markdown(cleaned, unsafe_allow_html=True)