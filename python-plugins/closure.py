# template python plugin for collectd 
#
import collectd

class CollectdPluginBase(object):

    def __init__(self):
        pass

    def config_cb(self, config, data=None):
        pass

    def init_cb(self, data=None):
        pass

    def shutdown_cb(self, data=None):
        pass

    def read_cb(self, data=None):
        pass

    def write_cb(self, vl, data=None):
        pass

    def notification_cb(self, notification, data=None):
        pass

    def flush_cb(self, timeout, identifier, data=None):
        pass

    def log_cb(self, severity, message, data=None):
        pass


## ########## Closure methods on the plugin #####

def config_closure(po):
    def config_cb(config, data=None):
        po.config_cb(config, data)
    return config_cb

def init_closure(po):
    def init_cb(data=None):
        po.init_cb(data)
    return init_cb

def shutdown_closure(po):
    def shutdown_cb(data=None):
        po.shutdown_cb(data)
    return shutdown_cb

def read_closure(po):
    def read_cb(data=None):
        po.read_cb(data)
    return read_cb

def write_closure(po):
    def write_cb(vl, data=None):
        po.write_cb(vl, data)
    return write_cb

def notification_closure(po):
    def notification_cb(notification, data=None):
        po.notification_cb(notification, data)
    return notification_cb

def flush_closure(po):
    def flush_cb(timeout, identifier, data=None):
        po.flush_cb(timeout, identifier, data)
    return flush_cb

def log_closure(po):
    def log_cb(severity, message, data=None):
        po.log_cb(severity, message, data)
    return log_cb


## Local Variables:
## module: python
## End:
