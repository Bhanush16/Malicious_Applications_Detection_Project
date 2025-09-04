from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('malicious_app_model.pkl')

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            # Get input values from the form and validate them
            app_type = request.form.get('app_type')
            number_of_downloads = request.form.get('number_of_downloads')
            rating = request.form.get('rating')
            permissions_count = request.form.get('permissions_count')
            redirects = request.form.get('redirects')
            privacy_policy_exists = request.form.get('privacy_policy_exists')
            is_verified_developer = request.form.get('is_verified_developer')
            is_open_source = request.form.get('is_open_source')
            user_reports = request.form.get('user_reports')
            malicious_activities = request.form.get('malicious_activities')
            support_response_time = request.form.get('support_response_time')
            app_age = request.form.get('app_age')
            advertisement_count = request.form.get('advertisement_count')

            # Ensure that the fields are not empty and are valid integers/floats
            try:
                app_type = int(app_type)
                number_of_downloads = int(number_of_downloads)
                rating = float(rating)
                permissions_count = int(permissions_count)
                redirects = int(redirects)
                privacy_policy_exists = int(privacy_policy_exists)
                is_verified_developer = int(is_verified_developer)
                is_open_source = int(is_open_source)
                user_reports = int(user_reports)
                malicious_activities = int(malicious_activities)
                support_response_time = int(support_response_time)
                app_age = int(app_age)
                advertisement_count = int(advertisement_count)
            except ValueError as ve:
                return f"Invalid input value: {ve}"

            # Prepare input data
            input_features = [[app_type, number_of_downloads, rating, permissions_count,
                               redirects, privacy_policy_exists, is_verified_developer,
                               is_open_source, user_reports, malicious_activities,
                               support_response_time, app_age, advertisement_count]]

            # Make prediction
            prediction = model.predict(input_features)
            result = "Safe" if prediction[0] == 1 else "Malicious"

            return render_template("result.html", result=result)

        except Exception as e:
            return f"Error: {e}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
