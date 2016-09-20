import json
import time
import requests

class ScheduleApiError(Exception):
    '''
    Raised if there is an error with the schedule API.
    '''
    pass

# The base API endpoint
base_url = 'http://umich-schedule-api.herokuapp.com'

# the amount of time to wait for the schedule API
timeout_duration = 25


def get_data(relative_path):
    '''
    Gets data from the schedule API at the specified path.
    Will raise a ScheduleApiError if unsuccessful.
    Assumes API will return JSON, returns as a dictionary.
    '''

    timeout_at = time.time() + timeout_duration

    while time.time() < timeout_at:
        r = requests.get(base_url + relative_path)
        if r.status_code == 200:
            return json.loads(r.text)
        if r.status_code == 400:
            break

    raise ScheduleApiError('error for url: {0} message: "{1}" code: {2}' \
        .format(relative_path, r.text, r.status_code))

def get_terms():
    '''
    Returns a list of valid terms.
    Each item in the list is a dictionary containing:
        ('TermCode', 'TermDescr', 'TermShortDescr')
    '''
    return get_data('/get_terms')

def get_schools(term_code):
    '''
    Returns a list of valid schools
    Each item in the list is a dictionary containing:
    ...('SchoolDesc', 'SchoolCode', 'SchoolShortDescr')
    '''


    return get_data('/get_schools?term_code={0}'.format(term_code))

def get_catalog_numbers(term_code, school, subject):
    '''
    Returns a list of valid catalog numbers
    Each item in the lsit is a dictionary containing:
    ...('CourseDesc', 'CatalogNumber')
    '''

    a = '/get_catalog_numbers?term_code={0}'.format(term_code)
    b = '&school={0}'.format(school)
    c = '&subject={0}'.format(subject)

    return get_data(a+b+c)

def get_course_description(term_code, school, subject, catalogNum):
    '''
    Returns  valid course descriptions
    '''

    a = '/get_course_description?term_code={0}'.format(term_code)
    b = '&school={0}'.format(school)
    c = '&subject={0}'.format(subject)
    d = '&catalog_num={0}'.format(catalogNum)

    return get_data(a+b+c+d)

def get_sections(term_code, school, subject, catalogNum):
    '''
    Returns a list of valid setions
    Each item in the list is a dictionary containing:
    ...('WaitTotal', 'Meeting', ClassTopic', 'WaitCapacity', etc.)
    '''
    a = '/get_sections?term_code={0}'.format(term_code)
    b = '&school={0}'.format(school)
    c = '&subject={0}'.format(subject)
    d = '&catalog_num={0}'.format(catalogNum)


    return get_data(a+b+c+d)    


def get_subjects(term_code, school):
    '''
    Returns a list of valid subjects.
    Each item is a dictionary containing the components:
        ('SubjectShortDescr', 'SubjectCode','SubjectDescr')
    '''
    a = '/get_subjects?term_code={0}'.format(term_code)
    b = '&school={0}'.format(school)
    
    return get_data(a+b)


def get_section_details(term_code, school, subject, catalogNum, sectionNum):
    '''
    Returns a list of valid sectoin details
    Each item in the lsit is a dictionary containing:
    ...('Instructor', 'WaitTotal', WaitCapacity', etc.)
    '''
    a = '/get_sections?term_code={0}'.format(term_code)
    b = '&school={0}'.format(school)
    c = '&subject={0}'.format(subject)
    d = '&catalog_num={0}'.format(catalogNum)
    e = '&section_num={0}'.format(sectionNum)

    return get_data(a+b+c+d+e)

def get_meetings(term_code, school, subject, catalogNum, sectionNum):
    '''
    Returns a list of valid meetings
    Each item in the lsit is a dictionary containing:
    ...('EndDate', 'MeetingNumber', 'Times', etc.)
    '''
    a = '/get_meetings?term_code={0}'.format(term_code)
    b = '&school={0}'.format(school)
    c = '&subject={0}'.format(subject)
    d = '&catalog_num={0}'.format(catalogNum)
    e = '&section_num={0}'.format(sectionNum)

    return get_data(a+b+c+d+e)

def get_textbooks(term_code, school, subject, catalogNum, sectionNum):
    '''
    Returns a list of valid textbooks
    Each item in the lsit is a dictionary containing:
    ...('CoursePackLocation', 'Textbook', 'ISBN')
    '''
    a = '/get_textbooks?term_code={0}'.format(term_code)
    b = '&school={0}'.format(school)
    c = '&subject={0}'.format(subject)
    d = '&catalog_num={0}'.format(catalogNum)
    e = '&section_num={0}'.format(sectionNum)

    return get_data(a+b+c+d+e)


def get_instructors(term_code, school, subject,
                    catalogNum, sectionNum):
    '''
    Returns a list of valid instructors
    Each item in the lsit is a dictionary containing:
    ...('LastName', 'InstructorName', 'InstructorRole', etc.)
    '''
    a = '/get_instructors?term_code={0}'.format(term_code)
    b = '&school={0}'.format(school)
    c = '&subject={0}'.format(subject)
    d = '&catalog_num={0}'.format(catalogNum)
    e = '&section_num={0}'.format(sectionNum)

    return get_data(a+b+c+d+e)



    

