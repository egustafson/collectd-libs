# Example usage of the closure helper for collectd-python plugins
#
import closure
import collectd

import config as cconfig



class DemoClosureCollectdPlugin(closure.CollectdPluginBase):

    def __init__(self):
        self._log("initializing.")

    def _log(self, msg):
        collectd.info("DemoClosureCollectdPlugin -- {}".format(msg))

    def init_cb(self, data=None):
        self._log("init_cb()")

    def config_cb(self, config, data=None):
        self.config = cconfig.map_collectd_config(config)
        if "Module.config" in self.config:
            self._log("config_cb: {!r}".format(self.config))
        if "Module.init" in self.config:
            collectd.register_init(closure.init_closure(self), name=self.__module__)
        if "Module.read" in self.config:
            collectd.register_read(closure.read_closure(self), name=self.__module__)
        if "Module.write" in self.config:
            collectd.register_write(closure.write_closure(self), name=self.__module__)
        if "Module.notification" in self.config:
            collectd.register_notification(closure.notification_closure(self), name=self.__module__)
        if "Module.flush" in self.config:
            collectd.register_flush(closure.flush_closure(self), name=self.__module__)
        if "Module.log" in self.config:
            collectd.register_log(closure.log_closure(self), name=self.__module__)
        if "Module.shutdown" in self.config:
            collectd.register_shutdown(closure.shutdown_closure(self), name=self.__module__)

    def read_cb(self, data=None):
        self._log("read_cb()")

    def write_cb(self, vl, data=None):
        self._log("write_cb(): {!r}".format(vl))

    def notification_cb(self, notification, data=None):
        self._log("notification_cb(): [{0}] {1}".format(notification.severity, 
                                                        notification.message))

    def flush_cb(self, timeout, identifier, data=None):
        self._log("flush_cb(): [{0}] {1}".format(timeout, identifier))

    def shutdown_cb(self, data=None):
        self._log("shutdown_cb()")

    def log_cb(self, severity, message, data=None):
        print("log_cb(): [{0}] {1}".format(severity, message))
        


## Install plugin

plugin = DemoClosureCollectdPlugin()

#collectd.register_init(closure.init_closure(plugin), name=plugin.__module__)
collectd.register_config(closure.config_closure(plugin), name=plugin.__module__)





## Local Variables:
## mode: python
## End:
