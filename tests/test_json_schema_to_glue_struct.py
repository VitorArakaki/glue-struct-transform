import os
import sys
import json
import pathlib
from glue_struct_transform import GlueStructTransform, working_with_arrays, working_with_objects, working_with_objects_json_body, working_with_arrays_json_body

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))


def test_json_schema_to_glue_struct_full_schema():
    local_path = pathlib.Path(__file__).parent.absolute()
    schema = open(r'{}/examples/schemas/teste_schema.json'.format(local_path),)
    schemaLoad = json.load(schema)

    test = GlueStructTransform.json_schema_to_glue_struct(schemaLoad)

    resultAwaited = "userId:int,id:double,title:string,completed:boolean,testeObject:struct<id:int,name:string,testeObjectInObject:struct<id:double,name:string>>,testeArray:array<struct<userId:int,id:double,title:string,completed:boolean,testeObject:struct<id:double,name:string,testeObjectInObject:struct<id:double,name:string>>>"

    assert test == resultAwaited


def test_json_schema_to_glue_struct_object_schema():
    local_path = pathlib.Path(__file__).parent.absolute()
    schema = open(r'{}/examples/schemas/teste_schema.json'.format(local_path),)
    schemaLoad = json.load(schema)

    test = GlueStructTransform.json_schema_to_glue_struct(schemaLoad, objectField = "testeObject", fullSchema = False)

    resultAwaited = "struct<id:int,name:string,testeObjectInObject:struct<id:double,name:string>>"

    assert test == resultAwaited


def test_working_with_arrays():
    local_path = pathlib.Path(__file__).parent.absolute()
    schema = open(r'{}/examples/schemas/teste_schema.json'.format(local_path),)
    schemaLoad = json.load(schema)['properties']

    test = working_with_arrays('testeArray', schemaLoad)[:-1]

    resultAwaited = "testeArray:array<struct<userId:int,id:double,title:string,completed:boolean,testeObject:struct<id:double,name:string,testeObjectInObject:struct<id:double,name:string>>>"

    assert test == resultAwaited


def test_working_with_objects():
    local_path = pathlib.Path(__file__).parent.absolute()
    schema = open(r'{}/examples/schemas/teste_schema.json'.format(local_path),)
    schemaLoad = json.load(schema)['properties']

    test = working_with_objects('testeObject', schemaLoad)[:-1]

    resultAwaited = "testeObject:struct<id:int,name:string,testeObjectInObject:struct<id:double,name:string>>"

    assert test == resultAwaited


def test_json_to_glue_struct_full_body():
    local_path = pathlib.Path(__file__).parent.absolute()
    payload = open(r'{}/examples/json/teste_json.json'.format(local_path),)
    payloadLoad = json.load(payload)

    test = GlueStructTransform.json_to_glue_struct(payloadLoad)

    resultAwaited = "userId:int,id:int,teste:double,title:string,completed:boolean,purchase:struct<id:int,amount:double,client:struct<firstName:string,lastName:string,address:string,age:int>,products:array<struct<id:int,name:string,price:int,quantity:int>>>,testeArray:array<struct<id:int,name:string,price:int,quantity:int>>"

    assert test == resultAwaited


def test_json_to_glue_struct_body():
    local_path = pathlib.Path(__file__).parent.absolute()
    payload = open(r'{}/examples/json/teste_json.json'.format(local_path),)
    payloadLoad = json.load(payload)

    test = GlueStructTransform.json_to_glue_struct(payloadLoad, objectField = 'purchase', fullBody = False)

    resultAwaited = "struct<id:int,amount:double,client:struct<firstName:string,lastName:string,address:string,age:int>,products:array<struct<id:int,name:string,price:int,quantity:int>>>"

    assert test == resultAwaited


def test_working_with_arrays_json_body():
    local_path = pathlib.Path(__file__).parent.absolute()
    payload = open(r'{}/examples/json/teste_json.json'.format(local_path),)
    payloadLoad = json.load(payload)

    key = 'testeArray'
    value = [{"id": 2,"name": "shirt","price": 20,"quantity": 1}]

    test = working_with_arrays_json_body(key, value, payloadLoad[key])[:-1]

    resultAwaited = "testeArray:array<struct<id:int,name:string,price:int,quantity:int>>"

    assert test == resultAwaited


def test_working_with_objects_json_body():
    local_path = pathlib.Path(__file__).parent.absolute()
    payload = open(r'{}/examples/json/teste_json.json'.format(local_path),)
    payloadLoad = json.load(payload)

    key = 'purchase'
    value = {"id": 2,"amount": 885.0,"client": {"firstName": "ABCDEFGHIJKLMNOPQ","lastName": "ABCDE","address": "ABCDEFGHIJKLMNOPQRSTU","age": 20
      },"products": [{"id": 2,"name": "shirt","price": 20,"quantity": 1}]}

    test = working_with_objects_json_body(key, value, payloadLoad[key])[:-1]

    resultAwaited = "purchase:struct<id:int,amount:double,client:struct<firstName:string,lastName:string,address:string,age:int>,products:array<struct<id:int,name:string,price:int,quantity:int>>>"

    assert test == resultAwaited