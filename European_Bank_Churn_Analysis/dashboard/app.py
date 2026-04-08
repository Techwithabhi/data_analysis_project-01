import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import warnings
warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ChurnSight | European Banking Analytics",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────────────
#  PREMIUM CSS
# ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.stApp {
    background: linear-gradient(135deg, #080c18 0%, #0c1220 50%, #0a1020 100%);
}

/* Hide streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1rem; padding-bottom: 2rem; }

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0b1120 0%, #0d1525 100%);
    border-right: 1px solid rgba(108,99,255,0.2);
}
section[data-testid="stSidebar"] * { color: #c8d0e8 !important; }
section[data-testid="stSidebar"] .stMarkdown p { color: #8a94b2 !important; }

/* ── Top banner ── */
.top-banner {
    background: linear-gradient(120deg,
        rgba(108,99,255,0.15) 0%,
        rgba(0,212,170,0.08) 60%,
        rgba(255,107,107,0.06) 100%);
    border: 1px solid rgba(108,99,255,0.3);
    border-radius: 18px;
    padding: 1.6rem 2.2rem;
    margin-bottom: 1.4rem;
    position: relative;
    overflow: hidden;
}
.top-banner::before {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 180px; height: 180px;
    background: radial-gradient(circle, rgba(108,99,255,0.15), transparent 70%);
    border-radius: 50%;
}
.top-banner .objective-tag {
    display: inline-block;
    background: rgba(108,99,255,0.2);
    border: 1px solid rgba(108,99,255,0.4);
    border-radius: 6px;
    padding: 2px 10px;
    font-size: 0.68rem;
    color: #a78bfa;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}
.top-banner h1 {
    margin: 0 0 0.3rem;
    font-size: 1.9rem;
    font-weight: 900;
    background: linear-gradient(90deg, #6C63FF 0%, #00D4AA 60%, #FFB347 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1.2;
}
.top-banner .subtitle {
    color: #8a94b2;
    font-size: 0.84rem;
    margin: 0;
    line-height: 1.5;
}
.top-banner .objective-quote {
    margin-top: 0.8rem;
    border-left: 3px solid #6C63FF;
    padding-left: 0.9rem;
    color: #c8d0e8;
    font-size: 0.85rem;
    font-style: italic;
}

/* ── KPI Cards ── */
.kpi-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    margin-bottom: 1.5rem;
}
.kpi-card {
    background: linear-gradient(145deg, #111827, #141e30);
    border-radius: 16px;
    padding: 1.3rem 1.2rem;
    border: 1px solid rgba(255,255,255,0.06);
    position: relative;
    overflow: hidden;
    transition: transform 0.2s;
}
.kpi-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 2px;
    border-radius: 0 0 16px 16px;
}
.kpi-card.blue::after   { background: linear-gradient(90deg,#6C63FF,#818cf8); }
.kpi-card.green::after  { background: linear-gradient(90deg,#00D4AA,#34d399); }
.kpi-card.red::after    { background: linear-gradient(90deg,#FF6B6B,#f97316); }
.kpi-card.amber::after  { background: linear-gradient(90deg,#FFB347,#fbbf24); }
.kpi-icon {
    font-size: 1.6rem;
    margin-bottom: 0.5rem;
    display: block;
}
.kpi-label {
    font-size: 0.68rem;
    color: #6b7280;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-weight: 600;
}
.kpi-value {
    font-size: 2rem;
    font-weight: 900;
    color: #f0f4ff;
    margin: 0.15rem 0 0.1rem;
    line-height: 1;
}
.kpi-card.blue   .kpi-value { color: #818cf8; }
.kpi-card.green  .kpi-value { color: #00D4AA; }
.kpi-card.red    .kpi-value { color: #FF6B6B; }
.kpi-card.amber  .kpi-value { color: #FFB347; }
.kpi-sub {
    font-size: 0.73rem;
    color: #6b7280;
}
.kpi-badge {
    display: inline-block;
    font-size: 0.62rem;
    padding: 1px 7px;
    border-radius: 99px;
    font-weight: 700;
    margin-top: 0.3rem;
}
.kpi-badge.danger  { background: rgba(255,107,107,0.15); color: #FF6B6B; border: 1px solid rgba(255,107,107,0.3); }
.kpi-badge.warning { background: rgba(255,179,71,0.15);  color: #FFB347; border: 1px solid rgba(255,179,71,0.3); }
.kpi-badge.ok      { background: rgba(0,212,170,0.15);   color: #00D4AA; border: 1px solid rgba(0,212,170,0.3); }

/* ── Section headers ── */
.sec-header {
    display: flex;
    align-items: center;
    gap: 0.7rem;
    margin: 1.8rem 0 1rem;
    padding-bottom: 0.6rem;
    border-bottom: 1px solid rgba(108,99,255,0.15);
}
/* FIX: The .bar div needs explicit display and min-width so it never collapses */
.sec-header .bar {
    display: block !important;
    min-width: 4px !important;
    width: 4px !important;
    height: 24px !important;
    background: linear-gradient(180deg, #6C63FF, #00D4AA) !important;
    border-radius: 4px !important;
    flex-shrink: 0 !important;
    opacity: 1 !important;
    visibility: visible !important;
}
.sec-header h3 {
    font-size: 1rem;
    font-weight: 700;
    color: #e2e8f0;
    margin: 0;
}
.sec-header .badge {
    background: rgba(108,99,255,0.15);
    color: #a78bfa;
    font-size: 0.65rem;
    padding: 2px 8px;
    border-radius: 99px;
    border: 1px solid rgba(108,99,255,0.25);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

/* ── Insight boxes ── */
.insight-box {
    background: linear-gradient(135deg,
        rgba(108,99,255,0.10) 0%,
        rgba(0,212,170,0.06) 100%);
    border: 1px solid rgba(108,99,255,0.2);
    border-left: 3px solid #6C63FF;
    border-radius: 0 12px 12px 0;
    padding: 0.9rem 1.2rem;
    margin: 0.8rem 0;
    font-size: 0.84rem;
    color: #c8d0e8;
    line-height: 1.6;
}
.insight-box .tag {
    font-size: 0.65rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #6C63FF;
    display: block;
    margin-bottom: 0.3rem;
}
.insight-box strong { color: #00D4AA; }
.insight-box .critical { color: #FF6B6B; font-weight: 700; }

/* ── Recommendation cards ── */
.reco-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.9rem;
    margin-top: 0.8rem;
}
.reco-card {
    background: linear-gradient(135deg, #111827, #141e30);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 14px;
    padding: 1.1rem 1.2rem;
    display: flex;
    gap: 0.8rem;
    align-items: flex-start;
}
.reco-icon { font-size: 1.4rem; flex-shrink: 0; margin-top: 2px; }
.reco-title { font-size: 0.85rem; font-weight: 700; color: #e2e8f0; margin-bottom: 0.2rem; }
.reco-desc  { font-size: 0.77rem; color: #6b7280; line-height: 1.5; }

/* ── Takeaway cards ── */
.takeaway-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.8rem;
}
.takeaway-item {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 10px;
    padding: 0.8rem 1rem;
    display: flex;
    gap: 0.7rem;
    align-items: center;
    font-size: 0.82rem;
    color: #c8d0e8;
}
.takeaway-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
}

/* ── Project Info Card in Sidebar ── */
.project-info-card {
    background: linear-gradient(145deg, rgba(108,99,255,0.08), rgba(0,212,170,0.04));
    border: 1px solid rgba(108,99,255,0.2);
    border-radius: 14px;
    padding: 1rem 1.1rem;
    margin-top: 0.6rem;
}
.project-info-title {
    font-size: 0.62rem !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.12em !important;
    color: #6b7280 !important;
    margin-bottom: 0.9rem !important;
    display: block;
}
.project-info-row {
    margin-bottom: 0.75rem;
}
.project-info-label {
    font-size: 0.6rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.1em !important;
    color: #4b5563 !important;
    font-weight: 600 !important;
    display: block;
    margin-bottom: 0.2rem;
}
.project-info-link {
    font-size: 0.82rem !important;
    font-weight: 700 !important;
    color: #818cf8 !important;
    text-decoration: none !important;
    display: flex !important;
    align-items: center !important;
    gap: 0.3rem !important;
    transition: color 0.2s !important;
}
.project-info-link:hover {
    color: #00D4AA !important;
}
.project-info-link .arrow {
    font-size: 0.7rem;
    opacity: 0.7;
}
.project-info-divider {
    border: none;
    border-top: 1px solid rgba(108,99,255,0.12);
    margin: 0.6rem 0;
}

/* ── Streamlit overrides ── */
div[data-baseweb="select"] > div {
    background: #111827 !important;
    border-color: rgba(108,99,255,0.25) !important;
    color: #c8d0e8 !important;
    border-radius: 8px !important;
}
.stMultiSelect [data-baseweb="tag"] {
    background: rgba(108,99,255,0.3) !important;
}
div[data-testid="stMetric"] {
    background: transparent !important;
}
button[data-baseweb="tab"] {
    background: transparent !important;
    color: #6b7280 !important;
    font-weight: 500;
    font-size: 0.87rem;
}
button[data-baseweb="tab"][aria-selected="true"] {
    color: #818cf8 !important;
    border-bottom-color: #6C63FF !important;
}
div[data-testid="stDataFrame"] {
    border-radius: 10px;
    overflow: hidden;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
#  PLOTLY THEME
# ─────────────────────────────────────────────────────────────
T = dict(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter", color="#8a94b2", size=11),
    margin=dict(t=44, b=36, l=40, r=24),
    title_font=dict(size=13, color="#e2e8f0", family="Inter"),
)
PAL = ["#6C63FF", "#00D4AA", "#FF6B6B", "#FFB347", "#818cf8",
       "#06b6d4", "#f97316", "#a78bfa", "#34d399", "#fb7185"]

def sfig(fig, xtitle="", ytitle=""):
    fig.update_layout(**T)
    if xtitle: fig.update_xaxes(title_text=xtitle)
    if ytitle: fig.update_yaxes(title_text=ytitle)
    fig.update_xaxes(showgrid=False, zeroline=False, color="#6b7280")
    fig.update_yaxes(showgrid=True, gridcolor="rgba(255,255,255,0.04)",
                     zeroline=False, color="#6b7280")
    return fig

# ─────────────────────────────────────────────────────────────
#  DATA LOADER
# ─────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    for fname in ["bank_churn.csv", "Churn_Modelling.csv",
                  "churn.csv", "data.csv"]:
        try:
            df = pd.read_csv(fname)
            df.columns = [c.strip() for c in df.columns]
            if "Exited" in df.columns and "Geography" in df.columns:
                break
        except FileNotFoundError:
            continue
    else:
        np.random.seed(2024)
        n = 10000
        geo = np.random.choice(["France","Spain","Germany"], n, p=[0.50,0.25,0.25])
        age = np.concatenate([
            np.random.randint(18, 30, int(n * 0.18)),
            np.random.randint(30, 45, int(n * 0.38)),
            np.random.randint(45, 60, int(n * 0.30)),
            np.random.randint(60, 92, int(n * 0.14)),
        ])
        if len(age) < n:
            age = np.append(age, np.random.randint(18, 92, n - len(age)))
        age = age[:n]
        np.random.shuffle(age)
        tenure  = np.random.randint(0, 11, n)
        balance = np.where(np.random.rand(n) < 0.28, 0,
                           np.random.uniform(8000, 260000, n))
        credit  = np.random.randint(350, 851, n)
        nprods  = np.random.choice([1,2,3,4], n, p=[0.46,0.46,0.05,0.03])
        has_cc  = np.random.choice([0,1], n, p=[0.29,0.71])
        active  = np.random.choice([0,1], n, p=[0.485,0.515])
        salary  = np.random.uniform(10000, 200001, n)
        gender  = np.random.choice(["Male","Female"], n)
        base = np.full(n, 0.12)
        base += np.where(geo == "Germany", 0.18, 0.02)
        base += np.where(active == 0, 0.10, -0.02)
        base += np.where((age >= 45) & (age < 60), 0.30, 0.0)
        base += np.where(age >= 60, 0.14, 0.0)
        base += np.where((age >= 30) & (age < 45), 0.02, 0.0)
        base += np.where(age < 30, -0.06, 0.0)
        base += np.where(nprods >= 3, 0.12, 0.0)
        base += np.where(balance == 0, -0.04, 0.0)
        base = np.clip(base, 0.02, 0.85)
        exited = np.random.binomial(1, base)
        df = pd.DataFrame({
            "CustomerId": range(15634000, 15634000+n),
            "Surname": [f"S_{i}" for i in range(n)],
            "CreditScore": credit,
            "Geography": geo,
            "Gender": gender,
            "Age": age,
            "Tenure": tenure,
            "Balance": balance.round(2),
            "NumOfProducts": nprods,
            "HasCrCard": has_cc,
            "IsActiveMember": active,
            "EstimatedSalary": salary.round(2),
            "Exited": exited,
        })

    df["AgeGroup"] = pd.cut(
        df["Age"],
        bins=[0, 29, 44, 59, 120],
        labels=["Young (<30)", "Mid (30–44)", "Senior (45–59)", "Elder (60+)"]
    )
    df["TenureGroup"] = pd.cut(
        df["Tenure"],
        bins=[-1, 2, 6, 10],
        labels=["New (0–2y)", "Mid-term (3–6y)", "Long-term (7+y)"]
    )
    df["CreditBand"] = pd.cut(
        df["CreditScore"],
        bins=[0, 579, 719, 850],
        labels=["Low (<580)", "Medium (580–719)", "High (720+)"]
    )
    df["BalanceSegment"] = pd.cut(
        df["Balance"],
        bins=[-1, 0, 75000, 1e9],
        labels=["Zero Balance", "Low Balance", "High Balance"]
    )
    df["ActivityLabel"] = df["IsActiveMember"].map({0: "Inactive", 1: "Active"})
    return df


# ─────────────────────────────────────────────────────────────
#  SIDEBAR FILTERS
# ─────────────────────────────────────────────────────────────
def render_sidebar(df):
    with st.sidebar:
        st.markdown("""
        <div style="text-align:center;padding:1rem 0 0.5rem;">
            <div style="font-size:2rem;">🏦</div>
            <div style="font-size:1.1rem;font-weight:800;
                        background:linear-gradient(90deg,#6C63FF,#00D4AA);
                        -webkit-background-clip:text;-webkit-text-fill-color:transparent;">
                ChurnSight
            </div>
            <div style="font-size:0.68rem;color:#6b7280;
                        text-transform:uppercase;letter-spacing:0.1em;margin-top:2px;">
                European Banking · 2026
            </div>
        </div>
        <hr style="border:none;border-top:1px solid rgba(108,99,255,0.2);margin:0.8rem 0;">
        """, unsafe_allow_html=True)

        st.markdown("**🔍 Segment Filters**")

        geo = st.multiselect(
            "Geography",
            options=sorted(df["Geography"].unique().tolist()),
            default=sorted(df["Geography"].unique().tolist()),
        )
        age_g = st.multiselect(
            "Age Group",
            options=df["AgeGroup"].cat.categories.tolist(),
            default=df["AgeGroup"].cat.categories.tolist(),
        )
        credit_b = st.multiselect(
            "Credit Band",
            options=df["CreditBand"].cat.categories.tolist(),
            default=df["CreditBand"].cat.categories.tolist(),
        )

        st.markdown("<hr style='border:none;border-top:1px solid rgba(108,99,255,0.2);margin:0.8rem 0;'>",
                    unsafe_allow_html=True)
        st.markdown("**💎 High-Value Threshold**")
        hv_pct = st.slider("Top Balance % (High-Value)", 50, 95, 75, step=5)

        # ── PROJECT INFO SECTION ──
        st.markdown("<hr style='border:none;border-top:1px solid rgba(108,99,255,0.2);margin:1rem 0 0.6rem;'>",
                    unsafe_allow_html=True)

        
        st.markdown(
        "<div style='margin-top:4px; padding:12px 14px; background:#131726; border-radius:10px; border:1px solid #252d45;'>"
        "<p style='margin:0 0 10px 0; font-size:0.6rem; letter-spacing:0.12em; color:#3d85ff; text-transform:uppercase; font-family:monospace; border-bottom:1px solid #252d45; padding-bottom:8px;'>Project Info</p>"
        "<p style='margin:0 0 2px 0; font-size:0.58rem; color:#7a86a1; text-transform:uppercase; letter-spacing:0.08em;'>Organization</p>"
        "<p style='margin:0 0 10px 0;'><a href='https://unifiedmentor.com/' target='_blank' style='color:#e2e8f5; font-size:0.8rem; font-weight:600; text-decoration:none;'>Unified Mentor &#8599;</a></p>"
        "<p style='margin:0 0 2px 0; font-size:0.58rem; color:#7a86a1; text-transform:uppercase; letter-spacing:0.08em;'>Instructor</p>"
        "<p style='margin:0 0 10px 0;'><a href='https://saikagne.github.io/' target='_blank' style='color:#e2e8f5; font-size:0.8rem; font-weight:600; text-decoration:none;'>Saiprasad Kagne &#8599;</a></p>"
        "<p style='margin:0 0 2px 0; font-size:0.58rem; color:#7a86a1; text-transform:uppercase; letter-spacing:0.08em;'>Analyst</p>"
        "<p style='margin:0;'><a href='https://techwithabhi.github.io/' target='_blank' style='color:#3d85ff; font-size:0.8rem; font-weight:600; text-decoration:none;'>Abhi Sarkar &#8599;</a></p>"
        "</div>",
        unsafe_allow_html=True)


    return dict(geo=geo, age_g=age_g, credit_b=credit_b, hv_pct=hv_pct)


def apply_filters(df, f):
    mask = (
        df["Geography"].isin(f["geo"]) &
        df["AgeGroup"].isin(f["age_g"]) &
        df["CreditBand"].isin(f["credit_b"])
    )
    dff = df[mask].copy()
    thresh = dff["Balance"].quantile(f["hv_pct"] / 100)
    dff["HighValue"] = (dff["Balance"] > thresh).astype(int)
    return dff


# ─────────────────────────────────────────────────────────────
#  SECTION HEADER HELPER
# ─────────────────────────────────────────────────────────────
def sh(title, badge=""):
    badge_html = f'<span class="badge">{badge}</span>' if badge else ""
    st.markdown(f"""
    <div class="sec-header">
        <div class="bar"></div>
        <h3>{title}</h3>
        {badge_html}
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
#  KPI SECTION
# ─────────────────────────────────────────────────────────────
def render_kpis(dff):
    n_total    = len(dff)
    n_churned  = int(dff["Exited"].sum())
    churn_rate = dff["Exited"].mean() * 100

    hv_mask    = dff["HighValue"] == 1
    hv_churn   = dff[hv_mask]["Exited"].mean() * 100 if hv_mask.sum() else 0

    inactive_mask  = dff["IsActiveMember"] == 0
    inactive_churn = dff[inactive_mask]["Exited"].mean() * 100 if inactive_mask.sum() else 0

    st.markdown(f"""
    <div class="kpi-row">
        <div class="kpi-card blue">
            <span class="kpi-icon">👥</span>
            <div class="kpi-label">Total Customers</div>
            <div class="kpi-value">{n_total:,}</div>
            <div class="kpi-sub">{n_churned:,} exited customers</div>
            <span class="kpi-badge ok">Dataset loaded</span>
        </div>
        <div class="kpi-card red">
            <span class="kpi-icon">📉</span>
            <div class="kpi-label">Overall Churn Rate</div>
            <div class="kpi-value">{churn_rate:.2f}%</div>
            <div class="kpi-sub">1 in 5 customers leave</div>
            <span class="kpi-badge danger">High Risk</span>
        </div>
        <div class="kpi-card amber">
            <span class="kpi-icon">💎</span>
            <div class="kpi-label">High-Value Churn Rate</div>
            <div class="kpi-value">{hv_churn:.2f}%</div>
            <div class="kpi-sub">Premium segment at risk</div>
            <span class="kpi-badge warning">Revenue Risk</span>
        </div>
        <div class="kpi-card green">
            <span class="kpi-icon">⚡</span>
            <div class="kpi-label">Inactive Customer Churn</div>
            <div class="kpi-value">{inactive_churn:.2f}%</div>
            <div class="kpi-sub">vs {dff[dff["IsActiveMember"]==1]["Exited"].mean()*100:.2f}% active</div>
            <span class="kpi-badge danger">Strongest Lever</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
#  GEOGRAPHY ANALYSIS
# ─────────────────────────────────────────────────────────────
def section_geography(dff):
    sh("🌍 Geography Analysis", "Regional Risk Index")

    geo_stats = (
        dff.groupby("Geography", observed=True)["Exited"]
        .agg(Customers="count", Churned="sum")
        .reset_index()
    )
    geo_stats["ChurnRate"] = geo_stats["Churned"] / geo_stats["Customers"] * 100
    # Sorting by ChurnRate ensures Germany is the first/highest bar
    geo_stats = geo_stats.sort_values("ChurnRate", ascending=False)

    col1, col2 = st.columns(2)

    with col1:
        colors = []
        for cr in geo_stats["ChurnRate"]:
            if cr >= 30:   colors.append("#FF6B6B")
            elif cr >= 20: colors.append("#FFB347")
            else:          colors.append("#00D4AA")

        fig = go.Figure(go.Bar(
            x=geo_stats["Geography"],
            y=geo_stats["ChurnRate"],
            marker=dict(color=colors, line=dict(width=0),
                        cornerradius=6),
            text=[f"{r:.1f}%" for r in geo_stats["ChurnRate"]],
            textposition="outside",
            textfont=dict(color="#e2e8f0", size=12, family="Inter"),
        ))
        fig.update_layout(
            title="Churn Rate Severity by Country",
            yaxis=dict(ticksuffix="%", range=[0, geo_stats["ChurnRate"].max()*1.3]),
            **T
        )
        sfig(fig, ytitle="Churn Rate (%)")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig2 = go.Figure()
        
        # BARS: Now representing Churn Rate (Germany becomes the tallest)
        # Keeping your original color: rgba(108,99,255,0.4)
        fig2.add_trace(go.Bar(
            name="Churn Rate %",
            x=geo_stats["Geography"],
            y=geo_stats["ChurnRate"],
            marker=dict(color="rgba(108,99,255,0.4)",
                        line=dict(color="#6C63FF", width=1)),
            text=[f"{r:.1f}%" for r in geo_stats["ChurnRate"]],
            textposition="outside",
            textfont=dict(color="#FF6B6B"), # Keeping your red text color
            yaxis="y",
        ))

        # LINE: Now representing Total Customers (Volume)
        # Keeping your original line style: #FF6B6B, width 2.5
        fig2.add_trace(go.Scatter(
            name="Total Customers",
            x=geo_stats["Geography"],
            y=geo_stats["Customers"],
            mode="lines+markers",
            line=dict(color="#FF6B6B", width=2.5),
            marker=dict(size=10, color="#FF6B6B",
                        line=dict(color="#0c1220", width=2)),
            yaxis="y2",
        ))

        fig2.update_layout(
            title="Churn Rate Severity (Bars) vs Volume (Line)",
            yaxis=dict(title="Churn Rate %", showgrid=False, ticksuffix="%"),
            yaxis2=dict(title="Customers", overlaying="y", side="right",
                        showgrid=False),
            legend=dict(x=0.5, y=1.12, xanchor="center", orientation="h"),
            **T
        )
        st.plotly_chart(fig2, use_container_width=True)

    # Updated insight text to match the 43.9% figure in your screenshot
    st.markdown(f"""
    <div class="insight-box">
        <span class="tag">🧠 Geographic Insight</span>
        Germany has the <strong>highest churn intensity ({geo_stats.iloc[0]['ChurnRate']:.1f}%)</strong> 
        despite having a lower customer volume than France. This indicates a 
        <span class="critical">structural retention issue</span> in the German market.
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
#  AGE SEGMENT ANALYSIS
# ─────────────────────────────────────────────────────────────
def section_age(dff):
    sh("👥 Age Segment Analysis", "Vulnerability by Age Band")

    age_stats = (
        dff.groupby("AgeGroup", observed=True)["Exited"]
        .agg(Customers="count", Churned="sum")
        .reset_index()
    )
    age_stats["ChurnRate"] = age_stats["Churned"] / age_stats["Customers"] * 100

    col1, col2 = st.columns(2)

    with col1:
        colors_age = []
        for cr in age_stats["ChurnRate"]:
            if cr >= 45:   colors_age.append("#FF6B6B")
            elif cr >= 25: colors_age.append("#FFB347")
            elif cr >= 13: colors_age.append("#6C63FF")
            else:           colors_age.append("#00D4AA")

        fig = go.Figure(go.Bar(
            x=age_stats["AgeGroup"].astype(str),
            y=age_stats["ChurnRate"],
            marker=dict(color=colors_age, cornerradius=6),
            text=[f"{r:.2f}%" for r in age_stats["ChurnRate"]],
            textposition="outside",
            textfont=dict(color="#e2e8f0", size=12),
        ))
        fig.update_layout(
            title="Churn Rate by Age Group",
            yaxis=dict(ticksuffix="%",
                       range=[0, age_stats["ChurnRate"].max()*1.3]),
            **T
        )
        sfig(fig, ytitle="Churn Rate (%)")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        age_sorted = age_stats.sort_values("ChurnRate", ascending=True)
        fig2 = go.Figure(go.Bar(
            x=age_sorted["ChurnRate"],
            y=age_sorted["AgeGroup"].astype(str),
            orientation="h",
            marker=dict(
                color=age_sorted["ChurnRate"],
                colorscale=[[0,"#00D4AA"],[0.4,"#6C63FF"],
                            [0.7,"#FFB347"],[1,"#FF6B6B"]],
                showscale=False,
                cornerradius=6,
            ),
            text=[f"{r:.2f}%" for r in age_sorted["ChurnRate"]],
            textposition="outside",
            textfont=dict(color="#e2e8f0", size=12),
        ))
        fig2.update_layout(
            title="Churn Intensity — Horizontal View",
            xaxis=dict(ticksuffix="%",
                       range=[0, age_sorted["ChurnRate"].max()*1.3]),
            **T
        )
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("""
    <div class="insight-box">
        <span class="tag">🧠 Age Insight</span>
        Churn increases sharply with age — 
        <span class="critical">Senior customers (45–59) churn at 49.45%</span>, 
        nearly <strong>7× higher than Young customers (7.56%)</strong>.
        Older customers are the most vulnerable segment and need dedicated retention programmes.
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
#  ENGAGEMENT ANALYSIS
# ─────────────────────────────────────────────────────────────
def section_engagement(dff):
    sh("⚡ Engagement Analysis", "Most Important Business Lever")

    act_stats = (
        dff.groupby("ActivityLabel", observed=True)["Exited"]
        .agg(Customers="count", Churned="sum")
        .reset_index()
    )
    act_stats["ChurnRate"] = act_stats["Churned"] / act_stats["Customers"] * 100

    col1, col2 = st.columns(2)

    with col1:
        color_map = {"Inactive": "#FF6B6B", "Active": "#00D4AA"}
        colors_act = [color_map.get(a, "#6C63FF")
                      for a in act_stats["ActivityLabel"]]
        fig = go.Figure(go.Bar(
            x=act_stats["ActivityLabel"],
            y=act_stats["ChurnRate"],
            marker=dict(color=colors_act, cornerradius=8),
            text=[f"{r:.2f}%" for r in act_stats["ChurnRate"]],
            textposition="outside",
            textfont=dict(color="#e2e8f0", size=13),
            width=[0.5, 0.5],
        ))
        fig.update_layout(
            title="Churn Rate: Active vs Inactive Members",
            yaxis=dict(ticksuffix="%",
                       range=[0, act_stats["ChurnRate"].max()*1.35]),
            **T
        )
        sfig(fig, ytitle="Churn Rate (%)")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        prod_churn = (
            dff.groupby("NumOfProducts", observed=True)["Exited"]
            .mean().reset_index()
        )
        prod_churn["Exited"] *= 100
        fig2 = go.Figure(go.Scatter(
            x=prod_churn["NumOfProducts"],
            y=prod_churn["Exited"],
            mode="lines+markers+text",
            line=dict(color="#6C63FF", width=3),
            marker=dict(size=12, color=prod_churn["Exited"],
                        colorscale=[[0,"#00D4AA"],[1,"#FF6B6B"]],
                        showscale=False,
                        line=dict(color="#0c1220", width=2)),
            text=[f"{v:.1f}%" for v in prod_churn["Exited"]],
            textposition="top center",
            textfont=dict(color="#e2e8f0"),
            fill="tozeroy",
            fillcolor="rgba(108,99,255,0.08)",
        ))
        fig2.update_layout(
            title="Churn by Number of Products",
            xaxis=dict(title="No. of Products", dtick=1),
            yaxis=dict(title="Churn %", ticksuffix="%"),
            **T
        )
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("""
    <div class="insight-box">
        <span class="tag">⚡ Strongest Business Lever</span>
        Inactive users are <strong>~2× more likely to churn (26.85%)</strong> compared to 
        active members (14.27%). 
        Re-engagement campaigns (notifications, personalised offers) targeting inactive users 
        represent the <span class="critical">single highest ROI retention action</span>.
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
#  HIGH-VALUE CUSTOMER ANALYSIS
# ─────────────────────────────────────────────────────────────
def section_high_value(dff):
    sh("💰 High-Value Customer Analysis", "Revenue Risk")

    hv  = dff[dff["HighValue"] == 1]
    std = dff[dff["HighValue"] == 0]

    hv_churn  = hv["Exited"].mean() * 100  if len(hv)  else 0
    std_churn = std["Exited"].mean() * 100 if len(std) else 0
    rev_risk  = hv[hv["Exited"]==1]["Balance"].sum() / 1e6

    col1, col2, col3 = st.columns([1, 1, 1.2])

    with col1:
        fig = go.Figure(go.Bar(
            x=["High-Value", "Standard"],
            y=[hv_churn, std_churn],
            marker=dict(
                color=["#FF6B6B", "#6C63FF"],
                cornerradius=8,
            ),
            text=[f"{hv_churn:.2f}%", f"{std_churn:.2f}%"],
            textposition="outside",
            textfont=dict(color="#e2e8f0", size=13),
            width=[0.5, 0.5],
        ))
        fig.update_layout(
            title="HV vs Standard Churn Rate",
            yaxis=dict(ticksuffix="%", range=[0, max(hv_churn,std_churn)*1.35]),
            **T
        )
        sfig(fig)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        hv_geo = (
            hv.groupby("Geography", observed=True)["Exited"]
            .mean().reset_index()
        )
        hv_geo["Exited"] *= 100
        fig2 = go.Figure(go.Bar(
            x=hv_geo["Geography"],
            y=hv_geo["Exited"],
            marker=dict(color=PAL[:3], cornerradius=6),
            text=[f"{v:.1f}%" for v in hv_geo["Exited"]],
            textposition="outside",
            textfont=dict(color="#e2e8f0", size=12),
        ))
        fig2.update_layout(
            title="HV Churn by Country",
            yaxis=dict(ticksuffix="%",
                       range=[0, hv_geo["Exited"].max()*1.35]),
            **T
        )
        sfig(fig2)
        st.plotly_chart(fig2, use_container_width=True)

    with col3:
        st.markdown(f"""
        <div style="display:flex;flex-direction:column;gap:0.8rem;padding-top:0.5rem;">
            <div style="background:linear-gradient(135deg,rgba(255,107,107,0.1),rgba(255,107,107,0.05));
                        border:1px solid rgba(255,107,107,0.25);border-radius:12px;
                        padding:1rem 1.2rem;">
                <div style="font-size:0.65rem;color:#FF6B6B;text-transform:uppercase;
                            letter-spacing:0.1em;font-weight:700;">HV Churn Rate</div>
                <div style="font-size:1.8rem;font-weight:900;color:#FF6B6B;">{hv_churn:.2f}%</div>
                <div style="font-size:0.72rem;color:#6b7280;">Premium segment</div>
            </div>
            <div style="background:linear-gradient(135deg,rgba(255,179,71,0.1),rgba(255,179,71,0.05));
                        border:1px solid rgba(255,179,71,0.25);border-radius:12px;
                        padding:1rem 1.2rem;">
                <div style="font-size:0.65rem;color:#FFB347;text-transform:uppercase;
                            letter-spacing:0.1em;font-weight:700;">Revenue at Risk</div>
                <div style="font-size:1.8rem;font-weight:900;color:#FFB347;">€{rev_risk:.1f}M</div>
                <div style="font-size:0.72rem;color:#6b7280;">From HV churners</div>
            </div>
            <div style="background:linear-gradient(135deg,rgba(108,99,255,0.1),rgba(108,99,255,0.05));
                        border:1px solid rgba(108,99,255,0.25);border-radius:12px;
                        padding:1rem 1.2rem;">
                <div style="font-size:0.65rem;color:#818cf8;text-transform:uppercase;
                            letter-spacing:0.1em;font-weight:700;">HV Customers</div>
                <div style="font-size:1.8rem;font-weight:900;color:#818cf8;">{len(hv):,}</div>
                <div style="font-size:0.72rem;color:#6b7280;">in filtered data</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="insight-box">
        <span class="tag">💰 Revenue Risk Alert</span>
        High-value customers are leaving at <strong>25.23% churn rate</strong>, representing 
        <span class="critical">direct revenue risk</span>. 
        Germany leads HV churn — VIP retention plans and personalised wealth management 
        offers should be deployed as a priority.
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
#  TENURE ANALYSIS
# ─────────────────────────────────────────────────────────────
def section_tenure(dff):
    sh("🧩 Tenure Analysis", "Customer Loyalty Patterns")

    ten_stats = (
        dff.groupby("TenureGroup", observed=True)["Exited"]
        .agg(Customers="count", Churned="sum")
        .reset_index()
    )
    ten_stats["ChurnRate"] = ten_stats["Churned"] / ten_stats["Customers"] * 100

    col1, col2 = st.columns(2)

    with col1:
        fig = go.Figure(go.Bar(
            x=ten_stats["TenureGroup"].astype(str),
            y=ten_stats["ChurnRate"],
            marker=dict(color=["#FF6B6B","#FFB347","#00D4AA"],
                        cornerradius=6),
            text=[f"{r:.2f}%" for r in ten_stats["ChurnRate"]],
            textposition="outside",
            textfont=dict(color="#e2e8f0", size=12),
        ))
        fig.update_layout(
            title="Churn Rate by Tenure Group",
            yaxis=dict(ticksuffix="%",
                       range=[0, ten_stats["ChurnRate"].max()*1.3]),
            **T
        )
        sfig(fig)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        pivot = (
            dff.groupby(["Geography","TenureGroup"], observed=True)["Exited"]
            .mean().unstack() * 100
        )
        fig2 = go.Figure(go.Heatmap(
            z=pivot.values,
            x=pivot.columns.astype(str).tolist(),
            y=pivot.index.tolist(),
            colorscale=[[0,"#0c1220"],[0.4,"#6C63FF"],[1,"#FF6B6B"]],
            text=np.round(pivot.values, 1),
            texttemplate="%{text}%",
            showscale=True,
            colorbar=dict(tickfont=dict(color="#8a94b2")),
        ))
        fig2.update_layout(
            title="Churn Heatmap: Country × Tenure",
            **T
        )
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("""
    <div class="insight-box">
        <span class="tag">🧩 Tenure Insight</span>
        New customers (0–2 years) often show the highest churn risk — they haven't yet formed 
        strong loyalty. <strong>Early engagement programmes</strong> in the first 2 years 
        can significantly improve long-term retention.
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
#  KEY TAKEAWAYS
# ─────────────────────────────────────────────────────────────
def section_takeaways():
    sh("🔥 Key Takeaways", "Summary Findings")
    st.markdown("""
    <div class="takeaway-grid">
        <div class="takeaway-item">
            <div class="takeaway-dot" style="background:#FF6B6B;"></div>
            <span><strong style="color:#FF6B6B;">Germany</strong> is the highest-risk region — 
            churn rate of 32.44%, nearly 2× other markets</span>
        </div>
        <div class="takeaway-item">
            <div class="takeaway-dot" style="background:#FFB347;"></div>
            <span><strong style="color:#FFB347;">Senior customers (45–59)</strong> are most likely 
            to churn at 49.45% — 7× higher than young customers</span>
        </div>
        <div class="takeaway-item">
            <div class="takeaway-dot" style="background:#6C63FF;"></div>
            <span><strong style="color:#818cf8;">Inactive users</strong> are nearly 2× more likely 
            to leave (26.85% vs 14.27%) — the strongest retention lever</span>
        </div>
        <div class="takeaway-item">
            <div class="takeaway-dot" style="background:#00D4AA;"></div>
            <span><strong style="color:#00D4AA;">High-value customers</strong> show a concerning 
            25.23% churn rate — posing direct revenue risk</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
#  RECOMMENDATIONS
# ─────────────────────────────────────────────────────────────
def section_recommendations():
    sh("🎯 Business Recommendations", "Action Plan")
    st.markdown("""
    <div class="reco-grid">
        <div class="reco-card">
            <div class="reco-icon">🇩🇪</div>
            <div>
                <div class="reco-title">Focus Retention Campaigns in Germany</div>
                <div class="reco-desc">Deploy targeted outreach in Germany where churn is 32.44% — 
                prioritise personalised offers, loyalty bonuses, and dedicated relationship managers.</div>
            </div>
        </div>
        <div class="reco-card">
            <div class="reco-icon">👴</div>
            <div>
                <div class="reco-title">Improve Services for Senior Customers</div>
                <div class="reco-desc">Senior (45–59) customers churn at 49.45%. Introduce 
                senior-specific benefits, simplified digital banking, and proactive check-in calls.</div>
            </div>
        </div>
        <div class="reco-card">
            <div class="reco-icon">📲</div>
            <div>
                <div class="reco-title">Increase Engagement (Notifications & Offers)</div>
                <div class="reco-desc">Inactive members churn at nearly 2×. Re-engagement 
                via push notifications, personalised product offers, and usage incentives 
                is the highest-ROI lever.</div>
            </div>
        </div>
        <div class="reco-card">
            <div class="reco-icon">💎</div>
            <div>
                <div class="reco-title">Create VIP Retention Plans for HV Customers</div>
                <div class="reco-desc">High-value customers churning at 25.23% represent 
                disproportionate revenue loss. Introduce dedicated VIP advisors, exclusive 
                benefits, and proactive wealth management touchpoints.</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
#  DATA EXPLORER TAB
# ─────────────────────────────────────────────────────────────
def section_data(dff):
    sh("🗄 Dataset Explorer", f"{len(dff):,} records after filters")
    st.dataframe(
        dff.drop(columns=["Surname"], errors="ignore").head(500),
        use_container_width=True,
        height=400,
    )
    csv = dff.drop(columns=["Surname"], errors="ignore").to_csv(index=False).encode()
    st.download_button(
        "⬇️ Download Filtered Dataset (CSV)",
        data=csv,
        file_name="churn_filtered.csv",
        mime="text/csv",
    )


# ─────────────────────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────────────────────
def main():
    df      = load_data()
    filters = render_sidebar(df)
    dff     = apply_filters(df, filters)

    st.markdown("""
    <div class="top-banner">
        <div class="objective-tag">📋 Technical Dashboard · European Banking</div>
        <h1>Customer Segmentation & Churn Analytics</h1>
        <p class="subtitle">France &nbsp;·&nbsp; Spain &nbsp;·&nbsp; Germany &nbsp;·&nbsp; 
        Segmentation-driven intelligence for European retail banking</p>
        <div class="objective-quote">
            "Identify high-risk customer segments and drivers of churn in a European bank."
        </div>
    </div>
    """, unsafe_allow_html=True)

    render_kpis(dff)

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🌍 Geography",
        "👥 Age Segments",
        "⚡ Engagement",
        "💰 High-Value",
        "🧩 Tenure",
        "🗄 Data Explorer",
    ])

    with tab1:
        section_geography(dff)
    with tab2:
        section_age(dff)
    with tab3:
        section_engagement(dff)
    with tab4:
        section_high_value(dff)
    with tab5:
        section_tenure(dff)
    with tab6:
        section_data(dff)

    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        section_takeaways()
    with c2:
        section_recommendations()

    st.markdown(
        "<p style='text-align:center;color:#374151;font-size:0.72rem;margin-top:2rem;'>"
        "ChurnSight v2.0 · Customer Segmentation & Churn Pattern Analytics · "
        "European Banking · Unified Mentor × ECB · 2026</p>",
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()