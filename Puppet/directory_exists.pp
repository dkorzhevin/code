# https://puppet.com/docs/puppet/latest/lang_resources.html

class sysctl {

    file { '/etc/sysctl.d':
    ensure => directory,}
}
