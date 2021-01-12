site_url = ""

def path_nav(page):
    separator = "<span class=\"path-separator\">›</span>"
    links = separator.join(list(page.path_nav_links)[1:])

    return f"<nav class=\"path-nav\">{links}</nav>"

def cell(column_index, value):
    if column_index == 0:
        value = f"<a href=\"/brokers/build-infra/index.html\">{value}</a>"

    return f"<td>{value}</td>"

headings = "Name", "Status", "Size", "Created"

data = (
    ("build-infra", "Active", 2, "4 hours ago"),
    ("order-processing", "Active", 3, "3 days ago"),
    ("notifications", "Disabled", 1, "1/8/2020"),
)

broker_table = html_table(data, headings=headings, cell_fn=cell)

props = (
    ("Name", "build-infra"),
    ("Status", "Active"),
    ("Size", 2),
    ("Persistence enabled", "Yes"),
    ("Message migration enabled", "Yes"),
    ("Image", "registry.redhat.io/amq7/amq-broker:7.8"),
    ("Created", "4 hours ago"),
)

broker_properties = html_table(props, class_="properties")

def cell(column_index, value):
    if column_index == 0:
        value = f"<a href=\"/brokers/build-infra/client-certificates/xxx/index.html\">{value}</a>"

    return f"<td>{value}</td>"

headings = "Name", "Status", "Connections", "Created"

data = (
    ("build-infra-36cd", "OK", 12, "3 minutes ago"),
    ("build-infra-4ed8", "OK", 2, "4 hours ago"),
    ("build-infra-e0d7", "Disabled", 0, "1/1/2020"),
)

client_certificate_table = html_table(data, headings=headings, cell_fn=cell)

def cell(column_index, value):
    if column_index == 0:
        value = f"<a href=\"/brokers/build-infra/addresses/jobs/index.html\">{value}</a>"

    return f"<td>{value}</td>"

headings = "Name", "Status", "Routing type", "Created"

data = (
    ("jobs", "OK", "Anycast", "3 minutes ago"),
    ("notifications", "OK", "Multicast", "4 hours ago"),
    ("agents.alpha", "OK", "Multicast", "1/1/2020"),
    ("agents.beta", "OK", "Multicast", "1/1/2020"),
)

address_table = html_table(data, headings=headings, cell_fn=cell)

props = (
    ("Name", "jobs"),
    ("Status", "OK"),
    ("Routing type", "Anycast"),
    ("Created", "3 minutes ago"),
)

address_properties = html_table(props, class_="properties")

def cell(column_index, value):
    if column_index == 0:
        value = f"<a href=\"/brokers/build-infra/address-settings/%23/index.html\">{value}</a>"

    return f"<td>{value}</td>"

headings = "Address match", "Auto-create queues?", "Auto-delete queues?", "Created"

data = (
    ("# (all addresses)", "Yes", "Yes", "3 minutes ago"),
    ("agents.#", "Yes", "No", "3/15/2020"),
)

address_setting_table = html_table(data, headings=headings, cell_fn=cell)

props = (
    ("Name", "na-east-d45e"),
    ("Status", "OK"),
    ("Site", "na-east (OpenShift)"),
    ("Created", "3 minutes ago",),
)

link_properties = html_table(props, class_="properties")

def cell(column_index, value):
    if column_index == 0:
        value = f"<a href=\"/brokers/build-infra/services/frontend/index.html\">{value}</a>"

    return f"<td>{value}</td>"

headings = "Name", "Status", "Bindings", "Created"

data = (
    ("frontend", "OK", 2, "3 minutes ago"),
    ("inventory", "OK", 1, "4 hours ago"),
    ("orders", "OK", 1, "2 days ago"),
    ("postgres", "OK", 1, "3/15/2020"),
    ("reviews", "Error", 1, "3/15/2020"),
)

service_table = html_table(data, headings=headings, cell_fn=cell)

props = (
    ("Name", "frontend"),
    ("Status", "OK"),
    ("Created", "3 minutes ago",),
)

service_properties = html_table(props, class_="properties")

def cell(column_index, value):
    if column_index == 0:
        value = f"<a href=\"/brokers/build-infra/services/frontend/bindings/frontend-2da6/index.html\">{value}</a>"

    return f"<td>{value}</td>"

headings = "Name", "Status", "Target", "Site", "Created"

data = (
    ("frontend-2da6", "OK", "deployment/frontend", "na-east (OpenShift)", "2 days ago"),
    ("frontend-45cc", "Error", "container/frontend", "na-west (Podman)", "1 day ago"),
)

binding_table = html_table(data, headings=headings, cell_fn=cell)
