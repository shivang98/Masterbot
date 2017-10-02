import os


# each website you go is a new project
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)


# define queue and crawled file
def create_date_file(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.exists(queue):
        write_file(queue, base_url);
    if not os.path.exists(crawled):
        write_file(crawled, '');


# create new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# add data to existing files
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# delete the content of a file
def delete_file_contents(path):
    with open(path, 'w'):
        pass


# read the file and convert each line to set
def file_to_set(file_name):
    result = set();
    with open(file_name, 'rt') as f:
        for line in f:
            result.add(line.replace('\n', ''))
    return result


# iterate through set each item will be in a file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)
