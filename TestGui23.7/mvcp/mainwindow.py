from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow
from qtpyvcp.plugins.notifications import Notifications
from qtpyvcp.actions.machine_actions import issue_mdi
# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)
        Notifications.max_messages = 10
        self.btnRunM428.clicked.connect(self.runM428)
        self.btnRunM429.clicked.connect(self.runM429)
    def runM428(self):
        print "Running M428"
        mdi_list = list()
        mdi_list.append("M428")
        mdi_command = " ".join(mdi_list)
        issue_mdi(mdi_command)
    def runM429(self):
        print "Running M428"
        mdi_list = list()
        mdi_list.append("M429")
        mdi_command = " ".join(mdi_list)
        issue_mdi(mdi_command)
    # add any custom methods here
