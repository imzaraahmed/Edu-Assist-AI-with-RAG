
import streamlit as st
from src.rag_answer import answer_question


# ─────────────────────────────────────────────
# Page configuration
# ─────────────────────────────────────────────

st.set_page_config(
    page_title="Edu-Assist AI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ─────────────────────────────────────────────
# Custom styling
# ─────────────────────────────────────────────

st.markdown(
    """
    <style>

    /* Remove Streamlit default spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* Main background */
    .stApp {
        background:
            radial-gradient(
                circle at 15% 15%,
                rgba(124, 92, 255, 0.12),
                transparent 28%
            ),
            radial-gradient(
                circle at 85% 80%,
                rgba(0, 210, 180, 0.08),
                transparent 25%
            ),
            #08090d;
    }

    /* Hide Streamlit branding */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    /* Brand */
    .brand {
        font-size: 1.15rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        color: #f4f4f5;
    }

    .brand span {
        color: #a78bfa;
    }

    /* Hero section */
    .hero {
        text-align: center;
        padding: 90px 20px 45px 20px;
    }

    .hero-badge {
        display: inline-block;
        padding: 7px 14px;
        border: 1px solid rgba(167, 139, 250, 0.25);
        border-radius: 999px;
        background: rgba(167, 139, 250, 0.08);
        color: #c4b5fd;
        font-size: 0.82rem;
        margin-bottom: 22px;
    }

    .hero h1 {
        font-size: clamp(3rem, 7vw, 5.8rem);
        line-height: 0.95;
        margin: 0;
        font-weight: 800;
        letter-spacing: -0.06em;
        color: #fafafa;
    }

    .hero h1 span {
        background: linear-gradient(
            90deg,
            #a78bfa,
            #67e8f9
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero p {
        max-width: 650px;
        margin: 25px auto 0 auto;
        color: #a1a1aa;
        font-size: 1.05rem;
        line-height: 1.7;
    }

    /* Study cards */
    div.stButton > button {
        min-height: 115px;
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 20px;
        background: rgba(255,255,255,0.035);
        color: #f4f4f5;
        transition: all 0.25s ease;
        font-size: 1rem;
        font-weight: 600;
        white-space: pre-line;
    }

    div.stButton > button:hover {
        transform: translateY(-4px);
        border-color: rgba(167,139,250,0.45);
        background: rgba(255,255,255,0.07);
        color: #ffffff;
    }

    /* Section label */
    .section-label {
        color: #71717a;
        text-transform: uppercase;
        letter-spacing: 0.14em;
        font-size: 0.72rem;
        font-weight: 700;
        margin: 35px 0 15px 2px;
    }

    /* Ask area */
    .ask-label {
        margin-top: 30px;
        margin-bottom: 10px;
        color: #a1a1aa;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #52525b;
        font-size: 0.75rem;
        margin-top: 70px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ─────────────────────────────────────────────
# Navigation
# ─────────────────────────────────────────────

st.markdown(
    '<div class="brand"><span>✦</span> EDU-ASSIST</div>',
    unsafe_allow_html=True,
)


# ─────────────────────────────────────────────
# Hero
# ─────────────────────────────────────────────

st.html(
    """
    <div class="hero">

        <div class="hero-badge">
            ✦ AI STUDY COMPANION
        </div>

        <h1>
            Learn smarter.<br>
            <span>Understand deeper.</span>
        </h1>

        <p>
            Your intelligent study companion powered by your
            Artificial Intelligence course notes.
            Ask questions, explore concepts, and learn with confidence.
        </p>

    </div>
    """
)


# ─────────────────────────────────────────────
# Interactive Study Cards
# ─────────────────────────────────────────────

st.markdown(
    '<div class="section-label">Explore your study companion</div>',
    unsafe_allow_html=True,
)


# Initialize session state
if "selected_question" not in st.session_state:
    st.session_state["selected_question"] = ""

if "last_question" not in st.session_state:
    st.session_state["last_question"] = ""


col1, col2, col3, col4 = st.columns(4)


with col1:
    if st.button(
        "🧠\n\nUnderstand Concepts",
        use_container_width=True,
        key="understand_card",
    ):
        st.session_state["selected_question"] = (
            "Explain an important Artificial Intelligence concept from my notes."
        )
        st.rerun()


with col2:
    if st.button(
        "🔎\n\nSearch My Notes",
        use_container_width=True,
        key="search_card",
    ):
        st.session_state["selected_question"] = (
            "What are the main topics covered in my Artificial Intelligence notes?"
        )
        st.rerun()


with col3:
    if st.button(
        "📚\n\nLecture Help",
        use_container_width=True,
        key="lecture_card",
    ):
        st.session_state["selected_question"] = (
            "Give me a simple explanation of a lecture topic from my AI notes."
        )
        st.rerun()


with col4:
    if st.button(
        "💡\n\nStudy Example",
        use_container_width=True,
        key="example_card",
    ):
        st.session_state["selected_question"] = (
            "Give me an example of an Artificial Intelligence concept from my notes."
        )
        st.rerun()


# ─────────────────────────────────────────────
# Ask Your Question
# ─────────────────────────────────────────────

if st.session_state["selected_question"]:

    st.markdown(
        '<div class="ask-label">Ask your AI study companion</div>',
        unsafe_allow_html=True,
    )

    question = st.text_area(
        "Your question",
        value=st.session_state["selected_question"],
        height=120,
        placeholder="Ask something about your Artificial Intelligence notes...",
        key="current_question",
    )

    ask = st.button(
        "✨ Ask AI",
        use_container_width=True,
        type="primary",
        key="ask_ai_button",
    )

    # IMPORTANT:
    # The ask button is handled INSIDE the same block where
    # it is created. This prevents the NameError you had.

    if ask:

        if question.strip():

            st.session_state["last_question"] = question

            st.markdown("### 🤖 AI Study Assistant")

            with st.spinner(
                "Searching your AI notes and preparing an answer..."
            ):

                try:

                    answer = answer_question(question)

                    st.markdown("#### Answer")

                    st.write(answer)

                except Exception as e:

                    st.error(
                        "Something went wrong while generating the answer."
                    )

                    st.exception(e)

        else:

            st.warning("Please enter a question first.")


# ─────────────────────────────────────────────
# Footer
# ─────────────────────────────────────────────

st.markdown(
    """
    <div class="footer">
        RAG • CrewAI • ChromaDB • AI COURSE NOTES
    </div>
    """,
    unsafe_allow_html=True,
)
