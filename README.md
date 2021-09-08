##  Jsonschema to Glue struct

  

A small library that works to read your provided jsonschema and convert it to a glue struct model, in this way you can integrate it in your pipeline or uses it just to get a output and insert manually in your glue table schema.

  

###  Installation
```
pip install glue-struct-transform
```

### Get Started
How to convert a jsonchema to a glue struct schema using this lib
```Python
import json
from glue_struct_transform import GlueStructTransform

# Read or set your json schema
schema = open(f'YOUR_JSON_SCHEMA.json',)
schemaLoad = json.load(schema)

# Pass your json schema in dict type to the function
result = GlueStructTransform.json_schema_to_glue_struct(schemaLoad)
```

### Conversions implementation status
|Json Schema Type	|Glue Schema type	| Implementation status	|Version
|-------------------------|---------------------|---------------|----------
|string	|string	|`implemented`	|`0.1.0`
|number	|double	|`implemented`	|`0.1.0`
|integer	|int	|`implemented`	|`0.1.0`
|object	|struct	|`implemented`	|`0.1.0`
|array	|array	|`implemented`	|`0.1.0`