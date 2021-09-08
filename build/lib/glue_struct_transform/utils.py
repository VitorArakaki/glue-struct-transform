def working_with_objects(item:str, jsonSchemaLoadProp:dict, isArray:bool = False)->str:
    """
    This function works to provide a return in the glue structure format when the data type is specified as an object, further allowing the inclusion of objects in the object and arrays within it.
    """
    if isArray == True:
        jsonSchemaObjectProp = jsonSchemaLoadProp[f'{item}']['items']
        returnStruct = f"struct<"
    else:
        jsonSchemaObjectProp = jsonSchemaLoadProp[f'{item}']
        returnStruct = f"{item}:struct<"

    for values in jsonSchemaObjectProp['properties']:
        objectStruct = ""
        if 'number' in jsonSchemaObjectProp['properties'][values]['type']:
            objectStruct = f"{values}:double,"
        elif 'string' in jsonSchemaObjectProp['properties'][values]['type']:
            objectStruct = f"{values}:string,"
        elif 'integer' in jsonSchemaObjectProp['properties'][values]['type']:
            objectStruct = f"{values}:int,"
        elif 'boolean' in jsonSchemaObjectProp['properties'][values]['type']:
            objectStruct = f"{values}:boolean,"
        elif 'null' == jsonSchemaLoadProp[f'{item}']['type']:
            raise Exception("Null is not acceptable as a schema type on glue schema.")
        elif 'object' in jsonSchemaObjectProp['type']:
            objectStruct = working_with_objects(values, jsonSchemaObjectProp['properties'])
        elif 'array' in jsonSchemaObjectProp['type']:
            objectStruct = working_with_arrays(item, jsonSchemaLoadProp)
        else:
            pass
        
        returnStruct += objectStruct
    returnStruct = returnStruct[:-1] + ">,"

    return returnStruct


def working_with_arrays(item:str, jsonSchemaLoadProp:dict)->str:
    """
    This function works to provide a return in the glue structure format when the data type is specified as array, further allowing the inclusion of objects in the array and other arrays within it.
    """
    returnArrayStruct = f"{item}:array<"
    jsonSchemaArray = jsonSchemaLoadProp[f'{item}']['items']
    if 'number' in jsonSchemaArray['type']:
        arrayStruct = f"double,"
    elif 'string' in jsonSchemaArray['type']:
        arrayStruct = f"string,"
    elif 'integer' in jsonSchemaLoadProp[f'{item}']['type']:
        arrayStruct = f"int,"
    elif 'boolean' in jsonSchemaArray['type']:
        arrayStruct = f"boolean,"
    elif 'null' == jsonSchemaLoadProp[f'{item}']['type']:
        raise Exception("Null is not acceptable as a schema type on glue schema.")
    elif 'object' in jsonSchemaArray['type']:
        arrayStruct = working_with_objects(item, jsonSchemaLoadProp, True)
    elif 'array' in jsonSchemaArray['type']:
        arrayStruct = working_with_arrays(item, jsonSchemaLoadProp)
    else:
        pass

    returnArrayStruct += arrayStruct
    return returnArrayStruct


def working_with_types(item:str, jsonSchemaLoadProp:dict)->str:
    """
    This function performs the basic handling for simple data types like number, string, integer... And for more complex types like array and object it asks for the help of another function.
    """
    returnStruct = ""
    if 'number' in jsonSchemaLoadProp[f'{item}']['type']:
        returnStruct = f"{item}:double,"
    elif 'string' in jsonSchemaLoadProp[f'{item}']['type']:
        returnStruct = f"{item}:string,"
    elif 'integer' in jsonSchemaLoadProp[f'{item}']['type']:
        returnStruct = f"{item}:int,"
    elif 'boolean' in jsonSchemaLoadProp[f'{item}']['type']:
        returnStruct = f"{item}:boolean,"
    elif 'null' == jsonSchemaLoadProp[f'{item}']['type']:
        raise Exception("Null is not acceptable as a schema type on glue schema.")
    elif 'object' in jsonSchemaLoadProp[f'{item}']['type']:
        returnStruct = working_with_objects(item, jsonSchemaLoadProp)
    elif 'array' in jsonSchemaLoadProp[f'{item}']['type']:
        returnStruct = working_with_arrays(item, jsonSchemaLoadProp)
    else:
        pass

    return returnStruct
