#for the backend connection using flask 
from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)

url_mapping={}
reverse_mapping={}

# Route for the home page
@app.route('/')
def home():
    return render_template('frontend.html')


# API endpoint to handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    # Get data from the form
    user_url = request.form.get('url')

    #the code for making the url shortner
    import secrets
    random_key=secrets.token_urlsafe(8)
    if user_url in reverse_mapping.keys():
        exsiting_key=reverse_mapping[user_url]
        response_message1=f'http://127.0.0.1:5000/{exsiting_key}'
        # return f'Already shortened! Shortened URL: <a href="{response_message}">{response_message}</a>'
        

        return jsonify({'message': response_message1,'existing':True})

    url_mapping[random_key]=user_url
    reverse_mapping[user_url]=random_key


    # Simple logic for demonstration (response message)
    response_message = f'http://127.0.0.1:5000/{random_key}'
    # Send a JSON response back to the frontend
    return jsonify({'message': response_message})

#to handle rediretcion 
@app.route('/<key>')
def redirect_to_original(key):
    original_url = url_mapping.get(key)
    
    # If the key exists, redirect to the original URL
    if original_url:
        return redirect(original_url)
    else:
        return "URL not found!", 404
    
# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
