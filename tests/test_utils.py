import json
import os
import pathlib
import sys

import pytest
from glue_struct_transform import (
    struct_validator,
    working_with_arrays,
    working_with_arrays_json_body,
    working_with_objects,
    working_with_objects_json_body,
)

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))


def test_working_with_arrays_json_body():
    local_path = pathlib.Path(__file__).parent.absolute()
    payload = open(
        rf"{local_path}/examples/json/teste_json.json",
    )
    payloadLoad = json.load(payload)

    key = "testeArray"
    value = [{"id": 2, "name": "shirt", "price": 20, "quantity": 1}]

    test = working_with_arrays_json_body(key, value, payloadLoad[key])[:-1]

    resultAwaited = "testeArray:array<struct<id:int,name:string,price:int,quantity:int>>"

    assert test == resultAwaited


def test_working_with_objects_json_body():
    local_path = pathlib.Path(__file__).parent.absolute()
    payload = open(
        rf"{local_path}/examples/json/teste_json.json",
    )
    payloadLoad = json.load(payload)

    key = "purchase"
    value = {
        "id": 2,
        "amount": 885.0,
        "client": {
            "firstName": "ABCDEFGHIJKLMNOPQ",
            "lastName": "ABCDE",
            "address": "ABCDEFGHIJKLMNOPQRSTU",
            "age": 20,
        },
        "products": [{"id": 2, "name": "shirt", "price": 20, "quantity": 1}],
    }

    test = working_with_objects_json_body(key, value, payloadLoad[key])[:-1]

    resultAwaited = (
        "purchase:struct<id:int,amount:double,client:struct<firstName:string,lastName:string,"
        "address:string,age:int>,products:array<struct<id:int,name:string,price:int,quantity:int>>>"
    )

    assert test == resultAwaited


def test_working_with_arrays():
    local_path = pathlib.Path(__file__).parent.absolute()
    schema = open(
        rf"{local_path}/examples/schemas/teste_schema.json",
    )
    schemaLoad = json.load(schema)["properties"]

    test = working_with_arrays("testeArray", schemaLoad)[:-1]

    resultAwaited = (
        "testeArray:array<struct<userId:int,id:double,title:string,completed:boolean,"
        "testeObject:struct<id:double,name:string,testeObjectInObject:struct<id:double,name:string>>>>"
    )

    assert test == resultAwaited


def test_working_with_objects():
    local_path = pathlib.Path(__file__).parent.absolute()
    schema = open(
        rf"{local_path}/examples/schemas/teste_schema.json",
    )
    schemaLoad = json.load(schema)["properties"]

    test = working_with_objects("testeObject", schemaLoad)[:-1]

    resultAwaited = "testeObject:struct<id:int,name:string,testeObjectInObject:struct<id:double,name:string>>"

    assert test == resultAwaited


def test_struct_validator_strict_inequality_count():
    glue_string = (
        "testeArray:array<struct<userId:int,id:double,title:string,completed:boolean,"
        "testeObject:struct<id:double,name:string,testeObjectInObject:struct<id:double,name:string>>>"
    )

    with pytest.raises(Exception, match="The count of strict inequality is not Even."):
        struct_validator(glue_string)


def test_struct_validator_strict_inequality_empty():
    glue_string = (
        "testeArray:array<struct<userId:int,id:double,title:string,completed:boolean,testeObject:struct<id:double,"
        "name:string,testeObjectInObject:struct<>>>>"
    )

    with pytest.raises(Exception, match="The strict inequality is empty or malformed."):
        struct_validator(glue_string)


def test_struct_validator_success():
    glue_string = (
        "userId:int,id:int,teste:double,title:string,completed:boolean,purchase:struct<id:int,amount:double,"
        "client:struct<firstName:string,lastName:string,address:string,age:int>,products:array<struct<id:int,"
        "name:string,price:int,quantity:int>>>,testeArray:array<struct<id:int,name:string,price:int,quantity:int>>"
    )

    validation = struct_validator(glue_string)

    resultAwaited = True

    assert validation is resultAwaited
