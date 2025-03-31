# Web Application implemented in Flask 

Flask used tue Model-View-Controller (MVC) architectural pattern 
to implement a web applikation.

## Model-View-Controller Pattern

The Model-View-Controller (MVC) pattern is a widely-used architectural 
design pattern for building software applications, particularly web 
applications. It organizes code into three interconnected components:

* **Model (M)**: Data and business logic.
    - Represents data and business logic.
    - Manages how data is structured, manipulated, stored, and validated.
    - Does not directly interact with the user interface or handle UI-specific logic.

    _Example_: A database or data classes that represent entities (e.g., User, Product).

* **View (V)**: User interface elements.
    - Presents data (user interface) to users.
    - Responsible solely for the presentation layer, rendering data 
        provided by the Controller.
    - Does not contain business logic; receives processed data from 
        Controllers.

    _Example_: HTML templates, web pages, or user interface screens.


* **Controller (C)**: Manages interactions between Model and View, 
    responding to user input.
    - Handles user requests and user interactions.
    - Acts as an intermediary between Model and View:
        - Receives input from users.
        - Invokes business logic on the Model.  
        - Passes the processed data to the View for presentation.

    _Example_: Flask routes handlers that process requests and return responses.


## Flask Implementation 

The following example demonstrates how to implement the MVC pattern in a Flask application:

* **Initialize the App**

```python
app = Flask(__name__)
```

- This creates an instance of the Flask app.
- This instance is needed to define routes and run the application.


* **Route for Homepage**

```python
@app.route('/')
def index():
    return render_template('index.html')
```

- Defines the root URL /.
- When a user visits this page, the app will render `index.html`.
- Typically, this page contains a form that asks the user to input 
    a word and select a language.

* **Route to Handle Translation**

```python
@app.route('/translator', methods=['POST'])
def translate():
    language = request.form.get('language')
    word = request.form.get('word')

    if language == "Deutsch":
        service = TranslatorServiceGerman()
    else:
        service = TranslatorServiceFrench()

    translation = service.translate(word)

    return render_template('translation.html', word=word, translation=translation)
```
- This route handles form submissions sent via `POST` method to `/translator`.

- `request.form.get(...)` retrieves user input from the form.
    - `language`: The selected language (`Deutsch` or anything else 
        assumed to be `French`).
    - word: The word the user wants translated.

- Based on the selected language, the appropriate translation service is instantiated.
- These services implement a method `.translate(word)` that returns the translated word.

- The app then renders `translation.html`, passing the original word 
    and its translation as template variables.
    The template will display the translation result to the user.


* **Run the Webb Application**

```python
if __name__ == '__main__':
    app.run(port=8080, debug=True)
```
- Starts the development server on port `8080`.
- `debug=True` enables hot reloading and detailed error messages for easier development.


* **HTML Templates**
The example uses a Jinja2 HTML template to display the translation result.

```html
<h2>
    Translate: {{ word }} into {{ translation }}
</h2>

- `{{ word }}` and `{{ translation }}` are Jinja2 placeholders.

- Flask passes values for these when rendering the template via `render_template(...)`.

```html
<a href="{{ url_for('index') }}">Back</a>
```

- This is a link that lets the user return to the home page.
- `{{ url_for('index') }}` generates the correct URL for the Flask route 
    named `'index'`.


The following table shows the mapping of MVC components to the Flask code:

| MVC Component | Flask Code |
|---------------|------------|
| **Model**     | `TranslatorServiceGerman`, `TranslatorServiceFrench` (external logic) |
| **View**      | `index.html`, `translation.html` (HTML templates) |
| **Controller**| Flask route functions: `index()`, `translate()` |


*Egon Teiniker, 2020-2025, GPL v3.0*