def indeed_job_scraper():
    job_results = []
    current_page = 1
    
    job_title = input("Enter your requested job title(e.g Test engineer):")
    location = input("Where are you located (e.g. New York?:")
    
    encoded_job = " + ".join(job_title.split())
    encoded_location = " + ".join(location.split())
    
    base_url = f"https://www.indeed.com/jobs?q={encoded_job}&l={encoded_location}" 