# -*- coding: utf-8 -*-

import os
import pytest
from dialex import dialex

@pytest.fixture
def no_api_key():
    """Returns instance with no API key provided"""
    return dialex.Dialex('')

@pytest.fixture
def client():
    """Returns instance with a working key"""
    key = os.environ['API_KEY']
    return dialex.Dialex(key)

def test_dialex_class_instanceof(client):
    """Check if instance of Dialex class"""
    assert isinstance(client, dialex.Dialex)

def test_dialex_transform_method(client):
    """Check if Dialex outputs correct result"""
    res = client.transform('diff column', 'en')
    assert res == 'difference column'

def test_dialex_raises_exception_for_wrong_no_key(no_api_key):
    """Check if error is raised for no api key"""
    with pytest.raises(Exception):
        no_api_key.transform('diff column', 'en')
