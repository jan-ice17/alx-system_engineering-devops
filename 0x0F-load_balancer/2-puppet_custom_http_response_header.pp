# Updatin' Ubuntu
exec { 'update server':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell',
}
->
# Installin' Nginx
package { 'nginx':
  ensure   => present,
  provider => 'apt'
}
->
# Addin' custom header response (X-Served-By: hostname)
file_line { 'add HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;'
}
->
# Startin' Nginx service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx']
}

