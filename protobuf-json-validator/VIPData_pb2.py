# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: VIPData.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rVIPData.proto\"\xd2\x15\n\x07VIPData\x12<\n\x11STAT_ENGINE_SPEED\x18\x01 \x01(\x0b\x32\x1c.VIPData.VehiclePropertyStatH\x00\x88\x01\x01\x12@\n\x15STAT_REAR_WHEEL_SPEED\x18\x02 \x01(\x0b\x32\x1c.VIPData.VehiclePropertyStatH\x01\x88\x01\x01\x12\x38\n\rSTAT_VBATTERY\x18\x03 \x01(\x0b\x32\x1c.VIPData.VehiclePropertyStatH\x02\x88\x01\x01\x12:\n\x0fSTAT_FUEL_LEVEL\x18\x04 \x01(\x0b\x32\x1c.VIPData.VehiclePropertyStatH\x03\x88\x01\x01\x12<\n\x11STAT_NVM_ODOMETER\x18\x05 \x01(\x0b\x32\x1c.VIPData.VehiclePropertyStatH\x04\x88\x01\x01\x12>\n\x13STAT_GEAR_INDICATOR\x18\x06 \x01(\x0b\x32\x1c.VIPData.VehiclePropertyStatH\x05\x88\x01\x01\x1a\xca\x02\n\x0e\x44\x62usAttributes\x12\x1b\n\x0einterface_name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\rproperty_name\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1a\n\rproperty_type\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x1c\n\x0fproperty_access\x18\x04 \x01(\tH\x03\x88\x01\x01\x12)\n\x1cproperty_update_rate_per_sec\x18\x05 \x01(\x05H\x04\x88\x01\x01\x12\x1b\n\x0eproperty_units\x18\x06 \x01(\tH\x05\x88\x01\x01\x42\x11\n\x0f_interface_nameB\x10\n\x0e_property_nameB\x10\n\x0e_property_typeB\x12\n\x10_property_accessB\x1f\n\x1d_property_update_rate_per_secB\x11\n\x0f_property_units\x1a\x8b\x04\n\x0fJ1939Attributes\x12\x10\n\x03PGN\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x03SPN\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x15\n\x08\x63omment0\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x1b\n\x0esource_address\x18\x04 \x01(\x05H\x03\x88\x01\x01\x12\x17\n\nbit_length\x18\x05 \x01(\x05H\x04\x88\x01\x01\x12\x13\n\x06\x66\x61\x63tor\x18\x06 \x01(\x01H\x05\x88\x01\x01\x12\x1a\n\ris_big_endian\x18\x07 \x01(\x08H\x06\x88\x01\x01\x12\x16\n\tis_signed\x18\x08 \x01(\x08H\x07\x88\x01\x01\x12\x11\n\x04name\x18\t \x01(\tH\x08\x88\x01\x01\x12\x13\n\x06offset\x18\n \x01(\x05H\t\x88\x01\x01\x12\x16\n\tstart_bit\x18\x0b \x01(\x05H\n\x88\x01\x01\x12\x12\n\x05units\x18\x0c \x01(\tH\x0b\x88\x01\x01\x12\x18\n\x0bsecure_read\x18\r \x01(\x08H\x0c\x88\x01\x01\x12\x19\n\x0csecure_write\x18\x0e \x01(\x08H\r\x88\x01\x01\x42\x06\n\x04_PGNB\x06\n\x04_SPNB\x0b\n\t_comment0B\x11\n\x0f_source_addressB\r\n\x0b_bit_lengthB\t\n\x07_factorB\x10\n\x0e_is_big_endianB\x0c\n\n_is_signedB\x07\n\x05_nameB\t\n\x07_offsetB\x0c\n\n_start_bitB\x08\n\x06_unitsB\x0e\n\x0c_secure_readB\x0f\n\r_secure_write\x1a\xd3\x03\n\rUdsAttributes\x12\x10\n\x03\x44ID\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x17\n\nbit_length\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x15\n\x08\x63omment0\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x13\n\x06\x66\x61\x63tor\x18\x04 \x01(\x01H\x03\x88\x01\x01\x12\x1a\n\ris_big_endian\x18\x05 \x01(\x08H\x04\x88\x01\x01\x12\x16\n\tis_signed\x18\x06 \x01(\x08H\x05\x88\x01\x01\x12\x11\n\x04name\x18\x07 \x01(\tH\x06\x88\x01\x01\x12\x13\n\x06offset\x18\x08 \x01(\x01H\x07\x88\x01\x01\x12\x16\n\tstart_bit\x18\t \x01(\x05H\x08\x88\x01\x01\x12\x12\n\x05units\x18\n \x01(\tH\t\x88\x01\x01\x12\x1d\n\x10securityReadMask\x18\x0b \x01(\tH\n\x88\x01\x01\x12\x1e\n\x11securityWriteMask\x18\x0c \x01(\tH\x0b\x88\x01\x01\x42\x06\n\x04_DIDB\r\n\x0b_bit_lengthB\x0b\n\t_comment0B\t\n\x07_factorB\x10\n\x0e_is_big_endianB\x0c\n\n_is_signedB\x07\n\x05_nameB\t\n\x07_offsetB\x0c\n\n_start_bitB\x08\n\x06_unitsB\x13\n\x11_securityReadMaskB\x14\n\x12_securityWriteMask\x1a\x33\n\x04\x44\x62us\x12+\n\nattributes\x18\x01 \x01(\x0b\x32\x17.VIPData.DbusAttributes\x1ap\n\x03Uds\x12/\n\nattributes\x18\x01 \x01(\x0b\x32\x16.VIPData.UdsAttributesH\x00\x88\x01\x01\x12 \n\x04\x44\x42us\x18\x02 \x01(\x0b\x32\r.VIPData.DbusH\x01\x88\x01\x01\x42\r\n\x0b_attributesB\x07\n\x05_DBus\x1a\x9c\x01\n\x05J1939\x12\x31\n\nattributes\x18\x01 \x01(\x0b\x32\x18.VIPData.J1939AttributesH\x00\x88\x01\x01\x12\x1e\n\x03UDS\x18\x02 \x01(\x0b\x32\x0c.VIPData.UdsH\x01\x88\x01\x01\x12 \n\x04\x44\x42us\x18\x03 \x01(\x0b\x32\r.VIPData.DbusH\x02\x88\x01\x01\x42\r\n\x0b_attributesB\x06\n\x04_UDSB\x07\n\x05_DBus\x1a\xd7\x04\n\x13VehiclePropertyStat\x12\x1e\n\x11\x64\x65\x66\x61ult_value_bin\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1e\n\x11\x64\x65\x66\x61ult_value_int\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12!\n\x14\x64\x65\x66\x61ult_value_string\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x12\n\x05sqlID\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x10\n\x03key\x18\x05 \x01(\x05H\x04\x88\x01\x01\x12\x13\n\x06\x61\x63\x63\x65ss\x18\x06 \x01(\tH\x05\x88\x01\x01\x12\x14\n\x07min_len\x18\x07 \x01(\tH\x06\x88\x01\x01\x12\x14\n\x07max_len\x18\x08 \x01(\tH\x07\x88\x01\x01\x12\x14\n\x07min_val\x18\t \x01(\tH\x08\x88\x01\x01\x12\x14\n\x07max_val\x18\n \x01(\tH\t\x88\x01\x01\x12\x14\n\x07persist\x18\x0b \x01(\x08H\n\x88\x01\x01\x12\x1e\n\x11period_default_ms\x18\x0c \x01(\x05H\x0b\x88\x01\x01\x12\x1d\n\x10period_update_ms\x18\r \x01(\x05H\x0c\x88\x01\x01\x12\"\n\x05J1939\x18\x0e \x01(\x0b\x32\x0e.VIPData.J1939H\r\x88\x01\x01\x42\x14\n\x12_default_value_binB\x14\n\x12_default_value_intB\x17\n\x15_default_value_stringB\x08\n\x06_sqlIDB\x06\n\x04_keyB\t\n\x07_accessB\n\n\x08_min_lenB\n\n\x08_max_lenB\n\n\x08_min_valB\n\n\x08_max_valB\n\n\x08_persistB\x14\n\x12_period_default_msB\x13\n\x11_period_update_msB\x08\n\x06_J1939B\x14\n\x12_STAT_ENGINE_SPEEDB\x18\n\x16_STAT_REAR_WHEEL_SPEEDB\x10\n\x0e_STAT_VBATTERYB\x12\n\x10_STAT_FUEL_LEVELB\x14\n\x12_STAT_NVM_ODOMETERB\x16\n\x14_STAT_GEAR_INDICATORb\x06proto3')



