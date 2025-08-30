from db import db_connect

def get_profile():
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, github, linkedin FROM profile LIMIT 1;")
    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "github": row[3],
            "linkedin": row[4],
        }
    return {"error": "No profile found"}

def create_project(data):
    conn = db_connect()
    cursor = conn.cursor()
    query = """
        INSERT INTO projects (
            profile_id,
            project_name,
            project_description,
            project_skill1,
            project_skill2,
            project_skill3,
            github_link
        ) VALUES (1, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        data["name"],
        data["description"],
        data["skill1"],
        data["skill2"],
        data["skill3"],
        data["ghlink"]
    ))
    conn.commit()
    conn.close()
    return {"message": "Project created successfully"}


def get_projects():
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, project_name, project_description,
               project_skill1, project_skill2, project_skill3,
               github_link
        FROM projects
    """)
    rows = cursor.fetchall()
    conn.close()

    projects = []
    for row in rows:
        projects.append({
            "id": row[0],
            "name": row[1],
            "description": row[2],
            "skill1": row[3],
            "skill2": row[4],
            "skill3": row[5],
            "github_link": row[6]
        })
    return projects


def update_project(project_id, data):
    conn = db_connect()
    cursor = conn.cursor()
    query = "UPDATE projects SET project_name=%s, project_description=%s WHERE id=%s"
    cursor.execute(query, (data["name"], data["description"], project_id))
    conn.commit()
    conn.close()
    return {"message": "Project updated successfully"}


def delete_project(project_id):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM projects WHERE id=%s", (project_id,))
    conn.commit()
    conn.close()
    return {"message": "Project deleted successfully"}



def get_top_skills():
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT skill, COUNT(*) AS frequency
        FROM (
            SELECT project_skill1 AS skill FROM projects
            UNION ALL
            SELECT project_skill2 FROM projects
            UNION ALL
            SELECT project_skill3 FROM projects
        ) AS all_skills
        WHERE skill IS NOT NULL
        GROUP BY skill
        ORDER BY frequency DESC
        LIMIT 5;
    """)
    rows = cursor.fetchall()
    conn.close()

    skills = []
    for row in rows:
        skills.append({
            "skill": row[0],
            "frequency": row[1]
        })
    return skills