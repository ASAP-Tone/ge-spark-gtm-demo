# Repeatable GTM & Support Friction Demo - Technical README

**Date:** September 2, 2026  
**Author:** Cloud Architecture & Revenue GTM Team  
**Scope:** Reusable Field Selling Demo Kit for Gemini Enterprise  

---

## 1. Demo Concept & Objectives
The goal of this demo is to show prospective clients (e.g. Cloud Architects, Support Directors, and GTM Executives) how **Gemini Enterprise** can bridge disparate silos (Sales, Support, Development, Engineering, GTM) to eliminate operational bottlenecks and unblock stalled revenue. 

It tells a unified, three-part story:
1.  **Find the Problem (Salesforce + BigQuery):** Detect that high-value opportunities ($1.34M for United Oil) are stalled in Salesforce, trace the blockage to an unassigned support case, and use BigQuery analytics to identify a 10.25-hour support latency bottleneck due to missing technical guidelines.
2.  **Act on the Problem (Jira + GitHub):** Create a high-priority escalation ticket (`SAM1-12`) in Jira, write a technical installation guide for the GC5060 generator system, and commit it directly to the repository main branch in GitHub (`docs/GC5060_wiring_guide.md`) to resolve the blocker.
3.  **Deliver & Automate (Google Workspace + Cron):** Automatically generate an executive briefing Google Doc, draft a proactive Gmail outreach, check tomorrow's Google Calendar availability, and schedule a daily background Pipeline Risk Monitor cron job in Cowork to proactively flag pipeline risk.

---

## 2. Environment Prerequisites & Connectors

To run this demo successfully, the field seller's Argolis sandbox must have the following connectors configured:

| Layer | System | Scope/Permissions Required | Name/ID in Demo |
| :--- | :--- | :--- | :--- |
| **Salesforce** | Salesforce SObject | Read opportunities & cases. | `collections/ge-sf-connector_1788294129306` |
| **Jira Cloud** | Jira Issues | Create tasks, update summaries, change status. | `collections/ge-app-jira-conn_1788284708607` |
| **BigQuery** | GCP BigQuery | Query dataset in `truiz-agy-demo` project. | `collections/bq-mcp-connector_1787236389359` |
| **GitHub** | GitHub Repositories | Read/write, create files, commit. | `collections/ge-github-ds_1788301011913` |
| **Workspace** | Google Workspace | Read/write Google Docs, Slides, Gmail, Calendar, Drive. | Native workspace server nodes. |

---

## 3. The Automation Utility (`demo_manager.py`)

A custom automation script is included at `scripts/demo_manager.py`. It is responsible for making this demo **100% reusable and repeatable** with zero residue in 3P systems.

### What it does on run:
1.  **Archives Local Run:** Copies all current session deliverables (`dashboard.html`, `logs.json`, etc.) from the workspace root into a dedicated `runs/run_<timestamp>_customer_name/` directory so you keep a history of past runs.
2.  **GitHub Revert:** Automatically resets the `docs/GC5060_wiring_guide.md` file in the GitHub repo back to its pristine baseline, removing the technical manual.
3.  **Jira Clean-up:** Updates the summary of Jira ticket `SAM1-12` to `[DEMO ARCHIVED] Escalation: ...`, flags it, and transitions the status to **Done/Closed** to clear the board.
4.  **Local Workspace Clear:** Deletes active local deliverables from the workspace root to clean the stage.
5.  **Workspace Instructions:** Outputs the exact `gdrive.trash` and `gmail` commands to clean up the cloud documents.

### How to use it:
*   Make the script executable: `chmod +x demo_manager.py`
*   Run the script: `./demo_manager.py`

---

## 4. How to Lead the Customer Conversation (Field Script)

*   **Slide 1 Introduction:** *"Hello! Today I'll show you why Gemini Enterprise is not just another chat app, but an agentic GTM accelerator. Imagine you have a $1.34M deal stalling because of support backlog..."*
*   **Slide 2 Data Story:** *"We query Salesforce, locate our blocked United Oil accounts, and hop into BigQuery. Look at this—we have a 10.25-hour latency bottleneck on generator support. Our L1 agents have the skills but lack the drawings..."*
*   **Slide 3 Action & Close:** *"In seconds, we escalate a Jira dev task, write a comprehensive wiring guide, commit it directly to our GitHub repository, and draft a personalized outreach email in Gmail based on our calendar slots. This is how we unblock pipeline proactively."*
