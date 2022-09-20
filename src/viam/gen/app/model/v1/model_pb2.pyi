"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
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

class _Status:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Status.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNSPECIFIED: _Status.ValueType
    'buf:lint:ignore ENUM_VALUE_PREFIX\n    buf:lint:ignore ENUM_ZERO_VALUE_SUFFIX\n    '
    FAIL: _Status.ValueType
    'buf:lint:ignore ENUM_VALUE_PREFIX'
    OK: _Status.ValueType
    'buf:lint:ignore ENUM_VALUE_PREFIX'

class Status(_Status, metaclass=_StatusEnumTypeWrapper):
    ...
UNSPECIFIED: Status.ValueType
'buf:lint:ignore ENUM_VALUE_PREFIX\nbuf:lint:ignore ENUM_ZERO_VALUE_SUFFIX\n'
FAIL: Status.ValueType
'buf:lint:ignore ENUM_VALUE_PREFIX'
OK: Status.ValueType
'buf:lint:ignore ENUM_VALUE_PREFIX'
global___Status = Status

class FileData(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATA_FIELD_NUMBER: builtins.int
    data: builtins.bytes

    def __init__(self, *, data: builtins.bytes=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['data', b'data']) -> None:
        ...
global___FileData = FileData

class UploadMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ORG_ID_FIELD_NUMBER: builtins.int
    MODEL_NAME_FIELD_NUMBER: builtins.int
    ASSOCIATED_DATASET_FIELD_NUMBER: builtins.int
    org_id: builtins.str
    model_name: builtins.str
    associated_dataset: builtins.str
    "TODO: Determine the format of the associated dataset. Update when it's decided\n    whether it should be by ID or name.\n    "

    def __init__(self, *, org_id: builtins.str=..., model_name: builtins.str=..., associated_dataset: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['associated_dataset', b'associated_dataset', 'model_name', b'model_name', 'org_id', b'org_id']) -> None:
        ...
global___UploadMetadata = UploadMetadata

class UploadRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    METADATA_FIELD_NUMBER: builtins.int
    FILE_CONTENTS_FIELD_NUMBER: builtins.int

    @property
    def metadata(self) -> global___UploadMetadata:
        ...

    @property
    def file_contents(self) -> global___FileData:
        ...

    def __init__(self, *, metadata: global___UploadMetadata | None=..., file_contents: global___FileData | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['file_contents', b'file_contents', 'metadata', b'metadata', 'upload_packet', b'upload_packet']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['file_contents', b'file_contents', 'metadata', b'metadata', 'upload_packet', b'upload_packet']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['upload_packet', b'upload_packet']) -> typing_extensions.Literal['metadata', 'file_contents'] | None:
        ...
global___UploadRequest = UploadRequest

class DeleteMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ORG_ID_FIELD_NUMBER: builtins.int
    MODEL_NAME_FIELD_NUMBER: builtins.int
    org_id: builtins.str
    model_name: builtins.str

    def __init__(self, *, org_id: builtins.str=..., model_name: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['model_name', b'model_name', 'org_id', b'org_id']) -> None:
        ...
global___DeleteMetadata = DeleteMetadata

class DeleteRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    METADATA_FIELD_NUMBER: builtins.int

    @property
    def metadata(self) -> global___DeleteMetadata:
        ...

    def __init__(self, *, metadata: global___DeleteMetadata | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['metadata', b'metadata']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['metadata', b'metadata']) -> None:
        ...
global___DeleteRequest = DeleteRequest

class DeployMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MODEL_NAME_FIELD_NUMBER: builtins.int
    model_name: builtins.str

    def __init__(self, *, model_name: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['model_name', b'model_name']) -> None:
        ...
global___DeployMetadata = DeployMetadata

class DeployRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    METADATA_FIELD_NUMBER: builtins.int

    @property
    def metadata(self) -> global___DeployMetadata:
        ...

    def __init__(self, *, metadata: global___DeployMetadata | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['metadata', b'metadata']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['metadata', b'metadata']) -> None:
        ...
global___DeployRequest = DeployRequest

class UploadResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MESSAGE_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    message: builtins.str
    status: global___Status.ValueType

    def __init__(self, *, message: builtins.str=..., status: global___Status.ValueType=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['message', b'message', 'status', b'status']) -> None:
        ...
global___UploadResponse = UploadResponse

class DeleteResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MESSAGE_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    message: builtins.str
    status: global___Status.ValueType

    def __init__(self, *, message: builtins.str=..., status: global___Status.ValueType=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['message', b'message', 'status', b'status']) -> None:
        ...
global___DeleteResponse = DeleteResponse

class DeployResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MESSAGE_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    message: builtins.str
    status: global___Status.ValueType

    def __init__(self, *, message: builtins.str=..., status: global___Status.ValueType=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['message', b'message', 'status', b'status']) -> None:
        ...
global___DeployResponse = DeployResponse

class SyncedModel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ORG_ID_FIELD_NUMBER: builtins.int
    MODEL_NAME_FIELD_NUMBER: builtins.int
    ASSOCIATED_DATASET_FIELD_NUMBER: builtins.int
    BLOB_PATH_FIELD_NUMBER: builtins.int
    SYNC_TIME_FIELD_NUMBER: builtins.int
    org_id: builtins.str
    model_name: builtins.str
    associated_dataset: builtins.str
    blob_path: builtins.str

    @property
    def sync_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        ...

    def __init__(self, *, org_id: builtins.str=..., model_name: builtins.str=..., associated_dataset: builtins.str=..., blob_path: builtins.str=..., sync_time: google.protobuf.timestamp_pb2.Timestamp | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['sync_time', b'sync_time']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['associated_dataset', b'associated_dataset', 'blob_path', b'blob_path', 'model_name', b'model_name', 'org_id', b'org_id', 'sync_time', b'sync_time']) -> None:
        ...
global___SyncedModel = SyncedModel