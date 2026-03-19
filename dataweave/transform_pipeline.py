"""Transform pipeline using registry-based dispatch."""

from typing import Any, Callable


class TransformError(Exception):
    """Raised when a transformation fails."""


_registry: dict[str, Callable] = {}


def register_transform(name: str):
    """Decorator to register a transform function."""
    def decorator(func: Callable) -> Callable:
        _registry[name] = func
        return func
    return decorator


def transform(data: Any, transform_type: str) -> Any:
    """Apply a transformation to the input data."""
    handler = _registry.get(transform_type)
    if handler is None:
        raise TransformError(f"Unknown transform type: {transform_type}")
    return handler(data)


@register_transform("csv")
def _transform_csv(data: Any) -> Any:
    if not data:
        return []
    return [row.split(",") for row in data.strip().split("\n")]


@register_transform("json")
def _transform_json(data: Any) -> Any:
    import json
    return json.loads(data)


@register_transform("ndjson")
def _transform_ndjson(data: Any) -> Any:
    import json
    return [json.loads(line) for line in data.strip().split("\n")]


@register_transform("tsv")
def _transform_tsv(data: Any) -> Any:
    return [row.split("\t") for row in data.strip().split("\n")]
