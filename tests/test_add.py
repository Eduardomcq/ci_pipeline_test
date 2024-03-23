import sys
import pandas as pd

sys.path.append("../dags")
import pytest

from utils.add import add


def test_add():
    resposta = add(1, 1)
    assert resposta == 2
