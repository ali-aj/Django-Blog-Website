# Django Blog Website

Welcome to the Django Blog Website repository! This project is a fully functional blog website developed using the Django framework. It allows users to create, read, and delete blog posts. Whether you're looking to showcase your writing skills or create a platform for sharing your thoughts, this project provides a solid foundation to get you started.

## Features

- User Authentication: Users can register, log in, and manage their own blog posts.
- Forget Password System (OTP): Forgot your password? No worries! OTP system guarantees a seamless and secure password recovery process.
- Blog Post Management: Create, delete, and publish blog posts with a user-friendly interface.
- Responsive Design: The website is designed to work seamlessly across various devices and screen sizes.
- User Profiles: Each user has a profile page showcasing their published blog posts.
- Admin Panel: Admins can manage users, and posts through the Django admin panel.
- Stay Connected: The "Contact Us" system ensures you're just a click away from reaching out, providing a direct line of communication.

## Installation

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/ali-aj/Django-Blog-Website.git
   ```

2. Create a virtual environment and activate it:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Set up the database:

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser account to access the admin panel:

   ```
   python manage.py createsuperuser
   ```

6. Install Required dependencies:

   ```
   pip install -r requirements.txt
   ```

6. Start the development server:

   ```
   python manage.py runserver
   ```

7. Access the website in your browser at `http://127.0.0.1:8000/` and the admin panel at `http://127.0.0.1:8000/admin/`.

## Usage

- Visit the home page to view the list of published blog posts.
- Register or log in to manage your own blog posts.
- Admins can log in to the admin panel to manage various aspects of the website.
- Visit the My Blogs page to view your blogs or delete your blogs.

## Contributing

Contributions are welcome and encouraged! If you have any improvements or bug fixes to propose, please follow these steps:

1. Fork the repository and create a new branch.
2. Make your changes and test them thoroughly.
3. Create a pull request with a clear description of your changes.

## Credits

This project was developed by Muhammad Ali Mustafa and is inspired by the Django web framework. Feel free to modify, distribute, and use this project as you see fit.

Thank you for checking out the Django Blog Website project! If you have any questions, issues, or suggestions, please don't hesitate to get in touch. 
