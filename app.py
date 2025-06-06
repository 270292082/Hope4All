from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        print("FILES:", request.files)
        if 'image' not in request.files:
            return "No file part in request.files", 400

        file = request.files['image']
        if file.filename == '':
            return "No file selected", 400

        return f"Received file: {file.filename}"
    
    return render_template_string('''
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="image" />
            <input type="submit" value="Upload" />
        </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
