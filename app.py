import streamlit as st
import pickle
import re

# ---------------- CONFIG ---------------- #
st.set_page_config(
    page_title="Support Triage AI",
    page_icon="🤖",
    layout="centered"
)

# ---------------- LOAD MODEL ---------------- #
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ---------------- FUNCTIONS ---------------- #

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text

def predict(text):
    text = clean_text(text)
    vec = vectorizer.transform([text])
    probs = model.predict_proba(vec)[0]
    label = model.predict(vec)[0]
    confidence = max(probs)
    return label, confidence

def escalate(confidence, text):
    if confidence < 0.4:
        return True
    
    risky_words = ["fraud", "legal", "complaint", "refund immediately"]
    if any(word in text.lower() for word in risky_words):
        return True
    
    return False

def generate_reply(label):
    replies = {
        "billing": "Sorry for the billing issue. Please share your transaction ID so we can assist you further.",
        "account": "It seems you're facing a login issue. Please try resetting your password using the 'Forgot Password' option."
    }
    return replies.get(label, "Thanks for reaching out. Our support team will review your issue and get back to you shortly.")

# Label display mapping
label_map = {
    "billing": "💳 Billing Issue",
    "account": "🔐 Account Issue",
    "bug": "🐛 Technical Bug",
    "content": "🎬 Content Access",
    "general": "💬 General Feedback"
}

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("ℹ️ About")
st.sidebar.info("""
This AI system classifies customer support tickets,
suggests replies, and flags tickets that need human attention.

Built using:
- TF-IDF + Logistic Regression
- Rule-based escalation
- Streamlit UI
""")

st.sidebar.markdown("### 🧪 Example Inputs")
st.sidebar.write("- I was charged twice")
st.sidebar.write("- Cannot login to my account")
st.sidebar.write("- App crashes on startup")

# ---------------- MAIN UI ---------------- #

st.title("🤖 Support Triage Agent")
st.markdown("Automatically classify support tickets, suggest replies, and flag risky cases.")

st.divider()

# Input
user_input = st.text_area(
    "📝 Enter Customer Ticket",
    height=150,
    placeholder="e.g. I was charged twice for my subscription..."
)

# Button
if st.button("🔍 Analyze Ticket"):

    if user_input.strip() == "":
        st.warning("⚠️ Please enter a ticket.")
    else:
        label, confidence = predict(user_input)
        esc = escalate(confidence, user_input)
        reply = generate_reply(label) if not esc else "Escalated to human agent"

        st.divider()

        # Layout columns
        col1, col2 = st.columns(2)

        # Category
        with col1:
            st.subheader("📂 Category")
            st.success(label_map.get(label, label))

        # Escalation
        with col2:
            st.subheader("🚨 Escalation")
            if esc:
                st.error("YES (Human Required)")
            else:
                st.success("NO")

        st.divider()

        # Confidence
        st.subheader("📊 Confidence Score")
        st.progress(float(confidence))
        st.write(f"{round(confidence * 100, 2)}%")

        st.divider()

        # Suggested reply
        st.subheader("💬 Suggested Reply")
        if esc:
            st.warning("This ticket has been escalated to a human agent.")
        else:
            st.info(reply)

        st.divider()

        # Debug section (for interview/demo)
        with st.expander("🔍 Debug Info"):
            st.write("Raw Confidence:", confidence)
            st.write("Predicted Label:", label)