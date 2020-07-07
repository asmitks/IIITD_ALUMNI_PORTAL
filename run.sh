# export FN_AUTH_REDIRECT_URI=http://byld.iiitd.edu.in/alumni/google/auth
# export FN_BASE_URI=http://byld.iiitd.edu.in/alumni/
# export FN_CLIENT_ID='371035254210-b0dfs4ll7un2cg9q916t65vp41oelul6.apps.googleusercontent.com'
# export FN_CLIENT_SECRET='JAbJZ9qIGv1sm8c_lhi7z688'
export FN_AUTH_REDIRECT_URI=http://localhost:5000/google/auth
export FN_BASE_URI=http://localhost:5000
export FN_CLIENT_ID='ur-id'
export FN_CLIENT_SECRET='ur password'
export FLASK_APP=app1.py
export FLASK_DEBUG=1
export FN_FLASK_SECRET_KEY=SOMETHING RANDOM AND SECRET

python3 -m flask run --host=0.0.0.0
    
