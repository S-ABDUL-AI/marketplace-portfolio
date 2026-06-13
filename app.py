import streamlit as st

st.set_page_config(
    page_title="Sherriff Abdul-Hamid | Marketplace Analytics Portfolio",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] { display: none; }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
    .main { background-color: #f8f9fa; }

    .hero {
        background: linear-gradient(135deg, #1F3864 0%, #0d2137 100%);
        padding: 56px 40px;
        border-radius: 16px;
        margin-bottom: 36px;
        text-align: center;
    }
    .hero h1 {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 8px;
        letter-spacing: -0.5px;
    }
    .hero .title {
        color: #90CAF9;
        font-size: 1.1rem;
        margin-bottom: 14px;
    }
    .hero .tagline {
        color: #CFD8DC;
        font-size: 0.98rem;
        max-width: 720px;
        margin: 0 auto;
        line-height: 1.65;
    }
    .section-heading {
        font-size: 1.3rem;
        font-weight: 700;
        color: #1F3864;
        border-bottom: 3px solid #1F3864;
        padding-bottom: 7px;
        margin-bottom: 22px;
        margin-top: 36px;
    }
    .app-card {
        background: white;
        border-radius: 14px;
        padding: 28px 24px;
        box-shadow: 0 3px 12px rgba(0,0,0,0.09);
        border-top: 5px solid #1F3864;
        height: 100%;
    }
    .app-card-green { border-top-color: #2e7d32; }
    .app-card-purple { border-top-color: #6a1b9a; }
    .app-card .icon { font-size: 2.1rem; margin-bottom: 11px; }
    .app-card h3 {
        color: #1F3864;
        font-size: 1.04rem;
        font-weight: 700;
        margin-bottom: 8px;
        line-height: 1.3;
    }
    .tag {
        display: inline-block;
        background: #E3F2FD;
        color: #1565C0;
        font-size: 0.71rem;
        font-weight: 600;
        padding: 3px 9px;
        border-radius: 20px;
        margin: 2px 2px 10px 0;
        letter-spacing: 0.02em;
        text-transform: uppercase;
    }
    .tag-green { background: #E8F5E9; color: #2e7d32; }
    .tag-purple { background: #F3E5F5; color: #6a1b9a; }
    .description {
        color: #555;
        font-size: 0.90rem;
        line-height: 1.58;
        margin-bottom: 18px;
    }
    .btn-primary {
        display: inline-block;
        background: #1F3864;
        color: white !important;
        padding: 9px 20px;
        border-radius: 8px;
        font-size: 0.87rem;
        font-weight: 600;
        text-decoration: none !important;
        margin-right: 8px;
        margin-bottom: 6px;
    }
    .btn-secondary {
        display: inline-block;
        background: transparent;
        color: #1F3864 !important;
        padding: 8px 18px;
        border-radius: 8px;
        font-size: 0.87rem;
        font-weight: 600;
        text-decoration: none !important;
        border: 2px solid #1F3864;
        margin-bottom: 6px;
    }
    .stat-card {
        background: white;
        border-radius: 12px;
        padding: 22px 18px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.07);
    }
    .stat-card .number {
        font-size: 1.9rem;
        font-weight: 700;
        color: #1F3864;
    }
    .stat-card .label {
        font-size: 0.80rem;
        color: #666;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-top: 4px;
    }
    .method-box {
        background: white;
        border-radius: 12px;
        padding: 26px 30px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.07);
        border-left: 5px solid #1F3864;
    }
    .method-box p {
        color: #444;
        font-size: 0.94rem;
        line-height: 1.7;
        margin-bottom: 11px;
    }
    .contact-card {
        background: linear-gradient(135deg, #1F3864 0%, #0d2137 100%);
        border-radius: 14px;
        padding: 34px 40px;
        text-align: center;
        margin-top: 36px;
    }
    .contact-card h3 {
        color: white;
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 7px;
    }
    .contact-card p {
        color: #CFD8DC;
        font-size: 0.93rem;
        margin-bottom: 18px;
    }
    .contact-link {
        display: inline-block;
        background: rgba(255,255,255,0.12);
        color: white !important;
        padding: 9px 20px;
        border-radius: 8px;
        font-size: 0.88rem;
        font-weight: 600;
        text-decoration: none !important;
        margin: 4px 5px;
        border: 1px solid rgba(255,255,255,0.25);
    }
    .footer {
        text-align: center;
        color: #999;
        font-size: 0.79rem;
        padding: 26px 0 8px 0;
    }
</style>
""",
    unsafe_allow_html=True,
)


# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown(
    """
<div class="hero">
    <div style="font-size:2.6rem; margin-bottom:14px;">🧪</div>
    <h1>Sherriff Abdul-Hamid</h1>
    <div class="title">Data Scientist · Applied Economist · Marketplace Analytics</div>
    <div class="tagline">
        Three production-grade marketplace analytics tools applying causal inference,
        experimentation science, and economic modelling to the strategic questions
        that two-sided platform teams face — from A/B testing and network effects
        to supply-demand optimisation and intervention incrementality.
    </div>
</div>
""",
    unsafe_allow_html=True,
)


# ── STATS ────────────────────────────────────────────────────────────────────
s1, s2, s3, s4 = st.columns(4)
with s1:
    st.markdown(
        """<div class="stat-card">
        <div class="number">3</div>
        <div class="label">Marketplace Tools</div>
    </div>""",
        unsafe_allow_html=True,
    )
with s2:
    st.markdown(
        """<div class="stat-card">
        <div class="number">5</div>
        <div class="label">Causal Methods</div>
    </div>""",
        unsafe_allow_html=True,
    )
with s3:
    st.markdown(
        """<div class="stat-card">
        <div class="number">16</div>
        <div class="label">App Tabs Built</div>
    </div>""",
        unsafe_allow_html=True,
    )
with s4:
    st.markdown(
        """<div class="stat-card">
        <div class="number">$265K</div>
        <div class="label">Target Role Salary</div>
    </div>""",
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)


# ── APP CARDS ────────────────────────────────────────────────────────────────
st.markdown(
    '<div class="section-heading">🧪 Marketplace Analytics Portfolio</div>',
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown(
        """
    <div class="app-card">
        <div class="icon">🔬</div>
        <h3>Marketplace Growth & Experimentation Lab</h3>
        <span class="tag">CUPED</span>
        <span class="tag">Sequential Testing</span>
        <span class="tag">Network Effects</span>
        <span class="tag">Uplift Modelling</span>
        <span class="tag">Bayesian A/B</span>
        <div class="description">
            Advanced experimentation platform for two-sided marketplace analytics.
            Demonstrates CUPED variance reduction (saving 30–50% sample size),
            network effects contamination analysis, sequential testing with alpha
            spending, promotion uplift modelling with four-quadrant segmentation,
            and a Bayesian decision framework with ship/no-ship recommendations.
            Includes an AI Analytics Copilot powered by Claude.
        </div>
        <a class="btn-primary" href="https://marketplace-experimentation-lab.streamlit.app" target="_blank">🚀 Open App</a>
        <a class="btn-secondary" href="https://github.com/S-ABDUL-AI/marketplace-experimentation-lab" target="_blank">⌥ GitHub</a>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
    <div class="app-card app-card-green">
        <div class="icon">📐</div>
        <h3>Marketplace Causal Inference & Incrementality Engine</h3>
        <span class="tag tag-green">DiD</span>
        <span class="tag tag-green">Synthetic Control</span>
        <span class="tag tag-green">PSM</span>
        <span class="tag tag-green">IV</span>
        <span class="tag tag-green">Event Study</span>
        <div class="description">
            Five-method causal inference platform for estimating the true
            incremental impact of marketplace interventions. Answers the question
            every growth team faces: did our programme cause booking growth, or
            would growth have happened anyway? Includes Difference-in-Differences,
            Synthetic Control, Propensity Score Matching, Instrumental Variables,
            Event Study, and an Incrementality Simulator with ROI decision output.
        </div>
        <a class="btn-primary" href="https://causal-inference-incrementality-engine.streamlit.app" target="_blank">🚀 Open App</a>
        <a class="btn-secondary" href="https://github.com/S-ABDUL-AI/causal-inference-incrementality-engine" target="_blank">⌥ GitHub</a>
    </div>
    """,
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

col3, col4 = st.columns(2, gap="large")

with col3:
    st.markdown(
        """
    <div class="app-card app-card-purple">
        <div class="icon">📈</div>
        <h3>Marketplace Economics & Supply-Demand Optimization Engine</h3>
        <span class="tag tag-purple">Price Elasticity</span>
        <span class="tag tag-purple">CLV</span>
        <span class="tag tag-purple">Monte Carlo</span>
        <span class="tag tag-purple">Market Expansion</span>
        <span class="tag tag-purple">Dynamic Pricing</span>
        <div class="description">
            Strategic decision-support platform answering the $50M question:
            should Airbnb invest in more hosts or more guests? Six-tab economics
            engine covering supply-demand health monitoring, log-log price
            elasticity and revenue optimisation, CLV and cohort retention
            analysis, multi-market expansion ROI scoring, 10,000-scenario
            Monte Carlo forecasting, and auto-generated executive recommendations.
        </div>
        <a class="btn-primary" href="https://marketplace-economics-engine.streamlit.app" target="_blank">🚀 Open App</a>
        <a class="btn-secondary" href="https://github.com/S-ABDUL-AI/marketplace-economics-engine" target="_blank">⌥ GitHub</a>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col4:
    st.markdown(
        """
    <div class="app-card" style="border-top-color:#90CAF9; background:#f8f9fa;
         display:flex; flex-direction:column; justify-content:center;
         align-items:center; text-align:center; min-height:300px;">
        <div style="font-size:2.5rem; margin-bottom:14px;">🔜</div>
        <h3 style="color:#1F3864;">Customer LTV & Churn Intelligence Platform</h3>
        <div class="description" style="margin-top:10px;">
            Coming soon — cohort LTV analysis, churn prediction modelling,
            retention intervention simulation, and lifetime value
            maximisation under budget constraints.
        </div>
        <div style="margin-top:12px; color:#90CAF9; font-size:0.85rem; font-weight:600;">
            IN DEVELOPMENT
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


# ── METHODOLOGY ──────────────────────────────────────────────────────────────
st.markdown(
    '<div class="section-heading">🧠 Methodology & Background</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="method-box">
    <p>
        These tools apply the analytical methods used by Staff-level and Principal
        data scientists at Airbnb, Uber, DoorDash, Lyft, and similar marketplace
        platforms — <strong>causal inference, experimentation science, and applied
        microeconomics</strong> — to the strategic questions that marketplace
        analytics teams face daily.
    </p>
    <p>
        The causal inference methods here — DiD, Synthetic Control, PSM, IV,
        and Event Study — are not academic demonstrations. They are the same
        identification strategies applied in published research on marketplace
        interventions, and the same methods Staff-level analysts use when
        leadership asks whether a programme actually worked. The experimentation
        tools address real marketplace challenges: CUPED for experiment velocity,
        network effects for SUTVA violations, and Bayesian frameworks for
        decision-making under uncertainty.
    </p>
    <p>
        All data is fully synthetic, generated from calibrated economic models
        and published marketplace research. No real user data, proprietary
        business data, or scraped data is used. Full transparency on every
        assumption is available in the <code>model.py</code> file of each repository.
    </p>
</div>
""",
    unsafe_allow_html=True,
)


# ── CONTACT ──────────────────────────────────────────────────────────────────
st.markdown(
    """
<div class="contact-card">
    <h3>Sherriff Abdul-Hamid</h3>
    <p>Data Scientist · Applied Economist · Marketplace Analytics<br>
    Los Angeles, CA · U.S. Permanent Resident (EB-1A)</p>
    <a class="contact-link" href="https://www.linkedin.com/in/abdul-hamid-sherriff-08583354/" target="_blank">💼 LinkedIn</a>
    <a class="contact-link" href="https://github.com/S-ABDUL-AI" target="_blank">⌥ GitHub</a>
    <a class="contact-link" href="https://s-abdul-ai.github.io/AI.github.io" target="_blank">🌐 Full Portfolio</a>
    <a class="contact-link" href="https://energy-portfolio.streamlit.app" target="_blank">⚡ Energy Portfolio</a>
    <a class="contact-link" href="mailto:sherriffhamid001@gmail.com">✉️ Email</a>
</div>
""",
    unsafe_allow_html=True,
)


# ── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown(
    """
<div class="footer">
    Built with Streamlit · All tools use fully synthetic data ·
    No real user or proprietary data used
</div>
""",
    unsafe_allow_html=True,
)
