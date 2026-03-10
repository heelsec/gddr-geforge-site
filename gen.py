import os 
from jinja2 import Template, Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('.'), lstrip_blocks=True, trim_blocks=True)
template = env.get_template("index.tmpl")

files = os.listdir("faqs")

faqs = []
files.sort()

TOPIC_CATEGORIES = [
    "",
    "Miscellaneous"
]

faq_groups = {idx : (group, []) for idx, group in enumerate(TOPIC_CATEGORIES)}
for f in files:
    if f[-5:] != ".html":
        continue

    group, _ = f.split("-", 1)
    group = int(group) - 1

    with open(f"faqs/{f}", "r") as f:
        q = f.readline().strip()
        a = f.readlines()
        faq_groups[group][1].append((q, "\n".join([l.strip() for l in a])))
        

with open("index.html", "w") as f:
    f.write(template.render(faq_groups=faq_groups))

