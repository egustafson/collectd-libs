# Skeleton python plugin for collectd
#
import collectd

## collectd call-back functions
##

def config_cb(config, data=None):
    return

def init_cb(data=None):
    return

def shutdown_cb(data=None):
    return


def read_cb(data=None):
    return

def write_cb(vl, data=None):
    return

def notification_cb(notification, data=None):
    return


def flush_cb(timeout, identifier, data=None):
    return

def log_cb(severity, message, data=None):
    return


## Register the call-back functions

data = "stub-string"         # placeholder
name = init_cb.__module__    # the default
interval = 10                # the default

collectd.register_config(config_cb, data, name)
collectd.register_init(init_cb, data, name)
collectd.register_shutdown(shutdown_cb, data, name)

collectd.register_read(read_cb, interval, data, name)
collectd.register_write(write_cb, data, name)
collectd.register_notification(notification_cb, data, name)

collectd.register_flush(flush_cb, data, name)
collectd.register_log(log_cb, data, name)

## Local Variables:
## mode: python
## End:
