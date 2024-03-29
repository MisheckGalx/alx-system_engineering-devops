#  Install Nginx web server (w/ Puppet)

# Update
exec { 'apt_update':
  command => 'apt-get update',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# Install nginx
package { 'nginx':
  ensure     => 'installed',
}

# Handle custom_header
file_line { 'add custom header':
  ensure => present,
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;',
}

# start nginx
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
