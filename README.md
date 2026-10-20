# 📊 Skills-Radar & AI Market Intelligence

Ein autonomes End-to-End-Data-Product zur Analyse von Stellenmärkten und Skill-Gaps im Bereich Data & AI.

---

## 🚀 Executive Summary

Um den Wandel von Anforderungsprofilen im Bereich Business Analysis, Data Intelligence und Process Automation datengestützt zu verstehen, wurde ein vollautomatisierter Data-Pipeline-Prototyp entwickelt.

Das System erzeugt tagesaktuelle Marktdaten für definierte Zielrollen, strukturiert diese mittels eines LLMs nach definierten Attributen und bereitet sie über ein relationales Sternschema in einem interaktiven Power BI Dashboard auf.

---

## 🛠️ Tech Stack & Architecture

- **Data Engineering & Automation:** Python (`Pandas`), Windows Task Scheduler
- **Artificial Intelligence:** OpenAI API (`GPT-4o-mini` mit strukturiertem JSON-Output)
- **Data Modeling & Storage:** Relationales Sternschema (`dim_jobs` & `fact_skills` via CSV-Append-Logik)
- **Business Intelligence & Visualization:** Power BI Desktop (DAX, Power Query)

![Projekt Dateistruktur](project-file-structure.png)

---

## ⚙️ Architektur & Funktionsweise (Der Pipeline-Flow)

1. **Automated Trigger & Execution:** Ein täglicher Windows-Task stößt ein modulares Python-Skript an (`ai_job_full_auto.py`).
2. **AI-Driven Data Extraction & Structuring:** Das System generiert und strukturiert tagesaktuelle Marktdaten für vier Kernrollen (*Business Analyst, Requirements Engineer, BI Consultant, Process Automation Specialist*). Über einen optimierten Prompt strukturiert die KI präzise Attribute wie Seniorität, Arbeitsmodell und granulare Skill-Kategorien.
3. **Data Integrity & Storage Management:** Um eine stabile Datenhistorie zu gewährleisten, prüft das Skript bestehende Bestände auf Duplikate, steuert IDs fortlaufend (`JOB-001`, `JOB-002` usw.) und schreibt die Daten sicher in ein relationales Sternschema, ohne Zeilenkorruption zu riskieren.
4. **BI Integration:** Power BI liest die normalisierten Tabellen ein und visualisiert Skill-Trends, Technologie-Schwerpunkte und Rollen-Profile über dynamische Kennzahlen.

![Python Script Terminal Output](python-script-terminal-output.png)

---

## 🔄 Projekt-Evolution & Architektur-Entscheidung

### 🚫 1. Die Ausgangslage: Der semi-automatisierte API-Ansatz
In der ersten Projektphase sollte die Pipeline vollautomat
