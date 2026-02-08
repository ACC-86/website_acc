from flask import Flask, render_template, request, redirect, url_for, flash, session, g
from flask_babel import Babel, _
from flask_babel import get_locale

app = Flask(__name__)
babel = Babel(app)
# Language toggle route (must be after app is defined)
@app.route('/set_language', methods=['POST'])
def set_language():
    lang = request.form.get('lang')
    if lang in app.config['BABEL_SUPPORTED_LOCALES']:
        session['lang'] = lang
    return redirect(request.referrer or url_for('home'))
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()
app.secret_key = os.environ.get('SECRET_KEY')

# --- Flask-Babel Setup ---
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'hi']
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

# Inject _ function into Jinja templates
@app.context_processor
def inject_translator():
    return {'_': _, 'get_locale': get_locale}



from db import get_courses, get_testimonials, save_inquiry, save_admission, save_homework, get_homework_for_today
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Placeholder for authentication logic
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # TODO: Authenticate user
        flash('Login functionality coming soon!', 'info')
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/study-material')
def study_material():
    return render_template('study_material.html')

@app.route('/announcements')
def announcements():
    return render_template('announcements.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/faculty')
def faculty():
    return render_template('faculty.html')

@app.route('/fee')
def fee():
    return render_template('fee.html')

@app.route('/achievements')
def achievements():
    return render_template('achievements.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/faqs')
def faqs():
    return render_template('faqs.html')

@app.route('/live-chat')
def live_chat():
    return render_template('live_chat.html')

@app.route('/mobile-app')
def mobile_app():
    return render_template('mobile_app.html')



@app.context_processor
def inject_year():
    from datetime import datetime
    return {'year': datetime.now().year}

@app.route('/')
def home():
    courses = get_courses(limit=6)
    testimonials = get_testimonials(limit=4)
    homework = get_homework_for_today()
    from db import get_schedule
    schedule = get_schedule()
    return render_template('home.html', courses=courses, testimonials=testimonials, homework=homework, schedule=schedule)

@app.route('/courses')
def courses():
    courses = get_courses()
    return render_template('courses.html', courses=courses)

@app.route('/course/<course_id>')
def course_detail(course_id):
    course = get_courses(course_id=course_id)
    return render_template('course_detail.html', course=course)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/results')
def results():
    testimonials = get_testimonials()
    return render_template('results.html', testimonials=testimonials)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        message = request.form['message']
        save_inquiry(name, phone, message)
        flash('Thank you for your inquiry! We will contact you soon.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/admission', methods=['GET', 'POST'])
def admission():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        class_name = request.form.get('class')
        board = request.form.get('board')
        medium = request.form.get('medium')
        course = request.form.get('course')
        save_admission(name, email, class_name, board, medium, course)
        flash('Your admission form has been submitted successfully!', 'success')
        return redirect(url_for('admission'))
    return render_template('admission.html')

@app.route('/admin/homework', methods=['GET', 'POST'])
def admin_homework():
    homework = get_homework_for_today()
    if request.method == 'POST':
        hw = {}
        for cls in [5,6,7,8]:
            hw[cls] = request.form.get(f'homework_{cls}', '')
        save_homework(hw)
        flash('Homework updated successfully!', 'success')
        homework = hw
    return render_template('admin/homework.html', homework=homework)

# Student Area (UI only)
@app.route('/student/dashboard')
def student_dashboard():
    return render_template('student/dashboard.html')

@app.route('/student/my-courses')
def student_my_courses():
    return render_template('student/my_courses.html')

@app.route('/student/progress')
def student_progress():
    return render_template('student/progress.html')

@app.route('/student/video-lessons')
def student_video_lessons():
    return render_template('student/video_lessons.html')

@app.route('/student/test-series')
def student_test_series():
    return render_template('student/test_series.html')

# Admin Panel (UI only)
@app.route('/admin/login')
def admin_login():
    return render_template('admin/login.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin/dashboard.html')

@app.route('/admin/courses')
def admin_courses():
    return render_template('admin/courses.html')

@app.route('/admin/students')
def admin_students():
    return render_template('admin/students.html')

@app.route('/admin/analytics')
def admin_analytics():
    return render_template('admin/analytics.html')

# Admin Class Schedules & Timetables
@app.route('/admin/class_schedules', methods=['GET', 'POST'])
def admin_class_schedules():
    from db import get_schedule, save_schedule
    is_admin = True  # Replace with real admin check
    schedule = get_schedule()
    if request.method == 'POST':
        # Parse multiple schedule entries from form
        schedule_list = []
        classes = request.form.getlist('class')
        subjects = request.form.getlist('subject')
        days = request.form.getlist('day')
        times = request.form.getlist('time')
        faculties = request.form.getlist('faculty')
        for i in range(len(classes)):
            schedule_list.append({
                'class': classes[i],
                'subject': subjects[i],
                'day': days[i],
                'time': times[i],
                'faculty': faculties[i]
            })
        save_schedule(schedule_list)
        schedule = get_schedule()
        flash('Class schedule updated!', 'success')
    return render_template('admin/class_schedules.html', is_admin=is_admin, schedule=schedule)
