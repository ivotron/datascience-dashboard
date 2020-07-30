#!/usr/bin/env python3

import os
import glob
from jinja2 import Environment, FileSystemLoader


def generate_template(template_type, apps):
    if not apps:
        print("No apps found...")
        return

    file_loader = FileSystemLoader('html-apps')
    env = Environment(loader=file_loader)

    outputs = []
    for app_name in apps:
        template = env.get_template(
            'new_app_{}_template.j2'.format(template_type)
        )
        output = template.render(
            app=app_name
        )
        outputs.append(output)

    template = env.get_template('{}_template.j2'.format(template_type))
    output = template.render(
        new_apps="\n".join(outputs)
    )
    file_content = output

    if template_type == "views":
        with open("app/views.py", 'w') as f:
            f.write(file_content)
    elif template_type == "init":
        with open("app/__init__.py", 'w') as f:
            f.write(file_content)


def generate_layout_template(apps):
    if not apps:
        print("No apps found...")
        return

    file_loader = FileSystemLoader('html-apps')
    env = Environment(loader=file_loader)

    for app_name in apps:
        template = env.get_template('new_app_layout_template.j2')
        output = template.render(
            app=app_name
        )

        with open("app/dashboard/{}.py".format(app_name), 'w') as f:
            f.write(output)


##############################################################################

if __name__ == "__main__":
    generator_dir = "html-apps"
    generator_file = "generate_html.*"
    if os.path.isdir(generator_dir):
        # list files
        apps = os.listdir(generator_dir)
        # filter to only get directory files including generate_html
        apps = [app for app in apps if glob.glob(os.path.join(
            generator_dir,
            app,
            generator_file
        ))]
    else:
        apps = []

    print("Starting layout templates...")
    generate_layout_template(apps)

    # list all python files in app/dashboard
    exceptions = ["__init__.py", "Dash_fun.py"]
    apps = (app for app in os.listdir("app/dashboard") if app.endswith(".py"))
    apps = (app for app in apps if app not in exceptions)
    apps = (app.split(".")[0] for app in apps)
    apps = list(apps)
    apps = sorted(apps)

    print("Starting views templates...")
    generate_template("views", apps)
    print("Starting init templates...")
    generate_template("init", apps)
