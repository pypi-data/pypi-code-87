# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/atlas/statement.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='eolymp/atlas/statement.proto',
  package='eolymp.atlas',
  syntax='proto3',
  serialized_options=b'Z1github.com/eolymp/contracts/go/eolymp/atlas;atlas',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1c\x65olymp/atlas/statement.proto\x12\x0c\x65olymp.atlas\"\xe0\x01\n\tStatement\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nproblem_id\x18\x02 \x01(\t\x12\x0e\n\x06locale\x18\x03 \x01(\t\x12\r\n\x05title\x18\x04 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\t\x12.\n\x06\x66ormat\x18\x06 \x01(\x0e\x32\x1e.eolymp.atlas.Statement.Format\x12\x0e\n\x06\x61uthor\x18\x65 \x01(\t\x12\x0e\n\x06source\x18\x66 \x01(\t\"3\n\x06\x46ormat\x12\x08\n\x04NONE\x10\x00\x12\x07\n\x03TEX\x10\x01\x12\x0c\n\x08MARKDOWN\x10\x02\x12\x08\n\x04HTML\x10\x03\x42\x33Z1github.com/eolymp/contracts/go/eolymp/atlas;atlasb\x06proto3'
)



_STATEMENT_FORMAT = _descriptor.EnumDescriptor(
  name='Format',
  full_name='eolymp.atlas.Statement.Format',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TEX', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MARKDOWN', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HTML', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=220,
  serialized_end=271,
)
_sym_db.RegisterEnumDescriptor(_STATEMENT_FORMAT)


_STATEMENT = _descriptor.Descriptor(
  name='Statement',
  full_name='eolymp.atlas.Statement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='eolymp.atlas.Statement.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='problem_id', full_name='eolymp.atlas.Statement.problem_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='locale', full_name='eolymp.atlas.Statement.locale', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='eolymp.atlas.Statement.title', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='eolymp.atlas.Statement.content', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='format', full_name='eolymp.atlas.Statement.format', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='author', full_name='eolymp.atlas.Statement.author', index=6,
      number=101, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='eolymp.atlas.Statement.source', index=7,
      number=102, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STATEMENT_FORMAT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=271,
)

_STATEMENT.fields_by_name['format'].enum_type = _STATEMENT_FORMAT
_STATEMENT_FORMAT.containing_type = _STATEMENT
DESCRIPTOR.message_types_by_name['Statement'] = _STATEMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Statement = _reflection.GeneratedProtocolMessageType('Statement', (_message.Message,), {
  'DESCRIPTOR' : _STATEMENT,
  '__module__' : 'eolymp.atlas.statement_pb2'
  # @@protoc_insertion_point(class_scope:eolymp.atlas.Statement)
  })
_sym_db.RegisterMessage(Statement)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
