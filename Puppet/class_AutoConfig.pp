# https://puppet.com/docs/puppet/latest/lang_resources.html

class AutoConfig {
  package { 'Executable':
    ensure => latest,
  }
  file { 'executable.cfg':
    source => 'puppet:///modules/executable/Autoconfig/executable.cfg'
    replace => true,
  }
  service { 'executable.exe':
    enable  => true,
    ensure  => running,
  }
}
