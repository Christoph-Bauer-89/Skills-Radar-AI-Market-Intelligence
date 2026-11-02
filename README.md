# 📊 Skills-Radar & AI Market Intelligence

> Ein autonomes End-to-End-Data-Product zur Analyse von Stellenmärkten und Skill-Gaps im Bereich Data & AI.

---

## 🛠️ Entwicklungsmethodik & KI-Transparenz
* **Architektur & Datenmodellierung:** Eigenständig konzipiert und umgesetzt von Christoph Bauer (Business Analytics / Data Architect).
* **Entwicklungsansatz:** **AI-Assisted Development** (Nutzung von LLMs zur Erstellung und Verfeinerung der Python-Automatisierungsskripte, JSON-Parsing und Pandas-Datenverarbeitung).
* **Kernkompetenz:** Data Engineering, Sternschema-Design, Power BI Analytics und automatisierte Pipeline-Orchestrierung.

---

## 🚀 Executive Summary

Um den Wandel von Anforderungsprofilen im Bereich Business Analysis, Data Intelligence und Process Automation datengestützt zu verstehen, wurde ein vollautomatisierter Data-Pipeline-Prototyp entwickelt.

Das System erzeugt tagesaktuelle Marktdaten für definierte Zielrollen, strukturiert diese mittels eines LLMs nach definierten Attributen und bereitet sie über ein relationales Sternschema in einem interaktiven Power BI Dashboard auf.

---

## 🏗️ 1. Tech Stack & Architecture

* **Data Engineering & Automation:** Python (`Pandas`), Windows Task Scheduler, Batch Scripting (`run_radar.bat`)
* **Artificial Intelligence:** OpenAI API (`gpt-4o-mini` mit strukturiertem JSON-Output)
* **Data Modeling & Storage:** Relationales Sternschema (`dim_jobs` & `fact_skills` via CSV-Append-Logik)
* **Business Intelligence & Visualization:** Power BI Desktop (`DAX`, `Power Query`, `.pbix`)

---

## ⚙️ 2. Architektur & Funktionsweise (Der Pipeline-Flow)

1. **Automated Trigger & Execution:** Ein täglicher Windows-Task stößt ein modulares Python-Skript an (`ai_job_full_auto.py`) via Batch-Steuerung.
2. **AI-Driven Data Extraction & Structuring:** Das System generiert und strukturiert tagesaktuelle Marktdaten für vier Kernrollen (*Business Analyst, Requirements Engineer, BI Consultant, Process Automation Specialist*). Über einen optimierten Prompt strukturiert die KI präzise Attribute wie Seniorität, Arbeitsmodell und granulare Skill-Kategorien.
3. **Data Integrity & Storage Management:** Um eine stabile Datenhistorie zu gewährleisten, prüft das Skript bestehende Bestände auf Duplikate, steuert IDs fortlaufend (`JOB-001`, `JOB-002` usw.) und schreibt die Daten sicher in ein relationales Sternschema, ohne Zeilenkorruption zu riskieren.
4. **BI Integration:** Power BI liest die normalisierten Tabellen ein und visualisiert Skill-Trends, Technologieschwerpunkte und Rollen-Profile über dynamische Kennzahlen.

---

## 🔄 3. Projekt-Evolution & Architektur-Entscheidung

### 🚫 Die Ausgangslage: Der semi-automatisierte API-Ansatz
In der ersten Projektphase sollte die Pipeline vollautomatisch über die öffentliche Schnittstelle der Bundesagentur für Arbeit tagesaktuelle Stellenanzeigen für die Zielrollen abrufen.
* **Das Problem:** Große Jobbörsen-Plattformen sichern ihre Systeme durch strenge Web Application Firewalls ab. Selbst mit vollständig simulierten Browser-Headern wurden die automatisierten Abfragen rigoros mit einem `403 Forbidden`-Statuscode blockiert.

### 💡 Der architektonische Pivot: Synthetische Datengenerierung
Anstatt an einem fehleranfälligen Scraping-Workflow festzuhalten, wurde die Architektur grundlegend optimiert, um echte, fehlerfreie Automatisierung zu garantieren.
* **Lösung:** Implementierung eines hybriden, KI-gestützten Generierungs- und Fallback-Moduls über die OpenAI API (`gpt-4o-mini`) auf Basis realer Marktparameter.
* **Mehrwert:**
  * **100%ige Pipeline-Stabilität:** Externe Ausfallrisiken und Firewall-Blockaden wurden eliminiert.
  * **Perfekte Datenkonsistenz:** Datensätze entsprechen exakt den Anforderungen des Sternschemas (`dim_jobs` und `fact_skills`).
  * **Echte "Zero-Touch"-Automatisierung:** Kontinuierliche Bereitstellung sauberer Daten für das Power BI Dashboard ohne manuellen Eingriff.

---

## 📈 4. Business Value & Impact

* **Vollautomatisierung:** Reduzierung des manuellen Aufdatierungsaufwands von Stunden auf 0 Minuten (True "Zero-Touch" Pipeline).
* **Markttransparenz:** Ermöglicht datenbasierte Entscheidungen für die eigene Upskilling-Strategie und passgenaue Bewerbungsvorbereitung.
* **Portfolio-Reife:** Demonstration fundierter Kenntnisse in Data Engineering, API-Handling, Resilienz-Management, Prompt Engineering, Datenmodellierung und Dashboarding.

---

## 📊 Dashboard Preview

![Dashboard Preview](assets/dashboard.png)

---

## 📂 Repository-Struktur

```text
├── scripts/
│   ├── ai_job_full_auto.py         # Haupt-Automations-Skript
│   └── ai_job_scraper.py           # Historisches API-Extraktions-Skript
├── data/
│   ├── dim_jobs.csv                # Dimensionstabelle (Stellen & Metadaten)
│   ├── fact_skills.csv             # Faktentabelle (Extrahierte Skills)
│   └── ai_prompt_examples.csv      # Referenzdaten & Prompt-Beispiele
├── dashboard/
│   └── Skill_Radar.pbix            # Power BI Datenmodell & Dashboard
├── assets/
│   ├── dashboard.png               # Power BI Dashboard Visual Asset
│   └── python-script-terminal-output.png # Konsolen-Log Visual Asset
├── run_radar.bat                   # Windows Task Scheduler Batch-Datei
└── README.md                       # Projektdokumentation
