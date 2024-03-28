import xmltodict
import yaml
import os

# Define the target folder
folder = r"D:\University\FYP\Data"

# Iterate through all the files in the target folder
for filename in os.listdir(folder):
    # Check if the file is an XML file
    if filename.endswith(".xml"):
        # Construct the full paths to the XML file and YAML file
        xml_filepath = os.path.join(folder, filename)
        yaml_filepath = os.path.join(folder, filename[:-4] + ".yaml")

        # Read the XML file
        with open(xml_filepath) as xml_file:
            xml_string = xml_file.read()

        # Convert the XML string to a Python dictionary
        python_dict = xmltodict.parse(xml_string)

        # Open a new YAML file and write the Python dictionary to it
        with open(yaml_filepath, "w") as yaml_file:
            yaml.dump(python_dict, yaml_file)