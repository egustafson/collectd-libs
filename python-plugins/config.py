# collectd Config class in a more python like manner.
#

import collectd


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

