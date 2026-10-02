import json
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Responsible AI Governance | Equity Monitoring Toolkit",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# PATHS + DATA
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent
REPORTS_DIR = BASE_DIR / "reports"


def load_json(filename):
    with open(REPORTS_DIR / filename, "r", encoding="utf-8") as file:
        return json.load(file)


baseline = load_json("baseline_metrics.json")
gender = load_json("gender_fairness_metrics.json")
education = load_json("education_fairness_metrics.json")
explainability = load_json("explainability_results.json")
genai = load_json("genai_safety_results.json")
governance = load_json("governance_decision.json")

status = governance.get("overall_status", "REVIEW")
status_class = status.lower()


# =========================================================
# LOVABLE-INSPIRED DESIGN SYSTEM
# =========================================================

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
    --bg: #f7f9fc;
    --surface: #ffffff;
    --surface-soft: #f1f4f9;
    --text: #17213b;
    --muted: #65718a;
    --border: #dfe5ef;
    --primary: #3974d8;
    --primary-soft: #edf3ff;
    --violet: #7956d8;
    --violet-soft: #f1edff;
    --teal: #168d9d;
    --teal-soft: #eaf8fa;
    --success: #209b68;
    --success-soft: #ebf8f1;
    --review: #c47a08;
    --review-soft: #fff7e5;
    --danger: #d84a43;
    --danger-soft: #fff0ef;
    --sidebar: #17233f;
    --shadow: 0 12px 34px rgba(31, 50, 82, .08);
}

html {
    scroll-behavior: smooth;
}

.stApp {
    background: var(--bg);
    color: var(--text);
    font-family: 'Manrope', ui-sans-serif, system-ui, sans-serif;
}

.block-container {
    max-width: 1480px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stSidebar"] {
    background: var(--sidebar);
    border-right: 1px solid rgba(255,255,255,.08);
}

[data-testid="stSidebar"] * {
    font-family: 'Manrope', sans-serif;
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] div {
    color: #dfe7f7;
}

.sidebar-brand {
    padding: 8px 4px 22px;
    border-bottom: 1px solid rgba(255,255,255,.10);
    margin-bottom: 20px;
}

.sidebar-icon {
    width: 42px;
    height: 42px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border-radius: 11px;
    background: #3974d8;
    color: white;
    font-size: 21px;
    margin-right: 10px;
    vertical-align: middle;
}

.sidebar-kicker {
    color: #8fb8ff;
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: .08em;
}

.sidebar-title {
    color: white;
    font-size: 15px;
    font-weight: 800;
}

.sidebar-status {
    margin-top: 26px;
    padding: 15px;
    border-radius: 11px;
    background: rgba(196,122,8,.13);
    border: 1px solid rgba(255,194,82,.22);
}

.sidebar-status .label {
    color: #f4bf57;
    font-size: 10px;
    font-weight: 800;
    text-transform: uppercase;
}

.sidebar-status .value {
    color: white;
    font-size: 19px;
    font-weight: 800;
    margin-top: 4px;
}

.sidebar-status .desc {
    color: #aebbd1;
    font-size: 11px;
    line-height: 1.5;
    margin-top: 4px;
}

.page-kicker {
    color: var(--primary);
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: .08em;
    margin-bottom: 8px;
}

.page-title {
    color: var(--text);
    font-size: clamp(30px, 4vw, 43px);
    line-height: 1.1;
    font-weight: 800;
    letter-spacing: -.035em;
    margin: 0;
}

.page-subtitle {
    color: var(--muted);
    font-size: 15px;
    margin-top: 11px;
}

.snapshot {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 9px 13px;
    border: 1px solid var(--border);
    border-radius: 10px;
    background: white;
    color: var(--muted);
    font-size: 11px;
    box-shadow: 0 3px 12px rgba(31,50,82,.05);
}

.snapshot-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--success);
}

.status-banner {
    margin: 25px 0 18px;
    border: 1px solid rgba(196,122,8,.28);
    border-radius: 14px;
    overflow: hidden;
    background: linear-gradient(110deg, #fffaf0, #f9f7ff);
    box-shadow: var(--shadow);
}

.status-grid {
    display: grid;
    grid-template-columns: .8fr 1.2fr;
}

.status-main {
    display: flex;
    align-items: center;
    gap: 15px;
    padding: 23px;
    border-right: 1px solid rgba(196,122,8,.18);
}

.status-icon {
    width: 49px;
    height: 49px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 11px;
    background: var(--review);
    color: white;
    font-size: 22px;
}

.status-label {
    color: var(--review);
    font-size: 10px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: .07em;
}

.status-value {
    color: var(--text);
    font-size: 30px;
    line-height: 1;
    font-weight: 800;
    margin-top: 5px;
}

.status-copy {
    padding: 23px;
    display: flex;
    align-items: center;
}

.status-copy strong {
    color: var(--text);
    font-size: 14px;
}

.status-copy p {
    color: var(--muted);
    font-size: 12px;
    line-height: 1.6;
    margin: 5px 0 0;
}

.kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    margin: 18px 0 28px;
}

.kpi-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 18px;
    box-shadow: var(--shadow);
    transition: transform .18s ease, box-shadow .18s ease;
}

.kpi-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 18px 38px rgba(31,50,82,.12);
}

.kpi-icon {
    width: 39px;
    height: 39px;
    border-radius: 9px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
}

.kpi-value {
    color: var(--text);
    font-size: 26px;
    font-weight: 800;
    margin-top: 14px;
}

.kpi-label {
    color: var(--muted);
    font-size: 11px;
    font-weight: 600;
    margin-top: 3px;
}

