# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: VIPData.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rVIPData.proto\"\xa5\x03\n\x05J1939\x12\x10\n\x03pgn\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x10\n\x03spn\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\x11\n\x04name\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x16\n\tbitLength\x18\x04 \x01(\rH\x03\x88\x01\x01\x12\x15\n\x08\x62itStart\x18\x05 \x01(\rH\x04\x88\x01\x01\x12\x13\n\x06\x66\x61\x63tor\x18\x06 \x01(\x02H\x05\x88\x01\x01\x12\x18\n\x0bisBigEndian\x18\x07 \x01(\x08H\x06\x88\x01\x01\x12\x15\n\x08isSigned\x18\x08 \x01(\x08H\x07\x88\x01\x01\x12\x13\n\x06offset\x18\t \x01(\x02H\x08\x88\x01\x01\x12\x17\n\nsecureRead\x18\n \x01(\x08H\t\x88\x01\x01\x12\x18\n\x0bsecureWrite\x18\x0b \x01(\x08H\n\x88\x01\x01\x12\x15\n\x08\x63omment0\x18\x0c \x01(\tH\x0b\x88\x01\x01\x42\x06\n\x04_pgnB\x06\n\x04_spnB\x07\n\x05_nameB\x0c\n\n_bitLengthB\x0b\n\t_bitStartB\t\n\x07_factorB\x0e\n\x0c_isBigEndianB\x0b\n\t_isSignedB\t\n\x07_offsetB\r\n\x0b_secureReadB\x0e\n\x0c_secureWriteB\x0b\n\t_comment0\"\x9d\x03\n\x03UDS\x12\x10\n\x03\x64id\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x11\n\x04name\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x16\n\tbitLength\x18\x03 \x01(\rH\x02\x88\x01\x01\x12\x15\n\x08\x62itStart\x18\x04 \x01(\rH\x03\x88\x01\x01\x12\x13\n\x06\x66\x61\x63tor\x18\x05 \x01(\x02H\x04\x88\x01\x01\x12\x13\n\x06offset\x18\x06 \x01(\x02H\x05\x88\x01\x01\x12\x15\n\x08isSigned\x18\x07 \x01(\x08H\x06\x88\x01\x01\x12\x18\n\x0bisBigEndian\x18\x08 \x01(\x08H\x07\x88\x01\x01\x12#\n\x08readMask\x18\t \x01(\x0e\x32\x0c.UdsSecurityH\x08\x88\x01\x01\x12$\n\twriteMask\x18\n \x01(\x0e\x32\x0c.UdsSecurityH\t\x88\x01\x01\x12\x15\n\x08\x63omment0\x18\x0b \x01(\tH\n\x88\x01\x01\x42\x06\n\x04_didB\x07\n\x05_nameB\x0c\n\n_bitLengthB\x0b\n\t_bitStartB\t\n\x07_factorB\t\n\x07_offsetB\x0b\n\t_isSignedB\x0e\n\x0c_isBigEndianB\x0b\n\t_readMaskB\x0c\n\n_writeMaskB\x0b\n\t_comment0\"\x8e\x02\n\x04\x44\x42US\x12\x1a\n\rinterfaceName\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x19\n\x0cpropertyName\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x19\n\x0cpropertyType\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x1b\n\x0epropertyAccess\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x1a\n\rpropertyUnits\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x15\n\x08\x63omment0\x18\x06 \x01(\tH\x05\x88\x01\x01\x42\x10\n\x0e_interfaceNameB\x0f\n\r_propertyNameB\x0f\n\r_propertyTypeB\x11\n\x0f_propertyAccessB\x10\n\x0e_propertyUnitsB\x0b\n\t_comment0\"\xc4\x03\n\x0c\x44\x61taBaseType\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x11\n\x04name\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1f\n\x04type\x18\x03 \x01(\x0e\x32\x0c.ElementTypeH\x02\x88\x01\x01\x12\x12\n\x05value\x18\x04 \x01(\rH\x03\x88\x01\x01\x12 \n\x06\x61\x63\x63\x65ss\x18\x05 \x01(\x0e\x32\x0b.AccessTypeH\x04\x88\x01\x01\x12\x13\n\x06minLen\x18\x06 \x01(\rH\x05\x88\x01\x01\x12\x13\n\x06maxLen\x18\x07 \x01(\rH\x06\x88\x01\x01\x12\x14\n\x07persist\x18\x08 \x01(\x08H\x07\x88\x01\x01\x12\x1a\n\x05j1939\x18\t \x01(\x0b\x32\x06.J1939H\x08\x88\x01\x01\x12\x16\n\x03uds\x18\n \x01(\x0b\x32\x04.UDSH\t\x88\x01\x01\x12\x18\n\x04\x64\x62us\x18\x0b \x01(\x0b\x32\x05.DBUSH\n\x88\x01\x01\x12\x15\n\x08\x63omment0\x18\x0c \x01(\tH\x0b\x88\x01\x01\x12\x12\n\x05sqlID\x18\r \x01(\tH\x0c\x88\x01\x01\x42\x05\n\x03_idB\x07\n\x05_nameB\x07\n\x05_typeB\x08\n\x06_valueB\t\n\x07_accessB\t\n\x07_minLenB\t\n\x07_maxLenB\n\n\x08_persistB\x08\n\x06_j1939B\x06\n\x04_udsB\x07\n\x05_dbusB\x0b\n\t_comment0B\x08\n\x06_sqlID\"(\n\x08\x44\x61taBase\x12\x1c\n\x05\x65ntry\x18\x01 \x03(\x0b\x32\r.DataBaseType*<\n\x0b\x45lementType\x12\x0b\n\x07INTEGER\x10\x00\x12\n\n\x06STRING\x10\x01\x12\x08\n\x04\x42OOL\x10\x03\x12\n\n\x06\x42INARY\x10\x04*\"\n\nAccessType\x12\x05\n\x01R\x10\x00\x12\x05\n\x01W\x10\x01\x12\x06\n\x02RW\x10\x02* \n\x0bPersistType\x12\x08\n\x04NONE\x10\x00\x12\x07\n\x03NVM\x10\x01*j\n\x0bUdsSecurity\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x0c\n\x08\x45XTENDED\x10\x01\x12\x0f\n\x0bPROGRAMMING\x10\x02\x12\x15\n\x11\x45XTENDED_UNLOCKED\x10\x03\x12\x18\n\x14PROGRAMMING_UNLOCKED\x10\x04\x62\x06proto3')

