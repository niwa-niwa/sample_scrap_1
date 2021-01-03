from jsonschema import validate


# Validation with Json Schema
schema = {
    'type':'object',
    'properties':{
        'name':{
            'type':'string'
        },
        'price':{
            "type":"string",
            "pattern":"^[0-9,]+$"
        }
    },
    "required":["name", "price"]
}


validate({
    'name':'ぶどう',
    'price':'3,000',
}, schema)

validate({
    'name':'みかん',
    'price':'無料',
}, schema)


# the error message
"""
Traceback (most recent call last):
  File "validate_with_jsonschema.py", line 24, in <module>
    validate({
  File "/Users/niwayama.takeyuki/.virtualenvs/scraping/lib/python3.8/site-packages/jsonschema/validators.py", line 934, in validate
    raise error
jsonschema.exceptions.ValidationError: '無料' does not match '^[0-9,]+$'

Failed validating 'pattern' in schema['properties']['price']:
    {'pattern': '^[0-9,]+$', 'type': 'string'}

On instance['price']:
    '無料'
"""
