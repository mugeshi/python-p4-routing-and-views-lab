# Import the Flask library
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def index():
    # Return HTML response with an h1 tag
    return '<h1>Welcome to our Application</h1>'

# Define the route for the print_string view with a dynamic parameter
@app.route('/print/<string:parameter>')
def print_string(parameter):
    # Print the parameter to the console
    print(parameter)
    
    # Return HTML response with the parameter displayed
    return f'<h1>{parameter}</h1>'

# Define the route for the count view with an integer parameter
@app.route('/count/<int:num>')
def count(num):
    # Generate a list of numbers from 1 to num
    numbers = list(range(1, num + 1))
    
    # Convert the list of numbers to a string with each number on a separate line
    numbers_str = '\n'.join(map(str, numbers))
    
    # Return HTML response with numbers displayed in a <pre> element
    return f'<pre>{numbers_str}</pre>'

# Define the route for the math view with float parameters and an operation
@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    result = None

    # Perform the appropriate mathematical operation based on the operation parameter
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            # Return an error message if attempting to divide by zero
            return "Cannot divide by zero!"
    elif operation == '%':
        result = num1 % num2
    else:
        # Return an error message for invalid operations
        return "Invalid operation"
    
    # Return HTML response with the result of the operation
    return f'Result: {result}'

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(port=5555, debug=True)
