class CV:
    def __init__(self, name, email, phone, address,
                 education=None, experience=None,
                 about=None, skills=None, languages=None):
        self.name = name
        self.email = email
        self.__phone = phone
        self.address = address
        self.education = education or []
        self.experience = experience or []
        self.about = about
        self.skills = skills or []
        self.languages = languages or []

    def add_education(self, degree, university, year, location, details):
        self.education.append({'degree': degree, 'university': university,
                               'year': year, 'location': location, 'details': details})

    def add_experience(self, position, company, year, location, details):
        self.experience.append({'position': position, 'company': company,
                                'year': year, 'location': location, 'details': details})

    def add_about(self, about):
        self.about = about

    def add_skills(self, skills):
        self.skills = skills

    def add_languages(self, language, level):
        self.languages.append({'language': language, 'level': level})

    def get_phone(self):
        return self.__phone


my_cv = CV('Bianca Olaru', 'olaru.bianca@yahoo.com', '0756089933', 'Iasi, Romania')

my_cv.add_about(['Motivated, adaptable and responsible professional'
                 ' currently studying about software development and machine learning.'
                 ' Experienced in various platforms and languages and passionate'
                 ' about discovering the latest technologies.',
                'My other hobbies include reading, yoga, swimming and hiking.'])
my_cv.add_skills(['Python (Selenium, Django, Flask and others)', 'Postman, REST API'
                  'JavaScript, React, Typescript', 'HTML, CSS', 'Fast learner', 'Highly organised',
                  'Problem-solving', 'Analytical thinking', 'Positive attitude',
                  'Project management', 'Marketing and brand management',
                  'Customer service'])

my_cv.add_languages('Romanian', 'Native')
my_cv.add_languages('English', 'Proficient')
my_cv.add_languages('French', 'Intermediate')

my_cv.add_education('Junior Programmer: Python and QA Testing', 'IT Factory', '2023-2024', 'Iasi, RO',
                    'This 8 month course helped me start my journey in software development with a hands-on approach, '
                    'working with trainers on different projects in Python. It involved learning thoroughly '
                    'about back-end development for 4 months, followed by an in-depth automated testing module using Selenium and Postman.')
my_cv.add_education('BSc Events Management', 'Canterbury Christ Church University', '2018-2021',
                    'Canterbury, Kent, UK', 'During university I learned about project management, '
                                            'marketing, accounting and research and data analysis, gaining business management, organisational '
                                            'and problem-solving skills through both a theoretical and practical approach.')


my_cv.add_experience('Bookstore Assistant', 'One Distribution Company', '2021 - present', 'Iasi, RO',
                     [
                         'Promoted positive communication and excellent service.',
                         'Organised marketing events.',
                         'Used problem-solving strategies to rectify difficulties quickly and effectively.',
                         'Supervised and mentored junior team members.',
                         'Reviewed and compared sales performance to meet desired targets.'])
my_cv.add_experience('Bartender', 'Jones Nightclubs LTD', '2019-2021', 'Canterbury, Kent, UK',
                     [
                         'Mixed drinks and served wine, beer and non-alcoholic beverages for multiple guests simultaneously.',
                         'Monitored supply levels and generated purchase orders for bar inventory.',
                         'Maintained facility compliance with health codes, sanitation requirements and licence regulations.'])

