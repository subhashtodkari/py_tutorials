
import configparser


def write_to_config_file():
    cp = configparser.ConfigParser()
    cp['DEFAULT'] = {
        'server.name': 'DefaultServerName',
        'server.port': 3030
    }
    cp['DEFAULT']['server.enabled'] = 'False'

    cp['DEV'] = {
        'name': 'www.DEV.com'
    }

    with open('output/config.ini', 'w') as cf:
        cp.write(cf)


if __name__ == "__main__":
    write_to_config_file()
