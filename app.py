import uvicorn
from fastapi import FastAPI
from fastapi import FastAPI

from menu import menu

app = FastAPI()

menu_instance = menu()

@app.get("/options")
async def get_options():
    options = {}
    for col in menu_instance.columns:
        unique_vals = menu_instance.db[col].dropna().unique().tolist()
        options[col] = unique_vals
    return options


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)