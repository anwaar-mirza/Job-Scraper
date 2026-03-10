import streamlit as st
import time

# ─────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Job URL Scraper",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
#  CUSTOM CSS  –  modern, minimal, mobile-ready
# ─────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* ── Google Font ── */
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    /* ── Page background ── */
    .stApp {
        background: linear-gradient(135deg, #0f1117 0%, #1a1d2e 100%);
        min-height: 100vh;
    }

    /* ── Main card container ── */
    .main-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 2.5rem 2rem;
        margin: 1.5rem auto;
        max-width: 680px;
        backdrop-filter: blur(12px);
        box-shadow: 0 24px 64px rgba(0, 0, 0, 0.4);
    }

    /* ── Hero header ── */
    .hero-title {
        font-size: clamp(1.6rem, 4vw, 2.2rem);
        font-weight: 700;
        color: #ffffff;
        text-align: center;
        letter-spacing: -0.5px;
        margin-bottom: 0.3rem;
    }
    .hero-badge {
        display: inline-block;
        background: linear-gradient(90deg, #4f8ef7, #8b5cf6);
        color: #fff;
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        padding: 3px 12px;
        border-radius: 20px;
        margin-bottom: 0.75rem;
    }
    .hero-desc {
        color: rgba(255,255,255,0.52);
        text-align: center;
        font-size: 0.93rem;
        line-height: 1.55;
        margin-bottom: 1.8rem;
    }

    /* ── Section label ── */
    .section-label {
        color: rgba(255,255,255,0.75);
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        margin-bottom: 0.4rem;
    }

    /* ── Divider ── */
    .divider {
        border: none;
        border-top: 1px solid rgba(255,255,255,0.07);
        margin: 1.5rem 0;
    }

    /* ── Streamlit widget overrides ── */
    div[data-testid="stSelectbox"] > div,
    div[data-testid="stNumberInput"] > div {
        background: rgba(255,255,255,0.06) !important;
        border: 1px solid rgba(255,255,255,0.12) !important;
        border-radius: 10px !important;
    }
    div[data-testid="stSelectbox"] label,
    div[data-testid="stNumberInput"] label {
        color: rgba(255,255,255,0.75) !important;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
    }

    /* ── Primary button ── */
    div[data-testid="stButton"] > button {
        background: linear-gradient(90deg, #4f8ef7 0%, #7c6df4 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 12px !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        padding: 0.75rem 2rem !important;
        width: 100% !important;
        transition: opacity 0.2s ease, transform 0.15s ease !important;
        letter-spacing: 0.2px;
    }
    div[data-testid="stButton"] > button:hover {
        opacity: 0.88 !important;
        transform: translateY(-1px) !important;
    }
    div[data-testid="stButton"] > button:active {
        transform: translateY(0) !important;
    }

    /* ── Result URL cards ── */
    .url-card {
        background: rgba(79, 142, 247, 0.07);
        border: 1px solid rgba(79, 142, 247, 0.18);
        border-radius: 10px;
        padding: 0.6rem 1rem;
        margin-bottom: 0.45rem;
        word-break: break-all;
        font-size: 0.85rem;
    }
    .url-card a {
        color: #6faeff;
        text-decoration: none;
    }
    .url-card a:hover { text-decoration: underline; }

    /* ── Stats pill ── */
    .stats-pill {
        display: inline-block;
        background: rgba(79,142,247,0.15);
        color: #7fc4fd;
        border: 1px solid rgba(79,142,247,0.3);
        border-radius: 20px;
        padding: 4px 14px;
        font-size: 0.82rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    /* ── Footer ── */
    .footer {
        text-align: center;
        color: rgba(255,255,255,0.28);
        font-size: 0.8rem;
        padding-top: 1.5rem;
    }

    /* ── Hide Streamlit branding ── */
    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)


# ─────────────────────────────────────────────
#  CONSTANTS
# ─────────────────────────────────────────────
JOB_WEBSITES = [
    "Dice",
    "Indeed",
    "Talent",
    "Built In",
    "ZipRecruiter",
    "Adzuna",
    "Himalayas.app",
    "CareerJet",
    "RemoteRocketship",
    "Startup.jobs",
    "SimplyHired",
    "Remotive",
    "Workable",
    "Glassdoor",
    "iHire",
    "LinkedIn",
    "Jobright AI",
]

JOB_KEYWORDS = [
    "Data Engineer",
    "Data Architect",
    "Solution Architect",
    "Data Warehousing",
    "ETL",
    "Data Integration",
    "Integration Engineer",
]


# ─────────────────────────────────────────────
#  STUB – replace with your real implementation
# ─────────────────────────────────────────────
def scrape_jobs(site: str, keyword: str, pages: int) -> list[str]:
    """
    Placeholder scraper function.
    Replace this body with your actual scraping logic.

    Args:
        site    – Job website name selected by the user.
        keyword – Job keyword / title to search for.
        pages   – Number of pages to scrape.

    Returns:
        A list of job posting URLs (strings).
    """
    # ── Simulate network latency for demo purposes ──
    time.sleep(2)

    # ── Return dummy URLs so the UI can be tested end-to-end ──
    dummy_urls = [
        f"https://{site.lower().replace(' ', '')}.com/job/{keyword.lower().replace(' ', '-')}-{i}"
        for i in range(1, pages * 5 + 1)
    ]
    return dummy_urls


# ─────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────
def render_results(urls: list[str]) -> None:
    """Renders scraped URLs as clickable cards with a summary pill."""
    st.success(f"✅ Scraping complete — {len(urls)} job URLs found.")
    st.markdown(
        f'<div class="stats-pill">📋 {len(urls)} URLs collected</div>',
        unsafe_allow_html=True,
    )
    for url in urls:
        st.markdown(
            f'<div class="url-card"><a href="{url}" target="_blank">🔗 {url}</a></div>',
            unsafe_allow_html=True,
        )


# ─────────────────────────────────────────────
#  MAIN UI
# ─────────────────────────────────────────────
def main() -> None:
    # ── Hero header ──
    st.markdown(
        """
        <div style="text-align:center; padding: 1rem 0 0.5rem;">
            <div class="hero-badge">⚡ Automated Job Discovery</div>
            <div class="hero-title">🔍 Job URL Scraper</div>
            <div class="hero-desc">
                Select a job portal, choose your target role, and let the scraper<br>
                collect all matching job URLs for you in seconds.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Input form ──
    with st.container():
        col_left, col_right = st.columns([1, 1], gap="medium")

        with col_left:
            site = st.selectbox(
                "🌐 Select Job Website",
                options=JOB_WEBSITES,
                help="Choose the job board you want to scrape.",
            )

        with col_right:
            keyword = st.selectbox(
                "🔎 Select Job Keyword",
                options=JOB_KEYWORDS,
                help="Select the job title or skill you are targeting.",
            )

        pages = st.number_input(
            "📄 Number of Pages to Scrape",
            min_value=1,
            value=1,
            step=1,
            help="Each page typically contains 10–25 job listings.",
        )

        st.markdown('<hr class="divider">', unsafe_allow_html=True)

        run = st.button("🚀  Start Scraping", use_container_width=True)

    # ── Execution & results ──
    if run:
        with st.spinner("⏳ Scraping job URLs… please wait"):
            results = scrape_jobs(site=site, keyword=keyword, pages=int(pages))

        st.markdown('<hr class="divider">', unsafe_allow_html=True)
        render_results(results)

    # ── Footer ──
    st.markdown(
        '<div class="footer">Thank you for using the Job URL Scraper.</div>',
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
