file { '/etc/issue' :
  mode => '0644',
  content => "Internal system \l \n",
}
