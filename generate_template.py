#!/usr/bin/env python3

import os
import glob
import yaml
from jinja2 import Environment, FileSystemLoader

APPS_DIR = "app/dashboard"
JINJA_DIR = "templates/jinja"


def generate_template(template_type, apps):
    if not apps:
        print("No apps found...")
        return

    file_loader = FileSystemLoader(JINJA_DIR)
    env = Environment(loader=file_loader)

    outputs = []
    for app in sorted(configs.keys()):
        template = env.get_template(
            'new_app_{}_template.j2'.format(template_type)
        )
        output = template.render(
            app=app,
            name=configs[app]["name"],
            category=configs[app]["category"]
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

    file_loader = FileSystemLoader(JINJA_DIR)
    env = Environment(loader=file_loader)

    for app_name in apps:
        template = env.get_template('new_app_layout_template.j2')
        output = template.render(
            app=app_name
        )

        if not os.path.isdir(os.path.join(APPS_DIR, app_name)):
            os.mkdir(os.path.join(APPS_DIR, app_name))

        if not os.path.isfile(os.path.join(APPS_DIR, app_name, "__init__.py")):
            with open(os.path.join(APPS_DIR, app_name, "__init__.py")) as f:
                pass

        with open(APPS_DIR + "/{0}/{0}.py".format(app_name), 'w') as f:
            f.write(output)


def read_config(path):
    config = {
        "name": path.split("/")[-2],
        "category": "Dashboard"
    }

    if not os.path.isfile(path):
        return config

    with open(path) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    return config

##############################################################################


if __name__ == "__main__":
    directories = os.listdir(APPS_DIR)

    generator_file = "generate_html.py"
    html_apps = []
    if os.path.isdir(APPS_DIR):
        # filter to only get directory files including generate_html
        html_apps = [app for app in directories if glob.glob(os.path.join(
            APPS_DIR,
            app,
            generator_file
        ))]

    print("html apps found: ", html_apps)

    # get directories with dash apps
    exceptions = []
    app_directories = [app for app in directories
        if os.path.isfile(APPS_DIR + "/{0}/{0}.py".format(app)) and
        app not in exceptions
    ] # noqa

    print("Dash apps found: ", app_directories)

    # get config for each app or use default
    configs = dict()
    for app in app_directories:
        config_path = os.path.join(APPS_DIR, app, "config.yml")
        configs[app] = read_config(config_path)

    # generate files from templates
    print("Generating html-app layouts...")
    generate_layout_template(html_apps)
    print("Generating views.py ...")
    generate_template("views", configs)
    print("Generating __init__.py ...")
    generate_template("init", configs)
