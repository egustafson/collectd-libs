# utility classes for building collectd plugins in python
#

import collectd


## ########## map_collectd_config() ##########
##
## Turn the collectd.Config object into a dictionary 
## with each key be a "." concatinated string of the
## key and it's parent's key.  The top key will always
## be "Module"
##
def map_collectd_config(config):
    cfgmap = {}
    child_stack = [ ("", config), ]
    while len(child_stack) > 0:
        (scope, cfg) = child_stack.pop()
        if len(scope) > 0:
            prefix = "{}.{}".format(scope, cfg.key)
        else:
            prefix = cfg.key
        for child in cfg.children:
            child_stack.append((prefix, child))
        if len(cfg.values) > 0:
            cfgmap[prefix] = cfg.values
    return cfgmap

## ########## class CollectdConfig ##########
##
## Another (incomplete) mechansim for mapping
## collectd.Config into a more versitile configuration
## object.
##

# class CollectdConfig(object):
# 
#     def __init__(self, config):
#         self.cfg = {}
#         child_stack = [ ("", config), ]
#         while len(child_stack) > 0:
#             (scope, cfg) = child_stack.pop()
#             if len(scope) > 0:
#                 prefix = "{}.{}".format(scope, cfg.key)
#             else:
#                 prefix = cfg.key
#             for child in cfg.children:
#                 child_stack.append((prefix, child))
#             if len(cfg.values) > 0:
#                 self.cfg[prefix] = cfg.values
# 
#     def to_str(self):
#         return repr(self.cfg)


## #################### Collectd-colosure ####################
##
## A base class that can be easily extended and registration 
## methods that return closures which include the "plugin class"
##
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

## ## End:  Collectd-closure ##############################

## Local Variables:
## module: python
## End:
