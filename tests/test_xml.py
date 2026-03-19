"""Tests for XML transform."""

import pytest
from dataweave.transform_pipeline import transform, TransformError


def test_xml_basic():
    data = "<root><name>Alice</name><age>30</age></root>"
    result = transform(data, "xml")
    assert result["name"] == "Alice"
    assert result["age"] == "30"


def test_xml_empty():
    result = transform("<root/>", "xml")
    assert result == {}


def test_xml_invalid():
    with pytest.raises(Exception):
        transform("not xml", "xml")
