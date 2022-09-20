"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from ... import app
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2
import sys
import typing
if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _CredentialsType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _CredentialsTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_CredentialsType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    CREDENTIALS_TYPE_UNSPECIFIED: _CredentialsType.ValueType
    CREDENTIALS_TYPE_INTERNAL: _CredentialsType.ValueType
    CREDENTIALS_TYPE_API_KEY: _CredentialsType.ValueType
    CREDENTIALS_TYPE_ROBOT_SECRET: _CredentialsType.ValueType
    CREDENTIALS_TYPE_ROBOT_LOCATION_SECRET: _CredentialsType.ValueType

class CredentialsType(_CredentialsType, metaclass=_CredentialsTypeEnumTypeWrapper):
    ...
CREDENTIALS_TYPE_UNSPECIFIED: CredentialsType.ValueType
CREDENTIALS_TYPE_INTERNAL: CredentialsType.ValueType
CREDENTIALS_TYPE_API_KEY: CredentialsType.ValueType
CREDENTIALS_TYPE_ROBOT_SECRET: CredentialsType.ValueType
CREDENTIALS_TYPE_ROBOT_LOCATION_SECRET: CredentialsType.ValueType
global___CredentialsType = CredentialsType

class RobotConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLOUD_FIELD_NUMBER: builtins.int
    REMOTES_FIELD_NUMBER: builtins.int
    COMPONENTS_FIELD_NUMBER: builtins.int
    PROCESSES_FIELD_NUMBER: builtins.int
    SERVICES_FIELD_NUMBER: builtins.int
    NETWORK_FIELD_NUMBER: builtins.int
    AUTH_FIELD_NUMBER: builtins.int
    DEBUG_FIELD_NUMBER: builtins.int

    @property
    def cloud(self) -> global___CloudConfig:
        ...

    @property
    def remotes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RemoteConfig]:
        ...

    @property
    def components(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ComponentConfig]:
        ...

    @property
    def processes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ProcessConfig]:
        ...

    @property
    def services(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ServiceConfig]:
        ...

    @property
    def network(self) -> global___NetworkConfig:
        ...

    @property
    def auth(self) -> global___AuthConfig:
        ...
    debug: builtins.bool
    'Turns on debug mode for robot, adding an echo server and more logging and tracing. Only works after restart'

    def __init__(self, *, cloud: global___CloudConfig | None=..., remotes: collections.abc.Iterable[global___RemoteConfig] | None=..., components: collections.abc.Iterable[global___ComponentConfig] | None=..., processes: collections.abc.Iterable[global___ProcessConfig] | None=..., services: collections.abc.Iterable[global___ServiceConfig] | None=..., network: global___NetworkConfig | None=..., auth: global___AuthConfig | None=..., debug: builtins.bool | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['_auth', b'_auth', '_debug', b'_debug', '_network', b'_network', 'auth', b'auth', 'cloud', b'cloud', 'debug', b'debug', 'network', b'network']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['_auth', b'_auth', '_debug', b'_debug', '_network', b'_network', 'auth', b'auth', 'cloud', b'cloud', 'components', b'components', 'debug', b'debug', 'network', b'network', 'processes', b'processes', 'remotes', b'remotes', 'services', b'services']) -> None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_auth', b'_auth']) -> typing_extensions.Literal['auth'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_debug', b'_debug']) -> typing_extensions.Literal['debug'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal['_network', b'_network']) -> typing_extensions.Literal['network'] | None:
        ...
global___RobotConfig = RobotConfig

class CloudConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    FQDN_FIELD_NUMBER: builtins.int
    LOCAL_FQDN_FIELD_NUMBER: builtins.int
    MANAGED_BY_FIELD_NUMBER: builtins.int
    SIGNALING_ADDRESS_FIELD_NUMBER: builtins.int
    SIGNALING_INSECURE_FIELD_NUMBER: builtins.int
    LOCATION_SECRET_FIELD_NUMBER: builtins.int
    SECRET_FIELD_NUMBER: builtins.int
    id: builtins.str
    'Robot part id.'
    fqdn: builtins.str
    local_fqdn: builtins.str
    managed_by: builtins.str
    signaling_address: builtins.str
    signaling_insecure: builtins.bool
    location_secret: builtins.str
    secret: builtins.str

    def __init__(self, *, id: builtins.str=..., fqdn: builtins.str=..., local_fqdn: builtins.str=..., managed_by: builtins.str=..., signaling_address: builtins.str=..., signaling_insecure: builtins.bool=..., location_secret: builtins.str=..., secret: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['fqdn', b'fqdn', 'id', b'id', 'local_fqdn', b'local_fqdn', 'location_secret', b'location_secret', 'managed_by', b'managed_by', 'secret', b'secret', 'signaling_address', b'signaling_address', 'signaling_insecure', b'signaling_insecure']) -> None:
        ...
