# ⚙️ Automated Sales Lead Routing & Scoring Engine

A proof-of-concept microservice architecture built to ingest, score, and dynamically route e-commerce leads into a Notion CRM without duplicates. 


## 📖 The Business Problem
Sales teams operating out of Notion often face data integrity issues (duplicate leads) and lack automated triage. When high-value leads are treated the same as low-value leads, conversion rates drop.

## 🛠️ The Solution
I engineered an automated pipeline using **Make.com**, **Notion**, and a custom **Python (FastAPI)** microservice to act as the "brain" of the operation.

### System Architecture
![Make.com Architecture Blueprint](<img width="1364" height="681" alt="screencapture-eu1-make-724499-scenarios-5780668-edit-2026-05-26-11_47_13" src="https://github.com/user-attachments/assets/9a801913-1110-4c5e-a8a0-0755ae493fc9" />
)

1. **Ingestion:** A webhook intercepts incoming JSON payloads (simulating a Shopify/storefront purchase).
2. **The Python Brain (main.py):** Make.com passes the payload to a custom Python API. The script evaluates the cart value, region, and acquisition channel to calculate a dynamic `Priority Score` and returns it to the pipeline.
3. **The Bouncer (Data Integrity):** The system queries the live Notion database to check if the email already exists, preventing duplicate entries.
4. **Dynamic Routing:** * **New Leads:** If no match is found, a new row is created in Notion with the calculated score.
   * **Existing Leads:** If a match is found, the system updates the existing Notion row with the new elevated Priority Score, alerting the sales agent to the up-sell opportunity.

## 💻 Tech Stack
* **Python 3.10+** (FastAPI, Pydantic)
* **Make.com** (Orchestration, Routing, API Integration)
* **Notion API** (CRM Database, Page ID Indexing)

## 🚀 How to Run Locally
1. Clone this repository.
2. Install dependencies: `pip install fastapi uvicorn pydantic`
3. Run the scoring API: `uvicorn main:app --reload`
4. Post JSON payloads to `http://localhost:8000/score-lead`
