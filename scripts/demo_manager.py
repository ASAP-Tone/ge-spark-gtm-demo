#!/usr/bin/env python3
import os
import json
import shutil
import subprocess
from datetime import datetime

STATE_FILE = "state_tracker.json"
RUNS_DIR = "runs"

def load_state():
    if not os.path.exists(STATE_FILE):
        print(f"[Error] State file {STATE_FILE} not found. Ensure you are in the correct directory.")
        return None
    with open(STATE_FILE, "r") as f:
        return json.load(f)

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def archive_run(state):
    active_id = state.get("active_run_id")
    if not active_id:
        print("[Warn] No active run ID found in state.")
        return False
    
    # Locate the active run metadata
    run_data = None
    for run in state["runs"]:
        if run["run_id"] == active_id:
            run_data = run
            break
            
    if not run_data:
        print(f"[Error] Active run {active_id} not found in state runs database.")
        return False
        
    if run_data["status"] == "archived_and_cleared":
        print(f"[Info] Run {active_id} is already archived and cleared.")
        return True

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest_dir = os.path.join(RUNS_DIR, f"run_{timestamp}_{run_data['customer'].lower().replace(' ', '_').replace('.', '')}")
    os.makedirs(dest_dir, exist_ok=True)
    
    print(f"[Step 1/5] Archiving local artifacts for {run_data['customer']} to {dest_dir}...")
    copied_files = []
    for file in run_data["local_artifacts"]:
        if os.path.exists(file):
            shutil.copy(file, dest_dir)
            copied_files.append(file)
            print(f"  ✓ Copied: {file}")
        else:
            print(f"  ⚠ Missing locally: {file}")
            
    print(f"[Info] Local backup completed successfully. {len(copied_files)} files archived.")
    return dest_dir

def reset_3p_assets(state):
    active_id = state.get("active_run_id")
    run_data = next((r for r in state["runs"] if r["run_id"] == active_id), None)
    if not run_data:
        return
        
    print("\n[Step 2/5] Reverting GitHub Codebase changes...")
    gh = run_data["remote_assets"].get("github_commit")
    if gh:
        # Revert file to original content via mcp_cli
        print(f"  reverting: {gh['path']} in {gh['owner']}/{gh['repo']}...")
        args = {
            "owner": gh["owner"],
            "repo": gh["repo"],
            "path": gh["path"],
            "branch": "main",
            "message": "revert: restore original GC5060 wiring guide to baseline [DEMO RESET]",
            "sha": gh["current_sha"],
            "content": gh["original_content"]
        }
        cmd = [
            "/Users/tonyruiz/ge_spark_workspace/.ge_spark/bin/mcp_cli",
            "--call-tool",
            "--connector=collections/ge-github-ds_1788301011913",
            "--tool-name=create_or_update_file",
            f"--args={json.dumps(args)}"
        ]
        try:
            print("  Executing GitHub revert command...")
            res = subprocess.run(cmd, capture_output=True, text=True, check=True)
            res_json = json.loads(res.stdout)
            if "error" in res_json:
                print(f"  ⚠ GitHub Revert Failed: {res_json['error']['message']}")
            else:
                print("  ✓ GitHub repository file reverted successfully.")
        except Exception as e:
            print(f"  ⚠ Failed to execute GitHub revert: {e}")
    else:
        print("  ✓ No GitHub assets to revert.")

    print("\n[Step 3/5] Cleaning up Jira Escalation task...")
    jira = run_data["remote_assets"].get("jira_issue")
    if jira:
        # Transition Jira task to closed/archived, or rename it
        print(f"  updating: {jira['key']} (ID: {jira['id']})...")
        args = {
            "ProjectId": "10000",
            "ProjectKey": "SAM1",
            "IssueTypeId": "10003",
            "IssueTypeName": "Task",
            "PriorityId": "2",
            "PriorityName": "High",
            "Summary": f"[DEMO ARCHIVED] {jira['summary']}",
            "Labels": "demo-reset,archived-run",
            "Description": "This task was automatically archived and closed by the Demo Reset utility."
        }
        cmd = [
            "/Users/tonyruiz/ge_spark_workspace/.ge_spark/bin/mcp_cli",
            "--call-tool",
            "--connector=collections/ge-app-jira-conn_1788284708607",
            "--tool-name=update_issue",
            f"--args={json.dumps({'issueIdOrKey': jira['key'], 'fields': args})}"
        ]
        cmd_status = [
            "/Users/tonyruiz/ge_spark_workspace/.ge_spark/bin/mcp_cli",
            "--call-tool",
            "--connector=collections/ge-app-jira-conn_1788284708607",
            "--tool-name=change_issue_status",
            f"--args={json.dumps({'issueIdOrKey': jira['key'], 'transitionNameOrId': 'Done'})}"
        ]
        try:
            print("  Executing Jira update command...")
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            print("  ✓ Jira ticket renamed and marked as archived.")
            
            print("  Transitioning Jira ticket to 'Done'...")
            subprocess.run(cmd_status, capture_output=True, text=True, check=True)
            print("  ✓ Jira ticket status transitioned to Done.")
        except Exception as e:
            print(f"  ⚠ Failed to update/transition Jira issue: {e}")
    else:
        print("  ✓ No Jira assets to clean up.")

