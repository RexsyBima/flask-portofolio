from dotenv import load_dotenv
import os
from flask import Flask, render_template, request
from flask_mail import Mail

load_dotenv()
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
EMAIL = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
app = Flask(__name__, static_folder="./../static", template_folder="./../templates")
app.secret_key = FLASK_SECRET_KEY


app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = EMAIL
app.config["MAIL_PASSWORD"] = EMAIL_PASSWORD
app.config["MAIL_DEFAULT_SENDER"] = EMAIL


mail = Mail(app)


portofolios = [
    {
        "title": "API Scraping for sg.iherb.com",
        "description": "Scraping for upwork client for sg.iherb.com, several tech has been used to make this possible",
        "url": "https://github.com/RexsyBima/sgiherb-api-scraping",
        "link": "GitHub Link",
        "isMediumArticle": False,
        "jobdesc": ["BeautifulSoup4", "Requests (curl_cffi)", "sqlalchemy", "pandas"],
        "year": "2023 - 2024",
    },
    {
        "title": "Scraping for sg.iherb.com",
        "description": "Scraping for upwork client for sg.iherb.com, several tech has been used to make this possible",
        "url": "https://github.com/RexsyBima/sgiherb-scrapy",
        "link": "GitHub Link",
        "tech_used": "BeautifulSoup4, Requests (curl_cffi), sqlalchemy, pandas",
        "isMediumArticle": False,
        "jobdesc": ["BeautifulSoup4", "Requests (curl_cffi)", "sqlalchemy", "pandas"],
        "year": "2023 - 2024",
    },
    {
        "title": "LangChain QNA PDF feat Streamlit",
        "description": "Personal Project for learning langchain and streamlit",
        "url": "https://github.com/RexsyBima/langchain-qna-pdf-streamlit",
        "link": "GitHub Link",
        "isMediumArticle": False,
        "jobdesc": ["Langchain", "Streamlit", "PyPDF2"],
        "year": "2023 - 2024",
    },
]

articles = [
    {
        "title": "Introduction Into Large Language Models",
        "description": "LLMs revolutionize NLP with deep understanding and generation of human language, powered by vast training data and transformer architectures.",
        "url": "https://medium.com/@rexsy.bimq12/introduction-into-large-language-models-11d37354daa1",
        "img_url": "https://miro.medium.com/v2/resize:fit:1100/format:webp/0*F6J_JKzODFRQTRPs",
    },
    {
        "title": "Machine Learning : Introduction",
        "description": "Machine learning is a broad term that refers to the use of algorithms or computer programs to learn from data and make predictions or decisions based on that data.",
        "url": "https://medium.com/@rexsy.bimq12/machine-learning-introduction-a5a05ebef96a",
        "img_url": "https://miro.medium.com/v2/resize:fit:1100/format:webp/0*YoPr-DsKOdsJr5Cc",
    },
    {
        "title": "How to Master Web Scraping of Complex JavaScript website with Scrapy and Selenium Python",
        "description": "Web scraping is a skill in programming the main purpose of it is to extract data from a website. It’s a skill that has a close tie to data entry but it’s programmed automatically to collect data from a website.",
        "url": "https://medium.com/@rexsy.bimq12/how-to-master-web-scraping-of-complex-javascript-website-with-scrapy-and-selenium-python-c51856854f75",
        "img_url": "https://miro.medium.com/v2/resize:fit:1100/format:webp/1*U-tDEXtRFjjt-bwNdRslFw.png",
    },
    {
        "title": "How You Can Use Udemy, ChatGPT and Notion to Master Python Programming Language",
        "description": "The first time I knew Python was way back in 2017, back when I was a member of the Olympiad science team for computer science in high school.",
        "url": "https://medium.com/@rexsy.bimq12/how-you-can-use-udemy-chatgpt-and-notion-to-master-python-programming-language-49481796f87b",
        "img_url": "https://miro.medium.com/v2/resize:fit:1100/format:webp/0*9FuFtFV6r0iV6cv6.png",
    },
    {
        "title": "Just What Algorithm Really is?",
        "description": "Algorithms are used to solve problems and can be found in everyday life, such as in food recipes, dealing with boredom and more. While humans can understand and execute complex algorithms, computers require specific instructions broken down into smaller steps.",
        "url": "https://medium.com/@rexsy.bimq12/just-what-algorithm-really-is-4a46e93cceb4",
        "img_url": "https://miro.medium.com/v2/resize:fit:1050/0*6yQutF9j3mp_cCPU",
    },
]


def render(template: str, **kwargs):
    kwargs["path"] = request.path
    return render_template(template, **kwargs)


from . import routes
