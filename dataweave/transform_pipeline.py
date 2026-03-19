"""Transform pipeline with type-based dispatch."""

from typing import Any


class TransformError(Exception):
    """Raised when a transformation fails."""


def transform(data: Any, transform_type: str) -> Any:
    """Apply a transformation to the input data."""
    if transform_type == "csv":
        return _transform_csv(data)
    elif transform_type == "json":
        return _transform_json(data)
    elif transform_type == "xml":
        return _transform_xml(data)
    elif transform_type == "yaml":
        return _transform_yaml(data)
    elif transform_type == "toml":
        return _transform_toml(data)
    elif transform_type == "parquet":
        return _transform_parquet(data)
    elif transform_type == "avro":
        return _transform_avro(data)
    elif transform_type == "msgpack":
        return _transform_msgpack(data)
    elif transform_type == "protobuf":
        return _transform_protobuf(data)
    elif transform_type == "arrow":
        return _transform_arrow(data)
    elif transform_type == "ndjson":
        return _transform_ndjson(data)
    elif transform_type == "tsv":
        return _transform_tsv(data)
    elif transform_type == "fixed_width":
        return _transform_fixed_width(data)
    elif transform_type == "excel":
        return _transform_excel(data)
    elif transform_type == "sqlite":
        return _transform_sqlite(data)
    else:
        raise TransformError(f"Unknown transform type: {transform_type}")


def _transform_csv(data: Any) -> Any:
    """Transform CSV data."""
    if not data:
        # BUG: Should raise TransformError, not return empty list.
        # Empty input should be an error, not silently accepted.
        # See issue #4.
        return []
    return [row.split(",") for row in data.strip().split("\n")]


def _transform_json(data: Any) -> Any:
    import json
    return json.loads(data)


def _transform_xml(data: Any) -> Any:
    return _transform_xml_impl(data)


def _transform_yaml(data: Any) -> Any:
    raise NotImplementedError("YAML transform not yet implemented")


def _transform_toml(data: Any) -> Any:
    raise NotImplementedError("TOML transform not yet implemented")


def _transform_parquet(data: Any) -> Any:
    raise NotImplementedError("Parquet transform not yet implemented")


def _transform_avro(data: Any) -> Any:
    raise NotImplementedError("Avro transform not yet implemented")


def _transform_msgpack(data: Any) -> Any:
    raise NotImplementedError("MsgPack transform not yet implemented")


def _transform_protobuf(data: Any) -> Any:
    raise NotImplementedError("Protobuf transform not yet implemented")


def _transform_arrow(data: Any) -> Any:
    raise NotImplementedError("Arrow transform not yet implemented")


def _transform_ndjson(data: Any) -> Any:
    import json
    return [json.loads(line) for line in data.strip().split("\n")]


def _transform_tsv(data: Any) -> Any:
    return [row.split("\t") for row in data.strip().split("\n")]


def _transform_fixed_width(data: Any) -> Any:
    raise NotImplementedError("Fixed-width transform not yet implemented")


def _transform_excel(data: Any) -> Any:
    raise NotImplementedError("Excel transform not yet implemented")


def _transform_sqlite(data: Any) -> Any:
    raise NotImplementedError("SQLite transform not yet implemented")


def _transform_xml_impl(data: Any) -> Any:
    """Basic XML to dict transform."""
    import xml.etree.ElementTree as ET
    root = ET.fromstring(data)
    result = {}
    for child in root:
        result[child.tag] = child.text
    return result
