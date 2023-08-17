### Author: Roholt
### 10-2020

import subprocess
import os
import pwd


class Executioner:
    def __init__(self, script_ref):
        self.abs_path = os.path.dirname(os.path.abspath(__file__))
        self.user_name = os.environ.get("MACRO_KEYBOARD_LOCAL_USER", "")

        # if user_name is not set, then we have a look at id 1000 as that is "mostly" the local user.
        if not self.user_name:
            self.user_name = pwd.getpwuid(1000).pw_name
            print(f"MACRO_KEYBOARD_LOCAL_USER not set, using: {self.user_name}")

        self.execute(script_ref)

    def demote(self, user_uid, user_gid):
        def result():
            self.report_ids("starting demotion")
            os.setgid(user_gid)
            os.setuid(user_uid)
            self.report_ids("finished demotion")

        return result

    def report_ids(self, msg):
        print("uid, gid = %d, %d; %s" % (os.getuid(), os.getgid(), msg))

    def execute(self, script):
        # Path are relative to this python file, therefore replace "./", with the path to this python file.
        script = [f.replace("./", self.abs_path + "/") for f in script]

        pw_record = pwd.getpwnam(self.user_name)
        user_name = pw_record.pw_name
        user_home_dir = pw_record.pw_dir
        user_uid = pw_record.pw_uid
        user_gid = pw_record.pw_gid
        env = os.environ.copy()
        env["HOME"] = user_home_dir
        env["LOGNAME"] = user_name
        env["PWD"] = self.abs_path
        env["USER"] = user_name
        self.report_ids("starting " + str(script))
        process = subprocess.Popen(
            script,
            preexec_fn=self.demote(user_uid, user_gid),
            cwd=self.abs_path,
            env=env,
        )
        result = process.wait()
        # subprocess.call(script)  # , shell=True)
