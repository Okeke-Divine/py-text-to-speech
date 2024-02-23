# importing required modules
import subprocess

#program

def execute_unix(inputcommand):
    p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE,shell=True)
    (output, err) = p.communicate()
    return output

a = 'Say something in natural lang.'



c = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % a
execute_unix(c)
print(a)
