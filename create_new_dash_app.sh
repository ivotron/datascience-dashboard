#!/bin/bash

dashboard_dir="app/dashboard"
app_name="$1"
app_dir="${dashboard_dir}/${app_name}"

main="${app_dir}/${app_name}.py"
dash_app="${app_dir}/dash_app.py"
config="${app_dir}/config.yml"

mkdir "${app_dir}"

echo "Created ${app_dir}/__init__.py"
touch "${app_dir}/__init__.py"

echo "Created ${main}"
cp "templates/new_app/main.py" "${main}"

echo "Created ${dash_app}"
cp "templates/new_app/dash_app.py" "${dash_app}"

echo "Created ${config}"
cp "templates/new_app/config.yml" "${config}"
