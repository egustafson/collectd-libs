# Skeleton python plugin for collectd
#
# Usage:  (add to the python plugin configuration)
#
#   <Plugin python>
#       ...
#       Import "missing_writes"
#       <Module "missing_writes">
#           interval 60
#       </Module>
#       ....
#
#  The "<Module>" configuration is optional.  Interval is the default
#  interval for capturing metrics in seconds.
#
## ######################################################################
import collectd

import collectd_util as util


## ########## 

def collectd_identifier(value):
    if len(value.plugin_instance) > 0:
        plug = "{}-{}".format(value.plugin, value.plugin_instance)
    else:
        plug = value.plugin
    if len(value.type_instance) > 0:
        type = "{}-{}".format(value.type, value.type_instance)
    else:
        type = value.type
    return "{}/{}/{}".format(value.host, plug, type)


class MetricWriteTracker:

    def __init__(self):
        self.interval = 10
        self.metrics = {}

    def _log(self, msg):
        collectd.warning(msg)

    def config(self, cfg):
        if "Module.interval" in cfg:
            try:
                self.interval = int(cfg["Module.interval"][0])
                collectd.info("MetricWriteTracker.interval == {}".format(self.interval))
            except ValueError:
                collectd.error("module {0}, interval parameter must be an integer".format(self.__module__))

    def track_metric(self, vl):
        key = collectd_identifier(vl)
        ts  = int(vl.time)
        inter = vl.interval
        if inter < 1: inter = self.interval
        if key not in self.metrics:
            self.metrics[key] = [ ts ]
            collectd.info("Tracking: {}".format(key))
        else:
            tvector = self.metrics[key]
            prev = tvector[-1]
            tvector.append(ts)
            interval = ts - prev
            if abs(inter - interval) > 1:
                self._log("Interval exceeded norms - measured interval: {}".format(interval))
                intervals = []
                for ii in xrange(0, len(tvector)-1):
                    intervals.append(tvector[ii+1] - tvector[ii])
                self._log("tvector:  {!r}".format(tvector))
                self._log("intervals:{!r}".format(intervals))



## collectd call-back functions
##

def config_cb(config, data):
    cfg = util.map_collectd_config(config)
    data.config(cfg)


def write_cb(vl, data):
    data.track_metric(vl)


## Register the call-back functions

data = MetricWriteTracker()

collectd.register_write(write_cb, data)
collectd.register_config(config_cb, data)


## Local Variables:
## mode: python
## End:
