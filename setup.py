# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
# with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
#     long_description = f.read()

long_description = """
##  Jsonschema to Glue struct

  

A small library that works to read your provided jsonschema and convert it to a glue struct model, in this way you can integrate it in your pipeline or uses it just to get a output and insert manually in your glue table schema.


[![PyPI](https://img.shields.io/pypi/v/glue-struct-transform)](https://pypi.org/project/glue-struct-transform/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/glue-struct-transform)](https://pypi.org/project/glue-struct-transform/)
[![PyPI License](https://img.shields.io/pypi/l/glue-struct-transform)](https://pypi.org/project/glue-struct-transform/)

###  Installation
    pip install glue-struct-transform

---
### Get Started
How to convert a full json schema to a glue struct schema using this lib
```Python
import json
from glue_struct_transform import GlueStructTransform

# Read or set your json schema
schema = open(f'YOUR_JSON_SCHEMA.json',)
schemaLoad = json.load(schema)

# Pass your json schema in dict type to the function
result = GlueStructTransform.json_schema_to_glue_struct(schemaLoad)
```

How to convert a object into the json schema to a glue struct schema using this lib
```Python
import json
from glue_struct_transform import GlueStructTransform

# Read or set your json schema
schema = open(f'YOUR_JSON_SCHEMA.json',)
schemaLoad = json.load(schema)

# Pass your json schema in dict type to the function
result = GlueStructTransform.json_schema_to_glue_struct(schemaLoad, objectField = "objectKey", fullSchema = False)
```

---

How to convert a full json to a glue struct schema using this lib
```Python
import json
from glue_struct_transform import GlueStructTransform

# Read or set your json schema
payload = open(f'YOUR_JSON_FILE.json',)
payloadLoad = json.load(payload)

# Pass your json schema in dict type to the function
result = GlueStructTransform.json_schema_to_glue_struct(payloadLoad)
```

How to convert a object into the json file to a glue struct schema using this lib
```Python
import json
from glue_struct_transform import GlueStructTransform

# Read or set your json schema
payload = open(f'YOUR_JSON_FILE.json',)
payloadLoad = json.load(payload)

# Pass your json schema in dict type to the function
result = GlueStructTransform.json_schema_to_glue_struct(payloadLoad, objectField = "objectKey", fullBody = False)
```


### Conversions implementation status
|From  |From Type	|Glue Schema type	| Implementation status	|Version
|-------------------------|-------------------------|---------------------|---------------|----------
|Json Schema |string	|string	|`implemented`	|`0.1.0`
|Json Schema |number	|double	|`implemented`	|`0.1.0`
|Json Schema |integer	|int	|`implemented`	|`0.1.0`
|Json Schema |object	|struct	|`implemented`	|`0.1.0`
|Json Schema |array	|array	|`implemented`	|`0.1.0`
|Json Schema |boolean	|boolean	|`implemented`	|`0.1.0`
|Json Schema |null	|Raises exception	|`implemented`	|`0.1.2`
|Json |str	|string	|`implemented`	|`0.3.0`
|Json |float    |double	|`implemented`	|`0.3.0`
|Json |int	|int	|`implemented`	|`0.3.0`
|Json |dict	|struct	|`implemented`	|`0.3.0`
|Json |list	|array	|`implemented`	|`0.3.0`
|Json |null	|Raises exception	|`implemented`	|`0.3.0`

"""

# This call to setup() does all the work
setup(
    name="glue-struct-transform",
    version="0.3.4",
    description="This libs works to convert a json schema or json to a glue schema struct.",
    long_description_content_type='text/markdown',
    long_description=long_description,
    url="https://github.com/VitorArakaki/glue-struct-transform",
    author="Vitor Guirardeli Arakaki",
    author_email="vi.arakaki@hotmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=["glue_struct_transform"],
    include_package_data=True
)