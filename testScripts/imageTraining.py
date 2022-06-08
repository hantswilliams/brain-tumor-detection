import pandas as pd 

# read in xlsx data file, first tab only, with no column name
df_no = pd.read_excel('/Users/hantswilliams/Downloads/brainnoyes.xlsx', sheet_name='no', header=None)
df_yes = pd.read_excel('/Users/hantswilliams/Downloads/brainnoyes.xlsx', sheet_name='yes', header=None)

# url for yes 
yesUrl = "https://raw.githubusercontent.com/Moorehe2/Brain-Tumor-Detection/master/augmented%20data/yes/"
noUrl = "https://raw.githubusercontent.com/Moorehe2/Brain-Tumor-Detection/master/augmented%20data/no/"

# keep only rows that begin with aug_ in df_no
df_no = df_no[df_no[0].str.startswith('aug_')]
# for whitespace replace with %
df_no[0] = df_no[0].str.replace(' ', '%20')
# for each row add in the noUrl to the first column
df_no[0] = df_no[0].apply(lambda x: noUrl + x)
# get first row

# keep only rows that begin with aug_ in df_yes
df_yes = df_yes[df_yes[0].str.startswith('aug_')]
# for whitespace replace with %
df_yes[0] = df_yes[0].str.replace(' ', '%20')
# for each row add in the yesUrl to the first column
df_yes[0] = df_yes[0].apply(lambda x: yesUrl + x)



merge = pd.concat([df_no, df_yes])

# save to csv
merge.to_csv('/Users/hantswilliams/Downloads/brainnoyes.csv')
