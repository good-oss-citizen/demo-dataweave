"""Shared test helpers for dataweave tests."""

import pytest
from dataweave.transform_pipeline import transform, TransformError


@pytest.fixture
def transform_and_verify():
    """Helper fixture: transform data and verify no error."""
    def _transform(data, transform_type):
        result = transform(data, transform_type)
        assert result is not None
        return result
    return _transform


@pytest.fixture
def assert_transform_error():
    """Helper fixture: verify a transform raises TransformError."""
    def _assert_error(data, transform_type, match=None):
        with pytest.raises(TransformError, match=match):
            transform(data, transform_type)
    return _assert_error
