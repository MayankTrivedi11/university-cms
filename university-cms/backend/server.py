from flask import Flask
from flask_cors import CORS
from routes import course_routes, student_routes, auth_routes
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, resources={r"/*": {"origins": "*"}})  # Enable CORS for all routes

# Register routes
app.register_blueprint(course_routes.course_bp)
app.register_blueprint(student_routes.student_bp)
app.register_blueprint(auth_routes.auth_bp)

if __name__ == '__main__':
    app.run(debug=True)
    