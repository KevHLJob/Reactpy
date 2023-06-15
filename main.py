from fastapi import FastAPI
from reactpy import component, html
from reactpy.backend.fastapi import configure


from reactpy import component, html, run


#component reactpy
@component
def MyTodoList():
    return html.div(
        html.h1("My Todo List"), 
        html.img({"src": "https://picsum.photos/id/0/500/300"}), 
        html.ul(html.li("The first thing I need to do is...")),
    )


#server
app = FastAPI()
configure(app, MyTodoList)
