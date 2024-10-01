from flask import Flask, redirect, render_template, request, url_for
from flask_mail import Mail

app = Flask(__name__, static_folder="./../static", template_folder="./../templates")
app.secret_key = "124b3052fe9ea632d36a2398a77af3a70d592922d64fa30836c7e075a1a28fd7"


app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = "rexsyflaskportofolio@gmail.com"
app.config["MAIL_PASSWORD"] = "rach qdew xxsh tabj"
app.config["MAIL_DEFAULT_SENDER"] = "rexsyflaskportofolio@gmail.com"


mail = Mail(app)


portofolios = [
    {
        "title": "API Scraping for sg.iherb.com",
        "description": "Scraping for upwork client for sg.iherb.com, several tech has been used to make this possible",
        "url": "https://github.com/RexsyBima/sgiherb-api-scraping",
        "link": "GitHub Link",
        "tech_used": "BeautifulSoup4, Requests (curl_cffi), sqlalchemy, pandas",
        "isMediumArticle": False,
        "jobdesc": ["todo1", "todo2", "todo3"],
    },
    {
        "title": "Scraping for sg.iherb.com",
        "description": "Scraping for upwork client for sg.iherb.com, several tech has been used to make this possible",
        "url": "https://github.com/RexsyBima/sgiherb-scrapy",
        "link": "GitHub Link",
        "tech_used": "BeautifulSoup4, Requests (curl_cffi), sqlalchemy, pandas",
        "isMediumArticle": False,
        "jobdesc": ["todo1", "todo2", "todo3"],
    },
    {
        "title": "LangChain QNA PDF feat Streamlit",
        "description": "Personal Project for learning langchain and streamlit",
        "url": "https://github.com/RexsyBima/langchain-qna-pdf-streamlit",
        "link": "GitHub Link",
        "tech_used": "Langchain, Streamlit, PyPDF2",
        "isMediumArticle": False,
        "jobdesc": ["todo1", "todo2", "todo3"],
    },
    {
        "title": "Just What Pseudocodes Really Is?",
        "description": "A Medium Article about Psuedocodes, designed for beginner friendly",
        "url": "https://medium.com/@rexsy.bimq12/just-what-pseudocodes-really-is-d3fb388a56ea",
        "link": "Medium Link",
        "tech_used": "",
        "isMediumArticle": True,
        "jobdesc": ["todo1", "todo2", "todo3"],
    },
    {
        "title": "Introduction Into Large Language Models",
        "description": "Personal Project for learning langchain and streamlit",
        "url": "https://medium.com/@rexsy.bimq12/introduction-into-large-language-models-11d37354daa1",
        "link": "Medium Link",
        "tech_used": "",
        "isMediumArticle": True,
        "jobdesc": ["todo1", "todo2", "todo3"],
    },
]


def render(template: str, **kwargs):
    kwargs["path"] = request.path
    return render_template(template, **kwargs)


from . import routes
