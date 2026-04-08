# Elena's Tech Journey Blog

A Django-based personal website featuring a blog with rich media support and a professional CV/resume section.

## 🌟 Features

- **Blog System**: Create and publish blog posts with text content
- **Rich Media Support**: Upload and display videos and images in blog posts
- **CV/Resume Section**: Professional portfolio with experience, skills, and education
- **Responsive Design**: Mobile-friendly layout using Bootstrap
- **Internationalization**: Multi-language support (English/Dutch)
- **Admin Panel**: Django admin interface for content management
- **Media Management**: Organized file uploads for videos and images

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/alenka134/my-first-blog.git
   cd my-first-blog
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin account)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

7. **Open your browser**

   - [Blog](http://127.0.0.1:8000/)
   - [Admin panel](http://127.0.0.1:8000/admin/)
   - [CV](http://127.0.0.1:8000/cv/)

## 📁 Project Structure

```text
my-first-blog/
├── blog/                    # Blog app
│   ├── migrations/         # Database migrations
│   ├── static/            # Static files (CSS, images)
│   ├── templates/         # HTML templates
│   └── models.py          # Blog post model
├── cv/                     # CV/Resume app
│   ├── static/            # CV-specific static files
│   └── templates/         # CV templates
├── media/                  # User-uploaded files
│   ├── videos/           # Uploaded videos
│   └── images/           # Uploaded images
├── mysite/                # Django project settings
├── staticfiles/           # Collected static files (production)
└── requirements.txt       # Python dependencies
```

## 🎨 Features in Detail

### Blog Posts

- Create rich blog posts with text content
- Upload videos that play inline
- Add screenshots/images alongside videos
- Responsive design that works on all devices

### CV Section

- Professional resume layout
- Skills, experience, and education sections
- Contact information and social links
- PDF download option

### Media Management

- Videos are stored in `media/videos/`
- Images are stored in `media/images/`
- Automatic thumbnail generation for images
- Responsive video players

## 🛠️ Technologies Used

- **Backend**: Django 4.x
- **Database**: SQLite (development), PostgreSQL (production)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Media Processing**: Pillow (for image handling)
- **Internationalization**: Django's i18n framework
- **Deployment**: PythonAnywhere ready

## 📝 Usage

### Adding Blog Posts

1. Log into the admin panel (`/admin/`)
2. Navigate to "Blog > Posts"
3. Click "Add Post"
4. Fill in title and text
5. Optionally upload video and/or image files
6. Set publish date to make it live

### Managing CV Content

The CV content is currently static but can be made dynamic by:

- Adding models for experience, skills, etc.
- Creating admin interfaces for content management
- Implementing dynamic sections

## 🌐 Deployment

### PythonAnywhere

1. Create a PythonAnywhere account
2. Upload your code
3. Set up a virtual environment
4. Configure static/media files
5. Set up the database
6. Configure the web app

### Environment Variables

Create a `.env` file for sensitive settings:

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
DATABASE_URL=your-database-url
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

Elena Ovcharenko

- LinkedIn: [Elena Ovcharenko](https://www.linkedin.com/in/elena-ovcharenko-0650b615/)
- GitHub: [@alenka134](https://github.com/alenka134)
- Website: [elenao.pythonanywhere.com](https://elenao.pythonanywhere.com/)

## 🙏 Acknowledgments

- Django Girls tutorial for the foundation
- Bootstrap for the responsive design
- PythonAnywhere for hosting
- All the amazing open-source contributors

---

⭐ If you find this project helpful, please give it a star!
