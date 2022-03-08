import matplotlib as matplotlib
from matplotlib import pyplot as plt
import numpy as np
import csv

states = ['alabama', 'alaska', 'arizona', 'arkansas', 'california',
          'colorado', 'connecticut', 'delaware', 'district of columbia', 'florida',
          'georgia', 'hawaii', 'idaho', 'illinois', 'indiana',
          'iowa', 'kansas', 'kentucky', 'louisiana', 'maine',
          'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi',
          'missouri', 'montana', 'nebraska', 'nevada', 'new hampshire',
          'new jersey', 'new mexico', 'new york', 'north carolina', 'north dakota',
          'ohio', 'oklahoma', 'oregon', 'pennsylvania', 'rhode island',
          'south carolina', 'south dakota', 'tennessee', 'texas', 'utah',
          'vermont', 'virginia', 'washington', 'west virginia', 'wisconsin',
          'wyoming']

userState = input('Enter what state you are from (type zero to look at every state): ')
if userState in states:
    userState = userState.lower()
else:
    userState = 0
userAge = int(input('Enter your age as long as it is at least 25 (type zero to look at every age): '))
if userAge < 25:
    userAge = 0
userSex = input('Enter if you are male or female (type zero to look at both sexes): ')
if userSex.lower() == 'male' or userSex.lower() == 'female':
    userSex = userSex.lower()
else:
    userSex = 0
rating = input('Enter a 1-100 rating (separated by commas with no spaces) for each of the following subjects in order '
                '(type zero to skip this step)\nScience and Engineering, Science and Engineering Related, Business, '
                'Education, and Arts/Humanities/Other: ')
rating = rating.split(",")
if len(rating) == 5:
    rating[0] = int(rating[0]) / 100
    rating[1] = int(rating[1]) / 100
    rating[2] = int(rating[2]) / 100
    rating[3] = int(rating[3]) / 100
    rating[4] = int(rating[4]) / 100
else:
    rating = 0
graph = {
    'Science': 0.0,
    'Science Related': 0.0,
    'Business': 0.0,
    'Education': 0.0,
    'Arts and Others': 0.0
}
graph2 = {
    'Science': 0.0,
    'Science Related': 0.0,
    'Business': 0.0,
    'Education': 0.0,
    'Arts and Others': 0.0
}
fig, (ax1, ax2) = plt.subplots(2)

