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
        'please enter ' + key + ': '
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
entries = {
    "firstName": "",
    "lastName": "",
    "nameLanguage": "",
    "moreNames": "",
    "academicDegrees": "",
    "academicDegreeInSalutation": "",
    "styleInSalutation": "",
    "companyName": "",
    "houseNumber": "",
    "street": "",
    "city": "",
    "postalCode": "",
    "postBox": "",
    "country": "",
}

# some special keys
mandatory_keys = ['firstName', 'lastName', 'nameLanguage']


# get necessary entries
for key in mandatory_keys:
    value = ''
    if key != 'lng':
        while not value:
            value = addr_entry(key)
        entries[key] = value
    else:
        entries[key] = addr_lang(key)


# get the bulk of the data
empty_keys = []
for key in dict.keys(entries):
    # some necessary entries are done elsewhere
    if key not in mandatory_keys:
        entries[key] = addr_entry(key)

        # add empty entries on list to be removed
        if not entries[key]:
            empty_keys.append(key)

# remove empty keys from list
for key in empty_keys:
    del entries[key]


# with open('result.json', 'w') as fp:
#        json.dump(sample, fp)

print(json.dumps(entries, indent=4, sort_keys=True))
