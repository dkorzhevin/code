exec { 'move example file' :
    command => 'mv /home/dkorzhevin/example.txt /home/dkorzhevin/Desktop',
    onlyif => 'test -e /home/dkorzhevin/example.txt' ,
}
