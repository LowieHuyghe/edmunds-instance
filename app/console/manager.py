
from edmunds.console.manager import Manager as EdmundsManager
from edmunds.foundation.testing.testcommand import TestCommand
from edmunds.foundation.gae.pipinstallinto import PipInstallIntoCommand
from app.console.commands.helloworldcommand import HelloWorldCommand


class Manager(EdmundsManager):
    """
    The manager to control the command-line usage of the application
    """

    def add_commands(self):
        """
        Add the commands
        """

        self.add_command('helloworld', HelloWorldCommand)

        self.add_command('test', TestCommand)
        self.add_command('pip-install-into', PipInstallIntoCommand)