.blue { color: var(--primary); background: var(--primary-soft); }
.purple { color: var(--violet); background: var(--violet-soft); }
.teal { color: var(--teal); background: var(--teal-soft); }
.orange { color: var(--review); background: var(--review-soft); }

.section-shell {
    margin-top: 26px;
    padding: 22px;
    border: 1px solid var(--border);
    border-radius: 14px;
    background: rgba(255,255,255,.78);
    box-shadow: var(--shadow);
}

.section-head {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 14px;
    margin-bottom: 18px;
}

.section-title-wrap {
    display: flex;
    gap: 11px;
}

.section-icon {
    width: 37px;
    height: 37px;
    flex: 0 0 37px;
    border-radius: 9px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--primary-soft);
    color: var(--primary);
    font-size: 17px;
}

.eyebrow {
    color: var(--primary);
    font-size: 9px;
    font-weight: 800;
    letter-spacing: .09em;
    text-transform: uppercase;
}

.section-title {
    color: var(--text);
    font-size: 21px;
    font-weight: 800;
    margin-top: 2px;
}

.section-desc {
    color: var(--muted);
    font-size: 11px;
    margin-top: 3px;
}

.review-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    color: var(--review);
    background: var(--review-soft);
    border: 1px solid rgba(196,122,8,.25);
    border-radius: 999px;
    padding: 7px 11px;
    font-size: 10px;
    font-weight: 800;
}

.inner-card {
    height: 100%;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 11px;
    padding: 19px;
}

.inner-title {
    color: var(--text);
    font-size: 14px;
    font-weight: 800;
}

.inner-desc {
    color: var(--muted);
    font-size: 10px;
    margin-top: 4px;
}

.data-stat-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    border-top: 1px solid var(--border);
    margin-top: 20px;
    padding-top: 15px;
}

.data-stat {
    text-align: center;
}

.data-stat .value {
    color: var(--text);
    font-size: 17px;
    font-weight: 800;
}

.data-stat .label {
    color: var(--muted);
    font-size: 9px;
    margin-top: 2px;
}

.bar-row {
    margin: 14px 0;
}

.bar-top {
    display: flex;
    justify-content: space-between;
    font-size: 11px;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 6px;
}

.bar-track {
    height: 9px;
    overflow: hidden;
    border-radius: 999px;
    background: #edf0f5;
}

.bar-fill {
    height: 100%;
    border-radius: 999px;
    background: var(--primary);
}

.bar-fill.purple-fill { background: var(--violet); }
.bar-fill.teal-fill { background: var(--teal); }

.matrix {
    display: grid;
    grid-template-columns: 42px 1fr 1fr;
    gap: 7px;
    margin-top: 16px;
}

.matrix-head {
    color: var(--muted);
    font-size: 8px;
    font-weight: 800;
    text-align: center;
    text-transform: uppercase;
}

.matrix-side {
    writing-mode: vertical-rl;
    transform: rotate(180deg);
    display: flex;
    justify-content: center;
    align-items: center;
    color: var(--muted);
    font-size: 8px;
    font-weight: 800;
    text-transform: uppercase;
}

.matrix-cell {
    min-height: 84px;
    border-radius: 9px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.matrix-cell .number {
    font-size: 24px;
    font-weight: 800;
}

.matrix-cell .code {
    font-size: 9px;
    font-weight: 800;
    margin-top: 2px;
}

.matrix-tn { background: var(--primary-soft); color: var(--primary); }
.matrix-fp, .matrix-fn { background: var(--review-soft); color: var(--review); }
.matrix-tp { background: var(--success-soft); color: var(--success); }

.fairness-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
}

.group-table {
    margin-top: 18px;
    display: grid;
    grid-template-columns: 1.1fr 1fr 1fr;
    gap: 0;
    border-top: 1px solid var(--border);
}

.group-table > div {
    padding: 9px 5px;
    border-bottom: 1px solid var(--border);
    font-size: 10px;
}

.group-head {
    color: var(--muted);
    font-weight: 800;
}

.group-name {
    color: var(--text);
    font-weight: 700;
}

.group-value {
    text-align: center;
    color: var(--text);
    font-weight: 700;
}

.evidence-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 16px;
}

.evidence-value {
    background: var(--surface-soft);
    border-radius: 9px;
    padding: 12px;
}

.evidence-label {
    color: var(--muted);
    font-size: 9px;
    line-height: 1.4;
}

.evidence-number {
    color: var(--text);
    font-size: 18px;
    font-weight: 800;
    margin-top: 4px;
}

.shap-list {
    margin-top: 12px;
}

.shap-row {
    display: grid;
    grid-template-columns: 25px 135px 1fr;
    align-items: center;
    gap: 9px;
    margin: 9px 0;
}

.shap-rank {
    color: var(--muted);
    font-size: 9px;
    font-weight: 800;
}

.shap-feature {
    color: var(--text);
    font-size: 10px;
    font-weight: 600;
}

.shap-track {
    height: 25px;
    background: #edf0f5;
    border-radius: 6px;
    overflow: hidden;
}

.shap-fill {
    height: 100%;
    background: rgba(121,86,216,.78);
    border-radius: 6px;
    display: flex;
    align-items: center;
    padding-left: 8px;
    color: white;
    font-size: 8px;
    font-weight: 800;
}

.shap-fill.strong {
    background: var(--primary);
}

.safety-big {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
}

.safety-score {
    color: var(--text);
    font-size: 38px;
    line-height: 1;
    font-weight: 800;
}

.safety-label {
    color: var(--muted);
    font-size: 11px;
    margin-top: 5px;
}

.safety-count {
    text-align: right;
}

