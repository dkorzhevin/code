# sudo apt install puppet-master
# install htop package
# sudo puppet apply -v tools.pp

package { 'htop' :
  ensure => present,
}
