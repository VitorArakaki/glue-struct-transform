import os
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from utils import working_with_types

class GlueStructTransform:
    """
    Instantiate a multiplication operation.
    Numbers will be multiplied by the given multiplier.
    
    :param multiplier: The multiplier.
    :type multiplier: int
    """

    def __init__(self):
        pass


    def json_schema_to_glue_struct(jsonSchemaLoadProp:dict)->str:
        """
        This function performs a loop for each data inside the json schema to understand the data type and return a string in the glue structure format at the end.
        """
        tempStruct = ""
        for item in jsonSchemaLoadProp['properties']:
            result = working_with_types(item, jsonSchemaLoadProp['properties'])
            tempStruct += result
        finalGlueStruct =  tempStruct[:-1]
        # finalGlueStruct = f"struct<{tempStruct[:-1]}>"
        return finalGlueStruct