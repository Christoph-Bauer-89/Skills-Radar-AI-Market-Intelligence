import json
import os
import pandas as pd
from openai import OpenAI

# 1. API KEY SETUP
API_KEY = "----"
client = OpenAI(api_key=API_KEY)

def analyze_job_posting(job_text, new_job_id):
  """Schickt den Text an OpenAI und gibt strukturiertes JSON zurück"""
  prompt = f"""
    Du bist ein KI-Datenanalyst. Analysiere folgenden Stellenanzeigentext und erstelle ein JSON.
    Antworte AUSSCHLIESSLICH mit reinem JSON im folgenden Format:

    {{
      "job_id": "{new_job_id}",
      "job_title": "Titel der Stelle",
      "company_name": "Name des Unternehmens",
      "location": "Ort (z.B. Chemnitz, Leipzig, Remote)",
      "work_model": "Vor-Ort / Hybrid / Remote / Unbekannt",
      "employment_type": "Vollzeit / Teilzeit / Unbekannt",
      "seniority_level": "Junior / Mid-Level / Senior / Lead / Unbekannt",
      "core_role_category": "Business Analysis / AI & Consulting / Data & BI / Tech & Dev",
      "extracted_skills": {{
        "business_analysis": ["Skill1", "Skill2"],
        "data_and_bi": ["Skill1", "Skill2"],
        "ai_and_automation": ["Skill1", "Skill2"],
        "methodologies": ["Skill1", "Skill2"]
      }},
      "required_experience_years": null
    }}

    Text der Stellenanzeige:
    {job_text}
    """

  response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[{"role": "user", "content": prompt}],
      response_format={"type": "json_object"},
      temperature=0.1,
  )

  return json.loads(response.choices[0].message.content)


def append_to_csvs(data):
  """Hängt das Ergebnis automatisch an dim_jobs.csv und fact_skills.csv an

  und stellt sicher, dass am Ende jeder Datei ein Zeilenumbruch existiert.
  """
  for filename in ["dim_jobs.csv", "fact_skills.csv"]:
    if os.path.exists(filename):
      with open(filename, "a+", encoding="utf-8") as f:
        f.seek(0, os.SEEK_END)
        if f.tell() > 0:
          f.seek(f.tell() - 1)
          if f.read(1) != "\n":
            f.write("\n")

  # --- 1. dim_jobs.csv erweitern (exakte Spaltenreihenfolge) ---
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

  df_job = pd.DataFrame([job_row])
  df_job.to_csv(
      "dim_jobs.csv",
      mode="a",
      header=not os.path.exists("dim_jobs.csv"),
      index=False,
      sep=";",
  )

  # --- 2. fact_skills.csv erweitern ---
  skill_rows = []
  category_mapping = {
      "business_analysis": "Business Analysis",
      "data_and_bi": "Data & BI",
      "ai_and_automation": "AI & Automation",
      "methodologies": "Methodologies",
  }

  for cat_key, skills in data["extracted_skills"].items():
    clean_cat_name = category_mapping.get(cat_key, cat_key)
    for skill in skills:
      skill_rows.append({
          "job_id": data["job_id"],
          "skill_category": clean_cat_name,
          "skill_name": skill,
      })

  if skill_rows:
    df_skills = pd.DataFrame(skill_rows)
    df_skills.to_csv(
        "fact_skills.csv",
        mode="a",
        header=not os.path.exists("fact_skills.csv"),
        index=False,
        sep=";",
    )

  print(f"✅ Erfolgreich hinzugefügt: {data['job_title']} ({data['job_id']})")


# --- AUSFÜHRUNG ---
if __name__ == "__main__":
  # Nächste freie ID anpassen (z. B. JOB-012)
  NEW_JOB_ID = "JOB-012"

  # Hier den Text der neuen Stellenanzeige einfügen:
  STELLEN_TEXT = """
    [Kopiere hier den Text der nächsten Stellenanzeige rein]
    """

  print("🤖 KI verarbeitet die Stellenanzeige...")
  result_json = analyze_job_posting(STELLEN_TEXT, NEW_JOB_ID)
  append_to_csvs(result_json)
  print("🎉 Fertig! Öffne Power BI und klicke auf 'Aktualisieren'!")