# -*- coding: utf-8 -*-
import os
import sys
from pathlib import Path

try:
    import core  # noqa
except ModuleNotFoundError:
    current_path = Path(os.getcwd())
    print('get exception import core need append path', current_path.parents[1])
    sys.path.append(str(current_path.parents[1]))
    import core  # noqa

from core.const import AUTHOR
print('author', AUTHOR)
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": f"World {AUTHOR} "}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