_ELEMENTTYPE = DESCRIPTOR.enum_types_by_name['ElementType']
ElementType = enum_type_wrapper.EnumTypeWrapper(_ELEMENTTYPE)
_ACCESSTYPE = DESCRIPTOR.enum_types_by_name['AccessType']
AccessType = enum_type_wrapper.EnumTypeWrapper(_ACCESSTYPE)
_PERSISTTYPE = DESCRIPTOR.enum_types_by_name['PersistType']
PersistType = enum_type_wrapper.EnumTypeWrapper(_PERSISTTYPE)
_UDSSECURITY = DESCRIPTOR.enum_types_by_name['UdsSecurity']
UdsSecurity = enum_type_wrapper.EnumTypeWrapper(_UDSSECURITY)
INTEGER = 0
STRING = 1
BOOL = 3
BINARY = 4
R = 0
W = 1
RW = 2
NONE = 0
NVM = 1
DEFAULT = 0
EXTENDED = 1
PROGRAMMING = 2
EXTENDED_UNLOCKED = 3
PROGRAMMING_UNLOCKED = 4


_J1939 = DESCRIPTOR.message_types_by_name['J1939']
_UDS = DESCRIPTOR.message_types_by_name['UDS']
_DBUS = DESCRIPTOR.message_types_by_name['DBUS']
_DATABASETYPE = DESCRIPTOR.message_types_by_name['DataBaseType']
_DATABASE = DESCRIPTOR.message_types_by_name['DataBase']
J1939 = _reflection.GeneratedProtocolMessageType('J1939', (_message.Message,), {
  'DESCRIPTOR' : _J1939,
  '__module__' : 'VIPData_pb2'
  # @@protoc_insertion_point(class_scope:J1939)
  })
_sym_db.RegisterMessage(J1939)

UDS = _reflection.GeneratedProtocolMessageType('UDS', (_message.Message,), {
  'DESCRIPTOR' : _UDS,
  '__module__' : 'VIPData_pb2'
  # @@protoc_insertion_point(class_scope:UDS)
  })
_sym_db.RegisterMessage(UDS)

DBUS = _reflection.GeneratedProtocolMessageType('DBUS', (_message.Message,), {
  'DESCRIPTOR' : _DBUS,
  '__module__' : 'VIPData_pb2'
  # @@protoc_insertion_point(class_scope:DBUS)
  })
_sym_db.RegisterMessage(DBUS)

DataBaseType = _reflection.GeneratedProtocolMessageType('DataBaseType', (_message.Message,), {
  'DESCRIPTOR' : _DATABASETYPE,
  '__module__' : 'VIPData_pb2'
  # @@protoc_insertion_point(class_scope:DataBaseType)
  })
_sym_db.RegisterMessage(DataBaseType)

DataBase = _reflection.GeneratedProtocolMessageType('DataBase', (_message.Message,), {
  'DESCRIPTOR' : _DATABASE,
  '__module__' : 'VIPData_pb2'
  # @@protoc_insertion_point(class_scope:DataBase)
  })
_sym_db.RegisterMessage(DataBase)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ELEMENTTYPE._serialized_start=1627
  _ELEMENTTYPE._serialized_end=1687
  _ACCESSTYPE._serialized_start=1689
  _ACCESSTYPE._serialized_end=1723
  _PERSISTTYPE._serialized_start=1725
  _PERSISTTYPE._serialized_end=1757
  _UDSSECURITY._serialized_start=1759
  _UDSSECURITY._serialized_end=1865
  _J1939._serialized_start=18
  _J1939._serialized_end=439
  _UDS._serialized_start=442
  _UDS._serialized_end=855
  _DBUS._serialized_start=858
  _DBUS._serialized_end=1128
  _DATABASETYPE._serialized_start=1131
  _DATABASETYPE._serialized_end=1583
  _DATABASE._serialized_start=1585
  _DATABASE._serialized_end=1625
# @@protoc_insertion_point(module_scope)
