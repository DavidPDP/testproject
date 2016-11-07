from subprocess import Popen, PIPE

def get_all_files():
  process = Popen(["ls","/home/../var/lib/Jenkins/dirTestJenkins"], stdout=PIPE, stderr=PIPE)
  file_list =  [path.rstrip('\n') for path in process.stdout.readlines()]
  return filter(None, file_list)

def add_file(filename,content):
<<<<<<< HEAD
  process = Popen(["touch", "/home/../var/lib/Jenkins/dirTestJenkins"" + filename], stdin=PIPE, stdout=PIPE, stderr=PIPE)
  log = open("/home/../var/lib/Jenkins/dirTestJenkins"" + filename, 'w')
=======
  process = Popen(["touch", "/home/../var/lib/Jenkins/dirTestJenkins/" + filename], stdin=PIPE, stdout=PIPE, stderr=PIPE)
  log = open("/home/../var/lib/Jenkins/dirTestJenkins/" + filename, 'w')
>>>>>>> 4db12a9353770a38458e0801c79fb6ec64d99fd4
  log.write(content)
  log.flush()
  return True if filename in get_all_files() else False


def remove_file():
  deleteCommand = 'find /home/../var/lib/Jenkins/dirTestJenkins -type f -maxdepth 1 -not -name ".*" -exec rm {} \;'  	
  process = Popen(deleteCommand, universal_newlines=True, shell=True, stdout=PIPE, stderr=PIPE).communicate()
  return True

def get_recently_files():
  process = Popen(["ls","/home/../var/lib/Jenkins/dirTestJenkins","-1t"], stdout=PIPE, stderr=PIPE)
  file_list =  [path.rstrip('\n') for path in process.stdout.readlines()]
  file_list = file_list[:3]
  return filter(None, file_list)

<<<<<<< HEAD
def get_content_by_file():
=======
def get_content_by_file(filename):
>>>>>>> 4db12a9353770a38458e0801c79fb6ec64d99fd4
  process = Popen(["cat","/home/../var/lib/Jenkins/dirTestJenkins/" + filename], stdin=PIPE, stdout=PIPE, stderr=PIPE)
  return process.communicate()[0].split('\n')[0]

