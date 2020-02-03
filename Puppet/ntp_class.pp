# ntp class which contains 3 resources
#
# https://puppet.com/docs/puppet/latest/lang_resources.html

class ntp {
  package { 'ntp' :
  ensure => latest,
  }
  file { '/etc/ntp.conf' :
    source => 'puppet:///modules/ntp/ntp.conf'
    replace => true,
  }
  service { 'ntp' :
    enable => true,
    ensure => running,
    }
}
