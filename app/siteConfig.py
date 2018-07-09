from collections import namedtuple

project_variables = ['brand', 'project_url', 'github_url', 'social_url']
SiteConfig = namedtuple('SiteConfig', " ".join(project_variables))