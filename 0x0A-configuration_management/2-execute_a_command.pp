#!/usr/bin/pup
# a manifest that kills a process named killmenow.
exec {'pkill_killmenow':
  command     => '/usr/bin/pkill killmenow',
  path        => '/alx-system_engineering-devops/0x0A-configuration_management',
  refreshonly => true,
  onlyif      => '/bin/pgrep killmenow',
}
