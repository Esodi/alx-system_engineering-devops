# changing for removing error massages

exec { 'hard-file-limit':
  command => 'sed -i "/holberton hard nofile 4/ holberton hard nofile 50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'soft-file-limit':
  command => 'sed -i "/holberton soft nofile 5/holberton soft nofile 50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
