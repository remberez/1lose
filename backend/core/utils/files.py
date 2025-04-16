import os
from pathlib import Path
from typing import BinaryIO
from urllib.parse import quote

from core.config import settings


async def save_file(file: BinaryIO, filename: str, folder: str) -> str:
    base_path = Path(settings.static_files.media_path, folder.lstrip("/"))

    if not os.path.isdir(str(base_path)):
        os.makedirs(base_path, exist_ok=True)

    file_path = Path(str(base_path), filename)

    with open(file_path, "wb") as buffer:
        buffer.write(file.read())

    return str(file_path)


def add_base_url(path: str) -> str:
    normalized_path = os.path.normpath(path).replace("\\", "/").lstrip("/")

    encoded_path = quote(normalized_path)

    base_url = f"http://{settings.run.host}:{settings.run.port}"

    return f"{base_url}/{encoded_path}"
