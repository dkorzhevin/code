node webserver.example.com {
  class { 'sudo': }
  class { 'ntp':
      servers => ['ntp1.example.com', 'ntp2.example.com']
    
  }
  class { 'apache' : }
}
