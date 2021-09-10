import os
import sys
import json
import pathlib
from glue_struct_transform import GlueStructTransform

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
