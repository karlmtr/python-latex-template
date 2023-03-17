# python-latex-template

Latex templates using Python, TOML configuration files and Jinja2, the templating engine. 

## Requirements

- Python
- $\LaTeX$ (pdflatex, didn't try with the other TeX engines)

## How to use it

Insert the informations in the `.toml` configuration file. Then just run the `create_invoice.py` python script.
```bash
python create_invoice.py <name of the configuration file> <name of the template file>
```
The script will compute de total amount automatically. 

## TODO :
- [ ] Add configuration option for english version
- [ ] Modular code to be able to use with different templates, not necessarly invoice. (separate templating and invoice section)