global___CloudConfig = CloudConfig

class ComponentConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    NAMESPACE_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    MODEL_FIELD_NUMBER: builtins.int
    FRAME_FIELD_NUMBER: builtins.int
    DEPENDS_ON_FIELD_NUMBER: builtins.int
    SERVICE_CONFIGS_FIELD_NUMBER: builtins.int
    ATTRIBUTES_FIELD_NUMBER: builtins.int
    name: builtins.str
    namespace: builtins.str
    type: builtins.str
    model: builtins.str

    @property
    def frame(self) -> global___Frame:
        ...

    @property
    def depends_on(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        ...

    @property
    def service_configs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ResourceLevelServiceConfig]:
        ...

    @property
    def attributes(self) -> google.protobuf.struct_pb2.Struct:
        ...

    def __init__(self, *, name: builtins.str=..., namespace: builtins.str=..., type: builtins.str=..., model: builtins.str=..., frame: global___Frame | None=..., depends_on: collections.abc.Iterable[builtins.str] | None=..., service_configs: collections.abc.Iterable[global___ResourceLevelServiceConfig] | None=..., attributes: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['attributes', b'attributes', 'frame', b'frame']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['attributes', b'attributes', 'depends_on', b'depends_on', 'frame', b'frame', 'model', b'model', 'name', b'name', 'namespace', b'namespace', 'service_configs', b'service_configs', 'type', b'type']) -> None:
        ...
global___ComponentConfig = ComponentConfig

