
import firebase_admin
from firebase_admin import credentials, db
import base64
# Initialize Firebase app and storage client
if not firebase_admin._apps:
    # Initialize Firebase app and storage client
    cred = credentials.Certificate('serviceAccountKey.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://patient-portal-d50d2-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })

# Get a reference to the database
db_ref = db.reference('/')


# Define function to retrieve image URL from Firebase Storage


def get_image_url(username):
    user_data = db_ref.child(username).get()
    if user_data is None or 'image' not in user_data:
        return None
    encoded_image = user_data['image']
    image_url = f"data:image/jpeg;base64,{encoded_image}"
    return image_url


def upload_image(username, image_file):
    # Convert image to base64 string
    image_bytes = image_file.read()
    encoded_image = base64.b64encode(image_bytes).decode('utf-8')

    # Upload image to Firebase Realtime Database
    db_ref.child(username).update({'image': encoded_image})

    # Get image URL and return it (optional)
    image_url = f"data:image/jpeg;base64,{encoded_image}"
    return image_url
