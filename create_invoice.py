import jinja2 as ja
import os, sys
from subprocess import call
import subprocess
import tomllib

def usage():
    print(f"USAGE : python {sys.argv[0]} <configPath> <templatePath>")

env = ja.Environment(
    block_start_string = r'\BLOCK{',
    block_end_string = r'}',
    variable_start_string = r'\VAR{',
    variable_end_string = r'}',
    comment_start_string = r'\#{',
    comment_end_string = r'}',
    line_statement_prefix = r'%-',
    line_comment_prefix = r'%#',
    trim_blocks = True,
    autoescape = False,
    loader = ja.FileSystemLoader(os.path.abspath("."))
)
if len(sys.argv) != 3 :
    usage()
    exit(1)

configFilename = sys.argv[1]
templateFilename = sys.argv[2]

with open(configFilename, "rb") as f:
    data = tomllib.load(f)

# create new category for computed values 
data["computed"] = {}

total = 0
for key in  data["content"].keys():
    total += float(data["content"][key])

data["computed"]["total"] = f"{total:.2f}"

template = env.get_template(templateFilename)
document = template.render(**data)



with open(f"{os.path.basename(configFilename).split('.')[0]}.tex","w") as f:
    f.write(document)

#
print("Compiling LaTex file...")
retcode = call(["pdflatex","-halt-on-error","-interaction nonstopmode",f"{os.path.basename(configFilename).split('.')[0]}.tex"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL  )
if retcode :
    print("Error in Latex, please look at the log files")
    print("Aborting")
else:
    print("Removing auxiliary files")
    # NOTE: would be better to use subprocess.call
    os.system("rm *.aux *.log *.tex")
    













