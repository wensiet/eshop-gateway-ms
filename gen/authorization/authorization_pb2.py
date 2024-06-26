# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gen/authorization/authorization.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%gen/authorization/authorization.proto\"/\n\x0cLoginRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x1e\n\rLoginResponse\x12\r\n\x05token\x18\x01 \x01(\t\"2\n\x0fRegisterRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x07\n\x05\x45mpty2a\n\rAuthorization\x12(\n\x05Login\x12\r.LoginRequest\x1a\x0e.LoginResponse\"\x00\x12&\n\x08Register\x12\x10.RegisterRequest\x1a\x06.Empty\"\x00\x42*Z(wensiet.authorization.v1;authorizationv1b\x06proto3')



_LOGINREQUEST = DESCRIPTOR.message_types_by_name['LoginRequest']
_LOGINRESPONSE = DESCRIPTOR.message_types_by_name['LoginResponse']
_REGISTERREQUEST = DESCRIPTOR.message_types_by_name['RegisterRequest']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
LoginRequest = _reflection.GeneratedProtocolMessageType('LoginRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREQUEST,
  '__module__' : 'gen.authorization.authorization_pb2'
  # @@protoc_insertion_point(class_scope:LoginRequest)
  })
_sym_db.RegisterMessage(LoginRequest)

LoginResponse = _reflection.GeneratedProtocolMessageType('LoginResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGINRESPONSE,
  '__module__' : 'gen.authorization.authorization_pb2'
  # @@protoc_insertion_point(class_scope:LoginResponse)
  })
_sym_db.RegisterMessage(LoginResponse)

RegisterRequest = _reflection.GeneratedProtocolMessageType('RegisterRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERREQUEST,
  '__module__' : 'gen.authorization.authorization_pb2'
  # @@protoc_insertion_point(class_scope:RegisterRequest)
  })
_sym_db.RegisterMessage(RegisterRequest)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'gen.authorization.authorization_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

_AUTHORIZATION = DESCRIPTOR.services_by_name['Authorization']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z(wensiet.authorization.v1;authorizationv1'
  _LOGINREQUEST._serialized_start=41
  _LOGINREQUEST._serialized_end=88
  _LOGINRESPONSE._serialized_start=90
  _LOGINRESPONSE._serialized_end=120
  _REGISTERREQUEST._serialized_start=122
  _REGISTERREQUEST._serialized_end=172
  _EMPTY._serialized_start=174
  _EMPTY._serialized_end=181
  _AUTHORIZATION._serialized_start=183
  _AUTHORIZATION._serialized_end=280
# @@protoc_insertion_point(module_scope)
