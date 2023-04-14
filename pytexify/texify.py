"""
    ./pytexify/texify.py

    Author: Fabian R. Lux
    Date:   14-04-2023
"""
import os
import sys
import subprocess

tex_prefix = """\\documentclass{standalone}
\\usepackage{mathtools}

\\begin{document}
$\displaystyle
"""

tex_postfix = """$
\\end{document}
"""

def get_next_filename(base_name, extension):
    """
    Generate a unique filename with a given base name and extension.
    
    The function appends an integer counter to the base name, starting from 1,
    and increments the counter until it finds a non-existing filename.
    
    Args:
        base_name (str): The base name for the file.
        extension (str): The file extension without the leading dot.

    Returns:
        str: A unique filename with the given base name and extension.
    """
    counter = 1
    while True:
        filename = f"{base_name}_{counter}.{extension}"
        if not os.path.exists(filename):
            return filename
        counter += 1
    
def render(tex):
    """
        Render tex
    """

    tex = tex_prefix + tex + tex_postfix

    tex_fname = "aux.tex"

    print(tex)

    with open(tex_fname, "w") as tex_file:
        tex_file.write(tex)

    subprocess.run(["pdflatex", tex_fname]) 
 
    fname = get_next_filename("texify", "pdf")

    subprocess.run(["mv", "aux.pdf" ,fname])
    from time import sleep

    sleep(1)
    subprocess.run(["rm", "./aux.*"])

def read(equation_fname):
    """
        Read the equation stored in the filed equation_fname
    """
    equation = ""
    with open(equation_fname, "r") as equation_file:
        equation = equation_file.read()
    
    return equation

def texify():
    command_line_arguments = sys.argv[1:]

    if len(command_line_arguments)==0:
        raise

    equation_fname = command_line_arguments[0]

    print(equation_fname)

    render(read(equation_fname))

if __name__=='__main__':
    texify()
    

