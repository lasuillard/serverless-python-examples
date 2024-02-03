from selenium import webdriver
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/")
def root(url: str = "http://example.com") -> str:
    print("API accessed:", url)

    print("Building webdriver options")
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--disable-gpu")
    options.add_argument(
        "--single-process"
    )  # NOTE: This solved the crash issue, but not sure why
    print("Launching webdriver")
    with webdriver.Chrome(options=options) as wd:
        print("New page created")
        wd.get(url)
        print("Page loaded")
        title = wd.title
        print("Title:", title)

    print("API finished")
    return title


handler = Mangum(app)