_VIPDATA = DESCRIPTOR.message_types_by_name['VIPData']
_VIPDATA_DBUSATTRIBUTES = _VIPDATA.nested_types_by_name['DbusAttributes']
_VIPDATA_J1939ATTRIBUTES = _VIPDATA.nested_types_by_name['J1939Attributes']
_VIPDATA_UDSATTRIBUTES = _VIPDATA.nested_types_by_name['UdsAttributes']
_VIPDATA_DBUS = _VIPDATA.nested_types_by_name['Dbus']
_VIPDATA_UDS = _VIPDATA.nested_types_by_name['Uds']
_VIPDATA_J1939 = _VIPDATA.nested_types_by_name['J1939']
_VIPDATA_VEHICLEPROPERTYSTAT = _VIPDATA.nested_types_by_name['VehiclePropertyStat']
VIPData = _reflection.GeneratedProtocolMessageType('VIPData', (_message.Message,), {

  'DbusAttributes' : _reflection.GeneratedProtocolMessageType('DbusAttributes', (_message.Message,), {
    'DESCRIPTOR' : _VIPDATA_DBUSATTRIBUTES,
    '__module__' : 'VIPData_pb2'
    # @@protoc_insertion_point(class_scope:VIPData.DbusAttributes)
    })
  ,

  'J1939Attributes' : _reflection.GeneratedProtocolMessageType('J1939Attributes', (_message.Message,), {
    'DESCRIPTOR' : _VIPDATA_J1939ATTRIBUTES,
    '__module__' : 'VIPData_pb2'
    # @@protoc_insertion_point(class_scope:VIPData.J1939Attributes)
    })
  ,

  'UdsAttributes' : _reflection.GeneratedProtocolMessageType('UdsAttributes', (_message.Message,), {
    'DESCRIPTOR' : _VIPDATA_UDSATTRIBUTES,
    '__module__' : 'VIPData_pb2'
    # @@protoc_insertion_point(class_scope:VIPData.UdsAttributes)
    })
  ,

  'Dbus' : _reflection.GeneratedProtocolMessageType('Dbus', (_message.Message,), {
    'DESCRIPTOR' : _VIPDATA_DBUS,
    '__module__' : 'VIPData_pb2'
    # @@protoc_insertion_point(class_scope:VIPData.Dbus)
    })
  ,

  'Uds' : _reflection.GeneratedProtocolMessageType('Uds', (_message.Message,), {
    'DESCRIPTOR' : _VIPDATA_UDS,
    '__module__' : 'VIPData_pb2'
    # @@protoc_insertion_point(class_scope:VIPData.Uds)
    })
  ,

  'J1939' : _reflection.GeneratedProtocolMessageType('J1939', (_message.Message,), {
    'DESCRIPTOR' : _VIPDATA_J1939,
    '__module__' : 'VIPData_pb2'
    # @@protoc_insertion_point(class_scope:VIPData.J1939)
    })
  ,

  'VehiclePropertyStat' : _reflection.GeneratedProtocolMessageType('VehiclePropertyStat', (_message.Message,), {
    'DESCRIPTOR' : _VIPDATA_VEHICLEPROPERTYSTAT,
    '__module__' : 'VIPData_pb2'
    # @@protoc_insertion_point(class_scope:VIPData.VehiclePropertyStat)
    })
  ,
  'DESCRIPTOR' : _VIPDATA,
  '__module__' : 'VIPData_pb2'
  # @@protoc_insertion_point(class_scope:VIPData)
  })
