# creating manifest to kill process killmenow
# Using exec and pkill

exec { 'pkill -f killmenow':
  path  => 'usr/bin/:/usr/local/bin/:/bin/'
}
