import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict(text):
    vec = vectorizer.transform([text])
    probs = model.predict_proba(vec)[0]
    label = model.predict(vec)[0]
    confidence = max(probs)
    return label, confidence

def escalate(confidence, text):
    if confidence < 0.6:
        return True
    
    if "refund immediately" in text.lower():
        return True
    
    return False

def reply(label):
    replies = {
        "billing": "Sorry for the billing issue. Please share your transaction ID.",
        "account": "Please try resetting your password using 'Forgot Password'."
    }
    return replies.get(label, "Our team will get back to you.")

# UI
st.title("Support Triage Agent")

text = st.text_area("Enter support ticket")

if st.button("Analyze"):
    label, confidence = predict(text)
    esc = escalate(confidence, text)
    rep = reply(label) if not esc else "Escalated to human agent"

    st.write("Category:", label)
    st.write("Confidence:", round(confidence, 2))
    st.write("Escalation:", esc)
    st.write("Reply:", rep)