_sym_db.RegisterMessage(VIPData)
_sym_db.RegisterMessage(VIPData.DbusAttributes)
_sym_db.RegisterMessage(VIPData.J1939Attributes)
_sym_db.RegisterMessage(VIPData.UdsAttributes)
_sym_db.RegisterMessage(VIPData.Dbus)
_sym_db.RegisterMessage(VIPData.Uds)
_sym_db.RegisterMessage(VIPData.J1939)
_sym_db.RegisterMessage(VIPData.VehiclePropertyStat)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _VIPDATA._serialized_start=18
  _VIPDATA._serialized_end=2788
  _VIPDATA_DBUSATTRIBUTES._serialized_start=402
  _VIPDATA_DBUSATTRIBUTES._serialized_end=732
  _VIPDATA_J1939ATTRIBUTES._serialized_start=735
  _VIPDATA_J1939ATTRIBUTES._serialized_end=1258
  _VIPDATA_UDSATTRIBUTES._serialized_start=1261
  _VIPDATA_UDSATTRIBUTES._serialized_end=1728
  _VIPDATA_DBUS._serialized_start=1730
  _VIPDATA_DBUS._serialized_end=1781
  _VIPDATA_UDS._serialized_start=1783
  _VIPDATA_UDS._serialized_end=1895
  _VIPDATA_J1939._serialized_start=1898
  _VIPDATA_J1939._serialized_end=2054
  _VIPDATA_VEHICLEPROPERTYSTAT._serialized_start=2057
  _VIPDATA_VEHICLEPROPERTYSTAT._serialized_end=2656
# @@protoc_insertion_point(module_scope)
