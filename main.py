from fastapi import FastAPI
from reactpy.backend.fastapi import configure

from reactpy import component, html, run


#componente parametrizado
def Photo(alt_text, image_id):
    return html.img(
        {
            "src": f"https://picsum.photos/id/{image_id}/500/200",
            "style": {"width": "50%"},
            "alt": alt_text,
        }
    )


@component
def Gallery():
    return html.section(
        html.h1("Photo Gallery"),
        Photo("Landscape", image_id=830),
        Photo("City", image_id=274),
        Photo("Puppy", image_id=237)
    )


#server
app = FastAPI()
configure(app, Gallery)
