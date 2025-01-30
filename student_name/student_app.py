from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    first_class = []
    second_class = []

    if request.method == 'POST':
        num_class = int(request.form['num_class'])

        for j in range(num_class):
            n = int(request.form[f'num_students_{j}'])
            for i in range(n):
                name = request.form[f'student_{j}_{i}']
                if j == 0:
                    first_class.append(name)
                elif j == 1:
                    second_class.append(name)

        # first_class_copy = first_class.copy()
        # first_class.extend(second_class)

        return render_template('index.html', first_class=first_class, second_class=second_class,
                               combined_class=first_class + second_class)

    return render_template('index.html', first_class=first_class, second_class=second_class, combined_class=[])


if __name__ == '__main__':
    app.run(debug=True)