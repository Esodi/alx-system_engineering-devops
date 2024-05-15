# script that fix nginx to accept more than 2000 requests

exec {'modifying files limit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx && sudo systemctl restart nginx',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}
