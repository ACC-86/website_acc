from pymongo import MongoClient

MONGO_URI = "mongodb+srv://sudeep:kNNmTOKJRIjL4YMV@cluster1.kul25iu.mongodb.net/?appName=Cluster1"
client = MongoClient(MONGO_URI)
db = client["mydatabase"]

# Collections
users_collection = db["users"]
courses_collection = db["courses"]
testimonials_collection = db["testimonials"]
inquiries_collection = db["inquiries"]

# Ensure indexes for performance
courses_collection.create_index("_id")
testimonials_collection.create_index("_id")
inquiries_collection.create_index("phone")
admissions_collection = db["admissions"]
admissions_collection.create_index("email")
schedule_collection = db["schedules"]
schedule_collection.create_index("class")
homework_collection = db["homework"]
homework_collection.create_index("class")
# Course functions
def get_courses(limit=None, course_id=None):
	if course_id:
		return courses_collection.find_one({'_id': course_id})
	if limit:
		return list(courses_collection.find().limit(limit))
		# Default limit to 50 if not specified
	return list(courses_collection.find().limit(50))

# Testimonial functions
def get_testimonials(limit=None):
	if limit:
		return list(testimonials_collection.find().limit(limit))
		# Default limit to 20 if not specified
	return list(testimonials_collection.find().limit(20))

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

# Schedule functions
schedule_collection = db["schedules"]
def save_schedule(schedule_list):
	# schedule_list: list of dicts [{class, subject, day, time, faculty}]
	schedule_collection.delete_many({})  # Remove old
	schedule_collection.insert_many(schedule_list)

def get_schedule():
		# Default limit to 30
	return list(schedule_collection.find().limit(30))

# Homework functions
homework_collection = db["homework"]
def save_homework(homework_dict):
	# homework_dict: {5: '...', 6: '...', 7: '...', 8: '...'}
	from datetime import date
	today = date.today().isoformat()
	# Convert keys to strings for MongoDB
	homework_str_keys = {str(k): v for k, v in homework_dict.items()}
	homework_collection.update_one(
		{'date': today},
		{'$set': {'homework': homework_str_keys}},
		upsert=True
	)

def get_homework_for_today():
	from datetime import date
	today = date.today().isoformat()
	doc = homework_collection.find_one({'date': today})
	# Convert keys back to int for display
	if doc and 'homework' in doc:
		return {int(k): v for k, v in doc['homework'].items()}
	return {}