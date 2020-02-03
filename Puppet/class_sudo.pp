# https://puppet.com/docs/puppet/latest/lang_resources.html

class sudo {
  package { 'sudo' :
  ensure => present,
  }
}
