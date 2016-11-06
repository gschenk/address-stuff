import json


def addr_lang(key):
    """querries for the language, taking posix strings"""
    known = ["de", "cn", "en"]
    line = ''
    while len(line) != 2:
        rawline = input(
            'please enter language '
            + str(known)
            + ': '
        )
        line = rawline.strip()
        if line not in known:
            line = ''
            print("Language key unknown.")


def addr_entry(key):
    """querries the user for address data, cleans it"""

    # getting the input
    rawline = input(
        'please enter ' + jkeys[key] + ': '
    )

    # get rid of trailing whitespace, abbr points
    line = rawline.rstrip('.').strip()

    # replace tabs
    line = line.replace('\t', ' ')

    # remove forbidden strings
    trans_tab = dict.fromkeys(
        map(ord, '\"\'!@#$\\\/'), None
    )

    line = line.translate(trans_tab)

    if rawline != line:
        print(
            'Warning: string has been changed: \''
            + rawline
            + '\' to \''
            + line
            + '\'.'
        )
    return line


# define strings for json keys
jkeys = {
    'fn': "firstName",
    'ln': "lastName",
    'lng': "nativeLanguage",
    'mn': "moreNames",
    'acd': "academicDegrees",
    'aca': "academicDegreeInSalutation",
    'sal': "styleInSalutation",
    'cmp': "companyName",
    'sno': "houseNumber",
    'str': "street",
    'cty': "city",
    'poc': "postalCode",
    'box': "postBox",
    'ctr': "country",
}

# some special keys
mandatory_keys = ['fn', 'ln', 'lng']

# empty copy of the keys
jvals = dict.fromkeys(dict.keys(jkeys))


# get necessary entries
for key in mandatory_keys:
    value = ''
    if key != 'lng':
        while not value:
            value = addr_entry(key)
        jvals[key] = value
    else:
        jvals[key] = addr_lang(key)


# get the bulk of the data
empty_keys = []
for key in dict.keys(jkeys):
    # some necessary entries are done elsewhere
    if key not in mandatory_keys:
        jvals[key] = addr_entry(key)

        # add empty entries on list to be removed
        if not jvals[key]:
            empty_keys.append(key)

# remove empty keys from list
for key in empty_keys:
    del jkeys[key]
    del jvals[key]



#with open('result.json', 'w') as fp:
#        json.dump(sample, fp)


# json structure
jsonStr = json.dumps(
    {
        jkeys['ln']: jvals['ln'],
        jkeys['fn']: jvals['fn']
    },
    sort_keys=True,
    indent=4
)


print(jsonStr)
