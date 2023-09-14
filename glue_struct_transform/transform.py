from .utils import working_with_types, working_with_types_json_body, struct_validator


class GlueStructTransform:
    """
    Instantiate a GlueStructTransform operation.
    
    This is the glue transform class, you can call the function that converts:
    - Json Schema > Glue Struct
    """

    def __init__(self):
        pass

    def json_schema_to_glue_struct(self: dict, **kwargs) -> str:
        """
        This function performs a loop for each data inside the json schema to understand the data type
        and return a string in the glue structure format at the end.
        """

        objectField = kwargs.get('objectField', None)
        fullSchema = kwargs.get('fullSchema', True)

        if not fullSchema:
            loopJsonSchemaLoadProp = self['properties'][f'{objectField}']['properties']
        else:
            loopJsonSchemaLoadProp = self['properties']

        tempStruct = ""
        for item in loopJsonSchemaLoadProp:
            result = working_with_types(item, loopJsonSchemaLoadProp)
            tempStruct += result

        finalGlueStruct = f"struct<{tempStruct[:-1]}>" if not fullSchema else tempStruct[:-1]

        glue_schema_string_validation = struct_validator(finalGlueStruct)

        if glue_schema_string_validation is True:
            return finalGlueStruct

    def json_to_glue_struct(self: dict, **kwargs) -> str:
        """
        This function performs a loop for each data inside the json to understand the data type
        and return a string in the glue structure format at the end.
        """

        objectField = kwargs.get('objectField', None)
        fullBody = kwargs.get('fullBody', True)
        loopJsonBodyLoadProp = self if fullBody else self[f'{objectField}']
        tempStruct = ""

        for key, value in loopJsonBodyLoadProp.items():
            result = working_with_types_json_body(key, value, loopJsonBodyLoadProp)
            tempStruct += result

        finalGlueStruct = tempStruct[:-1] if fullBody else f"struct<{tempStruct[:-1]}>"

        glue_schema_string_validation = struct_validator(finalGlueStruct)

        if glue_schema_string_validation:
            return finalGlueStruct
