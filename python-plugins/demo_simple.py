# Example (stub) python plugin for collectd
#
import collectd
import config as cconfig


## collectd call-back functions
##

def config_cb(config, data=None):
    collectd.info("config_cb: ")
    cfg = cconfig.map_collectd_config(config)
    collectd.info("{!r}".format(cfg))
    collectd.info("config_cb: -- end --")

def init_cb(data=None):
    collectd.info("init_cb:")

def shutdown_cb(data=None):
    collectd.info("shutdown_cb")


def read_cb(data=None):
    collectd.info("read_cb")

def write_cb(vl, data=None):
    collectd.info("write_cb: {!r}".format(vl))

def notification_cb(notification, data=None):
    collectd.info("notification_cb: {!r}".format(notification))


def flush_cb(timeout, identifier, data=None):
    collectd.info("flush_cb: [{0}] {1}".format(timeout, identifier)))

def log_cb(severity, message, data=None):
    # print here, if logging is used it will cause infinite recursion.
    print("log_cb: severity({}) - {}".format(severity, message))


## Register the call-back functions

collectd.register_config(config_cb)
collectd.register_init(init_cb)
collectd.register_shutdown(shutdown_cb)

collectd.register_read(read_cb, interval)
collectd.register_write(write_cb)
collectd.register_notification(notification_cb)

collectd.register_flush(flush_cb)
collectd.register_log(log_cb)


collectd.info("trace plugin module loaded")


## Local Variables:
## mode: python
## End:
