USE me_api;

CREATE TABLE profile (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    github VARCHAR(200),
    linkedin VARCHAR(200),
    portfolio VARCHAR(200)
);

CREATE TABLE education (
	id INT AUTO_INCREMENT PRIMARY KEY,
	profile_id INT,
	tenth_marks DECIMAL(5,2),
    twelfth_marks DECIMAL(5,2),
    cgpa DECIMAL(5,2),
    FOREIGN KEY (profile_id) REFERENCES profile(id) ON DELETE CASCADE
    );

CREATE TABLE skills(
	id INT AUTO_INCREMENT PRIMARY KEY,
	profile_id INT,
    name VARCHAR(50),
    FOREIGN KEY (profile_id) REFERENCES profile(id) ON DELETE CASCADE
    );
    
CREATE TABLE projects(
	id INT AUTO_INCREMENT PRIMARY KEY,
    profile_id INT,
    project_name VARCHAR(100),
    project_description TEXT,
    project_skill1 VARCHAR(20),
    project_skill2 VARCHAR(20),
    project_skill3 VARCHAR(20),
    github_link VARCHAR(100),
    FOREIGN KEY (profile_id) REFERENCES profile(id) ON DELETE CASCADE
    );
    
    