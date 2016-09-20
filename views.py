from flask import render_template, request
from app import app
from schedule_api import *

@app.route('/')
def index():
    options = {}
    options['terms'] = get_terms()
    return render_template('index.html', **options)
@app.route('/get_schools&term_code=<term_code>')
def schools(term_code):
	schools = {}
	schools['schools'] = get_schools(term_code)
	return render_template('schools.html', term_code = term_code,  **schools)
@app.route('/get_subjects&term_code=<term_code>&school=<school_code>')
def subjects(term_code, school_code):
	subjects = {}
	subjects['subjects'] = get_subjects(term_code, school_code)
	return render_template('subjects.html', term_code = term_code, school_code= school_code, **subjects)
@app.route('/get_catalogs&term_code=<term_code>&school=<school_code>&subject=<subject_code>')
def catalogs(term_code, school_code, subject_code):
	catalogs = {}
	catalogs['catalogs'] = get_catalog_numbers(term_code, school_code, subject_code)
	return render_template('catalogs.html', term_code = term_code, school_code= school_code, subject_code= subject_code, **catalogs)
@app.route('/get_courses&term_code=<term_code>&school=<school_code>&subject=<subject_code>&catalog_code=<catalog_code>')
def courses(term_code, school_code, subject_code, catalog_code):
	description = get_course_description(term_code, school_code, subject_code, catalog_code)
	sections = {}
	sections['sections'] = get_sections(term_code, school_code, subject_code, catalog_code)
	return render_template('courses.html', term_code = term_code, school_code= school_code, subject_code= subject_code, catalog_code= catalog_code, description= description, **sections)
@app.route('/get_sections&term_code=<term_code>&school=<school_code>&subject=<subject_code>&catalog_code=<catalog_code>&section_code=<section_code>')
def section_details(term_code, school_code, subject_code, catalog_code, section_code):
	details = {}
	details['details'] = get_meetings(term_code, school_code, subject_code, catalog_code, section_code)
	return render_template('details.html', term_code = term_code, school_code= school_code, subject_code= subject_code, catalog_code= catalog_code, section_code= section_code, **details)
@app.route('/get_instructors&term_code=<term_code>&school=<school_code>&subject=<subject_code>&catalog_code=<catalog_code>&section_code=<section_code>')
def instructors(term_code, school_code, subject_code, catalog_code, section_code):
	instructors = {}
	instructors['instructors'] = get_instructors(term_code, school_code, subject_code, catalog_code, section_code)
	return render_template('instructors.html',term_code = term_code, school_code= school_code, subject_code= subject_code, catalog_code= catalog_code, section_code= section_code, **instructors)
@app.route('/get_textbooks&term_code=<term_code>&school=<school_code>&subject=<subject_code>&catalog_code=<catalog_code>&section_code=<section_code>')
def textbooks(term_code, school_code, subject_code, catalog_code, section_code):
	textbooks = {}
	textbooks['textbooks'] = get_textbooks(term_code, school_code, subject_code, catalog_code, section_code)
	return render_template('textbooks.html',term_code = term_code, school_code= school_code, subject_code= subject_code, catalog_code= catalog_code, section_code= section_code, **textbooks)
