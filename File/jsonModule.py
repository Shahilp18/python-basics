
#! JSON Module
#* import json

import json

with open("/Applications/Career/Python/File/data.json", "r") as f:
    py_obj = json.load(f)
    print(py_obj)