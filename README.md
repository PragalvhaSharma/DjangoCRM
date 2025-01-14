
# DjangoCRM

DjangoCRM is a Customer Relationship Management (CRM) system built with Django. It is designed to help businesses manage customer relationships and streamline operations effectively.

## Features

- **Customer Management**: Add, update, and delete customer details easily.
- **Customizable**: Built with Django, making it easy to extend functionality.
- **Web-based Interface**: User-friendly interface for seamless interaction.

## Project Structure

```
DjangoCRM/
├── dcrm/             # Core CRM functionality
├── website/          # Frontend and templates
├── .gitignore        # Ignored files and folders
├── manage.py         # Django management script
```

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/PragalvhaSharma/DjangoCRM.git
   ```

2. Navigate to the project directory:

   ```bash
   cd DjangoCRM
   ```

3. Set up a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # For Linux/macOS
   venv\Scripts\activate      # For Windows
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open your browser and go to `http://127.0.0.1:8000` to access the app.

## Contribution

Feel free to fork this repository and create pull requests with your improvements. Contributions are always welcome!

## License

This project is licensed under the [MIT License](LICENSE).

---
