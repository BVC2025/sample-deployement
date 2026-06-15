from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>FastAPI Demo</title>
        </head>
        <body>
            <h1>Welcome to FastAPI</h1>
            <p>Application deployed through Jenkins.</p>
        </body>
    </html>
    """