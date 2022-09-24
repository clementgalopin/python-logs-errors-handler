import re
import sys
import json
import uuid
import os

from datetime import datetime

class Logs():

    def __init__(self):
        self.logs = []
        self.warnings = []
        self.runtime_started = self.get_datetime_str()
        self.runtime_id = str(uuid.uuid4())

        self.old_out = sys.stdout
        """Stamped stdout."""
        self.nl = True

    def get_datetime_str(self):
        return str(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))

    def write(self, log):
        """Write function overloaded."""
        if log == '\n':
            self.old_out.write(log)
            self.nl = True
        elif self.nl:
            log_withdatetime = '%s:%s> %s' % (self.runtime_id, self.get_datetime_str(), log)
            self.old_out.write(log_withdatetime)
            self.logs.append(log_withdatetime)
            self.nl = False
        else:
            self.old_out.write(log)
            self.logs.append(log)

        if re.match("^(Warning.*)$", log):
            self.warnings.append(log_withdatetime)

        if re.match("^(Error.*)$", log):
            self.do_exit()
    
    def flush(self):
        pass

    def send_logs(self):
        print('Sending logs...')

        logs_folder = './logs/'
        logs_json = json.dumps(
            {
                "id": self.runtime_id,
                "start": self.runtime_started,
                "warnings": self.warnings,
                "logs": self.logs
            }
        )
        logs_filename = '{0}_{1}.json'.format(datetime.strftime(datetime.now(), '%Y%m-%d-%H%M%S'), self.runtime_id)

        if not os.path.exists(logs_folder):
            os.makedirs(logs_folder)

        try:
            with open(logs_folder+'/'+logs_filename, 'w') as logs_file:
                logs_file.write(logs_json)
        except:
            print('Error: Impossible to write logs')

    def do_exit(self):
        print('Exiting...')
        sys.exit()

    def end_process(self):
        print('Stopping...')
        self.send_logs()