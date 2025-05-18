from flask import Blueprint, render_template

index_bp = Blueprint('index', __name__, template_folder='../static/html')

@index_bp.route('/')
def index():
    return render_template('index.html')


# routes/false_position.py
from flask import Blueprint, render_template, request, jsonify
from functions.false_position import false_position

false_position_bp = Blueprint('false_position', __name__, template_folder='../static/html')

@false_position_bp.route('/', methods=['GET'])
def show_false_position_form():
    return render_template('false_position.html')

@false_position_bp.route('/', methods=['POST'])
def compute_false_position():
    data = request.form
    equation = data.get('equation', '')
    x_lower = float(data.get('x_lower', 0))
    x_upper = float(data.get('x_upper', 0))
    tol = float(data.get('tol', 1e-6))
    max_iter = int(data.get('max_iter', 100))
    try:
        root, iterations, error = false_position(equation, x_lower, x_upper, tol, max_iter)
        return jsonify({'root': root, 'iterations': iterations, 'error': error})
    except Exception as e:
        return jsonify({'error': str(e)}), 400