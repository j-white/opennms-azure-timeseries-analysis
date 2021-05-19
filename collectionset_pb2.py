# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: collectionset.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='collectionset.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n)org.opennms.features.kafka.producer.modelB\023CollectionSetProtos',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x63ollectionset.proto\".\n\x0fStringAttribute\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x84\x01\n\x10NumericAttribute\x12\r\n\x05group\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x01\x12$\n\x04type\x18\x04 \x01(\x0e\x32\x16.NumericAttribute.Type\"\x1e\n\x04Type\x12\t\n\x05GAUGE\x10\x00\x12\x0b\n\x07\x43OUNTER\x10\x01\"v\n\x11NodeLevelResource\x12\x0f\n\x07node_id\x18\x01 \x01(\x03\x12\x16\n\x0e\x66oreign_source\x18\x02 \x01(\t\x12\x12\n\nforeign_id\x18\x03 \x01(\t\x12\x12\n\nnode_label\x18\x04 \x01(\t\x12\x10\n\x08location\x18\x05 \x01(\t\"^\n\x16InterfaceLevelResource\x12 \n\x04node\x18\x01 \x01(\x0b\x32\x12.NodeLevelResource\x12\x10\n\x08instance\x18\x02 \x01(\t\x12\x10\n\x08if_index\x18\x03 \x01(\x05\"W\n\x13GenericTypeResource\x12 \n\x04node\x18\x01 \x01(\x0b\x32\x12.NodeLevelResource\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x10\n\x08instance\x18\x03 \x01(\t\":\n\x14ResponseTimeResource\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x10\n\x08location\x18\x02 \x01(\t\"\x8f\x02\n\x15\x43ollectionSetResource\x12\"\n\x04node\x18\x01 \x01(\x0b\x32\x12.NodeLevelResourceH\x00\x12,\n\tinterface\x18\x02 \x01(\x0b\x32\x17.InterfaceLevelResourceH\x00\x12\'\n\x07generic\x18\x03 \x01(\x0b\x32\x14.GenericTypeResourceH\x00\x12)\n\x08response\x18\x04 \x01(\x0b\x32\x15.ResponseTimeResourceH\x00\x12 \n\x06string\x18\n \x03(\x0b\x32\x10.StringAttribute\x12\"\n\x07numeric\x18\x0b \x03(\x0b\x32\x11.NumericAttributeB\n\n\x08resource\"L\n\rCollectionSet\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12(\n\x08resource\x18\x02 \x03(\x0b\x32\x16.CollectionSetResourceB@\n)org.opennms.features.kafka.producer.modelB\x13\x43ollectionSetProtosb\x06proto3'
)



_NUMERICATTRIBUTE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='NumericAttribute.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GAUGE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COUNTER', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=174,
  serialized_end=204,
)
_sym_db.RegisterEnumDescriptor(_NUMERICATTRIBUTE_TYPE)


_STRINGATTRIBUTE = _descriptor.Descriptor(
  name='StringAttribute',
  full_name='StringAttribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='StringAttribute.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='StringAttribute.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=69,
)


_NUMERICATTRIBUTE = _descriptor.Descriptor(
  name='NumericAttribute',
  full_name='NumericAttribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='group', full_name='NumericAttribute.group', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='NumericAttribute.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='NumericAttribute.value', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='NumericAttribute.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NUMERICATTRIBUTE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=204,
)


_NODELEVELRESOURCE = _descriptor.Descriptor(
  name='NodeLevelResource',
  full_name='NodeLevelResource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_id', full_name='NodeLevelResource.node_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='foreign_source', full_name='NodeLevelResource.foreign_source', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='foreign_id', full_name='NodeLevelResource.foreign_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node_label', full_name='NodeLevelResource.node_label', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='NodeLevelResource.location', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=206,
  serialized_end=324,
)


