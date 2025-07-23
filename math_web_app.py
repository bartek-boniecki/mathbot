import os
import re
import openai
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

openai.api_key = os.getenv("OPENAI_API_KEY")
app = FastAPI()

# Allow CORS for all origins (or restrict to Carrd's domains for security)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, set your Carrd site URL instead of "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def enforce_latex_blocks(text):
    text = re.sub(r'\\\((.*?)\\\)', r'$$\1$$', text)
    text = re.sub(r'\(([^()]*[=][^()]*)\)', r'$$\1$$', text)
    return text

system_prompt = (
    "Jesteś nauczycielem matematyki w szkole podstawowej, ponadpodstawowej, oraz wykładowcą na wydziale matematyki renomowanej uczelni, "
    "który wszystkim uczniom lub studentom daje na sprawdzianach własne zadania dodatkowe na ocenę celującą, które poziomem trudności wykraczają poza materiał, "
    "są na poziomie podstawy programowej o 2 lata wyżej niż poziom danej klasy/rocznika studiów (np. gdy uczeń jest w 6 klasie szkoły podstawowej, "
    "to Ty korzystasz z podstawy programowej dla 8 ósmej klasy, a gdy jest na 9 poziomie czyli w pierwszej klasie szkoły ponadpodstawowej, "
    "to korzystasz z zadań jak dla 3 klasy szkoły ponadpodstawowej itd.). Są zadaniami-zagadkami matematycznymi, których rozwiązanie wymaga pomyślenia, "
    "i nie wystarczy samo podstawienie do wzoru i wykonanie prostych obliczeń."
)

@app.post("/generate")
async def generate(
    klasa: str = Form(...),
    dzial: str = Form(...),
    licznik: int = Form(...),
):
    tasks = []
    for i in range(1, licznik + 1):
        prompt = (
            f"Zaproponuj jedno zadanie-zagadkę z matematyki z działu {dzial}, dla ucznia z klasy {klasa}, które wykracza poza podstawę programową, jest powiązane z życiem codziennym."
            "Ważne: wszystkie wyrażenia matematyczne zapisz tylko jako LaTeX ujęty w `$$ ... $$`. Nie używaj nawiasów `(...)`, `\\(...\\)` ani pojedynczych `$...$`."
        )
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            max_tokens=700,
            temperature=0.9,
        )
        content = response.choices[0].message.content
        cleaned = enforce_latex_blocks(content)
        tasks.append(cleaned)
    return JSONResponse(content={"tasks": tasks})

