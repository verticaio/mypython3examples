CREATE TABLE IF NOT EXISTS login (
    id VARCHAR(255) NOT NULL PRIMARY KEY,
    userName LONGTEXT NOT NULL,
    login VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS contacts (
    id VARCHAR(255) NOT NULL PRIMARY KEY,
    name LONGTEXT NOT NULL,
    fk_login VARCHAR(255),
    FOREIGN KEY fk_login(fk_login)
    REFERENCES login(id)
);

CREATE TABLE IF NOT EXISTS PersonalInfo (
    id VARCHAR(255) NOT NULL PRIMARY KEY,
    perinfo_v LONGTEXT NOT NULL,
    perinfo_k LONGTEXT NOT NULL,
    fk_contacts VARCHAR(255),
    FOREIGN KEY fk_PersonalInfo(fk_contacts)
    REFERENCES contacts(id)
);


CREATE TABLE IF NOT EXISTS Numbers (
    id VARCHAR(255) NOT NULL PRIMARY KEY,
    num_v LONGTEXT NOT NULL,
    num_k  LONGTEXT  NOT NULL,
    fk_contacts VARCHAR(255),
    FOREIGN KEY fk_Numbers(fk_contacts)
    REFERENCES contacts(id)
);


CREATE TABLE IF NOT EXISTS Emails (
    id VARCHAR(255) NOT NULL PRIMARY KEY,
    email_v LONGTEXT NOT NULL,
    email_k LONGTEXT NOT NULL,
    fk_contacts VARCHAR(255),
    FOREIGN KEY fk_Emails(fk_contacts)
    REFERENCES contacts(id)
);

CREATE TABLE IF NOT EXISTS SocialProfiles (
    id VARCHAR(255) NOT NULL PRIMARY KEY,
    soc_pro_v LONGTEXT NOT NULL,
    soc_pro_k LONGTEXT NOT NULL,
    fk_contacts VARCHAR(255),
    FOREIGN KEY fk_SocialProfiles(fk_contacts)
    REFERENCES contacts(id)
);

CREATE TABLE IF NOT EXISTS Address (
    id VARCHAR(255) NOT NULL PRIMARY KEY,
    addr_v LONGTEXT NOT NULL,
    addr_k LONGTEXT  NOT NULL,
    fk_contacts VARCHAR(255),
    FOREIGN KEY fk_Address(fk_contacts)
    REFERENCES contacts(id)
);


----------------------------------------------
Solve russian charter problem
ALTER TABLE PersonalInfo MODIFY COLUMN v VARCHAR(255)
CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL;

ALTER DATABASE mybb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


SET FOREIGN_KEY_CHECKS = 0
TRUNCATE table contacts
SET FOREIGN_KEY_CHECKS = 1



ALTER TABLE database.table MODIFY COLUMN col VARCHAR(255)  
    CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL;
--
--
General select and join
SELECT * from login l
join contacts con on con.fk_login=l.id
left join Numbers num on num.fk_contacts=con.id
left join PersonalInfo per on per.fk_contacts=con.id
left join SocialProfiles  social on social.fk_contacts=con.id
left join Emails  em on em.fk_contacts=con.id
--
SELECT userName,login from login l
join contacts con on con.fk_login=l.id
left join Numbers num on num.fk_contacts=con.id where l.userName=Number



for post in get_mongo_db().umongo.find({"_id": ObjectId("5cbc98610cc2d6e69efc4529")}):

SELECT COLUMN_NAME,CHARACTER_SET_NAME FROM information_schema.`COLUMNS` 
WHERE table_schema = "mybb"
AND table_name = "Address"
AND column_name = "fk_contacts";



SELECT COLUMN_NAME,CHARACTER_SET_NAME FROM information_schema.`COLUMNS` 
WHERE table_schema = "mybb"
AND table_name = "Emails"



ALTER TABLE contacts CHANGE name name VARCHAR(140) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL;
ALTER TABLE contacts CHANGE name name VARCHAR(140) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL;

Problem
https://andy-carter.com/blog/saving-emoticons-unicode-from-twitter-to-a-mysql-database 
SET FOREIGN_KEY_CHECKS = 0
TRUNCATE table Address
SET FOREIGN_KEY_CHECKS = 1
--