_INTERFACELEVELRESOURCE = _descriptor.Descriptor(
  name='InterfaceLevelResource',
  full_name='InterfaceLevelResource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='InterfaceLevelResource.node', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instance', full_name='InterfaceLevelResource.instance', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_index', full_name='InterfaceLevelResource.if_index', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=326,
  serialized_end=420,
)


_GENERICTYPERESOURCE = _descriptor.Descriptor(
  name='GenericTypeResource',
  full_name='GenericTypeResource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='GenericTypeResource.node', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='GenericTypeResource.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instance', full_name='GenericTypeResource.instance', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=422,
  serialized_end=509,
)


_RESPONSETIMERESOURCE = _descriptor.Descriptor(
  name='ResponseTimeResource',
  full_name='ResponseTimeResource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='ResponseTimeResource.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='ResponseTimeResource.location', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=511,
  serialized_end=569,
)


_COLLECTIONSETRESOURCE = _descriptor.Descriptor(
  name='CollectionSetResource',
  full_name='CollectionSetResource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='CollectionSetResource.node', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='interface', full_name='CollectionSetResource.interface', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='generic', full_name='CollectionSetResource.generic', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response', full_name='CollectionSetResource.response', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='string', full_name='CollectionSetResource.string', index=4,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='numeric', full_name='CollectionSetResource.numeric', index=5,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='resource', full_name='CollectionSetResource.resource',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=572,
  serialized_end=843,
)


_COLLECTIONSET = _descriptor.Descriptor(
  name='CollectionSet',
  full_name='CollectionSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='CollectionSet.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource', full_name='CollectionSet.resource', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=845,
  serialized_end=921,
)

_NUMERICATTRIBUTE.fields_by_name['type'].enum_type = _NUMERICATTRIBUTE_TYPE
_NUMERICATTRIBUTE_TYPE.containing_type = _NUMERICATTRIBUTE
_INTERFACELEVELRESOURCE.fields_by_name['node'].message_type = _NODELEVELRESOURCE
_GENERICTYPERESOURCE.fields_by_name['node'].message_type = _NODELEVELRESOURCE
_COLLECTIONSETRESOURCE.fields_by_name['node'].message_type = _NODELEVELRESOURCE
_COLLECTIONSETRESOURCE.fields_by_name['interface'].message_type = _INTERFACELEVELRESOURCE
_COLLECTIONSETRESOURCE.fields_by_name['generic'].message_type = _GENERICTYPERESOURCE
_COLLECTIONSETRESOURCE.fields_by_name['response'].message_type = _RESPONSETIMERESOURCE
_COLLECTIONSETRESOURCE.fields_by_name['string'].message_type = _STRINGATTRIBUTE
_COLLECTIONSETRESOURCE.fields_by_name['numeric'].message_type = _NUMERICATTRIBUTE
_COLLECTIONSETRESOURCE.oneofs_by_name['resource'].fields.append(
  _COLLECTIONSETRESOURCE.fields_by_name['node'])
_COLLECTIONSETRESOURCE.fields_by_name['node'].containing_oneof = _COLLECTIONSETRESOURCE.oneofs_by_name['resource']
_COLLECTIONSETRESOURCE.oneofs_by_name['resource'].fields.append(
  _COLLECTIONSETRESOURCE.fields_by_name['interface'])
_COLLECTIONSETRESOURCE.fields_by_name['interface'].containing_oneof = _COLLECTIONSETRESOURCE.oneofs_by_name['resource']
_COLLECTIONSETRESOURCE.oneofs_by_name['resource'].fields.append(
  _COLLECTIONSETRESOURCE.fields_by_name['generic'])
_COLLECTIONSETRESOURCE.fields_by_name['generic'].containing_oneof = _COLLECTIONSETRESOURCE.oneofs_by_name['resource']
_COLLECTIONSETRESOURCE.oneofs_by_name['resource'].fields.append(
  _COLLECTIONSETRESOURCE.fields_by_name['response'])
