import yaml

# path to the configuration file
cfgfile = 'address.cfg'

# temporary asgt
handle = 'test_test'

def get_path_filename(handle):
    """ cleans path, combines it"""
    path = yamlPath.strip('/').strip()
    return path + '/' + handle + yamlExtension


# read the configuration file, wherin paths, data
# structures and keys of the yaml input are defined.
with open(cfgfile) as f:
        code = compile(f.read(), cfgfile, 'exec')
        exec(code)


# read address entries from yaml
infile = get_path_filename(handle)
with open(infile, 'r') as fp:
        entries = yaml.load(fp)


# what follows is only an example, print to stdout
for key, val in dict.items(entries):
    if key != 'theAddress':
        print(key, val)

for key, val in dict.items(entries["theAddress"]):
    print(key, val)
