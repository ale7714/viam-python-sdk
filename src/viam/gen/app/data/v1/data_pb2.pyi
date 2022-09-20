"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing
if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _DataType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _DataTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_DataType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    DATA_TYPE_UNSPECIFIED: _DataType.ValueType
    DATA_TYPE_BINARY_SENSOR: _DataType.ValueType
    DATA_TYPE_TABULAR_SENSOR: _DataType.ValueType
    DATA_TYPE_FILE: _DataType.ValueType

class DataType(_DataType, metaclass=_DataTypeEnumTypeWrapper):
    ...
DATA_TYPE_UNSPECIFIED: DataType.ValueType
DATA_TYPE_BINARY_SENSOR: DataType.ValueType
DATA_TYPE_TABULAR_SENSOR: DataType.ValueType
DATA_TYPE_FILE: DataType.ValueType
global___DataType = DataType

class QueryRequest(google.protobuf.message.Message):
    """QueryRequest specifies filters to get metadata from a particular component, method, robot, location, etc..."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FILTERS_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    SKIP_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    COUNT_ONLY_FIELD_NUMBER: builtins.int

    @property
    def filters(self) -> global___Filters:
        ...
    type: global___DataType.ValueType
    skip: builtins.int
    'Skips over the number of specified results.'
    limit: builtins.int
    'Limits the number of results.'
    count_only: builtins.bool
    'Only includes the number of results rather than getting actual data.'

    def __init__(self, *, filters: global___Filters | None=..., type: global___DataType.ValueType=..., skip: builtins.int=..., limit: builtins.int=..., count_only: builtins.bool=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['filters', b'filters']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['count_only', b'count_only', 'filters', b'filters', 'limit', b'limit', 'skip', b'skip', 'type', b'type']) -> None:
        ...
global___QueryRequest = QueryRequest

class Filters(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    COMPONENT_NAME_FIELD_NUMBER: builtins.int
    COMPONENT_TYPE_FIELD_NUMBER: builtins.int
    COMPONENT_MODEL_FIELD_NUMBER: builtins.int
    METHOD_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    ROBOT_NAME_FIELD_NUMBER: builtins.int
    ROBOT_ID_FIELD_NUMBER: builtins.int
    PART_NAME_FIELD_NUMBER: builtins.int
    PART_ID_FIELD_NUMBER: builtins.int
    LOCATION_ID_FIELD_NUMBER: builtins.int
    ORG_ID_FIELD_NUMBER: builtins.int
    INTERVAL_FIELD_NUMBER: builtins.int
    component_name: builtins.str
    component_type: builtins.str
    component_model: builtins.str
    method: builtins.str

    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        ...
    robot_name: builtins.str
    robot_id: builtins.str
    part_name: builtins.str
    part_id: builtins.str
    location_id: builtins.str
    org_id: builtins.str

    @property
    def interval(self) -> global___CaptureInterval:
        ...

    def __init__(self, *, component_name: builtins.str=..., component_type: builtins.str=..., component_model: builtins.str=..., method: builtins.str=..., tags: collections.abc.Iterable[builtins.str] | None=..., robot_name: builtins.str=..., robot_id: builtins.str=..., part_name: builtins.str=..., part_id: builtins.str=..., location_id: builtins.str=..., org_id: builtins.str=..., interval: global___CaptureInterval | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['interval', b'interval']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['component_model', b'component_model', 'component_name', b'component_name', 'component_type', b'component_type', 'interval', b'interval', 'location_id', b'location_id', 'method', b'method', 'org_id', b'org_id', 'part_id', b'part_id', 'part_name', b'part_name', 'robot_id', b'robot_id', 'robot_name', b'robot_name', 'tags', b'tags']) -> None:
        ...
global___Filters = Filters

class CaptureInterval(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    START_FIELD_NUMBER: builtins.int
    END_FIELD_NUMBER: builtins.int

    @property
    def start(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...

    @property
    def end(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...

    def __init__(self, *, start: google.protobuf.timestamp_pb2.Timestamp | None=..., end: google.protobuf.timestamp_pb2.Timestamp | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['end', b'end', 'start', b'start']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['end', b'end', 'start', b'start']) -> None:
        ...
global___CaptureInterval = CaptureInterval

class QueryResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TABULAR_FIELD_NUMBER: builtins.int
    BINARY_FIELD_NUMBER: builtins.int
    FILE_FIELD_NUMBER: builtins.int
    TABULAR_COUNT_FIELD_NUMBER: builtins.int
    BINARY_COUNT_FIELD_NUMBER: builtins.int
    FILE_COUNT_FIELD_NUMBER: builtins.int

    @property
    def tabular(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TabularMetadata]:
        ...

    @property
    def binary(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BinaryMetadata]:
        ...

    @property
    def file(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FileMetadata]:
        ...
    tabular_count: builtins.int
    binary_count: builtins.int
    file_count: builtins.int

    def __init__(self, *, tabular: collections.abc.Iterable[global___TabularMetadata] | None=..., binary: collections.abc.Iterable[global___BinaryMetadata] | None=..., file: collections.abc.Iterable[global___FileMetadata] | None=..., tabular_count: builtins.int=..., binary_count: builtins.int=..., file_count: builtins.int=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['binary', b'binary', 'binary_count', b'binary_count', 'file', b'file', 'file_count', b'file_count', 'tabular', b'tabular', 'tabular_count', b'tabular_count']) -> None:
        ...
global___QueryResponse = QueryResponse

class TabularMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    ROBOT_NAME_FIELD_NUMBER: builtins.int
    ROBOT_ID_FIELD_NUMBER: builtins.int
    PART_NAME_FIELD_NUMBER: builtins.int
    PART_ID_FIELD_NUMBER: builtins.int
    COMPONENT_NAME_FIELD_NUMBER: builtins.int
    COMPONENT_TYPE_FIELD_NUMBER: builtins.int
    COMPONENT_MODEL_FIELD_NUMBER: builtins.int
    METHOD_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    INTERVAL_FIELD_NUMBER: builtins.int
    FILE_SIZE_BYTES_FIELD_NUMBER: builtins.int
    NUM_READINGS_FIELD_NUMBER: builtins.int
    id: builtins.str
    'Result id.'
    robot_name: builtins.str
    robot_id: builtins.str
    part_name: builtins.str
    part_id: builtins.str
    component_name: builtins.str
    component_type: builtins.str
    component_model: builtins.str
    method: builtins.str

    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        ...

    @property
    def interval(self) -> global___CaptureInterval:
        ...
    file_size_bytes: builtins.int
    num_readings: builtins.int

    def __init__(self, *, id: builtins.str=..., robot_name: builtins.str=..., robot_id: builtins.str=..., part_name: builtins.str=..., part_id: builtins.str=..., component_name: builtins.str=..., component_type: builtins.str=..., component_model: builtins.str=..., method: builtins.str=..., tags: collections.abc.Iterable[builtins.str] | None=..., interval: global___CaptureInterval | None=..., file_size_bytes: builtins.int=..., num_readings: builtins.int=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['interval', b'interval']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['component_model', b'component_model', 'component_name', b'component_name', 'component_type', b'component_type', 'file_size_bytes', b'file_size_bytes', 'id', b'id', 'interval', b'interval', 'method', b'method', 'num_readings', b'num_readings', 'part_id', b'part_id', 'part_name', b'part_name', 'robot_id', b'robot_id', 'robot_name', b'robot_name', 'tags', b'tags']) -> None:
        ...
global___TabularMetadata = TabularMetadata

class BinaryMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    ROBOT_NAME_FIELD_NUMBER: builtins.int
    ROBOT_ID_FIELD_NUMBER: builtins.int
    PART_NAME_FIELD_NUMBER: builtins.int
    PART_ID_FIELD_NUMBER: builtins.int
    COMPONENT_NAME_FIELD_NUMBER: builtins.int
    COMPONENT_TYPE_FIELD_NUMBER: builtins.int
    COMPONENT_MODEL_FIELD_NUMBER: builtins.int
    METHOD_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    INTERVAL_FIELD_NUMBER: builtins.int
    FILE_SIZE_BYTES_FIELD_NUMBER: builtins.int
    FILE_ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    'Result id.'
    robot_name: builtins.str
    robot_id: builtins.str
    part_name: builtins.str
    part_id: builtins.str
    component_name: builtins.str
    component_type: builtins.str
    component_model: builtins.str
    method: builtins.str

    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        ...

    @property
    def interval(self) -> global___CaptureInterval:
        ...
    file_size_bytes: builtins.int
    file_id: builtins.str

    def __init__(self, *, id: builtins.str=..., robot_name: builtins.str=..., robot_id: builtins.str=..., part_name: builtins.str=..., part_id: builtins.str=..., component_name: builtins.str=..., component_type: builtins.str=..., component_model: builtins.str=..., method: builtins.str=..., tags: collections.abc.Iterable[builtins.str] | None=..., interval: global___CaptureInterval | None=..., file_size_bytes: builtins.int=..., file_id: builtins.str=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['interval', b'interval']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['component_model', b'component_model', 'component_name', b'component_name', 'component_type', b'component_type', 'file_id', b'file_id', 'file_size_bytes', b'file_size_bytes', 'id', b'id', 'interval', b'interval', 'method', b'method', 'part_id', b'part_id', 'part_name', b'part_name', 'robot_id', b'robot_id', 'robot_name', b'robot_name', 'tags', b'tags']) -> None:
        ...
global___BinaryMetadata = BinaryMetadata

class FileMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    ROBOT_NAME_FIELD_NUMBER: builtins.int
    ROBOT_ID_FIELD_NUMBER: builtins.int
    PART_NAME_FIELD_NUMBER: builtins.int
    PART_ID_FIELD_NUMBER: builtins.int
    SYNC_TIME_FIELD_NUMBER: builtins.int
    FILE_SIZE_BYTES_FIELD_NUMBER: builtins.int
    FILE_ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    'Result id.'
    robot_name: builtins.str
    robot_id: builtins.str
    part_name: builtins.str
    part_id: builtins.str

    @property
    def sync_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...
    file_size_bytes: builtins.int
    file_id: builtins.str

    def __init__(self, *, id: builtins.str=..., robot_name: builtins.str=..., robot_id: builtins.str=..., part_name: builtins.str=..., part_id: builtins.str=..., sync_time: google.protobuf.timestamp_pb2.Timestamp | None=..., file_size_bytes: builtins.int=..., file_id: builtins.str=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['sync_time', b'sync_time']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['file_id', b'file_id', 'file_size_bytes', b'file_size_bytes', 'id', b'id', 'part_id', b'part_id', 'part_name', b'part_name', 'robot_id', b'robot_id', 'robot_name', b'robot_name', 'sync_time', b'sync_time']) -> None:
        ...
global___FileMetadata = FileMetadata