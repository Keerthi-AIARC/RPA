from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate')
def calculate():
    try:
        # Get numbers and operation from query parameters
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        operation = request.args.get('operation')  # add, sub, mul, div

        # Perform operation
        if operation == 'add':
            result = num1 + num2
        elif operation == 'sub':
            result = num1 - num2
        elif operation == 'mul':
            result = num1 * num2
        elif operation == 'div':
            if num2 == 0:
                return jsonify({"error": "Cannot divide by zero"}), 400
            result = num1 / num2
        else:
            return jsonify({"error": "Invalid operation"}), 400

        return jsonify({
            "num1": num1,
            "num2": num2,
            "operation": operation,
            "result": result
        })

    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Use query params num1, num2, and operation"}), 400

if __name__ == '__main__':
    app.run(debug=True)