_COLLECTIONSETRESOURCE.fields_by_name['response'].containing_oneof = _COLLECTIONSETRESOURCE.oneofs_by_name['resource']
_COLLECTIONSET.fields_by_name['resource'].message_type = _COLLECTIONSETRESOURCE
DESCRIPTOR.message_types_by_name['StringAttribute'] = _STRINGATTRIBUTE
DESCRIPTOR.message_types_by_name['NumericAttribute'] = _NUMERICATTRIBUTE
DESCRIPTOR.message_types_by_name['NodeLevelResource'] = _NODELEVELRESOURCE
DESCRIPTOR.message_types_by_name['InterfaceLevelResource'] = _INTERFACELEVELRESOURCE
DESCRIPTOR.message_types_by_name['GenericTypeResource'] = _GENERICTYPERESOURCE
DESCRIPTOR.message_types_by_name['ResponseTimeResource'] = _RESPONSETIMERESOURCE
DESCRIPTOR.message_types_by_name['CollectionSetResource'] = _COLLECTIONSETRESOURCE
DESCRIPTOR.message_types_by_name['CollectionSet'] = _COLLECTIONSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StringAttribute = _reflection.GeneratedProtocolMessageType('StringAttribute', (_message.Message,), {
  'DESCRIPTOR' : _STRINGATTRIBUTE,
  '__module__' : 'collectionset_pb2'
  # @@protoc_insertion_point(class_scope:StringAttribute)
  })
_sym_db.RegisterMessage(StringAttribute)

NumericAttribute = _reflection.GeneratedProtocolMessageType('NumericAttribute', (_message.Message,), {
  'DESCRIPTOR' : _NUMERICATTRIBUTE,
  '__module__' : 'collectionset_pb2'
  # @@protoc_insertion_point(class_scope:NumericAttribute)
  })
_sym_db.RegisterMessage(NumericAttribute)

NodeLevelResource = _reflection.GeneratedProtocolMessageType('NodeLevelResource', (_message.Message,), {
  'DESCRIPTOR' : _NODELEVELRESOURCE,
  '__module__' : 'collectionset_pb2'
  # @@protoc_insertion_point(class_scope:NodeLevelResource)
  })
_sym_db.RegisterMessage(NodeLevelResource)

InterfaceLevelResource = _reflection.GeneratedProtocolMessageType('InterfaceLevelResource', (_message.Message,), {
  'DESCRIPTOR' : _INTERFACELEVELRESOURCE,
  '__module__' : 'collectionset_pb2'
  # @@protoc_insertion_point(class_scope:InterfaceLevelResource)
  })
_sym_db.RegisterMessage(InterfaceLevelResource)

GenericTypeResource = _reflection.GeneratedProtocolMessageType('GenericTypeResource', (_message.Message,), {
  'DESCRIPTOR' : _GENERICTYPERESOURCE,
  '__module__' : 'collectionset_pb2'
  # @@protoc_insertion_point(class_scope:GenericTypeResource)
  })
_sym_db.RegisterMessage(GenericTypeResource)

ResponseTimeResource = _reflection.GeneratedProtocolMessageType('ResponseTimeResource', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSETIMERESOURCE,
  '__module__' : 'collectionset_pb2'
  # @@protoc_insertion_point(class_scope:ResponseTimeResource)
  })
_sym_db.RegisterMessage(ResponseTimeResource)

CollectionSetResource = _reflection.GeneratedProtocolMessageType('CollectionSetResource', (_message.Message,), {
  'DESCRIPTOR' : _COLLECTIONSETRESOURCE,
  '__module__' : 'collectionset_pb2'
  # @@protoc_insertion_point(class_scope:CollectionSetResource)
  })
_sym_db.RegisterMessage(CollectionSetResource)

CollectionSet = _reflection.GeneratedProtocolMessageType('CollectionSet', (_message.Message,), {
  'DESCRIPTOR' : _COLLECTIONSET,
  '__module__' : 'collectionset_pb2'
  # @@protoc_insertion_point(class_scope:CollectionSet)
  })
_sym_db.RegisterMessage(CollectionSet)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
