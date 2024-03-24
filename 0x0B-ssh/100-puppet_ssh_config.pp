#!/usr/bin/pup
# make changes to the ssh configuration file.
file {~/.ssh/config:
  ensure  => present,
  mode    => '0700',
  content => "Host remote_host\n
       User ubuntu\n
       HostName 18.207.207.117\n
       IdentifyFile ~/.ssh/school",
  owner   => 'root'
}