class ResourceLevelServiceConfig(google.protobuf.message.Message):
    """A ResourceLevelServiceConfig describes component or remote configuration for a service."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TYPE_FIELD_NUMBER: builtins.int
    ATTRIBUTES_FIELD_NUMBER: builtins.int
    type: builtins.str

    @property
    def attributes(self) -> google.protobuf.struct_pb2.Struct:
        """TODO(adam): Should this be move to a structured type as defined in the typescript frontend."""

    def __init__(self, *, type: builtins.str=..., attributes: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['attributes', b'attributes']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['attributes', b'attributes', 'type', b'type']) -> None:
        ...
global___ResourceLevelServiceConfig = ResourceLevelServiceConfig

class ProcessConfig(google.protobuf.message.Message):
    """A ProcessConfig describes how to manage a system process."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    CWD_FIELD_NUMBER: builtins.int
    ONE_SHOT_FIELD_NUMBER: builtins.int
    LOG_FIELD_NUMBER: builtins.int
    id: builtins.str
    name: builtins.str

    @property
    def args(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        ...
    cwd: builtins.str
    one_shot: builtins.bool
    log: builtins.bool

    def __init__(self, *, id: builtins.str=..., name: builtins.str=..., args: collections.abc.Iterable[builtins.str] | None=..., cwd: builtins.str=..., one_shot: builtins.bool=..., log: builtins.bool=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['args', b'args', 'cwd', b'cwd', 'id', b'id', 'log', b'log', 'name', b'name', 'one_shot', b'one_shot']) -> None:
        ...
global___ProcessConfig = ProcessConfig

class ServiceConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    NAMESPACE_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    ATTRIBUTES_FIELD_NUMBER: builtins.int
    name: builtins.str
    namespace: builtins.str
    type: builtins.str

    @property
    def attributes(self) -> google.protobuf.struct_pb2.Struct:
        ...

    def __init__(self, *, name: builtins.str=..., namespace: builtins.str=..., type: builtins.str=..., attributes: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['attributes', b'attributes']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['attributes', b'attributes', 'name', b'name', 'namespace', b'namespace', 'type', b'type']) -> None:
        ...
global___ServiceConfig = ServiceConfig

class NetworkConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FQDN_FIELD_NUMBER: builtins.int
    BIND_ADDRESS_FIELD_NUMBER: builtins.int
    TLS_CERT_FILE_FIELD_NUMBER: builtins.int
    TLS_KEY_FILE_FIELD_NUMBER: builtins.int
    fqdn: builtins.str
    bind_address: builtins.str
    tls_cert_file: builtins.str
    tls_key_file: builtins.str

    def __init__(self, *, fqdn: builtins.str=..., bind_address: builtins.str=..., tls_cert_file: builtins.str=..., tls_key_file: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['bind_address', b'bind_address', 'fqdn', b'fqdn', 'tls_cert_file', b'tls_cert_file', 'tls_key_file', b'tls_key_file']) -> None:
        ...
global___NetworkConfig = NetworkConfig

class AuthConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HANDLERS_FIELD_NUMBER: builtins.int
    TLS_AUTH_ENTITIES_FIELD_NUMBER: builtins.int

    @property
    def handlers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AuthHandlerConfig]:
        ...

    @property
    def tls_auth_entities(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        ...

    def __init__(self, *, handlers: collections.abc.Iterable[global___AuthHandlerConfig] | None=..., tls_auth_entities: collections.abc.Iterable[builtins.str] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['handlers', b'handlers', 'tls_auth_entities', b'tls_auth_entities']) -> None:
        ...
global___AuthConfig = AuthConfig

class AuthHandlerConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TYPE_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    type: global___CredentialsType.ValueType

    @property
    def config(self) -> google.protobuf.struct_pb2.Struct:
        ...

    def __init__(self, *, type: global___CredentialsType.ValueType=..., config: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['config', b'config']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['config', b'config', 'type', b'type']) -> None:
        ...
global___AuthHandlerConfig = AuthHandlerConfig

class Frame(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARENT_FIELD_NUMBER: builtins.int
    TRANSLATION_FIELD_NUMBER: builtins.int
    ORIENTATION_FIELD_NUMBER: builtins.int
    parent: builtins.str

    @property
    def translation(self) -> global___Translation:
        ...

    @property
    def orientation(self) -> global___Orientation:
        ...

    def __init__(self, *, parent: builtins.str=..., translation: global___Translation | None=..., orientation: global___Orientation | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['orientation', b'orientation', 'translation', b'translation']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['orientation', b'orientation', 'parent', b'parent', 'translation', b'translation']) -> None:
        ...
global___Frame = Frame

class Translation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    Z_FIELD_NUMBER: builtins.int
    x: builtins.float
    y: builtins.float
    z: builtins.float

    def __init__(self, *, x: builtins.float=..., y: builtins.float=..., z: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['x', b'x', 'y', b'y', 'z', b'z']) -> None:
        ...
global___Translation = Translation

class Orientation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class NoOrientation(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        def __init__(self) -> None:
            ...

    class OrientationVectorRadians(google.protobuf.message.Message):
        """OrientationVector containing ox, oy, oz, theta represents an orientation vector
        Structured similarly to an angle axis, an orientation vector works differently. Rather than representing an orientation
        with an arbitrary axis and a rotation around it from an origin, an orientation vector represents orientation
        such that the ox/oy/oz components represent the point on the cartesian unit sphere at which your end effector is pointing
        from the origin, and that unit vector forms an axis around which theta rotates. This means that incrementing/decrementing
        theta will perform an in-line rotation of the end effector.
        Theta is defined as rotation between two planes: the plane defined by the origin, the point (0,0,1), and the rx,ry,rz
        point, and the plane defined by the origin, the rx,ry,rz point, and the new local Z axis. So if theta is kept at
        zero as the north/south pole is circled, the Roll will correct itself to remain in-line.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        THETA_FIELD_NUMBER: builtins.int
        X_FIELD_NUMBER: builtins.int
        Y_FIELD_NUMBER: builtins.int
        Z_FIELD_NUMBER: builtins.int
        theta: builtins.float
        x: builtins.float
        y: builtins.float
        z: builtins.float

        def __init__(self, *, theta: builtins.float=..., x: builtins.float=..., y: builtins.float=..., z: builtins.float=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['theta', b'theta', 'x', b'x', 'y', b'y', 'z', b'z']) -> None:
            ...

    class OrientationVectorDegrees(google.protobuf.message.Message):
        """OrientationVectorDegrees is the orientation vector between two objects, but expressed in degrees rather than radians.
        Because protobuf Pose is in degrees, this is necessary.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        THETA_FIELD_NUMBER: builtins.int
        X_FIELD_NUMBER: builtins.int
        Y_FIELD_NUMBER: builtins.int
        Z_FIELD_NUMBER: builtins.int
        theta: builtins.float
        x: builtins.float
        y: builtins.float
        z: builtins.float

        def __init__(self, *, theta: builtins.float=..., x: builtins.float=..., y: builtins.float=..., z: builtins.float=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['theta', b'theta', 'x', b'x', 'y', b'y', 'z', b'z']) -> None:
            ...

    class EulerAngles(google.protobuf.message.Message):
        """EulerAngles are three angles (in radians) used to represent the rotation of an object in 3D Euclidean space
        The Tait–Bryan angle formalism is used, with rotations around three distinct axes in the z-y′-x″ sequence.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        ROLL_FIELD_NUMBER: builtins.int
        PITCH_FIELD_NUMBER: builtins.int
        YAW_FIELD_NUMBER: builtins.int
        roll: builtins.float
        pitch: builtins.float
        yaw: builtins.float

        def __init__(self, *, roll: builtins.float=..., pitch: builtins.float=..., yaw: builtins.float=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['pitch', b'pitch', 'roll', b'roll', 'yaw', b'yaw']) -> None:
            ...

    class AxisAngles(google.protobuf.message.Message):
        """See here for a thorough explanation: https://en.wikipedia.org/wiki/Axis%E2%80%93angle_representation
        Basic explanation: Imagine a 3d cartesian grid centered at 0,0,0, and a sphere of radius 1 centered at
        that same point. An orientation can be expressed by first specifying an axis, i.e. a line from the origin
        to a point on that sphere, represented by (rx, ry, rz), and a rotation around that axis, theta.
        These four numbers can be used as-is (R4), or they can be converted to R3, where theta is multiplied by each of
        the unit sphere components to give a vector whose length is theta and whose direction is the original axis.
        AxisAngles represents an R4 axis angle.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        THETA_FIELD_NUMBER: builtins.int
        X_FIELD_NUMBER: builtins.int
        Y_FIELD_NUMBER: builtins.int
        Z_FIELD_NUMBER: builtins.int
        theta: builtins.float
        x: builtins.float
        y: builtins.float
        z: builtins.float

        def __init__(self, *, theta: builtins.float=..., x: builtins.float=..., y: builtins.float=..., z: builtins.float=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['theta', b'theta', 'x', b'x', 'y', b'y', 'z', b'z']) -> None:
            ...

    class Quaternion(google.protobuf.message.Message):
        """Quaternion is a float64 precision quaternion."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        W_FIELD_NUMBER: builtins.int
        X_FIELD_NUMBER: builtins.int
        Y_FIELD_NUMBER: builtins.int
        Z_FIELD_NUMBER: builtins.int
        w: builtins.float
        x: builtins.float
        y: builtins.float
        z: builtins.float

        def __init__(self, *, w: builtins.float=..., x: builtins.float=..., y: builtins.float=..., z: builtins.float=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['w', b'w', 'x', b'x', 'y', b'y', 'z', b'z']) -> None:
            ...
    NO_ORIENTATION_FIELD_NUMBER: builtins.int
    VECTOR_RADIANS_FIELD_NUMBER: builtins.int
    VECTOR_DEGREES_FIELD_NUMBER: builtins.int
    EULER_ANGLES_FIELD_NUMBER: builtins.int
    AXIS_ANGLES_FIELD_NUMBER: builtins.int
    QUATERNION_FIELD_NUMBER: builtins.int

    @property
    def no_orientation(self) -> global___Orientation.NoOrientation:
        ...

    @property
    def vector_radians(self) -> global___Orientation.OrientationVectorRadians:
        ...

    @property
    def vector_degrees(self) -> global___Orientation.OrientationVectorDegrees:
        ...

    @property
    def euler_angles(self) -> global___Orientation.EulerAngles:
        ...

    @property
    def axis_angles(self) -> global___Orientation.AxisAngles:
        ...

    @property
    def quaternion(self) -> global___Orientation.Quaternion:
        ...

    def __init__(self, *, no_orientation: global___Orientation.NoOrientation | None=..., vector_radians: global___Orientation.OrientationVectorRadians | None=..., vector_degrees: global___Orientation.OrientationVectorDegrees | None=..., euler_angles: global___Orientation.EulerAngles | None=..., axis_angles: global___Orientation.AxisAngles | None=..., quaternion: global___Orientation.Quaternion | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['axis_angles', b'axis_angles', 'euler_angles', b'euler_angles', 'no_orientation', b'no_orientation', 'quaternion', b'quaternion', 'type', b'type', 'vector_degrees', b'vector_degrees', 'vector_radians', b'vector_radians']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['axis_angles', b'axis_angles', 'euler_angles', b'euler_angles', 'no_orientation', b'no_orientation', 'quaternion', b'quaternion', 'type', b'type', 'vector_degrees', b'vector_degrees', 'vector_radians', b'vector_radians']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['type', b'type']) -> typing_extensions.Literal['no_orientation', 'vector_radians', 'vector_degrees', 'euler_angles', 'axis_angles', 'quaternion'] | None:
        ...
global___Orientation = Orientation

class RemoteConfig(google.protobuf.message.Message):
    """A RemoteConfig describes a remote robot that should be integrated.
    The Frame field defines how the "world" node of the remote robot should be reconciled with the "world" node of the
    the current robot. All components of the remote robot who have Parent as "world" will be attached to the parent defined
    in Frame, and with the given offset as well.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    ADDRESS_FIELD_NUMBER: builtins.int
    FRAME_FIELD_NUMBER: builtins.int
    AUTH_FIELD_NUMBER: builtins.int
    MANAGED_BY_FIELD_NUMBER: builtins.int
    INSECURE_FIELD_NUMBER: builtins.int
    CONNECTION_CHECK_INTERVAL_FIELD_NUMBER: builtins.int
    RECONNECT_INTERVAL_FIELD_NUMBER: builtins.int
    SERVICE_CONFIGS_FIELD_NUMBER: builtins.int
    SECRET_FIELD_NUMBER: builtins.int
    name: builtins.str
    address: builtins.str

    @property
    def frame(self) -> global___Frame:
        ...

    @property
    def auth(self) -> global___RemoteAuth:
        ...
    managed_by: builtins.str
    insecure: builtins.bool

    @property
    def connection_check_interval(self) -> google.protobuf.duration_pb2.Duration:
        ...

    @property
    def reconnect_interval(self) -> google.protobuf.duration_pb2.Duration:
        ...

    @property
    def service_configs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ResourceLevelServiceConfig]:
        ...
    secret: builtins.str
    'Secret is a helper for a robot location secret.'

    def __init__(self, *, name: builtins.str=..., address: builtins.str=..., frame: global___Frame | None=..., auth: global___RemoteAuth | None=..., managed_by: builtins.str=..., insecure: builtins.bool=..., connection_check_interval: google.protobuf.duration_pb2.Duration | None=..., reconnect_interval: google.protobuf.duration_pb2.Duration | None=..., service_configs: collections.abc.Iterable[global___ResourceLevelServiceConfig] | None=..., secret: builtins.str=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['auth', b'auth', 'connection_check_interval', b'connection_check_interval', 'frame', b'frame', 'reconnect_interval', b'reconnect_interval']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['address', b'address', 'auth', b'auth', 'connection_check_interval', b'connection_check_interval', 'frame', b'frame', 'insecure', b'insecure', 'managed_by', b'managed_by', 'name', b'name', 'reconnect_interval', b'reconnect_interval', 'secret', b'secret', 'service_configs', b'service_configs']) -> None:
        ...
global___RemoteConfig = RemoteConfig

class RemoteAuth(google.protobuf.message.Message):
    """RemoteAuth specifies how to authenticate against a remote. If no credentials are
    specified, authentication does not happen. If an entity is specified, the
    authentication request will specify it.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class Credentials(google.protobuf.message.Message):
        """Credentials packages up both a type of credential along with its payload which
        is formatted specific to the type.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        TYPE_FIELD_NUMBER: builtins.int
        PAYLOAD_FIELD_NUMBER: builtins.int
        type: global___CredentialsType.ValueType
        payload: builtins.str

        def __init__(self, *, type: global___CredentialsType.ValueType=..., payload: builtins.str=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['payload', b'payload', 'type', b'type']) -> None:
            ...
    CREDENTIALS_FIELD_NUMBER: builtins.int
    ENTITY_FIELD_NUMBER: builtins.int

    @property
    def credentials(self) -> global___RemoteAuth.Credentials:
        ...
    entity: builtins.str

    def __init__(self, *, credentials: global___RemoteAuth.Credentials | None=..., entity: builtins.str=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['credentials', b'credentials']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['credentials', b'credentials', 'entity', b'entity']) -> None:
        ...
global___RemoteAuth = RemoteAuth

class AgentInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HOST_FIELD_NUMBER: builtins.int
    OS_FIELD_NUMBER: builtins.int
    IPS_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    GIT_REVISION_FIELD_NUMBER: builtins.int
    host: builtins.str
    os: builtins.str

    @property
    def ips(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """list of all ipv4 ips."""
    version: builtins.str
    'RDK version'
    git_revision: builtins.str

    def __init__(self, *, host: builtins.str=..., os: builtins.str=..., ips: collections.abc.Iterable[builtins.str] | None=..., version: builtins.str=..., git_revision: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['git_revision', b'git_revision', 'host', b'host', 'ips', b'ips', 'os', b'os', 'version', b'version']) -> None:
        ...
global___AgentInfo = AgentInfo

class ConfigRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    AGENT_INFO_FIELD_NUMBER: builtins.int
    id: builtins.str
    'Robot part id.'

    @property
    def agent_info(self) -> global___AgentInfo:
        """Details about the RDK (os, version) are updated during this request."""

    def __init__(self, *, id: builtins.str=..., agent_info: global___AgentInfo | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['_agent_info', b'_agent_info', 'agent_info', b'agent_info']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['_agent_info', b'_agent_info', 'agent_info', b'agent_info', 'id', b'id']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['_agent_info', b'_agent_info']) -> typing_extensions.Literal['agent_info'] | None:
        ...
global___ConfigRequest = ConfigRequest

class ConfigResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONFIG_FIELD_NUMBER: builtins.int

    @property
    def config(self) -> global___RobotConfig:
        ...

    def __init__(self, *, config: global___RobotConfig | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['config', b'config']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['config', b'config']) -> None:
        ...
global___ConfigResponse = ConfigResponse

class CertificateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    'Robot part id.'

    def __init__(self, *, id: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['id', b'id']) -> None:
        ...
global___CertificateRequest = CertificateRequest

class CertificateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    TLS_CERTIFICATE_FIELD_NUMBER: builtins.int
    TLS_PRIVATE_KEY_FIELD_NUMBER: builtins.int
    id: builtins.str
    'Robot part id.'
    tls_certificate: builtins.str
    tls_private_key: builtins.str

    def __init__(self, *, id: builtins.str=..., tls_certificate: builtins.str=..., tls_private_key: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['id', b'id', 'tls_certificate', b'tls_certificate', 'tls_private_key', b'tls_private_key']) -> None:
        ...
global___CertificateResponse = CertificateResponse

class LogRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    LOGS_FIELD_NUMBER: builtins.int
    id: builtins.str
    'Robot part id.'

    @property
    def logs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[app.v1.app_pb2.LogEntry]:
        ...

    def __init__(self, *, id: builtins.str=..., logs: collections.abc.Iterable[app.v1.app_pb2.LogEntry] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['id', b'id', 'logs', b'logs']) -> None:
        ...
global___LogRequest = LogRequest

class LogResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___LogResponse = LogResponse

class NeedsRestartRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    'Robot part id.'

    def __init__(self, *, id: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['id', b'id']) -> None:
        ...
global___NeedsRestartRequest = NeedsRestartRequest

class NeedsRestartResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    MUST_RESTART_FIELD_NUMBER: builtins.int
    RESTART_CHECK_INTERVAL_FIELD_NUMBER: builtins.int
    id: builtins.str
    'Robot part id.'
    must_restart: builtins.bool

    @property
    def restart_check_interval(self) -> google.protobuf.duration_pb2.Duration:
        ...

    def __init__(self, *, id: builtins.str=..., must_restart: builtins.bool=..., restart_check_interval: google.protobuf.duration_pb2.Duration | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['restart_check_interval', b'restart_check_interval']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['id', b'id', 'must_restart', b'must_restart', 'restart_check_interval', b'restart_check_interval']) -> None:
        ...
global___NeedsRestartResponse = NeedsRestartResponse