import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
nltk.download('stopwords')

# Load the pickled model and vectorizer
port_stem = PorterStemmer()
cv = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))


# Function for text preprocessing (stemming)
def stemming(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    text = text.split()
    text = [port_stem.stem(word) for word in text if word.lower() not in stopwords.words('english')]
    text = ' '.join(text)
    return text


# Streamlit app title and sidebar configuration
st.set_page_config(page_title="Spam Classifier", page_icon=":fire:", layout="wide")

# Sidebar with app information
st.sidebar.title("About")
st.sidebar.info("This is a simple spam classifier app. Enter a message to check if it's spam or not.")

# Main content
st.title('SPAM CLASSIFIER')

# Input box for the user to enter a message
inp = st.text_area('Enter the message')

# Button to trigger classification
if st.button('Classify'):
    if inp:
        # Preprocess the input text
        trans_inp = stemming(inp)
        transf = [trans_inp]

        # Transform the text using the vectorizer
        vectorized = cv.transform(transf)

        # Make prediction using the model
        result = model.predict(vectorized)

        # Display the result dynamically
        with st.spinner('Classifying...'):
            st.markdown('## Result')
            if result == 1:
                st.error('Spam :warning:')
            else:
                st.success('Not Spam :white_check_mark:')
    else:
        st.warning('Please enter a message.')
print(st.__version__)
# Adding a footer
st.sidebar.title("Connect with Me")
st.sidebar.info(
    "If you have any questions or suggestions, feel free to connect!\n"
    "Email: your.email@example.com\n"
    "LinkedIn: Mohammed Abdul Rahman (https://www.linkedin.com/in/yourname/)"
)
