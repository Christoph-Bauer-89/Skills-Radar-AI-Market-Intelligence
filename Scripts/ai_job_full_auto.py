import json
import os
import random
import re
import pandas as pd
from openai import OpenAI

# 1. SETUP
API_KEY = "----"
client = OpenAI(api_key=API_KEY)


def generate_realistic_job_posting(role):
  """Erzeugt realistische, tagesaktuelle Stellenmarktdaten für die gewünschte Rolle"""
  print(f"🔎 Generiere aktuelle Markt-Stellenanzeige für '{role}'...")

  prompt = f"""
    Erstelle eine realistische, professionelle Stellenanzeige für die Position "{role}" in einem deutschen Unternehmen.
    Die Anzeige soll typische Aufgaben, Anforderungen und geforderte Skills enthalten.
    Antworte AUSSCHLIESSLICH mit reinem JSON im folgenden Format:

    {{
      "job_title": "Realistischer Titel der Stelle",
      "company_name": "Fiktives deutsches Unternehmen GmbH",
      "location": "Berlin (Hybrid)",
      "work_model": "Hybrid",
      "employment_type": "Vollzeit",
      "seniority_level": "Mid-Level",
      "core_role_category": "Business Analysis / AI & Consulting / Data & BI",
      "extracted_skills": {{
        "business_analysis": ["Skill1", "Skill2"],
        "data_and_bi": ["Skill1", "Skill2"],
        "ai_and_automation": ["Skill1", "Skill2"],
        "methodologies": ["Skill1", "Skill2"]
      }},
      "required_experience_years": {random.choice([2, 3, 4, 5])}
    }}
    """

  response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[{"role": "user", "content": prompt}],
      response_format={"type": "json_object"},
      temperature=0.7,
  )

  return json.loads(response.choices[0].message.content)


def append_to_csvs(data):
  """Hängt die extrahierten Daten abgesichert an die CSVs an (inkl. Duplikatsprüfung)"""
  if os.path.exists("dim_jobs.csv"):
    try:
      df_existing = pd.read_csv("dim_jobs.csv", sep=";")
      if (
          not df_existing.empty
          and "job_title" in df_existing.columns
          and "company_name" in df_existing.columns
      ):
        duplikat = df_existing[
            (df_existing["job_title"] == data["job_title"])
            & (df_existing["company_name"] == data["company_name"])
        ]
        if not duplikat.empty:
          print(
              f"⚠️ Stelle '{data['job_title']}' bei"
              f" '{data['company_name']}' existiert bereits. Überspringe..."
          )
          return False
    except Exception:
      pass

  # Korrekte Formatierung und Anhängen an dim_jobs.csv und fact_skills.csv
  for filename in ["dim_jobs.csv", "fact_skills.csv"]:
    if os.path.exists(filename):
      with open(filename, "a+", encoding="utf-8") as f:
        f.seek(0, os.SEEK_END)
        if f.tell() > 0:
          f.seek(f.tell() - 1)
          if f.read(1) != "\n":
            f.write("\n")

  job_row = {
      "job_id": data["job_id"],
      "job_title": data["job_title"],
      "company_name": data["company_name"],
      "location": data["location"],
      "work_model": data["work_model"],
      "employment_type": data["employment_type"],
      "seniority_level": data["seniority_level"],
      "core_role_category": data["core_role_category"],
      "req_exp_years": (
          ""
          if data.get("required_experience_years") is None
          else data.get("required_experience_years")
      ),
  }

  pd.DataFrame([job_row]).to_csv(
      "dim_jobs.csv", mode="a", header=False, index=False, sep=";"
  )

  skill_rows = []
  cat_map = {
      "business_analysis": "Business Analysis",
      "data_and_bi": "Data & BI",
      "ai_and_automation": "AI & Automation",
      "methodologies": "Methodologies",
  }

  for cat_key, skills in data["extracted_skills"].items():
    clean_cat = cat_map.get(cat_key, cat_key)
    for skill in skills:
      skill_rows.append({
          "job_id": data["job_id"],
          "skill_category": clean_cat,
          "skill_name": skill,
      })

  if skill_rows:
    pd.DataFrame(skill_rows).to_csv(
        "fact_skills.csv", mode="a", header=False, index=False, sep=";"
    )

  return True


def get_next_job_id():
  """Ermittelt automatisch die nächste freie JOB-ID"""
  if not os.path.exists("dim_jobs.csv"):
    return "JOB-001"

  try:
    df = pd.read_csv("dim_jobs.csv", sep=";")
    if df.empty or "job_id" not in df.columns:
      return "JOB-001"

    ids = df["job_id"].dropna().tolist()
    numbers = []
    for item in ids:
      match = re.search(r"\d+", str(item))
      if match:
        numbers.append(int(match.group()))

    next_num = max(numbers) + 1 if numbers else 1
    return f"JOB-{next_num:03d}"
  except Exception:
    return "JOB-001"


# --- VOLLAUTOMATISCHER RUN (4 ROLLEN) ---
if __name__ == "__main__":
  TARGET_ROLES = [
      "Business Analyst",
      "Requirements Engineer",
      "BI Consultant",
      "Process Automation Specialist",
  ]

  print(
      "🚀 Starte vollautomatischen Multi-Rollen Import mit Duplikatsprüfung...\n"
  )

  for role in TARGET_ROLES:
    job_data = generate_realistic_job_posting(role)

    next_id = get_next_job_id()
    job_data["job_id"] = next_id

    print(
        f"⚙️ Prüfe Rolle '{role}' -> Titel: '{job_data['job_title']}' ({next_id})"
    )

    success = append_to_csvs(job_data)
    if success:
      print(f"✅ {next_id} erfolgreich integriert!\n")
    else:
      print(f"ℹ️ Übersprungen.\n")

  print("🎉 Vollautomatischer Durchlauf beendet!")
  print("👉 Öffne Power BI und klicke oben auf 'Aktualisieren'!")