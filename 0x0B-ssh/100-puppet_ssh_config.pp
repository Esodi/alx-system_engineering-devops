#!/usr/bin/pup
# make changes to the ssh configuration file.
file {~/.ssh/config:
  ensure       => present,
  mode         => 700,
  Host         => remote_host,
  user         => ubuntu,
  HostName     => 18.207.207.117,
  IdentifyFile => ~/.ssh/school
}
