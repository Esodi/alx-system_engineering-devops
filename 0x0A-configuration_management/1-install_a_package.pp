#!/usr/bin/pup
# installing flask from pip3
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  notify   => Exec['echo_newline'],
}

exec { 'echo_newline':
  command     => 'echo -e "\n"',
  path        => '/usr/bin',
  refreshonly => true,
}