def delete_local_deliverables(run_data):
    print("\n[Step 4/5] Clearing active files from workspace root...")
    removed_count = 0
    for file in run_data["local_artifacts"]:
        if os.path.exists(file):
            try:
                os.remove(file)
                print(f"  ✓ Deleted local file: {file}")
                removed_count += 1
            except Exception as e:
                print(f"  ⚠ Failed to delete {file}: {e}")
    print(f"[Info] Root workspace cleared. {removed_count} files removed.")

def generate_workspace_instructions(run_data):
    print("\n" + "="*60)
    print(" [Step 5/5] WORKSPACE ASSETS CLEANUP REQUIRED (HUMAN / AGENT ACTION)")
    print("="*60)
    print("Because Google Workspace APIs require active OAuth flows and confirmation,")
    print("please copy-paste and ask Gemini to execute the following reset actions:")
    print("-"*60)
    
    gdocs = run_data["remote_assets"].get("google_docs")
    gslides = run_data["remote_assets"].get("google_slides")
    gmail = run_data["remote_assets"].get("gmail_draft")
    
    prompt = "Please clean up the following Workspace assets generated for this demo:\n"
    if gdocs:
        prompt += f"1. call_mcp_tool(\"gdrive\", \"trash\", {{\"file_id\": \"{gdocs['id']}\"}}) - Trashes Google Doc ''{gdocs['title']}''\n"
    if gslides:
        prompt += f"2. call_mcp_tool(\"gdrive\", \"trash\", {{\"file_id\": \"{gslides['id']}\"}}) - Trashes Google Slide ''{gslides['title']}''\n"
    if gmail:
        prompt += f"3. call_mcp_tool(\"gmail\", \"trash\", {{\"message_id\": \"{gmail['id']}\"}}) - Trashes Gmail Draft ID: {gmail['id']}\n"
    
    prompt += "4. Let me know when they are successfully moved to the trash so the reset is 100% complete!"
    print(prompt)
    print("="*60 + "\n")

def main():
    state = load_state()
    if not state:
        return
        
    active_id = state.get("active_run_id")
    run_data = next((r for r in state["runs"] if r["run_id"] == active_id), None)
    if not run_data:
        print(f"[Error] Active run {active_id} is missing in runs registry.")
        return
        
    print(f"============================================================")
    print(f" DEMO RESET UTILITY: Active Run ''{active_id}'' for {run_data['customer']}")
    print(f"============================================================\n")
    
    dest_dir = archive_run(state)
    if not dest_dir:
        return
        
    reset_3p_assets(state)
    delete_local_deliverables(run_data)
    generate_workspace_instructions(run_data)
    
    run_data["status"] = "archived_and_cleared"
    run_data["archive_directory"] = dest_dir
    save_state(state)
    print(f"[Success] State tracker updated. Run {active_id} status is now ''archived_and_cleared''.")

if __name__ == "__main__":
    main()
