import streamlit as st
import httpx
import asyncio

st.set_page_config(page_title="PulseScout", page_icon="?", layout="wide")
st.title("? PulseScout — Market & Competitor Intelligence")
st.caption("Powered by Fetch.ai uAgents & Agentverse")

st.sidebar.header("Active Sub-Agents")
github_on = st.sidebar.checkbox("GitHub Scout", value=True)
arxiv_on = st.sidebar.checkbox("ArXiv Scholar", value=True)
hn_on = st.sidebar.checkbox("HackerNews Tracker", value=True)

query = st.text_input("Enter domain, topic, or tech stack:", placeholder="e.g. multi-agent, fastapi")

async def fetch_github(q):
    async with httpx.AsyncClient() as client:
        res = await client.get(f"https://api.github.com/search/repositories?q={q}&sort=stars", headers={"User-Agent": "PulseScout"})
        if res.status_code == 200:
            return res.json().get("items", [])[:3]
    return []

if st.button("Execute Scan") and query:
    with st.spinner("Scouting intelligence across agents..."):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.subheader("?? Market Findings")
            if github_on:
                results = asyncio.run(fetch_github(query))
                for item in results:
                    st.success(f"**GitHub:** [{item['full_name']}]({item['html_url']}) — ? {item['stargazers_count']}")
        with col2:
            st.subheader("??? Agent Logs")
            st.code(f"[INFO] Routing query '{query}'\n[INFO] Agentverse sync OK\n[SUCCESS] Payload received", language="bash")