.safety-count .number {
    color: var(--text);
    font-size: 19px;
    font-weight: 800;
}

.safety-count .label {
    color: var(--muted);
    font-size: 9px;
}

.safety-bar {
    display: flex;
    height: 11px;
    border-radius: 999px;
    overflow: hidden;
    background: #edf0f5;
    margin-top: 21px;
}

.safe-part { background: var(--success); }
.review-part { background: var(--review); }
.block-part { background: var(--danger); }

.safety-legend {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 7px;
    margin-top: 12px;
}

.safety-chip {
    border-radius: 8px;
    padding: 9px;
    text-align: center;
}

.safety-chip .number {
    font-size: 18px;
    font-weight: 800;
}

.safety-chip .label {
    font-size: 8px;
    font-weight: 800;
    text-transform: uppercase;
    margin-top: 2px;
}

.chip-safe { color: var(--success); background: var(--success-soft); }
.chip-review { color: var(--review); background: var(--review-soft); }
.chip-block { color: var(--danger); background: var(--danger-soft); }

.note-box {
    display: flex;
    gap: 9px;
    margin-top: 14px;
    padding: 11px;
    border: 1px solid var(--border);
    border-radius: 8px;
    background: var(--surface-soft);
    color: var(--muted);
    font-size: 9px;
    line-height: 1.55;
}

.pipeline-wrap {
    display: grid;
    grid-template-columns: 1fr auto 1fr auto 1fr auto 1fr auto 1fr;
    align-items: center;
    gap: 8px;
    margin-top: 18px;
}

.pipeline-card {
    min-height: 148px;
    padding: 15px;
    border: 1px solid var(--border);
    border-radius: 10px;
    background: white;
}

.pipeline-card.review {
    border-color: rgba(196,122,8,.35);
    background: var(--review-soft);
}

.pipeline-icon {
    width: 36px;
    height: 36px;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 9px;
    background: var(--primary-soft);
    color: var(--primary);
    font-size: 17px;
}

.pipeline-card.review .pipeline-icon {
    background: var(--review);
    color: white;
}

.pipeline-name {
    color: var(--text);
    font-size: 12px;
    font-weight: 800;
    margin-top: 12px;
}

.pipeline-desc {
    color: var(--muted);
    font-size: 9px;
    line-height: 1.4;
    min-height: 27px;
    margin-top: 3px;
}

.pipeline-status {
    color: var(--success);
    font-size: 8px;
    font-weight: 800;
    text-transform: uppercase;
    margin-top: 12px;
}

.pipeline-card.review .pipeline-status {
    color: var(--review);
}

.pipeline-arrow {
    color: var(--primary);
    font-size: 18px;
    font-weight: 800;
}

.action-list {
    margin-top: 15px;
}

.action-row {
    display: flex;
    gap: 10px;
    align-items: flex-start;
    padding: 10px 0;
    border-bottom: 1px solid var(--border);
}

.action-number {
    width: 25px;
    height: 25px;
    flex: 0 0 25px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    background: var(--review-soft);
    color: var(--review);
    border: 1px solid rgba(196,122,8,.25);
    font-size: 9px;
    font-weight: 800;
}

.action-text {
    color: var(--text);
    font-size: 11px;
    font-weight: 600;
    padding-top: 4px;
}

.evidence-row {
    display: flex;
    gap: 10px;
    align-items: center;
    padding: 11px 0;
    border-bottom: 1px solid var(--border);
}

.evidence-icon {
    width: 34px;
    height: 34px;
    border-radius: 8px;
    background: var(--surface-soft);
    color: var(--primary);
    display: flex;
    align-items: center;
    justify-content: center;
}

.evidence-name {
    color: var(--text);
    font-size: 10px;
    font-weight: 800;
}

.evidence-detail {
    color: var(--muted);
    font-size: 9px;
    margin-top: 2px;
}

.evidence-check {
    margin-left: auto;
    color: var(--success);
    font-size: 15px;
}

.footer {
    margin-top: 30px;
    padding: 18px 0;
    border-top: 1px solid var(--border);
    display: flex;
    justify-content: space-between;
    gap: 15px;
    color: var(--muted);
    font-size: 9px;
}

@media (max-width: 1100px) {
    .kpi-grid { grid-template-columns: repeat(2, 1fr); }
    .fairness-grid { grid-template-columns: 1fr; }
    .pipeline-wrap {
        grid-template-columns: 1fr;
    }
    .pipeline-arrow {
        transform: rotate(90deg);
        justify-self: center;
    }
    .status-grid { grid-template-columns: 1fr; }
    .status-main { border-right: 0; border-bottom: 1px solid rgba(196,122,8,.18); }
}

