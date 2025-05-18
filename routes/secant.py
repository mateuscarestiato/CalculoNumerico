from flask import Blueprint, render_template, request, jsonify
from functions.secant import secant

secant_bp = Blueprint('secant', __name__, template_folder='../static/html')

@secant_bp.route('/', methods=['GET'])
def show_secant_form():
    return render_template('secant.html')

@secant_bp.route('/', methods=['POST'])
def compute_secant():
    data = request.form
    equation = data.get('equation', '')
    x0 = float(data.get('x0', 0))
    x1 = float(data.get('x1', 0))
    tol = float(data.get('tol', 1e-6))
    max_iter = int(data.get('max_iter', 100))
    try:
        root, iterations, error = secant(equation, x0, x1, tol, max_iter)
        return jsonify({'root': root, 'iterations': iterations, 'error': error})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
