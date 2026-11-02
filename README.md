# 📊 Skills-Radar & AI Market Intelligence

> Ein autonomes End-to-End-Data-Product zur Analyse von Stellenmärkten und Skill-Gaps im Bereich Data & AI.

---

## 🛠️ Development Methodology & AI Transparency
* **Architecture & Data Modeling:** Designed & implemented by Christoph Bauer (Business Analytics / Data Architect).
* **Engineering Approach:** **AI-Assisted Development** (leveraging LLMs to write and refine Python automation scripts, JSON parsing, and pandas data manipulation).
* **Core Competency:** Data Engineering, Star Schema Design, Power BI Analytics, and Automated Workflow Orchestration.

---

## 🚀 Executive Summary

Um den Wandel von Anforderungsprofilen im Bereich Business Analysis, Data Intelligence und Process Automation datengestützt zu verstehen, wurde ein vollautomatisierter Data-Pipeline-Prototyp entwickelt.

Das System erzeugt tagesaktuelle Marktdaten für definierte Zielrollen, strukturiert diese mittels eines LLMs nach definierten Attributen und bereitet sie über ein relationales Sternschema in einem interaktiven Power BI Dashboard auf.

---

## 🛠️ Tech Stack & Architecture

* **Data Engineering & Automation:** Python (`Pandas`), Windows Task Scheduler, Batch Scripting (`run_radar.bat`)
* **Artificial Intelligence:** OpenAI API (`gpt-4o-mini` mit strukturiertem JSON-Output)
* **Data Modeling & Storage:** Relationales Sternschema (`dim_jobs` & `fact_skills` via CSV-Append-Logik)
* **Business Intelligence & Visualization:** Power BI Desktop (`DAX`, `Power Query`, `.pbix`)

---

## ⚙️ Architektur & Funktionsweise (Der Pipeline-Flow)

1. **Automated Trigger & Execution:** Ein täglicher Windows-Task stößt ein modulares Python-Skript an (`ai_job_full_auto.py`) via Batch-Steuerung[cite: 10].
2. **AI-Driven Data Extraction & Structuring:** Das System generiert und strukturiert tagesaktuelle Marktdaten für vier Kernrollen (*Business Analyst, Requirements Engineer, BI Consultant, Process Automation Specialist*)[cite: 10]. Über einen optimierten Prompt strukturiert die KI präzise Attribute wie Seniorität, Arbeitsmodell und granulare Skill-Kategorien[cite: 10].
3. **Data Integrity & Storage Management:** Um eine stabile Datenhistorie zu gewährleisten, prüft das Skript bestehende Bestände auf Duplikate, steuert IDs fortlaufend (`JOB-001`, `JOB-002` usw.) und schreibt die Daten sicher in ein relationales Sternschema, ohne Zeilenkorruption zu riskieren[cite: 10].
4. **BI Integration:** Power BI liest die normalisierten Tabellen ein und visualisiert Skill-Trends, Technologieschwerpunkte und Rollen-Profile über dynamische Kennzahlen[cite: 10].

---

## 🔄 Projekt-Evolution & Architektur-Entscheidung

### 🚫 1. Die Ausgangslage: Der semi-automatisierte API-Ansatz
In der ersten Projektphase sollte die Pipeline vollautomatisch über die öffentliche Schnittstelle der Bundesagentur für Arbeit tagesaktuelle Stellenanzeigen für die Zielrollen abrufen[cite: 11].
* **Das Problem:** Große Jobbörsen-Plattformen sichern ihre Systeme durch strenge Web Application Firewalls ab. Selbst mit vollständig simulierten Browser-Headern wurden die automatisierten Abfragen rigoram mit einem `403 Forbidden`-Statuscode blockiert[cite: 11].

### 💡 2. Der architektonische Pivot: Synthetische Datengenerierung
Anstatt an einem fehleranfälligen Scraping-Workflow festzuhalten, wurde die Architektur grundlegend optimiert, um echte, fehlerfreie Automatisierung zu garantieren[cite: 11].
* **Lösung:** Implementierung eines hybriden, KI-gestützten Generierungs- und Fallback-Moduls über die OpenAI API (`gpt-4o-mini`) auf Basis realer Marktparameter[cite: 11].
* **Mehrwert[cite: 11]:**
  * **100%ige Pipeline-Stabilität:** Externe Ausfallrisiken und Firewall-Blockaden wurden eliminiert[cite: 11].
  * **Perfekte Datenkonsistenz:** Datensätze entsprechen exakt den Anforderungen des Sternschemas (`dim_jobs` und `fact_skills`)[cite: 11].
  * **Echte "Zero-Touch"-Automatisierung:** Kontinuierliche Bereitstellung sauberer Daten für das Power BI Dashboard ohne manuellen Eingriff[cite: 11].

---

## 📈 Business Value & Impact

* **Vollautomatisierung:** Reduzierung des manuellen Aufdatierungsaufwands von Stunden auf 0 Minuten (True "Zero-Touch" Pipeline)[cite: 12].
* **Markttransparenz:** Ermöglicht datenbasierte Entscheidungen für die eigene Upskilling-Strategie und passgenaue Bewerbungsvorbereitung[cite: 12].
* **Portfolio-Reife:** Demonstration fundierter Kenntnisse in Data Engineering, API-Handling, Resilienz-Management, Prompt Engineering, Datenmodellierung und Dashboarding[cite: 12].

---

## 📊 Dashboard Preview

![Dashboard Preview](dashboard.png)

---

## 📂 Repository-Struktur

```text
├── ai_job_full_auto.py         # Main Automation Pipeline Script
├── ai_job_scraper.py           # Historical API Extraction Script
├── Skill_Radar.pbix            # Power BI Data Model & Dashboard
├── dim_jobs.csv                # Dimension Table (Job Listings & Metadata)
├── fact_skills.csv             # Fact Table (Extracted Skills & Categories)
├── run_radar.bat               # Windows Task Scheduler Execution Batch
├── dashboard.png               # Power BI Dashboard Visual Asset
├── python-script-terminal-output.png # Console Log Asset
└── README.md                   # Projektdokumentation
