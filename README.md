# Truth or Dare Game - Flask Web Application

This is a simple web application built using Flask that lets users play a game of Truth or Dare. It fetches random truths and dares either from a predefined list or external APIs. The game features an interactive user interface where users can spin a bottle and get a random Truth or Dare.

## Features
- **Truth or Dare Game**: Players can spin a bottle to randomly get either a Truth or Dare.
- **Predefined List of Truths and Dares**: The app includes a list of funny and embarrassing truths and dares.
- **Interactive UI**: Includes a spinning bottle animation and a stylish, responsive layout.
- **External API Integration**: Fetches random jokes and questions from external APIs when needed.

## Requirements

- Python 3.6+
- Flask
- requests

## Installation

1. Clone the repository or download the files.
   
2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

   - On Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To start the Flask web application, run the following command:

```bash
python app.py
```

This will start the server on `http://127.0.0.1:5000` (or a different port if specified in the `PORT` environment variable).

## How it Works

- **Home Page**: The homepage displays a bottle that can be spun. Once the bottle stops spinning, a random truth or dare is displayed.
- **Truths and Dares**: You can get either a funny truth question or a dare, fetched from a predefined list.
- **API Endpoints**:
   - `/truth`: Returns a random truth question.
   - `/dare`: Returns a random dare.
   
## API Integration

- **Truth API**: Uses the [Open Trivia Database API](https://opentdb.com/api_config.php) to fetch trivia questions (Category 9: General Knowledge).
- **Dare API**: Uses the [Chuck Norris Jokes API](https://api.chucknorris.io/) to fetch random jokes that can be used as dares.

## Example Output

1. When you spin the bottle, a random truth or dare is shown like:

   **Truth**: "What is your biggest fear?"
   
   **Dare**: "Try to lick your elbow."

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

- **Flask**: A lightweight WSGI web application framework in Python.
- **requests**: A simple HTTP library for Python.
- **Unsplash**: For the background image used in the web interface.
```

### Instructions:
- Replace the placeholders (like the `LICENSE` file) with actual files if needed.
- You can also add any additional details about customization, configuration, or usage, as required.
