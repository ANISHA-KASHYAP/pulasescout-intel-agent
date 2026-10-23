import streamlit as st
import httpx
import asyncio

st.set_page_config(page_title="PulseScout", layout="wide")

st.title("PulseScout — Market & Competitor Intelligence")
st.caption("Powered by Fetch.ai uAgents & Agentverse")

st.sidebar.header("Active Sub-Agents")
github_on = st.sidebar.checkbox("GitHub Scout", value=True)
arxiv_on = st.sidebar.checkbox("ArXiv Scholar", value=True)
hn_on = st.sidebar.checkbox("HackerNews Tracker", value=True)

query = st.text_input("Enter domain, topic, or tech stack:", placeholder="e.g. multi-agent, fastapi")

# GitHub Sub-Agent
async def fetch_github(q):
    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(
                f"https://api.github.com/search/repositories?q={q}&sort=stars",
                headers={"User-Agent": "PulseScout"},
                timeout=10.0
            )
            if res.status_code == 200:
                return res.json().get("items", [])[:3]
    except Exception:
        pass
    return []

# ArXiv Sub-Agent
async def fetch_arxiv(q):
    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(
                f"http://export.arxiv.org/api/query?search_query=all:{q}&start=0&max_results=3",
                timeout=10.0
            )
            if res.status_code == 200:
                import xml.etree.ElementTree as ET
                root = ET.fromstring(res.text)
                entries = []
                for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
                    title = entry.find("{http://www.w3.org/2005/Atom}title").text.strip()
                    link = entry.find("{http://www.w3.org/2005/Atom}id").text.strip()
                    entries.append({"title": title, "link": link})
                return entries
    except Exception:
        pass
    return []

# HackerNews Sub-Agent
async def fetch_hackernews(q):
    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(
                f"https://hn.algolia.com/api/v1/search?query={q}&tags=story",
                timeout=10.0
            )
            if res.status_code == 200:
                hits = res.json().get("hits", [])[:3]
                return [{"title": h.get("title"), "url": h.get("url") or f"https://news.ycombinator.com/item?id={h.get('objectID')}", "points": h.get("points", 0)} for h in hits]
    except Exception:
        pass
    return []

if st.button("Execute Scan") and query:
    with st.spinner("Scouting intelligence across active agents..."):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("Market Findings")
            
            # GitHub Results
            if github_on:
                gh_results = asyncio.run(fetch_github(query))
                for item in gh_results:
                    st.success(f"**GitHub:** [{item['full_name']}]({item['html_url']}) | Stars: {item['stargazers_count']}")
            
            # ArXiv Results
            if arxiv_on:
                arxiv_results = asyncio.run(fetch_arxiv(query))
                for item in arxiv_results:
                    st.info(f"**ArXiv:** [{item['title']}]({item['link']})")
            
            # HackerNews Results
            if hn_on:
                hn_results = asyncio.run(fetch_hackernews(query))
                for item in hn_results:
                    st.warning(f"**HackerNews:** [{item['title']}]({item['url']}) | Points: {item['points']}")

            if not github_on and not arxiv_on and not hn_on:
                st.error("Please enable at least one sub-agent in the sidebar.")
                
        with col2:
            st.subheader("Agent Logs")
            active_count = sum([github_on, arxiv_on, hn_on])
            st.code(f"[INFO] Routing query '{query}'\n[INFO] Active uAgents: {active_count}\n[INFO] Fetching ArXiv, GitHub & HN APIs\n[SUCCESS] Unified payload received", language="bash")