@media (max-width: 650px) {
    .kpi-grid { grid-template-columns: 1fr; }
    .section-shell { padding: 16px; }
    .footer { flex-direction: column; }
}
</style>
""",
    unsafe_allow_html=True,
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    st.html(
        """
        <div class="sidebar-brand">
            <span class="sidebar-icon">⚖</span>
            <span>
                <span class="sidebar-kicker">Responsible AI</span><br>
                <span class="sidebar-title">Governance Toolkit</span>
            </span>
        </div>
        """,
    
    )

    st.markdown("### Dashboard")
    st.caption("AI/ML assurance workspace")

    nav = [
        ("📋", "Baseline Comparison", "#baseline"),
        ("🔍", "Confidence & Evidence", "#confidence"),
        ("⚡", "Exception Handling", "#exceptions"),
        ("🚦", "Deployment Controls", "#deployment"),
        ("📊", "Model Performance", "#performance"),
        ("⚖️", "Fairness Evaluation", "#fairness"),
        ("🧠", "Explainable AI", "#explainability"),
        ("🛡️", "GenAI Safety", "#safety"),
        ("✓", "Governance Actions", "#governance"),
    ]

    for icon, label, href in nav:
        st.html(
            f'<a href="{href}" style="display:block;color:#dfe7f7;text-decoration:none;'
            f'padding:8px 5px;font-size:12px;font-weight:600;">{icon}&nbsp;&nbsp;{label}</a>',
            )

    st.html(
        f"""
        <div class="sidebar-status">
            <div class="label">Governance status</div>
            <div class="value">{status}</div>
            <div class="desc">Human assessment required before approval.</div>
        </div>
        """,
    )

    st.markdown("")
    st.caption("Evidence loaded from project reports")
    st.caption("Academic Project • 2026")


# =========================================================
# HEADER
# =========================================================

head_left, head_right = st.columns([5, 1])

with head_left:
    st.html(
        """
        <div class="page-kicker">✦ AI/ML assurance workspace</div>
        <div class="page-title">Responsible AI Governance</div>
        <div class="page-subtitle">
            Equity, Explainability, Performance &amp; Generative-AI Safety Monitoring
        </div>
        """,
    )

with head_right:
    st.html(
        """
        <div style="display:flex;justify-content:flex-end;margin-top:10px;">
            <div class="snapshot">
                <span class="snapshot-dot"></span>
                Evidence snapshot ready
            </div>
        </div>
        """,
    )


# =========================================================
# GOVERNANCE STATUS
# =========================================================

st.html(
    f"""
    <div class="status-banner">
        <div class="status-grid">
            <div class="status-main">
                <div class="status-icon">⚠</div>
                <div>
                    <div class="status-label">Governance status</div>
                    <div class="status-value">{status}</div>
                </div>
            </div>
            <div class="status-copy">
                <div>
                    <strong>Fairness evidence requires human review before governance approval.</strong>
                    <p>
                        The toolkit supports human oversight and does not replace human governance decisions.
                    </p>
                </div>
            </div>
        </div>
    </div>
    """,
)


# =========================================================
# KPI ROW
# =========================================================

kpis = [
    ("📐", "Model Accuracy", f"{baseline['accuracy']:.2%}", "blue"),
    ("◒", "F1 Score", f"{baseline['f1_score']:.2%}", "purple"),
    ("⚖", "Gender DP Gap", f"{gender['fairness_metrics']['demographic_parity_difference']:.4f}", "teal"),
    ("⚠", "Governance Status", status, "orange"),
]

kpi_html = '<div class="kpi-grid">'
for icon, label, value, tone in kpis:
    kpi_html += f"""
    <div class="kpi-card">
        <div class="kpi-icon {tone}">{icon}</div>
        <div class="kpi-value">{value}</div>
        <div class="kpi-label">{label}</div>
    </div>
    """
kpi_html += "</div>"
st.html(kpi_html)


# =========================================================
# BASELINE COMPARISON
# =========================================================

st.html('<div id="baseline"></div>')

fp_rate = baseline["confusion_matrix"]["false_positive"] / max(
    baseline["confusion_matrix"]["false_positive"] + baseline["confusion_matrix"]["true_negative"], 1
)
fn_rate = baseline["confusion_matrix"]["false_negative"] / max(
    baseline["confusion_matrix"]["false_negative"] + baseline["confusion_matrix"]["true_positive"], 1
)

st.html(
    f"""
    <div class="section-shell">
        <div class="section-head">
            <div class="section-title-wrap">
                <div class="section-icon">📋</div>
                <div>
                    <div class="eyebrow">BASELINE COMPARISON</div>
                    <div class="section-title">Baseline reference</div>
                    <div class="section-desc">Single-model evaluation. No second model was trained. Metrics reflect the Logistic Regression baseline only.</div>
                </div>
            </div>
        </div>

        <div class="fairness-grid">
            <div class="inner-card">
                <div class="inner-title">Logistic Regression — Baseline Reference</div>
                <div class="inner-desc" style="margin-bottom:4px;">Current approach · Test set · n = {baseline['testing_rows']}</div>
                <div class="group-table">
                    <div class="group-head">Metric</div>
                    <div class="group-head" style="text-align:center;">Value</div>
                    <div class="group-head" style="text-align:center;">Assessment</div>
                    <div class="group-name">Accuracy</div>
                    <div class="group-value">{baseline['accuracy']:.2%}</div>
                    <div class="group-value">Acceptable</div>
                    <div class="group-name">Precision</div>
                    <div class="group-value">{baseline['precision']:.2%}</div>
                    <div class="group-value">Acceptable</div>
                    <div class="group-name">Recall</div>
                    <div class="group-value">{baseline['recall']:.2%}</div>
                    <div class="group-value">Strong</div>
                    <div class="group-name">F1 Score</div>
                    <div class="group-value">{baseline['f1_score']:.2%}</div>
                    <div class="group-value">Acceptable</div>
                    <div class="group-name">False Positive Rate</div>
                    <div class="group-value">{fp_rate:.2%}</div>
                    <div class="group-value">Monitor</div>
                    <div class="group-name">False Negative Rate</div>
                    <div class="group-value">{fn_rate:.2%}</div>
                    <div class="group-value">Low</div>
                </div>
            </div>

            <div class="inner-card">
                <div class="inner-title">Trade-offs and findings</div>
                <div class="inner-desc">What the baseline establishes and what remains required</div>
                <div class="action-list">
                    <div class="action-row">
                        <div class="action-number">1</div>
                        <div class="action-text">High recall ({baseline['recall']:.0%}) minimises missed approvals but produces a false positive rate of {fp_rate:.0%}, meaning some ineligible cases are approved.</div>
                    </div>
                    <div class="action-row">
                        <div class="action-number">2</div>
                        <div class="action-text">Predictive performance alone is insufficient for governance approval. Fairness, explainability and GenAI safety evidence are also required.</div>
                    </div>
                    <div class="action-row">
                        <div class="action-number">3</div>
                        <div class="action-text">Demographic parity gaps (gender: {gender['fairness_metrics']['demographic_parity_difference']:.4f}, education: {education['fairness_metrics']['demographic_parity_difference']:.4f}) were identified and require human review before approval.</div>
                    </div>
                    <div class="action-row">
                        <div class="action-number">4</div>
                        <div class="action-text">A single baseline model is evaluated. Comparison against an alternative model is outside the current project scope.</div>
                    </div>
                </div>
                <div class="note-box">
                    🏛 <span>Governance status is <strong>{status}</strong>. Performance metrics satisfy the predictive threshold, but fairness evidence requires human review before this model can be approved for deployment.</span>
                </div>
            </div>
        </div>
    </div>
    """,
)


# =========================================================
# CONFIDENCE & EVIDENCE
# =========================================================

st.html('<div id="confidence"></div>')

evidence_states = [
    (
        "📊",
        "Performance Evidence",
        "baseline_metrics.json",
        "CONFIRMED",
        "success",
        "✓",
    ),
    (
        "⚖",
        "Fairness Evidence",
        "gender_fairness_metrics.json · education_fairness_metrics.json",
        "REVIEW REQUIRED",
        "review",
        "⚠",
    ),
    (
        "🧠",
        "Explainability Evidence",
        "explainability_results.json",
        "CONFIRMED",
        "success",
        "✓",
    ),
    (
        "🛡",
        "GenAI Safety Evidence",
        "genai_safety_results.json",
        "CONTROLLED REVIEW",
        "teal",
        "◎",
    ),
]

rows_html = ""
for icon, name, source, state, tone, marker in evidence_states:
    chip_class = (
        "chip-safe" if tone == "success"
        else "chip-review" if tone == "review"
        else "safety-chip"
    )
    chip_color = (
        "var(--success)" if tone == "success"
        else "var(--review)" if tone == "review"
        else "var(--teal)"
    )
    chip_bg = (
        "var(--success-soft)" if tone == "success"
        else "var(--review-soft)" if tone == "review"
        else "var(--teal-soft)"
    )
    rows_html += f"""
    <div class="evidence-row">
        <div class="evidence-icon">{icon}</div>
        <div style="flex:1;">
            <div class="evidence-name">{name}</div>
            <div class="evidence-detail">{source}</div>
        </div>
        <div style="display:inline-flex;align-items:center;gap:5px;padding:5px 10px;
                    border-radius:999px;font-size:9px;font-weight:800;
                    color:{chip_color};background:{chip_bg};white-space:nowrap;">
            {marker} {state}
        </div>
    </div>
    """

st.html(
    f"""
    <div class="section-shell">
        <div class="section-head">
            <div class="section-title-wrap">
                <div class="section-icon">🔍</div>
                <div>
                    <div class="eyebrow">CONFIDENCE &amp; EVIDENCE</div>
                    <div class="section-title">Evidence states</div>
                    <div class="section-desc">Governance component coverage across all evaluation reports.</div>
                </div>
            </div>
        </div>
        <div class="inner-card">
            {rows_html}
            <div class="note-box">
                ℹ <span>Evidence states indicate whether the governance component has supporting
                evaluation evidence; they are not statistical confidence scores.</span>
            </div>
        </div>
    </div>
    """,
)


# =========================================================
# EXCEPTION HANDLING
# =========================================================

st.html('<div id="exceptions"></div>')

exceptions = [
    (
        "⚖",
        "Fairness threshold exceeded",
        "Gender and education fairness reports",
        "REVIEW",
        "review",
        "Human review required",
    ),
    (
        "🛡",
        "GenAI ambiguous / incomplete case",
        "genai_safety_results.json",
        "REVIEW",
        "review",
        "Require additional context before approval",
    ),
    (
        "🚫",
        "High-risk GenAI request",
        "genai_safety_results.json",
        "BLOCK",
        "danger",
        "Prevent unsafe decision and escalate for review",
    ),
    (
        "📂",
        "Missing / incomplete evidence",
        "One or more required report files absent",
        "INCOMPLETE",
        "muted",
        "Do not approve deployment until required evidence is available",
    ),
]

exc_rows = ""
for icon, title, source, state, tone, action in exceptions:
    state_color = (
        "var(--review)" if tone == "review"
        else "var(--danger)" if tone == "danger"
        else "var(--muted)"
    )
    state_bg = (
        "var(--review-soft)" if tone == "review"
        else "var(--danger-soft)" if tone == "danger"
        else "var(--surface-soft)"
    )
    marker = "⚠" if tone == "review" else ("✕" if tone == "danger" else "○")
    exc_rows += f"""
    <div class="evidence-row">
        <div class="evidence-icon">{icon}</div>
        <div style="flex:1;">
            <div class="evidence-name">{title}</div>
            <div class="evidence-detail">{source}</div>
            <div class="evidence-detail" style="margin-top:3px;font-style:italic;">Action: {action}</div>
        </div>
        <div style="display:inline-flex;align-items:center;gap:5px;padding:5px 10px;
                    border-radius:999px;font-size:9px;font-weight:800;
                    color:{state_color};background:{state_bg};white-space:nowrap;">
            {marker} {state}
        </div>
    </div>
    """

st.html(
    f"""
    <div class="section-shell">
        <div class="section-head">
            <div class="section-title-wrap">
                <div class="section-icon">⚡</div>
                <div>
                    <div class="eyebrow">EXCEPTION HANDLING</div>
                    <div class="section-title">Governance exception states</div>
                    <div class="section-desc">Defined exception routes and the governance action each triggers.</div>
                </div>
            </div>
        </div>
        <div class="inner-card">
            {exc_rows}
            <div class="note-box">
                ⚡ <span>Exceptions do not automatically approve or reject a system.
                They route the case to the appropriate governance action and human review state.</span>
            </div>
        </div>
    </div>
    """,
)


# =========================================================
# DEPLOYMENT CONTROLS
# =========================================================

st.html('<div id="deployment"></div>')

controls = [
    ("⚖",  "Fairness review",           "Human review before deployment when fairness thresholds are exceeded.",          "REQUIRED",     "review"),
    ("🧠",  "Explainability evidence",   "Review the documented feature-level explanation evidence before deployment.",    "REQUIRED",     "review"),
    ("🛡",  "GenAI safety testing",      "Block high-risk requests and review ambiguous or incomplete cases.",             "REQUIRED",     "review"),
    ("📂",  "Evidence completeness",     "Do not approve deployment when required governance evidence is missing.",         "REQUIRED",     "review"),
    ("🏛",  "Governance approval",       "Final deployment decision remains subject to documented governance review.",      "HUMAN REVIEW", "orange"),
]

ctrl_rows = ""
for icon, title, control, state, tone in controls:
    state_color = "var(--review)" if tone in ("review", "orange") else "var(--muted)"
    state_bg    = "var(--review-soft)" if tone in ("review", "orange") else "var(--surface-soft)"
    marker      = "⚠" if tone == "orange" else "✓"
    ctrl_rows += f"""
    <div class="evidence-row">
        <div class="evidence-icon">{icon}</div>
        <div style="flex:1;">
            <div class="evidence-name">{title}</div>
            <div class="evidence-detail">{control}</div>
        </div>
        <div style="display:inline-flex;align-items:center;gap:5px;padding:5px 10px;
                    border-radius:999px;font-size:9px;font-weight:800;
                    color:{state_color};background:{state_bg};white-space:nowrap;">
            {marker} {state}
        </div>
    </div>
    """

st.html(
    f"""
    <div class="section-shell">
        <div class="section-head">
            <div class="section-title-wrap">
                <div class="section-icon">🚦</div>
                <div>
                    <div class="eyebrow">DEPLOYMENT CONTROLS</div>
                    <div class="section-title">Release conditions</div>
                    <div class="section-desc">Human-review gates that must be satisfied before deployment.</div>
                </div>
            </div>
        </div>
        <div class="inner-card">
            {ctrl_rows}
            <div class="note-box">
                🚦 <span>Deployment controls define release conditions and human-review gates;
                they do not replace human accountability.</span>
            </div>
        </div>
    </div>
    """,
)


# =========================================================
# PERFORMANCE
# =========================================================

st.html('<div id="performance"></div>')
st.html(
    """
    <div class="section-shell">
        <div class="section-head">
            <div class="section-title-wrap">
                <div class="section-icon">◔</div>
                <div>
                    <div class="eyebrow">MODEL PERFORMANCE</div>
                    <div class="section-title">Performance overview</div>
                    <div class="section-desc">Evaluation results from the held-out test set.</div>
                </div>
            </div>
        </div>
    """,
)

perf_col, matrix_col = st.columns([1.35, .65])

with perf_col:
    metrics = [
        ("Accuracy", baseline["accuracy"] * 100, ""),
        ("Precision", baseline["precision"] * 100, ""),
        ("Recall", baseline["recall"] * 100, "purple-fill"),
        ("F1 Score", baseline["f1_score"] * 100, "teal-fill"),
    ]

    html = '<div class="inner-card"><div class="inner-title">Core evaluation metrics</div><div class="inner-desc">Percentage scores across the test set</div>'
    for label, value, extra in metrics:
        html += f"""
        <div class="bar-row">
            <div class="bar-top"><span>{label}</span><span>{value:.2f}%</span></div>
            <div class="bar-track"><div class="bar-fill {extra}" style="width:{value:.2f}%"></div></div>
        </div>
        """
    html += f"""
        <div class="data-stat-row">
            <div class="data-stat"><div class="value">{baseline['dataset_rows']}</div><div class="label">Total rows</div></div>
            <div class="data-stat"><div class="value">{baseline['training_rows']}</div><div class="label">Training</div></div>
            <div class="data-stat"><div class="value">{baseline['testing_rows']}</div><div class="label">Testing</div></div>
        </div></div>
    """
    st.html(html)

with matrix_col:
    cm = baseline["confusion_matrix"]
    st.html(
        f"""
        <div class="inner-card">
            <div class="inner-title">Confusion matrix</div>
            <div class="inner-desc">Predicted outcomes versus actual labels</div>
            <div class="matrix">
                <div></div><div class="matrix-head">Pred. 0</div><div class="matrix-head">Pred. 1</div>
                <div class="matrix-side">Actual 0</div>
                <div class="matrix-cell matrix-tn"><span class="number">{cm['true_negative']}</span><span class="code">TN</span></div>
                <div class="matrix-cell matrix-fp"><span class="number">{cm['false_positive']}</span><span class="code">FP</span></div>
                <div class="matrix-side">Actual 1</div>
                <div class="matrix-cell matrix-fn"><span class="number">{cm['false_negative']}</span><span class="code">FN</span></div>
                <div class="matrix-cell matrix-tp"><span class="number">{cm['true_positive']}</span><span class="code">TP</span></div>
            </div>
            <div style="display:flex;justify-content:space-between;border-top:1px solid #dfe5ef;margin-top:15px;padding-top:12px;color:#65718a;font-size:9px;">
                <span>Logistic Regression</span><b style="color:#17213b;">n = {baseline['testing_rows']}</b>
            </div>
        </div>
        """,
    )

st.html("</div>")


# =========================================================
# FAIRNESS
# =========================================================

st.html('<div id="fairness"></div>')
st.html(
    """
    <div class="section-shell">
        <div class="section-head">
            <div class="section-title-wrap">
                <div class="section-icon">⚖</div>
                <div>
                    <div class="eyebrow">FAIRNESS EVALUATION</div>
                    <div class="section-title">Subgroup evidence</div>
                    <div class="section-desc">Neutral comparison of observed performance and selection outcomes.</div>
                </div>
            </div>
            <span class="review-badge">⚠ REVIEW</span>
        </div>
    """,
)


def fairness_panel(title, icon, metrics, parity, odds):
    rows = ""
    for group, values in metrics.items():
        rows += f"""
            <div class="group-name">{group}</div>
            <div class="group-value">{values['accuracy']:.2%}</div>
            <div class="group-value">{values['selection_rate']:.2%}</div>
        """

    return f"""
    <div class="inner-card">
        <div style="display:flex;align-items:center;gap:8px;">
            <span style="color:#3974d8;font-size:17px;">{icon}</span>
            <span class="inner-title">{title}</span>
            <span style="margin-left:auto;color:#65718a;font-size:9px;">Observed values</span>
        </div>
        <div class="group-table">
            <div class="group-head">Group</div>
            <div class="group-head" style="text-align:center;">Accuracy</div>
            <div class="group-head" style="text-align:center;">Selection</div>
            {rows}
        </div>
        <div class="evidence-grid">
            <div class="evidence-value">
                <div class="evidence-label">Demographic Parity Difference</div>
                <div class="evidence-number">{parity:.4f}</div>
            </div>
            <div class="evidence-value">
                <div class="evidence-label">Equalized Odds Difference</div>
                <div class="evidence-number">{odds:.4f}</div>
            </div>
        </div>
    </div>
    """


gender_html = fairness_panel(
    "Gender Fairness",
    "●",
    gender["metrics"],
    gender["fairness_metrics"]["demographic_parity_difference"],
    gender["fairness_metrics"]["equalized_odds_difference"],
)

education_html = fairness_panel(
    "Education Fairness",
    "🎓",
    education["metrics"],
    education["fairness_metrics"]["demographic_parity_difference"],
    education["fairness_metrics"]["equalized_odds_difference"],
)

st.html(
    f'<div class="fairness-grid">{gender_html}{education_html}</div>',
)

st.html("</div>")


# =========================================================
# EXPLAINABILITY + GENAI SAFETY
# =========================================================

st.html('<div id="explainability"></div><div id="safety"></div>')

left, right = st.columns([1.2, .8])

with left:
    st.html(
        """
        <div class="section-shell">
            <div class="section-head">
                <div class="section-title-wrap">
                    <div class="section-icon">🧠</div>
                    <div>
                        <div class="eyebrow">EXPLAINABLE AI</div>
                        <div class="section-title">Model explainability</div>
                        <div class="section-desc">Global feature importance based on SHAP analysis.</div>
                    </div>
                </div>
            </div>
        """,
    )

    feature_df = pd.DataFrame(explainability["top_features"]).sort_values(
        "mean_absolute_shap", ascending=False
    )

    max_shap = feature_df["mean_absolute_shap"].max()
    html = '<div class="inner-card"><div class="shap-list">'
    for idx, row in feature_df.head(10).iterrows():
        width = (row["mean_absolute_shap"] / max_shap) * 100 if max_shap else 0
        strong = "strong" if row["feature"] == feature_df.iloc[0]["feature"] else ""
        label = "STRONGEST" if strong else ""
        html += f"""
        <div class="shap-row">
            <div class="shap-rank">{feature_df.index.get_loc(idx) + 1}</div>
            <div class="shap-feature">{row['feature']}</div>
            <div class="shap-track">
                <div class="shap-fill {strong}" style="width:{width:.1f}%">{label}</div>
            </div>
        </div>
        """
    html += "</div></div>"
    st.html(html)

    st.html(
        """
        <div class="note-box">
            🔎 <span>SHAP values provide feature-level evidence for model behavior.
            They support interpretation of the model but do not establish causality.</span>
        </div>
        </div>
        """,
    )

with right:
    st.html(
        """
        <div class="section-shell">
            <div class="section-head">
                <div class="section-title-wrap">
                    <div class="section-icon">🛡</div>
                    <div>
                        <div class="eyebrow">GENAI SAFETY</div>
                        <div class="section-title">Safety test outcomes</div>
                        <div class="section-desc">Rule-based evaluation against predefined expectations.</div>
                    </div>
                </div>
            </div>
        """,
    )

    summary = genai["summary"]
    safe_count = sum(1 for x in genai["results"] if x["actual_status"] == "SAFE")
    review_count = sum(1 for x in genai["results"] if x["actual_status"] == "REVIEW")
    block_count = sum(1 for x in genai["results"] if x["actual_status"] == "BLOCK")
    total = max(summary["total_cases"], 1)

    st.html(
        f"""
        <div class="inner-card">
            <div class="safety-big">
                <div>
                    <div class="safety-score">{summary['pass_rate']:.0%}</div>
                    <div class="safety-label">Expectation pass rate</div>
                </div>
                <div class="safety-count">
                    <div class="number">{summary['passed_cases']} / {summary['total_cases']}</div>
                    <div class="label">tests matched</div>
                </div>
            </div>

            <div class="safety-bar">
                <div class="safe-part" style="width:{safe_count/total*100:.1f}%"></div>
                <div class="review-part" style="width:{review_count/total*100:.1f}%"></div>
                <div class="block-part" style="width:{block_count/total*100:.1f}%"></div>
            </div>

            <div class="safety-legend">
                <div class="safety-chip chip-safe"><div class="number">{safe_count}</div><div class="label">Safe</div></div>
                <div class="safety-chip chip-review"><div class="number">{review_count}</div><div class="label">Review</div></div>
                <div class="safety-chip chip-block"><div class="number">{block_count}</div><div class="label">Block</div></div>
            </div>

            <div class="note-box">
                🔒 <span>Results represent agreement with predefined safety test expectations.
                This does not prove real-world AI safety.</span>
            </div>
        </div>
        """,
    )

    st.html("</div>")


# =========================================================
# EVIDENCE PIPELINE
# =========================================================

st.html(
    """
    <div class="section-shell">
        <div class="section-head">
            <div class="section-title-wrap">
                <div class="section-icon">▱</div>
                <div>
                    <div class="eyebrow">EVIDENCE FLOW</div>
                    <div class="section-title">Governance evidence pipeline</div>
                    <div class="section-desc">A traceable path from technical evaluation to accountable human review.</div>
                </div>
            </div>
        </div>

        <div class="pipeline-wrap">
    """,
)

pipeline = [
    ("📊", "Performance", "Quality metrics evaluated", "Complete", False),
    ("⚖", "Fairness", "Subgroups compared", "Review", True),
    ("🧠", "Explainability", "SHAP evidence ranked", "Complete", False),
    ("🛡", "GenAI Safety", "8 expectations tested", "Complete", False),
    ("🏛", "Governance", "Human decision required", "Review", True),
]

parts = []
for i, (icon, title, desc, stage_status, review) in enumerate(pipeline):
    parts.append(
        f"""
        <div class="pipeline-card {'review' if review else ''}">
            <div class="pipeline-icon">{icon}</div>
            <div class="pipeline-name">{title}</div>
            <div class="pipeline-desc">{desc}</div>
            <div class="pipeline-status">{'⚠' if review else '✓'} {stage_status}</div>
        </div>
        """
    )
    if i < len(pipeline) - 1:
        parts.append('<div class="pipeline-arrow">→</div>')

st.html("".join(parts) + "</div></div>")


# =========================================================
# GOVERNANCE ACTIONS + EVIDENCE REGISTER
# =========================================================

st.html('<div id="governance"></div>')

st.html(
    """
    <div class="section-shell">
        <div class="section-head">
            <div class="section-title-wrap">
                <div class="section-icon">✓</div>
                <div>
                    <div class="eyebrow">GOVERNANCE ACTIONS</div>
                    <div class="section-title">Human review workspace</div>
                    <div class="section-desc">Required actions and the evidence supporting the governance decision.</div>
                </div>
            </div>
            <span class="review-badge">⚠ REVIEW</span>
        </div>
    """,
)

actions = governance.get("governance_actions", [])

action_html = '<div class="action-list">'
for i, action in enumerate(actions, 1):
    action_html += f"""
    <div class="action-row">
        <div class="action-number">{i}</div>
        <div class="action-text">{action}</div>
    </div>
    """
action_html += """
    <div style="margin-top:14px;color:#c47a08;font-size:9px;font-weight:800;text-transform:uppercase;">
        ⚠ Decision pending human review
    </div>
