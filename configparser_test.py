import configparser

config = configparser.ConfigParser()
config.read("yoga.config", encoding='utf-8')
ret = config.sections()

print("sections is:{}".format(ret))

db = config.items('db')
print("db sections is: {}".format(db))

db_options = config.options('db')
print("db sections keys is: {}".format(db_options))

v = config.get('db', 'name')
print("db name value is: {}".format(v))

has_sec = config.has_section('db')
print(has_sec)

config.add_section("aws")
config.write(open('yoga.config', 'w'))

config.remove_section('aws')
config.write(open('yoga.config', 'w'))


has_opt = config.has_option('db', 'name')
print(has_opt)

config.remove_option('db', 'name')
config.write(open('yoga.config', 'w'))

config.set('db', 'muisc', 'you are beautiful')
config.write(open('yoga.config', 'w'))

