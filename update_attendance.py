import firebase_admin
from firebase_admin import credentials, firestore
import json
import os

# Read the service account key from GitHub Secrets
service_account_info = json.loads(os.getenv("FIREBASE_KEY"))

# Initialize Firebase with credentials
cred = credentials.Certificate(service_account_info)
firebase_admin.initialize_app(cred)
db = firestore.client()

# Update attendance collection: Mark all records as "absent"
attendance_ref = db.collection("attendance")

try:
    docs = attendance_ref.get()
    for doc in docs:
        attendance_ref.document(doc.id).update({"attendance": "absent"})
    
    print("✅ All attendance records marked as absent!")

except Exception as e:
    print(f"❌ Error updating attendance: {e}")