"""
action_html += "</div>"

evidence_items = [
    ("📊", "Performance metrics", "Accuracy, precision, recall, F1"),
    ("⚖", "Fairness metrics", "Gender and education comparisons"),
    ("🧠", "SHAP analysis", "Global feature importance"),
    ("🔒", "GenAI safety tests", "8 predefined expectations"),
]

evidence_html = '<div class="inner-card"><div class="inner-title">Evidence register</div><div class="inner-desc">Sources supporting the governance assessment</div>'
for icon, name, detail in evidence_items:
    evidence_html += f"""
    <div class="evidence-row">
        <div class="evidence-icon">{icon}</div>
        <div>
            <div class="evidence-name">{name}</div>
            <div class="evidence-detail">{detail}</div>
        </div>
        <div class="evidence-check">✓</div>
    </div>
    """
evidence_html += "</div>"

action_col, evidence_col = st.columns([.85, 1.15])

with action_col:
    st.html(
        f'<div class="inner-card"><div class="inner-title">Required review actions</div>{action_html}</div>',
    )

with evidence_col:
    st.html(evidence_html)

st.html("</div>")


# =========================================================
# ABOUT + FOOTER
# =========================================================

st.html(
    """
    <div class="section-shell">
        <div class="section-title">About This Toolkit</div>
        <div class="section-desc" style="font-size:11px;line-height:1.7;margin-top:10px;">
            This dashboard integrates model performance, subgroup fairness,
            SHAP explainability and controlled Generative-AI safety testing
            into an evidence-based governance workflow.
            <br><br>
            <strong style="color:#17213b;">Governance principle:</strong>
            Automated checks support human review; they do not replace human decision-making.
        </div>
    </div>

    <div class="footer">
        <span>Responsible AI Equity Monitoring and Model Governance Toolkit</span>
        <span>Decision support for human oversight • Logistic Regression • 614 rows</span>
    </div>
    """,
)
