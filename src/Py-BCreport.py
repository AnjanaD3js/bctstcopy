import csv, sys, os, requests


def save_input():
    ''' Downloads file from the url and save it as filename '''
    # check if file already exists
    print(os.getcwd())
    os.chdir(os.path.abspath('../input'))
    print(os.getcwd())
    if not os.path.isfile(filename):
        print('Downloading File')
        response = requests.get(url)
        # Check if the response is ok (200)
        if response.status_code == 200:
            # Open file and write the content
            with open(filename, 'wb') as file:
                # A chunk of 128 bytes
                for chunk in response:
                    file.write(chunk)
    else:
        print('File exists. Updating file...')
        response = requests.get(url)
        # Check if the response is ok (200)
        if response.status_code == 200:
            # Open file and write the content
            os.remove(filename)
            with open(filename, 'wb') as file:
                # A chunk of 128 bytes
                for chunk in response:
                    file.write(chunk)
    os.chdir('../src')
    print(os.getcwd())


def analyse():
    os.chdir(os.path.abspath('../input'))
    with open(filename, 'r') as f:
        reader = csv.DictReader(f, dialect='myd')
        os.chdir('../output')
        try:
            for row in reader:
                # process(row)
                print(row)
        except csv.Error as e:
            sys.exit('file{}, line{}: {}'.format(filename, reader.line_num, e))
        print(reader.fieldnames)
        print(type(reader))
        print(os.getcwd())


def save_output():
    # check if file already exists
    print(os.getcwd())
    os.chdir(os.path.abspath('../input'))
    print(os.getcwd())
    with open(filename1, 'r') as f:
        reader = csv.reader(f, dialect='myd')
        os.chdir('../output')
        print(os.getcwd())
        if not os.path.isfile(filename):
            with open(filename2, 'w', newline='') as op:
                writer = csv.DictWriter(op, fieldnames=["Border", "Date", 'Measure', "Value", "Average"])
                writer.writeheader()
                next(reader)
                writer.writerows(
                    {'Border': row[3], 'Date': row[4], 'Measure': row[5], 'Value': row[6], "Average": 0.00} for row in
                    reader)
        else:
            print('File exists. Updating file...')
            os.remove(filename)
            with open(filename2, 'w', newline='') as op:
                writer = csv.DictWriter(op, fieldnames=["Border", "Date", 'Measure', "Value", "Average"])
                writer.writeheader()
                next(reader)
                writer.writerows(
                    {'Border': row[3], 'Date': row[4], 'Measure': row[5], 'Value': row[6], "Average": 0.00} for row in
                    reader)
    os.chdir('../')
    print(os.getcwd())


url = 'https://data.transportation.gov/api/views/keg4-3bc2/rows.csv?accessType=DOWNLOAD'
filename = 'Border_Crossing_Entry_Data.csv'
csv.register_dialect(
    'myd',
    delimiter=',',
    quotechar='"',
    doublequote=True,
    skipinitialspace=True,
    lineterminator='\r\n',
    quoting=csv.QUOTE_MINIMAL)
filename1 = filename  # data analysis
filename2 = 'Report.csv'

save_input()
# analyse()
save_output()
