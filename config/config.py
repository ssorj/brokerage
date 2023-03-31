import os

site_url = os.environ.get("SITE_URL", "")

def path_nav(page):
    separator = "<span class=\"path-separator\">&#8250;</span>"
    links = [x.replace("href=\"", f"href=\"{site_url}") for x in list(page.path_nav_links)[1:]]
    links = separator.join(links)

    return f"<nav class=\"path-nav\">{links}</nav>"

def cell(column_index, value):
    if column_index == 0:
        value = f"<a href=\"{site_url}/address-spaces/build-infra/index.html\">{value}</a>"

    return f"<td>{value}</td>"

headings = "Name", "Clients", "Queues", "Topics", "Created"

data = (
    ("build-infra", 3, 2, 3, "4 hours ago"),
    ("order-processing", 4, 3, 0, "3 days ago"),
    ("cicd-pipeline", 12, 1, 1, "1/8/2020"),
)

address_space_table = html_table(data, headings=headings, cell_fn=cell)

props = (
    ("Name", "build-infra"),
    ("Created", "4 hours ago"),
)

address_space_properties = html_table(props, class_="properties")

def cell(column_index, value):
    if column_index == 0:
        value = f"<a href=\"{site_url}/address-spaces/build-infra/clients/build-infra-36cd/index.html\">{value}</a>"

    return f"<td>{value}</td>"

headings = "Name", "Connections", "Expires", "Created"

data = (
    ("build-infra-36cd", 12, "12/21/2021", "3 minutes ago"),
    ("build-infra-4ed8", 2, "Never", "4 hours ago"),
    ("build-infra-e0d7", 0, "-", "1/1/2020"),
)

client_table = html_table(data, headings=headings, cell_fn=cell)

def cell(column_index, value):
    if column_index == 0:
        value = f"<a href=\"{site_url}/address-spaces/build-infra/queues/jobs/index.html\">{value}</a>"

    return f"<td>{value}</td>"

headings = "Name", "Created"

data = (
    ("jobs", "3 minutes ago"),
    ("commands", "1/1/2020"),
)

queue_table = html_table(data, headings=headings, cell_fn=cell)

def cell(column_index, value):
    if column_index == 0:
        value = f"<a href=\"{site_url}/address-spaces/build-infra/topics/notifications/index.html\">{value}</a>"

    return f"<td>{value}</td>"

headings = "Name", "Created"

data = (
    ("notifications", "4 hours ago"),
    ("agents.alpha", "1/1/2020"),
    ("agents.beta", "1/1/2020"),
)

topic_table = html_table(data, headings=headings, cell_fn=cell)

props = (
    ("Name", "jobs"),
    ("Created", "3 minutes ago"),
)

queue_properties = html_table(props, class_="properties")

props = (
    ("Name", "notifications"),
    ("Created", "4 hours ago"),
)

topic_properties = html_table(props, class_="properties")
