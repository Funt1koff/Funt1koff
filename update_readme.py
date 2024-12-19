from datetime import datetime

# Даты начала опыта
experience_dates = {
    "Java": datetime(2022, 8, 1),
    "Spring": datetime(2023, 2, 1),
    "Hibernate": datetime(2023, 2, 1),
    "HTML": datetime(2023, 7, 1),
    "CSS": datetime(2023, 7, 1),
    "Maven": datetime(2021, 2, 1),
    "Postgres": datetime(2021, 2, 1),
    "Git": datetime(2021, 2, 1),
    "Docker": datetime(2023, 2, 1),
    "OpenApi": datetime(2024, 3, 1),
}

# Вычисление опыта
def calculate_experience(start_date):
    current_date = datetime.now()
    delta = current_date - start_date
    years = delta.days // 365
    months = (delta.days % 365) // 30
    if years > 0:
        return f"{years} year(s)"
    else:
        return f"{months} month(s)"

# Генерация текста
def generate_readme():
    with open("README.md", "w", encoding="utf-8") as file:
        file.write("# My GitHub Profile\n\n")
        file.write("## :hammer_and_wrench: Languages and Tools :\n\n")
        
        tools = {
            "Java": "https://github.com/devicons/devicon/blob/master/icons/java/java-original-wordmark.svg",
            "Spring": "https://github.com/devicons/devicon/blob/master/icons/spring/spring-original-wordmark.svg",
            "Hibernate": "https://github.com/devicons/devicon/blob/master/icons/hibernate/hibernate-original-wordmark.svg",
            "HTML": "https://github.com/devicons/devicon/blob/master/icons/html5/html5-original.svg",
            "CSS": "https://github.com/devicons/devicon/blob/master/icons/css3/css3-plain-wordmark.svg",
            "Maven": "https://github.com/devicons/devicon/blob/master/icons/maven/maven-original-wordmark.svg",
            "Postgres": "https://github.com/devicons/devicon/blob/master/icons/postgresql/postgresql-original-wordmark.svg",
            "Git": "https://github.com/devicons/devicon/blob/master/icons/git/git-original-wordmark.svg",
            "Docker": "https://github.com/devicons/devicon/blob/master/icons/docker/docker-original-wordmark.svg",
            "OpenApi": "https://github.com/devicons/devicon/blob/master/icons/openapi/openapi-original.svg",
        }

        for tool, icon_url in tools.items():
            experience = calculate_experience(experience_dates[tool])
            file.write(
                f"- ![{tool}]({icon_url}) **{tool}**: {experience} of experience.\n"
            )

# Обновление README.md
generate_readme()
