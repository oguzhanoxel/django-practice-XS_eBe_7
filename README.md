# Django Practice Project

This repository contains practice projects for learning Django, including:

* `firstproject`: A basic Django project setup.
* `littlelemon`: A Django application simulating a restaurant website.

## 📺 Reference

I built this project by following Django tutorial:

[![Django Tutorial](https://img.youtube.com/vi/0roB7wZMLqI/0.jpg)](https://www.youtube.com/watch?v=0roB7wZMLqI)

## Getting Started

### Prerequisites

* Python 3.x
* Pipenv (for managing virtual environments)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/oguzhanoxel/django-practice-XS_eBe_7.git
   cd django-practice-XS_eBe_7
   ```

2. Install dependencies:

   ```bash
   pipenv install
   ```

3. Activate the virtual environment:

   ```bash
   pipenv shell
   ```

4. Navigate to the desired project directory and run migrations:

   ```bash
   cd firstproject  # or cd littlelemon
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

## License

This project is licensed under the MIT License.