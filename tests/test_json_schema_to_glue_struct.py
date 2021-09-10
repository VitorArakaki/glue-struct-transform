import os
import sys
import json
import pathlib
from glue_struct_transform import GlueStructTransform, working_with_arrays, working_with_objects

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))


def test_json_schema_to_glue_struct_full_schema():
    local_path = pathlib.Path(__file__).parent.absolute()
    schema = open(r'{}/schemas/teste_schema.json'.format(local_path),)
    schemaLoad = json.load(schema)

    test = GlueStructTransform.json_schema_to_glue_struct(schemaLoad, fullSchema = True)

    resultAwaited = "userId:int,id:double,title:string,completed:boolean,testeObject:struct<id:int,name:string,testeObjectInObject:struct<id:double,name:string>>,testeArray:array<struct<userId:int,id:double,title:string,completed:boolean,testeObject:struct<id:double,name:string,testeObjectInObject:struct<id:double,name:string>>>"

    assert test == resultAwaited


def test_json_schema_to_glue_struct_object_schema():
    local_path = pathlib.Path(__file__).parent.absolute()
    schema = open(r'{}/schemas/teste_schema.json'.format(local_path),)
    schemaLoad = json.load(schema)

    test = GlueStructTransform.json_schema_to_glue_struct(schemaLoad, objectField = "testeObject", fullSchema = False)

    resultAwaited = "struct<id:int,name:string,testeObjectInObject:struct<id:double,name:string>>"

    assert test == resultAwaited


def test_working_with_arrays():
    local_path = pathlib.Path(__file__).parent.absolute()
    schema = open(r'{}/schemas/teste_schema.json'.format(local_path),)
    schemaLoad = json.load(schema)['properties']

    test = working_with_arrays('testeArray', schemaLoad)[:-1]

    resultAwaited = "testeArray:array<struct<userId:int,id:double,title:string,completed:boolean,testeObject:struct<id:double,name:string,testeObjectInObject:struct<id:double,name:string>>>"

    assert test == resultAwaited


def test_working_with_objects():
    local_path = pathlib.Path(__file__).parent.absolute()
    schema = open(r'{}/schemas/teste_schema.json'.format(local_path),)
    schemaLoad = json.load(schema)['properties']

    test = working_with_objects('testeObject', schemaLoad)[:-1]

    resultAwaited = "testeObject:struct<id:int,name:string,testeObjectInObject:struct<id:double,name:string>>"

    assert test == resultAwaited