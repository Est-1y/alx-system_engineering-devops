# Enabling holberton user login

exec { 'Hard limit':
  command => "sed -i 's/5/4000/' /etc/security/limits.conf",
  path    => '/bin'
}

exec { 'Soft limit':
  command => "sed -i 's/4/2000/' /etc/security/limits.conf",
  path    => '/bin'
}
