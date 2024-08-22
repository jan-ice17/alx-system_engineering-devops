# This script optimizes the Nginx server to handle more traffic by increasing file descriptor limits

# Increase the maximum number of open files for Nginx from 15 to 4096
exec { 'increase-file-limit-for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart the Nginx service to apply the changes
-> exec { 'restart-nginx-service':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}

