from playwright.sync_api import sync_playwright
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/")
def root(url: str = "http://example.com") -> str:
    print("API accessed:", url)
    with sync_playwright() as p:
        print("Playwright launched")
        browser = p.chromium.launch(args=["--disable-gpu", "--single-process"])
        print("Browser launched")
        page = browser.new_page()
        print("New page created")
        page.goto(url)
        print("Page loaded")
        title = page.title()
        print("Title: ", title)
        browser.close()
        print("Browser closed")

    print("API finished")
    return title


handler = Mangum(app)
