from pymongo import MongoClient

MONGO_URI = "mongodb+srv://sudeep:kNNmTOKJRIjL4YMV@cluster1.kul25iu.mongodb.net/?appName=Cluster1"
client = MongoClient(MONGO_URI)
db = client["mydatabase"]

# Collections
users_collection = db["users"]
courses_collection = db["courses"]
testimonials_collection = db["testimonials"]
inquiries_collection = db["inquiries"]

# Course functions
def get_courses(limit=None, course_id=None):
	if course_id:
		return courses_collection.find_one({'_id': course_id})
	if limit:
		return list(courses_collection.find().limit(limit))
	return list(courses_collection.find())

# Testimonial functions
def get_testimonials(limit=None):
	if limit:
		return list(testimonials_collection.find().limit(limit))
	return list(testimonials_collection.find())

# Inquiry form
def save_inquiry(name, phone, message):
	inquiries_collection.insert_one({
		'name': name,
		'phone': phone,
		'message': message
	})

# Admission form
admissions_collection = db["admissions"]
def save_admission(name, email, class_name, board, medium, course):
	admissions_collection.insert_one({
		'name': name,
		'email': email,
		'class': class_name,
		'board': board,
		'medium': medium,
		'course': course
	})