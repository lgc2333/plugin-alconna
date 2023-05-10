from typing import Literal
from pathlib import Path
from tarina import lang

lang.load(Path(__file__).parent / "i18n")
ALCONNA_RESULT: Literal["_alc_result"] = "_alc_result"
