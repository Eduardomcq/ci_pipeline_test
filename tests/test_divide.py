import sys

sys.path.append("../dags")
import pytest

from utils.divide import divide


def test_add():
    resposta = divide(2, 2)
    assert resposta == 1
