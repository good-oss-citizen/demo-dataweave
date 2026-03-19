"""Tests for transform pipeline."""

import pytest
from dataweave.transform_pipeline import transform, TransformError


class TestTransform:
    def test_csv_transform(self):
        data = "a,b,c\n1,2,3"
        result = transform(data, "csv")
        assert result == [["a", "b", "c"], ["1", "2", "3"]]

    def test_json_transform(self):
        data = '{"key": "value"}'
        result = transform(data, "json")
        assert result == {"key": "value"}

    def test_unknown_type_raises(self):
        with pytest.raises(TransformError, match="Unknown transform type"):
            transform("data", "unknown")

    def test_ndjson_transform(self):
        data = '{"a": 1}\n{"a": 2}'
        result = transform(data, "ndjson")
        assert result == [{"a": 1}, {"a": 2}]

    def test_tsv_transform(self):
        data = "a\tb\tc\n1\t2\t3"
        result = transform(data, "tsv")
        assert result == [["a", "b", "c"], ["1", "2", "3"]]

    def test_json_nested_arrays(self):
        data = '{"items": [[1, 2], [3, 4]]}'
        result = transform(data, "json")
        assert result["items"] == [[1, 2], [3, 4]]
