from utils.dataloader import *
import pytest

def test_fetch_ucirepo():
    data = fetch_ucirepo(id=159)
    X = data.data.features
    y = data.data.targets

    assert X.shape == (19020, 10)
    assert y.shape == (19020, 1)

