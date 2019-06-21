from flask import Blueprint, request
import json
from ..sample_models.addition_model import Model

bp = Blueprint('addition', __name__, url_prefix='/addition')
model = Model()

@bp.route('/', methods=('GET',))
def home():
    return """
Addition Model

Call options:
    using GET method with parameters a, b
        URL: ".../evaluate/?a=10&b=20"
    
    using POST method with parameters passed in json:
        URL: ".../evaluate_json/"
        JSON: ```
            {
            	"a": 10,
            	"b": 22
            }
        ```
"""


@bp.route('/evaluate/', methods=('GET',))
def evaluate():
    print()
    a = request.args.get("a")
    b = request.args.get("b")
    a, b = float(a), float(b)
    
    result = float(model(a, b))
    return json.dumps({"a":a, "b":b, "sum": result})

@bp.route('/evaluate_json/', methods=('POST',))
def evaluate_json():
    in_json = request.get_json()
    if in_json is None:
        return "Error: JSON required."
    in_dic = in_json#json.loads(in_json)
    a = float(in_dic["a"])
    b = float(in_dic["b"])
    
    result = float(model(a, b))
    return json.dumps({"a":a, "b":b, "sum": result})
    
    
    
    
    

    