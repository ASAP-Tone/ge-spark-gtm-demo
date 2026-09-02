# repeatable-gtm-support-demo

This skill encapsulates the execution and automated reset of the cross-system **Salesforce CRM \u2192 BigQuery Analytics \u2192 Jira Escalation \u2192 GitHub Codebase \u2192 Google Workspace** demonstration. It shows a GTM prospect how technical support latency drags customer CSAT and stalls high-value sales pipeline, and demonstrates how Gemini Enterprise automates the entire cross-functional fix.

## Prerequisites & Connectors Required

To execute this demo, the active session must have access to the following 5 connectors:
1.  **Salesforce Connector (salesforce):** Querying opportunities (`Amount`, `CloseDate`, `Probability`) and cases.
2.  **Jira Cloud Connector (jira):** Mapping projects (`SAM1`), issue types (`Task`), priorities (`High`), and creating/transitioning escalations.
3.  **BigQuery Connector (custom_mcp):** Querying support tables in GCP project `truiz-agy-demo` to extract latency and CSAT averages.
4.  **GitHub Connector (github):** Auditing and committing guidelines directly to repository `ASAP-Tone/adk-salesforce-agent`.
5.  **Google Workspace Server Nodes:** Native Workspace MCP servers (`gdocs`, `gcalendar`, `gmail`, `gslides`, `gdrive`).

---

## Phase A: Running the Demo (Step-by-Step)

### Step 1: Discover Risk in Salesforce
Query Salesforce for high-value open opportunities (Amount >= $100k) where the close dates are past due (e.g. stalled in 2025). Cross-reference with open support cases on those accounts.
*   *Key Insight:* Identify that **United Oil & Gas Corp.** has **$1.34M in exposure** stalled due to Salesforce Case #00001002 seeking "electrical wiring guidance for GC5060".

### Step 2: Query Support Latency in BigQuery
Run analytical queries on GCP project `truiz-agy-demo` support tables to prove *why* the Case is unassigned.
*   *Key Insight:* Support categories related to generator setup average **10.25 hours** to resolve (41% slower than baseline) and drag CSAT down to **4.00/5.00** (target is 4.70). 94.5% are resolved at L1, revealing a documentation deficit.

### Step 3: Create Engineering Escalation in Jira
Create a high-priority task in Jira project `SAM1` (Issue Type `Task`, Priority `High`) to escalate the GC5060 electrical wiring documentation bottleneck.

### Step 4: Deploy Documentation to GitHub
Commit the comprehensive, code-compliant **`GC5060_wiring_guide.md`** technical manual directly to the `main` branch of repository `ASAP-Tone/adk-salesforce-agent` under path `docs/GC5060_wiring_guide.md`. Reference Jira ticket `SAM1-11`.

### Step 5: Render Workspace Collateral
Generate high-quality GTM materials:
1.  **Google Doc Briefing:** Import a detailed Markdown executive briefing.
2.  **Gmail Outreach Draft:** Draft a professional outreach email to `engineering-leads@unitedoil.com` with tomorrow's open schedule slots and the GitHub guide link.
3.  **Google Slides Pitch Deck:** Render a beautifully themed 3-slide pitch presentation using the `batch` tool.
4.  **Proactive Automation:** Schedule a daily background cron job ("Pipeline Risk Monitor") to run daily risk sweeps.

---

## Phase B: Resetting the Demo (Automated Clean-up)

To make the demo repeatable for the next customer, execute the automated reset:

1.  **Execute the Script:** Run `./demo_manager.py` in your workspace terminal. This script will:
    *   Archive active root reports (`dashboard.html`, `logs.json`, etc.) into `runs/run_<timestamp>/` so you keep client-specific histories.
    *   Restore the GitHub file `docs/GC5060_wiring_guide.md` back to its pristine pre-demo state.
    *   Rename and archive the Jira ticket (`SAM1-12`), moving it to 'Done'.
    *   Delete the active root workspace deliverables to clear the stage.
2.  **Trash Workspace Files:** Execute the following Workspace trash commands to clear the cloud assets:
    *   `call_mcp_tool("gdrive", "trash", {"file_id": "<Google Doc ID>"})`
    *   `call_mcp_tool("gdrive", "trash", {"file_id": "<Google Slides ID>"})`
    *   `call_mcp_tool("gmail", "delete_draft", {"draft_id": "<Gmail Draft ID>"})`
3.  **Ready:** Your workspace is now 100% clean and ready for your next prospective buyer!