@app.route('/get_locations&term_code=<term_code>&school=<school_code>&subject=<subject_code>&catalog_code=<catalog_code>&section_code=<section_code>&location_code=<location_code>')
def location(term_code, school_code, subject_code, catalog_code, section_code, location_code):
	locations = {}
	room_number, building_code = location_code.split()
	locations = {"A&AB": "Art and Architecture Building", "AH": "Angell Hall", "AL": "Walter E. Lay Automotive Lab", "ALH": "Alice Lloyd Hall", "ANNEX": "Public Policy Annex, 1015 E. Huron", "ARGUS2": "Argus Building II, Television Center, 408 S. Fourth Street", "ARGUS3": "Argus Building III, 416 S. Fourth Street", "ARR": "Location to be Arranged", "BAM HALL": "Blanch Anderson Moore Hall, School of Music", "BELL POOL": "Margaret Bell Pool, Central Campus Recreation Building", "BEYST": "Bob and Betty Beyster Building", "BIOL STAT": "Biological Station", "BMT": "Burton Memorial Tower", "BOT GARD": "Matthaei Botanical Gardens, Dixboro Road", "BSRB": "Biomedical Science Research Building", "BURS": "Bursley Hall", "BUS": "Business Administration", "CAMP DAVIS": "Camp Davis", "CCL": "Clarence Cook Little Building", "CCRB": "Central Campus Recreation Building", "CHEM": "Chemistry Building", "CHRYS": "Chrysler Center", "COMM PARK": "Commerce Park", "COOL": "Cooley Building", "COUZENS": "Couzens Hall", "CPH": "Children's Psychiatric Hospital", "CRISLER": "Crisler Arena", "CCSB": "Campus Safety Services Building, 1239 Kipke Dr.", "DANA": "Dana Building", "DANCE": "Dance Building, 1310 N University Court", "DC": "Duderstadt Center", "DENN": "David M. Dennison Building", "DENT": "Dental Building", "DOW": "Dow Engineering Building", "E-BUS": "Executive Education", "EECS": "Electrical Engineering and Computer Science Building", "EH": "East Hall", "EQ": "East Quadrangle", "ERB1": "Engineering Research Building 1", "ERB2": "Engineering Research Building 2", "EWRE": "Environmental and Water Resources Engineering Building", "FA CAMP": "Fresh Air Camp, Pinckney", "FORD LIB": "Ford Library", "FXB": "Francois-Xavier Bagnoud Building", "GFL": "Gorguze Family Laboratory", "GGBL": "G. G. Brown Laboratory", "GLIBN": "Harlan Hatcher Graduate Library, North", "HH": "Haven Hall", "HUTCH": "Hutchins Hall", "IM POOL": "Intramural Building", "IOE": "Industrial and Operations Engineering Building", "ISR": "Institute for Social Research", "K-BUS": "Kresge Library", "KEC": "Kellogg Eye Center", "KEENE THTR EQ": "Keene Theater, Residential College, East Quadrangle", "KELSEY": "Kelsey Museum of Archaeology", "KHRI": "Kresge Hearing Research Institute", "LANE": "Lane Hall", "LBME": "Lurie Biomedical Engineering Building", "LEAG": "Michigan League", "LEC": "Lurie Engineering Center", "LLIB": "Law Library", "LORCH": "Lorch Hall", "LSA": "Literature, Science, and the Arts Building", "LSI": "Life Sciences Institute", "LSSH": "Law School South Hall", "MARKLEY": "Mary Markley Hall", "MAX KADE": "Max Kade House, 627 Oxford Street", "MH": "Mason Hall", "MHRI": "Mental Health Research Institute", "MLB": "Modern Languages Building", "MONREOCTY HD": "Monroe County Health Department", "MOSHER": "Mosher Jordan Hall", "MOTT": "C. S. Mott Children's Hospital", "MSC1": "Medical Science, Building I", "MSC2": "Medical Science, Building II", "MSRB3": "Medical Science Research, Building III", "NAME": "Naval Architecture and Marine Engineering Building", "NCRB": "North Campus Recreation Building", "NH": "North Hall", "NIB": "300 North Ingalls Building", "400NI": "400 North Ingalls Building", "NORTHVILLEPH": "Northville State Hospital", "NQ": "North Quad", "NS": "Edward Henry Kraus Natural Science Building", "OBL": "Observatory Lodge, 1402 Washington Heights", "PALM": "Palmer Commons", "PHOENIXLAB": "Phoenix Memorial Laboratory", "PIER": "Pierpont Commons", "POWER CTR": "Power Center for the Performing Arts", "RACK": "Horace H. Rackham, School of Graduate Studies", "RAND": "Randall Laboratory", "R-BUS": "Ross School of Business Building", "REVELLI": "William D. Revelli Hall", "ROSS AC": "Stephen M. Ross Academic Center", "RUTHVEN": "A. G. Ruthven Museums Building", "SCHEM": "Glenn E. Schembechler Hall", "SEB": "School of Education Building", "SHAPIRO": "Shapiro Undergraduate Library", "SM": "Earl V. Moore Building, School of Music", "SNB": "School of Nursing Building", "SPH1": "Henry Vaughan Building, School of Public Health I", "SPH2": "Thomas Francis, Jr Building, School of Public Health II", "SRB": "Space Research Building", "SSWB": "School of Social Work Building", "STAMPS": "Stamps Auditorium", "STB": "202 South Thayer Building", "STJOSEPH HOSP": "St. Joseph Mercy Hospital", "STOCKWELL": "Stockwell Hall", "STRNS": "Sterns Building", "T&TB": "Track and Tennis Building", "TAP": "Tappan Hall", "TAUBL": "Learning Resource Center, Taubman Medical Library", "TISCH": "Tisch Hall", "UM HOSP": "University Hospital", "UMMA": "University of Michigan Museum of Art", "UNION": "Michigan Union", "USB": "Undergraduate Science Building", "UTOWER": "University Towers, 1225 S. University", "VETERANSHOSP": "Veterans Administration Hospital", "WASHCTY HD": "Washtenaw County Health Department", "W-BUS": "Wyly Hall", "WDC": "Charles R. Walgreen, Jr. Drama Center", "WEILL": "Joan and Sanford Weill Hall", "WEIS": "Weiser Hall", "WH": "West Hall", "WOMEN'S HOSP": "Women's Hospital"}
	building_name = locations[building_code]
	return render_template('locations.html', building_name = building_name)
@app.route('/specialpage')
def specialpage(specialpage = None):
	return render_template('specialpage.html', specialpage = specialpage)
