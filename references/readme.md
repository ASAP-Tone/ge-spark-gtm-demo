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
3.  **Deliver & Automate (Google Workspace + Cron):** Automatically generate an executive briefing Google Doc, draft a proactive Gmail outreach, check tomorrow's Google Calendar availability, and schedule a daily background Pipeline Risk Monitor cron job in Gemini Enterprise Spark to proactively flag pipeline risk.

---

## 2. Environment Prerequisites & Connectors

To run this demo successfully, the field seller's Argolis sandbox must have the following connectors configured:

| Layer | System | Scope/Permissions Required | Name/ID in Demo |
| :--- | :--- | :--- | :--- |
| **Salesforce** | Salesforce SObject | Read opportunities & cases. | `<SALESFORCE_CONNECTOR_ID>` |
| **Jira Cloud** | Jira Issues | Create tasks, update summaries, change status. | `<JIRA_CONNECTOR_ID>` |
| **BigQuery** | GCP BigQuery | Query dataset in `<GCP_PROJECT_ID>` project. | `<BIGQUERY_CONNECTOR_ID>` |
| **GitHub** | GitHub Repositories | Read/write, create files, commit. | `<GITHUB_CONNECTOR_ID>` |
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

---

## 5. Precise Prompts for GE Spark (Live Demo Script)

To execute this demo live in front of a customer, copy-paste or type these precise prompts in order. Replace placeholder values like `<GCP_PROJECT_ID>` with your specific sandbox IDs.

### 🎬 Step 1: Discover Risk in Salesforce
*   **Narrative:** Check your active, open pipeline and discover what is holding up late-stage revenue.
*   **Precise Prompt:**
    ```text
    Show me my high-value opportunities at risk in Salesforce and check if there are any related customer support cases in our system.
    ```

### 📊 Step 2: Query Support Latency in BigQuery
*   **Narrative:** Deep-dive into support metrics to find the systemic operational bottleneck dragging down your deals.
*   **Precise Prompt:**
    ```text
    Analyze our support metrics in the BigQuery '<GCP_PROJECT_ID>' GCP project to see if tickets like this are bottlenecked or impacting our CSAT scores.
    ```

### 🎫 Step 3: Create Engineering Escalation in Jira
*   **Narrative:** Bridge the gap between GTM and Development by creating a high-priority tracking task.
*   **Precise Prompt:**
    ```text
    Create a high-priority task in Jira project 'SAM1' to escalate this GC5060 electrical wiring documentation issue to our engineering team.
    ```

### 💻 Step 4: Deploy Documentation to GitHub
*   **Narrative:** Solve the technical blocker by committing the official guidelines directly into the codebase.
*   **Precise Prompt:**
    ```text
    Write the technical electrical wiring installation guide for the GC5060 generator system and commit it directly to our 'adk-salesforce-agent' GitHub repository on branch 'main' under the path 'docs/GC5060_wiring_guide.md'. Reference Jira ticket 'SAM1-11'.
    ```

### 📝 Step 5: Render Workspace Deliverables (Gdocs, Gmail, Calendar)
*   **Narrative:** Automatically package GTM briefs, look up your open schedule, and draft client-facing email outreach.
*   **Precise Prompt:**
    ```text
    Generate an executive briefing document in Google Docs detailing this resolution, check my Google Calendar schedule for tomorrow, and draft a professional email to United Oil in Gmail with the guide link.
    ```

### 🎨 Step 6: Google Slides Pitch Deck
*   **Narrative:** Build a stunning, beautifully formatted customer pitch deck.
*   **Precise Prompt:**
    ```text
    Create a high-impact Google Slides pitch deck detailing this GC5060 resolution plan, utilizing our corporate styling guidelines (Navy `#1E2761`, Ice Blue `#CADCFC`, and Amber `#F5B841`) to unblock the pipeline.
    ```

### 🤖 Step 7: Proactive Automation (Daily Background Cron)
*   **Narrative:** Set up a proactive, daily background scanner to alert GTM teams of support friction on high-value accounts.
*   **Precise Prompt:**
    ```text
    Create and schedule a daily background job in Gemini Enterprise Spark that runs a proactive sweep of our Salesforce opportunities and support cases to detect high-value pipeline risk from customer friction.
    ```

### 🧹 Step 8: Automated Clean-up & Reset
*   **Narrative:** Run the clean-up script to archive your active run history, clear your workspace, and restore your baseline systems.
*   **Precise Prompt:**
    ```text
    Run the demo manager reset script to archive this run and clean up our active workspace root and 3P resources.
    ```
