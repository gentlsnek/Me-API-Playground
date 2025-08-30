USE me_api;

INSERT INTO profile (name,email,github,linkedin) VALUES ("Erwin Pimenta","erwinpimenta1644@gmail.com","https://github.com/gentlsnek","https://www.linkedin.com/in/erwin-pimenta/");

INSERT INTO education (profile_id,tenth_marks,twelfth_marks,cgpa) VALUES (1,88.45,60.10,7.32);

INSERT INTO skills (profile_id,name) VALUES (1,"python"),(1,"golang"),(1,"java"),(1,"SQL"),(1,"HTML/CSS"),(1,"JavaScript"),(1,"BASH"),(1,"git"),(1,"github"),(1,"linux"),(1,"AndroGuard"),(1,"CustomTKinter"),(1,"Scikit-Learn"),(1,"NetCDF4"),
(1,"Flask"),(1,"Seaborn"),(1,"Keras"),(1,"Pandas");

INSERT into projects (profile_id,project_name,project_description,project_skill1,project_skill2,project_skill3,github_link) VALUES
(1,"NetDiagnose","Network Diagnostic Tool made using python and its modules","python","Keras","Scikit-Learn","https://github.com/gentlsnek/NetDiagnose"),
(1,"AndroFuzz","ANFIS based Android Malware Classification","python","Pandas","Androguard","https://github.com/gentlsnek/AndroFuzz-MLC"),
(1,"Missing Data Prediction","Missing satellite data prediction","python","Keras","Scikit-Learn","https://github.com/gentlsnek/internship"),
(1,"WebScrapper-Go","basic webscrapper made using go","golang","Linux","Bash","https://github.com/gentlsnek/webscrapper-go");


