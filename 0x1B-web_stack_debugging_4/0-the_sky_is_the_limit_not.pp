# Increasing the maximum amount of traffic

exec {'nginx_connection_limit':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['nginx_restart'],
}

# Restart nginx
exec {'nginx_restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
