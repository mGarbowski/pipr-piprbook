# Generate python code from Qt designer templates using pyside2-uic

templates_dir="./gui/ui_component_templates"
components_dir="./gui/ui_components"

for file in "$templates_dir"/*.ui
do
  filename=$(basename $file)
  new_filename="ui_$(echo $filename | sed s/".ui"/".py"/)"
  new_file_path="$components_dir/$new_filename"
  pyside2-uic $file > $new_file_path
done