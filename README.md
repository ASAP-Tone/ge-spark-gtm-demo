# Gemini Enterprise repeatable-gtm-support-demo

[![Platform: Gemini Enterprise](https://img.shields.io/badge/Platform-Gemini%20Enterprise-blue.svg)](https://cloud.google.com/gemini)
[![Connectors: 5 Active](https://img.shields.io/badge/Connectors-5%20Active-emerald.svg)](#2-prerequisites--connectors)
[![Demo Lifecycle: Auto-Reset](https://img.shields.io/badge/Lifecycle-Auto--Reset-orange.svg)](#3-automated-reusable-reset-utility)

A complete, version-controlled **"Demo-as-Code"** package designed for Cloud Architects, GTM Field Sellers, and Developer Advocates. This kit encapsulates a high-impact, cross-functional GTM scenario that bridges five enterprise systems to resolve support friction, unblock stalled pipelines, and automate proactive GTM deliverables.

---

## 1. What This Skill Does

This skill demonstrates the power of **Gemini Enterprise**'s agentic reasoning and tool integration by rallying five enterprise systems to resolve support friction, unblock stalled pipelines, and automate GTM deliverables.

### The Business Scenario:
*   **The Problem:** High-value enterprise accounts (e.g., United Oil & Gas Corp) are experiencing stalled sales pipelines because of unresolved technical customer support cases. 
*   **The Bottleneck:** support latency diagnostics show a critical **10.25-hour resolution delay** for generator setup queries, dragging customer CSAT down to **4.00/5.00** (below the 4.70 corporate target). This is due to a lack of clear L1 engineering documentation.
*   **The Resolution:** Gemini Enterprise automatically detects this pipeline-at-risk, escalates a high-priority dev task in **Jira**, authors and commits a comprehensive wiring guide directly to the engineering codebase in **GitHub**, generates polished **Google Docs** briefings and **Gmail** outreach drafts based on open **Google Calendar** slots, and schedules a daily **Pipeline Risk Monitor** background automation.

---

## 2. The End-to-End Demo Script (Field Narrative)

Use this script during live client engagements to guide the prospect through each phase of the demo:

```
┌──────────────────────────┐     ┌──────────────────────────┐     ┌──────────────────────────┐
│   1. FIND THE PROBLEM    │  →  │    2. ACT ON THE RISK    │  →  │  3. DELIVER & AUTOMATE   │
│   Salesforce + BigQuery  │     │      Jira + GitHub       │     │     Workspace + Cron     │
└──────────────────────────┘     └──────────────────────────┘     └──────────────────────────┘
```

### Phase 1: Find the Problem (Salesforce & BigQuery Analytics)
*   **Action:** Query Salesforce to locate at-risk, open opportunities $\ge \$100\text{k}$ with overdue close dates, and cross-reference them with open support cases.
*   **The Storyteller's Voice:** 
    > *"Let's check our pipeline. We see that we have $2.91M in stalled deals. Most critically, $1.34M of that exposure is concentrated within United Oil. Why? They've had a Salesforce support case unassigned since July 2025 asking for GC5060 generator wiring guidance."*
*   **Action:** Query our historical support database in BigQuery (`<GCP_PROJECT_ID>` project) to find the bottleneck.
*   **The Storyteller's Voice:** 
    > *"Let's analyze our support logs. BigQuery reveals that generator inquiries average a slow 10.25 hours to resolve—41% slower than standard tickets. It's dragging our CSAT down to 4.00. Since L1 agents resolve 94.5% of these without escalation, this isn't a skill deficit; it's a documentation deficit."*

### Phase 2: Act on the Risk (Jira & GitHub Codebase)
*   **Action:** Create a high-priority escalation task in Jira project `SAM1`.
*   **The Storyteller's Voice:** 
    > *"We immediately escalate this bottleneck. In one click, Gemini creates high-priority task SAM1-12 in Jira to mobilize our engineering team, passing the complete revenue and support analytics."*
*   **Action:** Author and commit the comprehensive, code-compliant GC5060 technical wiring guide directly to GitHub.
*   **The Storyteller's Voice:** 
    > *"Instead of waiting, Gemini compiles our engineering schematics and commits a full technical wiring manual directly into our core repository at `docs/GC5060_wiring_guide.md`, referencing the Jira ticket. The blocker is now permanently resolved in our codebase."*

### Phase 3: Deliver & Automate (Google Workspace & Proactive Cron)
*   **Action:** Import the briefing to Google Docs, draft the Gmail outreach, check Google Calendar, and schedule the daily monitor.
*   **The Storyteller's Voice:** 
    > *"Now, we package our deliverables. Gemini generates a polished Executive Briefing in Google Docs, checks our Calendar to find open slots for tomorrow, and drafts a personalized email in Gmail enclosing the GitHub guide link. Finally, we schedule a daily background Cron Job in Gemini Enterprise Spark that automatically sweeps Salesforce and Jira so we never have a GTM blindspot again."*

---

## 3. How to Use This Skill

This repository is designed to run in **Gemini Enterprise (Spark/Gogo)** as a reusable, version-controlled skill.

### Running the Demo:
1.  **Load the Skill:** Start an agentic session and instruct the agent to load the skill:
    ```markdown
    load_skill(skill_name="repeatable-gtm-support-demo")
    ```
2.  **Execute the Playbook:** Instruct the agent to run the step-by-step playbook described in [`SKILL.md`](./SKILL.md) for a prospective client.

### Archiving & Resetting the Demo (Making it Repeatable):
To clean up remote systems and archive local files so you can repeat the demo for a new client:

1.  **Run the Local Reset Script:**
    ```bash
    chmod +x scripts/demo_manager.py
    ./scripts/demo_manager.py
    ```
    This script will:
    *   Archive local active deliverables (`dashboard.html`, `logs.json`, etc.) to **`runs/run_<timestamp>/`** to preserve history.
    *   Restore the GitHub file `docs/GC5060_wiring_guide.md` back to its pristine pre-demo state.
    *   Archive the Jira ticket `SAM1-12` and move it to **Done**.
    *   Clear the local workspace root files.
2.  **Clean up Google Workspace Assets:**
    The script will output the exact commands to trash your generated cloud documents on the gateway. Ask Gemini to execute them:
    ```markdown
    Please clean up the Workspace assets:
    1. call_mcp_tool("gdrive", "trash", {"file_id": "<Google Doc ID>"})
    2. call_mcp_tool("gdrive", "trash", {"file_id": "<Google Slides ID>"})
    3. call_mcp_tool("gmail", "delete_draft", {"draft_id": "<Gmail Draft ID>"})
    ```

---

## 4. Prerequisites & Connectors Setup

Before starting, verify that your field Argolis sandbox is configured with the following active integrations:
*   **Salesforce Connector:** ID `<SALESFORCE_CONNECTOR_ID>`
*   **Jira Cloud Connector:** ID `<JIRA_CONNECTOR_ID>`
*   **BigQuery Connector:** ID `<BIGQUERY_CONNECTOR_ID>`
*   **GitHub Connector:** ID `<GITHUB_CONNECTOR_ID>`
*   **Workspace Connectors:** Native Google Docs, Google Slides, Google Calendar, Gmail, and Google Drive server permissions.

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
