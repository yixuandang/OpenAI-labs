from fastapi import FastAPI
from pydantic import BaseModel
from Langchain_Semantic_Search_Pinecone import get_answer

app = FastAPI(
    title="MosesAI API",
    description="This API allows to ask Talmud questions. \
                Click on the blue GET button, \
                Then click on 'Try it out', \
                Then ask your question. ",
    version="0.0.7",
)


class Item(BaseModel):
    question: str
    answer: str


@app.get("/{question}", response_model=Item, summary="Ask Moses AI a question",
         description="Click on 'Try it out', then ask away!")
def read_item(question: str):
    answer = get_answer(question)
    with open('OpenAI.log', 'a') as f:
        f.write("Q: " + question + "\n")
        f.write("A: " + answer + "\n")
    return {"question": question, "answer": answer}


@app.get("/{question_with_options}/{num_sources}")
def read_item(question_with_options: str, num_sources: int):
    answer = get_answer(question_with_options)
    with open('OpenAI.log', 'a') as f:
        # Write the string to the file
        f.write("O: " + str(num_sources) + "\n")
        f.write("Q: " + question_with_options + "\n")
        f.write("A: " + answer + "\n")
    return {"question": question_with_options, "answer": answer}


@app.get("/", summary="Who am I?", description="Shalom. I am MosesAI, and right now, I know Talmud Illuminated")
def read_root():
    return {"Hello": "Shalom"}