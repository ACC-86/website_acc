
from flask import Flask, render_template, request, redirect, url_for, flash, session
app = Flask(__name__)
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
app.secret_key = os.environ.get('SECRET_KEY')

from db import get_courses, get_testimonials, save_inquiry, save_admission
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
    return render_template('home.html', courses=courses, testimonials=testimonials)

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

if __name__ == '__main__':
    app.run(debug=True)
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)