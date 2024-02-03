from selenium import webdriver
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/")
def root(url: str = "http://example.com") -> str:
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")

    print("API accessed:", url)
    with webdriver.Chrome(options=options) as wd:
        print("Selenium launched")
        print("New page created")
        wd.get(url)
        print("Page loaded")
        title = wd.title
        print("Title:", title)

    print("API finished")
    return title


handler = Mangum(app)
