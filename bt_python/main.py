import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

RAPIDAPI_HOST = "google-translate113.p.rapidapi.com"
RAPIDAPI_KEY = "5ec05ab7edmshbe10efb439ada79p17ec62jsnd15fba2b805b"
API_URL = f"https://{RAPIDAPI_HOST}/api/v1/translator/detect-language"

class TranslationRequest(BaseModel):
    text: str

@app.post("/detect-language/")
async def detect_language(request: TranslationRequest):
    payload = {"text": request.text}
    headers = {
        "x-rapidapi-host": RAPIDAPI_HOST,
        "x-rapidapi-key": RAPIDAPI_KEY,
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        raise HTTPException(status_code=response.status_code, detail=str(http_err))
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))

@app.get("/sample-data/")
async def get_sample_data():
    sample_data = [
        [
            {"text": "Hello, how are you?", "language": "English"},
            {"text": "Xin chào, bạn khỏe không?", "language": "Vietnamese"},
            {"text": "Hola, ¿cómo estás?", "language": "Spanish"},
            {"text": "Bonjour, comment ça va?", "language": "French"},
            {"text": "Hallo, wie geht es dir?", "language": "German"},
            {"text": "Ciao, come stai?", "language": "Italian"},
            {"text": "Sawubona Unjani？", "language": "Zulu"},
            {"text": "Halo, ciamar a tha thu?", "language": "Scots Gaelic"},

        ]

    ]
    return sample_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8888)
