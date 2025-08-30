from db import db_connect

def get_profile():
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM profile")
    result = cursor.fetchall()
    conn.close()
    return result

# Create project
def create_project(data):
    conn = db_connect
    cursor = conn.cursor()
    query = "INSERT INTO projects (profile_id,project_name,project_description,project_skill1,project_skill2,project_skill3,github_link) VALUES (1,%s, %s,%s,%s,%s,%s)"
    cursor.execute(query, (data["name"], data["description"]), data["skill1"],data["skill2"],data["skill3"],data["ghlink"])
    conn.commit()
    conn.close()
    return {"message": "Project created successfully"}

# Read all projects
def get_projects():
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects")
    result = cursor.fetchall()
    conn.close()
    return result

# Update project
def update_project(project_id, data):
    conn = db_connect()
    cursor = conn.cursor()
    query = "UPDATE projects SET name=%s, description=%s WHERE id=%s"
    cursor.execute(query, (data["name"], data["description"], project_id))
    conn.commit()
    conn.close()
    return {"message": "Project updated successfully"}

# Delete project
def delete_project(project_id):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM projects WHERE id=%s", (project_id,))
    conn.commit()
    conn.close()
    return {"message": "Project deleted successfully"}

# Top skills
def get_top_skills():
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute("SELECT skill, COUNT(*) AS frequency FROM ( SELECT project_skill1 AS skill FROM projects UNION ALL SELECT project_skill2 FROM projects UNION ALL SELECT project_skill3 FROM projects ) AS all_skills WHERE skill IS NOT NULL GROUP BY skill ORDER BY frequency DESC LIMIT 5;")
    result = cursor.fetchall()
    conn.close()
    return result
