from subprocess import Popen, PIPE

def get_all_files():
  process = Popen(["ls","/home/filesystem_user"], stdout=PIPE, stderr=PIPE)
  file_list =  [path.rstrip('\n') for path in process.stdout.readlines()]
  return filter(None, file_list)

def add_file(filename,content):
  process = Popen(["touch", "/home/filesystem_user/" + filename], stdin=PIPE, stdout=PIPE, stderr=PIPE)
  log = open("/home/filesystem_user/" + filename, 'w')
  log.write(content)
  log.flush()
  return True if filename in get_all_files() else False


def remove_file():
  deleteCommand = 'find /home/filesystem_user -type f -maxdepth 1 -not -name ".*" -exec rm {} \;'  	
  process = Popen(deleteCommand, universal_newlines=True, shell=True, stdout=PIPE, stderr=PIPE).communicate()
  return True

def get_recently_files():
  process = Popen(["ls","/home/filesystem_user","-1t"], stdout=PIPE, stderr=PIPE)
  file_list =  [path.rstrip('\n') for path in process.stdout.readlines()]
  file_list = file_list[:3]
  return filter(None, file_list)