def challenge():
    reader = csv.DictReader(open('challenge.csv'))
    denominator = 0
    for row in reader:
        state = row['State']
        sex = row['Sex']
        age = row['Age Group']

        if userState == state.lower():
            if 25 <= userAge <= 39 and age == '25 to 39':
                if userSex == 'female' and sex == 'Female':
                    graph['Science'] = int(row['Science and Engineering'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Science Related'] = int(
                        row['Science and Engineering Related Fields'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Business'] = int(row['Business'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Education'] = int(row['Education'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Arts and Others'] = int(row["Arts, Humanities and Others"].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                elif userSex == 'male' and sex == 'Male':
                    graph['Science'] = int(row['Science and Engineering'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Science Related'] = int(
                        row['Science and Engineering Related Fields'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Business'] = int(row['Business'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Education'] = int(row['Education'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Arts and Others'] = int(row["Arts, Humanities and Others"].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                elif userSex == 0 and sex == 'Total':
                    graph['Science'] = int(row['Science and Engineering'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Science Related'] = int(
                        row['Science and Engineering Related Fields'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Business'] = int(row['Business'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Education'] = int(row['Education'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Arts and Others'] = int(row["Arts, Humanities and Others"].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
            elif 40 <= userAge <= 64 and age == '40 to 64':
                if userSex == 'female' and sex == 'Female':
                    graph['Science'] = int(row['Science and Engineering'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Science Related'] = int(
                        row['Science and Engineering Related Fields'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Business'] = int(row['Business'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Education'] = int(row['Education'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Arts and Others'] = int(row["Arts, Humanities and Others"].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                elif userSex == 'male' and sex == 'Male':
                    graph['Science'] = int(row['Science and Engineering'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Science Related'] = int(
                        row['Science and Engineering Related Fields'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Business'] = int(row['Business'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Education'] = int(row['Education'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Arts and Others'] = int(row["Arts, Humanities and Others"].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                elif userSex == 0 and sex == 'Total':
                    graph['Science'] = int(row['Science and Engineering'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Science Related'] = int(
                        row['Science and Engineering Related Fields'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Business'] = int(row['Business'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Education'] = int(row['Education'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Arts and Others'] = int(row["Arts, Humanities and Others"].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
            elif 65 <= userAge and age == '65 and older':
                if userSex == 'female' and sex == 'Female':
                    graph['Science'] = int(row['Science and Engineering'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Science Related'] = int(
                        row['Science and Engineering Related Fields'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Business'] = int(row['Business'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Education'] = int(row['Education'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Arts and Others'] = int(row["Arts, Humanities and Others"].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                elif userSex == 'male' and sex == 'Male':
                    graph['Science'] = int(row['Science and Engineering'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Science Related'] = int(
                        row['Science and Engineering Related Fields'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Business'] = int(row['Business'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Education'] = int(row['Education'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Arts and Others'] = int(row["Arts, Humanities and Others"].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                elif userSex == 0 and sex == 'Total':
                    graph['Science'] = int(row['Science and Engineering'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Science Related'] = int(
                        row['Science and Engineering Related Fields'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Business'] = int(row['Business'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Education'] = int(row['Education'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Arts and Others'] = int(row["Arts, Humanities and Others"].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
            elif userAge == 0 and age == '25 and older':
                if userSex == 'female' and sex == 'Female':
                    graph['Science'] = int(row['Science and Engineering'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Science Related'] = int(
                        row['Science and Engineering Related Fields'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Business'] = int(row['Business'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Education'] = int(row['Education'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Arts and Others'] = int(row["Arts, Humanities and Others"].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                elif userSex == 'male' and sex == 'Male':
                    graph['Science'] = int(row['Science and Engineering'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Science Related'] = int(
                        row['Science and Engineering Related Fields'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Business'] = int(row['Business'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Education'] = int(row['Education'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Arts and Others'] = int(row["Arts, Humanities and Others"].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                elif userSex == 0 and sex == 'Total':
                    graph['Science'] = int(row['Science and Engineering'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Science Related'] = int(
                        row['Science and Engineering Related Fields'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Business'] = int(row['Business'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Education'] = int(row['Education'].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
                    graph['Arts and Others'] = int(row["Arts, Humanities and Others"].replace(',', '')) / int(
                        row["Bachelor's Degree Holders"].replace(',', ''))
        elif userState == 0:
            if 25 <= userAge <= 39 and age == '25 to 39':
                if userSex == 'female' and sex == 'Female':
                    graph['Science'] += int(row['Science and Engineering'].replace(',', ''))
                    graph['Science Related'] += int(row['Science and Engineering Related Fields'].replace(',', ''))
                    graph['Business'] += int(row['Business'].replace(',', ''))
                    graph['Education'] += int(row['Education'].replace(',', ''))
                    graph['Arts and Others'] += int(row["Arts, Humanities and Others"].replace(',', ''))
                    denominator += int(row["Bachelor's Degree Holders"].replace(',', ''))
                elif userSex == 'male' and sex == 'Male':
                    graph['Science'] += int(row['Science and Engineering'].replace(',', ''))
                    graph['Science Related'] += int(row['Science and Engineering Related Fields'].replace(',', ''))
                    graph['Business'] += int(row['Business'].replace(',', ''))
                    graph['Education'] += int(row['Education'].replace(',', ''))
                    graph['Arts and Others'] += int(row["Arts, Humanities and Others"].replace(',', ''))
                    denominator += int(row["Bachelor's Degree Holders"].replace(',', ''))
                elif userSex == 0 and sex == 'Total':
                    graph['Science'] += int(row['Science and Engineering'].replace(',', ''))
                    graph['Science Related'] += int(row['Science and Engineering Related Fields'].replace(',', ''))
                    graph['Business'] += int(row['Business'].replace(',', ''))
                    graph['Education'] += int(row['Education'].replace(',', ''))
                    graph['Arts and Others'] += int(row["Arts, Humanities and Others"].replace(',', ''))
                    denominator += int(row["Bachelor's Degree Holders"].replace(',', ''))
            elif 40 <= userAge <= 64 and age == '40 to 64':
                if userSex == 'female' and sex == 'Female':
                    graph['Science'] += int(row['Science and Engineering'].replace(',', ''))
                    graph['Science Related'] += int(row['Science and Engineering Related Fields'].replace(',', ''))
                    graph['Business'] += int(row['Business'].replace(',', ''))
                    graph['Education'] += int(row['Education'].replace(',', ''))
                    graph['Arts and Others'] += int(row["Arts, Humanities and Others"].replace(',', ''))
                    denominator += int(row["Bachelor's Degree Holders"].replace(',', ''))
                elif userSex == 'male' and sex == 'Male':
                    graph['Science'] += int(row['Science and Engineering'].replace(',', ''))
                    graph['Science Related'] += int(row['Science and Engineering Related Fields'].replace(',', ''))
                    graph['Business'] += int(row['Business'].replace(',', ''))
                    graph['Education'] += int(row['Education'].replace(',', ''))
                    graph['Arts and Others'] += int(row["Arts, Humanities and Others"].replace(',', ''))
                    denominator += int(row["Bachelor's Degree Holders"].replace(',', ''))
                elif userSex == 0 and sex == 'Total':
                    graph['Science'] += int(row['Science and Engineering'].replace(',', ''))
                    graph['Science Related'] += int(row['Science and Engineering Related Fields'].replace(',', ''))
                    graph['Business'] += int(row['Business'].replace(',', ''))
                    graph['Education'] += int(row['Education'].replace(',', ''))
                    graph['Arts and Others'] += int(row["Arts, Humanities and Others"].replace(',', ''))
                    denominator += int(row["Bachelor's Degree Holders"].replace(',', ''))
            elif 65 <= userAge and age == '65 and older':
                if userSex == 'female' and sex == 'Female':
                    graph['Science'] += int(row['Science and Engineering'].replace(',', ''))
                    graph['Science Related'] += int(row['Science and Engineering Related Fields'].replace(',', ''))
                    graph['Business'] += int(row['Business'].replace(',', ''))
                    graph['Education'] += int(row['Education'].replace(',', ''))
                    graph['Arts and Others'] += int(row["Arts, Humanities and Others"].replace(',', ''))
                    denominator += int(row["Bachelor's Degree Holders"].replace(',', ''))
                elif userSex == 'male' and sex == 'Male':
                    graph['Science'] += int(row['Science and Engineering'].replace(',', ''))
                    graph['Science Related'] += int(row['Science and Engineering Related Fields'].replace(',', ''))
                    graph['Business'] += int(row['Business'].replace(',', ''))
                    graph['Education'] += int(row['Education'].replace(',', ''))
                    graph['Arts and Others'] += int(row["Arts, Humanities and Others"].replace(',', ''))
                    denominator += int(row["Bachelor's Degree Holders"].replace(',', ''))
                elif userSex == 0 and sex == 'Total':
                    graph['Science'] += int(row['Science and Engineering'].replace(',', ''))
                    graph['Science Related'] += int(row['Science and Engineering Related Fields'].replace(',', ''))
                    graph['Business'] += int(row['Business'].replace(',', ''))
                    graph['Education'] += int(row['Education'].replace(',', ''))
                    graph['Arts and Others'] += int(row["Arts, Humanities and Others"].replace(',', ''))
                    denominator += int(row["Bachelor's Degree Holders"].replace(',', ''))
            elif userAge == 0 and age == '25 and older':
                if userSex == 'female' and sex == 'Female':
                    graph['Science'] += int(row['Science and Engineering'].replace(',', ''))
                    graph['Science Related'] += int(row['Science and Engineering Related Fields'].replace(',', ''))
                    graph['Business'] += int(row['Business'].replace(',', ''))
                    graph['Education'] += int(row['Education'].replace(',', ''))
                    graph['Arts and Others'] += int(row["Arts, Humanities and Others"].replace(',', ''))
                    denominator += int(row["Bachelor's Degree Holders"].replace(',', ''))
                elif userSex == 'male' and sex == 'Male':
                    graph['Science'] += int(row['Science and Engineering'].replace(',', ''))
                    graph['Science Related'] += int(row['Science and Engineering Related Fields'].replace(',', ''))
                    graph['Business'] += int(row['Business'].replace(',', ''))
                    graph['Education'] += int(row['Education'].replace(',', ''))
                    graph['Arts and Others'] += int(row["Arts, Humanities and Others"].replace(',', ''))
                    denominator += int(row["Bachelor's Degree Holders"].replace(',', ''))
                elif userSex == 0 and sex == 'Total':
                    graph['Science'] += int(row['Science and Engineering'].replace(',', ''))
                    graph['Science Related'] += int(row['Science and Engineering Related Fields'].replace(',', ''))
                    graph['Business'] += int(row['Business'].replace(',', ''))
                    graph['Education'] += int(row['Education'].replace(',', ''))
                    graph['Arts and Others'] += int(row["Arts, Humanities and Others"].replace(',', ''))
                    denominator += int(row["Bachelor's Degree Holders"].replace(',', ''))

    if(rating != 0):
        reader = csv.DictReader(open('challenge.csv'))
        diff = [100, 100, 100, 100, 100, 'state', 'sex', 'age group']
        for row in reader:
            diffSum = diff[0] + diff[1] + diff[2] + diff[3] + diff[4]
            denom = int(row["Bachelor's Degree Holders"].replace(',', ''))
            state2 = row['State']
            sex2 = row['Sex']
            age2 = row['Age Group']
            num_sci = int(row['Science and Engineering'].replace(',', '')) / denom
            num_rel = int(row['Science and Engineering Related Fields'].replace(',', '')) / denom
            num_bus = int(row['Business'].replace(',', '')) / denom
            num_edu = int(row['Education'].replace(',', '')) / denom
            num_art = int(row['Arts, Humanities and Others'].replace(',', '')) / denom
            newDiff = [abs(num_sci - rating[0]), abs(num_rel - rating[1]), abs(num_bus - rating[2]),
                   abs(num_edu - rating[3]), abs(num_art - rating[4])]
            sum = newDiff[0] + newDiff[1] + newDiff[2] + newDiff[3] + newDiff[4]

            if sum < diffSum:
                diff[0] = num_sci
                diff[1] = num_rel
                diff[2] = num_bus
                diff[3] = num_edu
                diff[4] = num_art
                diff[5] = state2
                diff[6] = sex2
                diff[7] = age2
        graph2['Science'] = diff[0]
        graph2['Science Related'] = diff[1]
        graph2['Business'] = diff[2]
        graph2['Education'] = diff[3]
        graph2['Arts and Others'] = diff[4]
        keys2 = graph2.keys()
        values2 = graph2.values()


    if userState == 0:
        graph['Science'] = graph['Science'] / denominator
        graph['Science Related'] = graph['Science Related'] / denominator
        graph['Business'] = graph['Business'] / denominator
        graph['Education'] = graph['Education'] / denominator
        graph['Arts and Others'] = graph['Arts and Others'] / denominator
    keys = graph.keys()
    values = graph.values()
    ax1.set_title("Probability of Field of Study")
    ax1.bar(keys, values, width=0.6)
    if rating != 0:
        ax2str = "Closest to: state- " + diff[5] + ", sex- " + diff[6] + ", age- " + diff[7]
        ax2.set_title(ax2str)
        ax2.bar(keys2, values2, width=0.6)
        fig.tight_layout(pad=2.0)
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    challenge()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
