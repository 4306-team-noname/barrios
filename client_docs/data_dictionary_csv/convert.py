import pandas as pd
import sys

args = sys.argv
# remove the first arg, because the first
# arg when running a python script will
# always be the script's filename
del args[0]

for arg in args:
  df = pd.read_csv(arg)
  mdname = arg.replace('.csv', '.md')
  noextname = arg.replace('.csv', '')
  print('Converting ' + arg + ' to ' + mdname)
  with open(noextname + '.md', 'w') as md:
    df.to_markdown(buf=md, tablefmt='grid')
