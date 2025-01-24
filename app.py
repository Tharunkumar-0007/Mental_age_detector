from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Questions and answers mapping to scores
questions = [
    {"id": 1, "question": "Do you enjoy trying new things?", "options": ["Always", "Often", "Sometimes", "Rarely", "Never"]},
    {"id": 2, "question": "Do you feel nostalgic often?", "options": ["Always", "Often", "Sometimes", "Rarely", "Never"]},
    {"id": 3, "question": "Do you prefer routines over surprises?", "options": ["Always", "Often", "Sometimes", "Rarely", "Never"]},
    {"id": 4, "question": "Are you curious about the latest trends?", "options": ["Always", "Often", "Sometimes", "Rarely", "Never"]},
    {"id": 5, "question": "Do you take risks often?", "options": ["Always", "Often", "Sometimes", "Rarely", "Never"]},
    {"id": 6, "question": "Do you find it hard to adapt to change?", "options": ["Always", "Often", "Sometimes", "Rarely", "Never"]},
    {"id": 7, "question": "Do you enjoy spending time with younger people?", "options": ["Always", "Often", "Sometimes", "Rarely", "Never"]},
    {"id": 8, "question": "Do you often daydream?", "options": ["Always", "Often", "Sometimes", "Rarely", "Never"]},
    {"id": 9, "question": "Do you prioritize fun over responsibilities?", "options": ["Always", "Often", "Sometimes", "Rarely", "Never"]},
    {"id": 10, "question": "Do you enjoy reflecting on your past decisions?", "options": ["Always", "Often", "Sometimes", "Rarely", "Never"]},
]

# New Score mapping
score_mapping = {
    "Always": 4,
    "Often": 3,
    "Sometimes": 2,
    "Rarely": 1,
    "Never": 0
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/questions', methods=['GET'])
def get_questions():
    return jsonify(questions)

@app.route('/submit', methods=['POST'])
def submit():
    answers = request.json.get('answers', [])
    total_score = sum([score_mapping.get(answer, 0) for answer in answers])
    
    # New formula to calculate mental age
    mental_age = round(0 + (total_score * 1.1))  # Adjust scaling factor as needed
    
    # Refined categories
    if mental_age <= 20:
        category = "A child's mind"
    elif 21 <= mental_age <= 30:
        category = "Young at Heart"
    elif 31 <= mental_age <= 45:
        category = "Mature Thinker"
    else:
        category = "Wise Soul"
    
    return jsonify({"mental_age": mental_age, "category": category})

if __name__ == '__main__':
    app.run(debug=True)
