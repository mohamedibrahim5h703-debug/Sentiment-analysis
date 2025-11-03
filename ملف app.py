from flask import Flask, request, render_template, jsonify
from sentiment_analyzer import analyze_sentiment

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form.get('text', '')
    if not text.strip():
        return jsonify({"error": "يرجى إدخال نص للتحليل"}), 400

    result = analyze_sentiment(text)
    return jsonify(result)

# نقطة البداية
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
