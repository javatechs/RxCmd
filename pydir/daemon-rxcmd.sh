#!/bin/bash

### BEGIN INIT INFO
# Provides:          Daemonized rxcmd
# Required-Start:    
# Required-Stop:     
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start/stops the rxcmd
# Description:       Start/stops the rxcmd
### END INIT INFO

# Change the next 8 lines to suit where things live in your environment
DIR=/home/robot/pydir
DAEMON=$DIR/daemon-rxcmd.py
DAEMON_NAME=daemon-rxcmd
PIDFILE=/tmp/RxCmdDaemon.pid
SRC1=/opt/ros/kinetic/setup.bash
SRC2=/home/robot/catkin_ws/devel/setup.bash
SRC3=/home/robot/.bashrc
PATHFIX='$PATH:/opt/ros/kinetic/bin'

# This next line determines what user the script runs as.
DAEMON_USER=robot

# It would be nice to use LSB, but the following line acts like the init-functions runs an exit instead
# of a return, however I find no exits in init-functions.  Will need more research to use this
# . /lib/lsb/init-functions

do_start () {
    # When init-functions is working properly uncomment these lines and comment the su line
    #log_daemon_msg "Starting system $DAEMON_NAME daemon"
    #start-stop-daemon --start start --daemonize --pidfile $PIDFILE --make-pidfile --user $DAEMON_USER --chuid $DAEMON_USER --exec $DAEMON
    #log_end_msg $?
    su -l -c "source $SRC1;source $SRC2;source $SRC3;export PATH=$PATHFIX;$DAEMON start" $DAEMON_USER &
}

do_stop () {
    # When init-functions is working properly uncomment these lines and comment the kill line
    #log_daemon_msg "Stopping system $DAEMON_NAME daemon"
    #start-stop-daemon --stop stop --pidfile $PIDFILE --retry 10
    #log_end_msg $?
    kill `cat ${PIDFILE}`
}

case "$1" in

    start|stop)
        do_${1}
        ;;

    restart|reload|force-reload)
        do_stop
        do_start
        ;;

    status)
        #When init-functions is working properly uncomment this line and comment the if section
        #status_of_proc "$DAEMON_NAME" "$DAEMON" && exit 0 || exit $?
        if [ -f "$PIDFILE" ]; then
           echo 'daemonize-rxcmd.py is RUNNING with PID: ' `cat ${PIDFILE}`
        else
           echo 'No PIDFILE found at: ' $PIDFILE
           echo 'daemonize-rxcmd.py is NOT RUNNING'
        fi
        ;;
    *)
        echo "Usage: /etc/init.d/$DAEMON_NAME {start|stop|restart|status}"
        exit 1
        ;;

esac
exit 0

