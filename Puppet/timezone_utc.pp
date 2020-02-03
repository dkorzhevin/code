# https://puppet.com/docs/puppet/latest/lang_resources.html

class timzone {
    file { '/etc/timezone':
      ensure => file,
      content => "UTC\n",
      replace => true,
    }
}
