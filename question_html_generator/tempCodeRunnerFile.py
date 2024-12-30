@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    book_name = request.form['book_name']
    session_name = request.form['session_name']
    topic_title = request.form['topic_title']
    total_questions= request.form['total_questions']
    question_number = request.form['question_number']
    question_stem = request.form['question_stem']
    options = [request.form[f'option_{i}'] for i in range(1, 5)]
    correct_answer = int(request.form['correct_answer']) - 1  # Zero-based index for options
    
    generated_file = generate_html(session_name, topic_title, total_questions, question_number, question_stem, options, correct_answer)
    
    return send_file(generated_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
