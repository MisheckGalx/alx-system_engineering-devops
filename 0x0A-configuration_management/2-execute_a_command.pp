# create a manifest that kills a process named killmenow

exec {' killmenow':
  command  => '/bin/pkill killmenow'
}
