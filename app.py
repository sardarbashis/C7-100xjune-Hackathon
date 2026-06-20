import csv
import os
from datetime import datetime

import streamlit as st

st.set_page_config(page_title="Concept Check", page_icon="🧠", layout="centered")

RESULTS_FILE = "evidence/results.csv"


def save_result(
    learner,
    concept,
    first_answer,
    first_result,
    followup_question,
    second_answer,
    second_result,
    tool_reason,
):
    os.makedirs("evidence", exist_ok=True)
    file_exists = os.path.isfile(RESULTS_FILE)

    with open(RESULTS_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Timestamp",
                "Learner",
                "Concept",
                "First Answer",
                "First Result",
                "Follow-up Question",
                "Second Answer",
                "Second Result",
                "Tool Reason",
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            learner,
            concept,
            first_answer,
            first_result,
            followup_question,
            second_answer,
            second_result,
            tool_reason,
        ])


st.markdown("""
<style>
.main-title {
    font-size: 48px;
    font-weight: 800;
}
.card {
    padding: 18px;
    border-radius: 14px;
    background-color: #151923;
    border: 1px solid #2b3040;
    margin-bottom: 16px;
}
.small-muted {
    color: #9ca3af;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🧠 Concept Check</div>', unsafe_allow_html=True)
st.markdown("**Track A Hackathon MVP** — detects whether a learner is recognizing words or deriving concepts.")

st.info("Flow: first explanation → gap detection → follow-up → second attempt → pass/fail result.")

concept = st.selectbox(
    "Choose a concept",
    ["API", "Backend", "Database", "Interface"]
)

learner_name = st.text_input("Learner name / ID", placeholder="Example: Cold User 1")

answer = st.text_area(
    "First answer: Explain this concept in your own words",
    height=150,
    placeholder="Write your natural explanation here..."
)

questions = {
    "API": [
        "Why do APIs exist?",
        "What breaks if APIs disappear?",
        "Why not connect the frontend directly to the database?"
    ],
    "Backend": [
        "Why does a backend exist?",
        "What breaks if there is no backend?",
        "Where would user passwords and shared data be stored?"
    ],
    "Database": [
        "Why do databases exist?",
        "What happens if data is stored only in memory?",
        "Why not just use files instead of a database?"
    ],
    "Interface": [
        "Why does an interface exist?",
        "What breaks without an interface?",
        "Can two systems communicate without one?"
    ]
}

memorized_labels = [
    "bridge", "communication", "connect", "stores data",
    "frontend and backend", "middleman", "interface between",
    "helps communicate"
]

causal_words = [
    "because", "without", "break", "problem", "security",
    "persistent", "shared", "request", "response", "access",
    "authentication", "multiple users", "server", "logic",
    "control", "protect", "data", "user"
]


def evaluate(text):
    text_lower = text.lower()
    label_hits = [word for word in memorized_labels if word in text_lower]
    causal_hits = [word for word in causal_words if word in text_lower]

    if len(text.strip()) < 40:
        return "GAP", "The answer is too short to show real derivation.", label_hits, causal_hits

    if label_hits and len(causal_hits) < 3:
        return "GAP", f"The answer uses memorized labels like {label_hits}, but does not explain enough cause-effect reasoning.", label_hits, causal_hits

    if len(causal_hits) >= 3:
        return "PASS", "The answer shows causal reasoning and explains why the concept exists.", label_hits, causal_hits

    return "GAP", "The answer gives a definition but does not clearly derive the concept from first principles.", label_hits, causal_hits


st.divider()

if "first_result" not in st.session_state:
    st.session_state.first_result = None

if "first_reason" not in st.session_state:
    st.session_state.first_reason = ""

if st.button("Check First Answer", use_container_width=True):
    if not answer.strip():
        st.warning("Please write the first explanation.")
    else:
        first_result, first_reason, label_hits, causal_hits = evaluate(answer)

        st.session_state.first_result = first_result
        st.session_state.first_reason = first_reason

        st.subheader("First Answer Result")

        if first_result == "PASS":
            st.success("PASS — Understanding appears derived.")
        else:
            st.error("DERIVATION GAP DETECTED")

        st.markdown(f"**Reason:** {first_reason}")
        st.markdown(f"**Memorized label hits:** `{label_hits}`")
        st.markdown(f"**Causal reasoning hits:** `{causal_hits}`")

        st.subheader("Follow-up Questions")
        for q in questions[concept]:
            st.write("• " + q)

st.divider()

st.subheader("Second Attempt")

selected_followup = st.selectbox(
    "Choose the follow-up question used",
    questions[concept]
)

second_answer = st.text_area(
    "Second answer: Answer the follow-up after thinking again",
    height=150,
    placeholder="Now explain the concept causally..."
)

if st.button("Check Second Answer", use_container_width=True):
    if not second_answer.strip():
        st.warning("Please write the second answer.")
    else:
        second_result, second_reason, label_hits_2, causal_hits_2 = evaluate(second_answer)

        st.subheader("Second Answer Result")

        if second_result == "PASS":
            st.success("PASS — Gap likely closed.")
        else:
            st.error("FAIL — Gap still present.")

        st.markdown(f"**Reason:** {second_reason}")
        st.markdown(f"**Causal reasoning hits:** `{causal_hits_2}`")

        st.info("Human verification required: compare first answer and second answer before final judgment.")

        first_result_for_report = st.session_state.first_result or "First check not recorded"

        save_result(
            learner_name,
            concept,
            answer,
            first_result_for_report,
            selected_followup,
            second_answer,
            second_result,
            second_reason,
        )

        st.success("✅ Test result saved to evidence/results.csv")

        report = f"""
# Move 5 Test Record

Timestamp: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Learner:
{learner_name}

Concept:
{concept}

First Answer:
{answer}

First Result:
{first_result_for_report}

Follow-up Question Used:
{selected_followup}

Second Answer:
{second_answer}

Second Result:
{second_result}

Tool Reason:
{second_reason}

Human Verification:
Pending / Confirmed

Did the learner close the gap?
Yes / No / Partially
"""

        st.subheader("Copyable Move 5 Evidence")
        st.code(report, language="markdown")

st.divider()

st.subheader("Saved Test Evidence")

if os.path.exists(RESULTS_FILE):
    with open(RESULTS_FILE, "rb") as file:
        st.download_button(
            "📥 Download results.csv",
            file,
            file_name="results.csv",
            mime="text/csv",
            use_container_width=True,
        )
else:
    st.caption("No saved test results yet.")