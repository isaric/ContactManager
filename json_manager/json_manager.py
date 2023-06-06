# define json helper functions here
# can import other functions (ex. file manager)
import json

def load_json_from_file(path):
    file = open(path,"r")
    return json.load(file)

def write_json_to_file(path, object):
    obj_d = _make_object_json_serializable_(object)
    write_json_str_to_file(path,json.dumps(obj_d))

def write_json_str_to_file(path, json_str):
    file = open(path,"w")
    file.write(json_str)

def _make_object_json_serializable_(object):
    if not _is_json_serializable_(object):
        try: 
            d = object.__dict__
        except Exception:
            d = str(object)
        if isinstance(d, dict):
            for key,value in d.items():
                if not _is_json_serializable_(value):
                    d[key] = _make_object_json_serializable_(value)
        return d
    return object

def _is_json_serializable_(object):
    try:
        json.dumps(object)
        return True
    except (TypeError, OverflowError):
        return False
