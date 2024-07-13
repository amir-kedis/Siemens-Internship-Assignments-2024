"""Server: manages server options and configuration."""

###################################################################
#
#
#    ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗ ██╗ ██╗
#    ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗╚██╗╚██╗
#    ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝ ╚██╗╚██╗
#    ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗ ██╔╝██╔╝
#    ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║██╔╝██╔╝██╗
#    ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝ ╚═╝ ╚═╝
#
#
#       Author: Amir Kedis
#
#       A stub for the server module.
#
#
###################################################################


class Server:
    """
    Represents a Server with configuration options.

    Attributes:
        options (dict): A map/dict containing server optinos

    Methods:
        __init__(self, options):
            Initializes the server with default value for option which is true.

        configure(self, config_options):
            Configures server options based on given dict.

        get_options(self):
            Return current server options.
    """

    def __init__(self, options) -> None:
        """
        Initialize the server with default value for option which is true.

        Args:
            options (list): A list of string of server options.

        """
        self.options = {option: True for option in options}

    def configure(self, config_options):
        """
        Configure the server with a new set of options.

        Args:
            config_options (dict): A dict of options and values.
        """
        for option, value in config_options.items():
            if value is not None:
                self.options[option] = value

    def get_options(self) -> dict[str, bool]:
        """
        Return the current server config.

        Returns:
            dict: A dictionary containing current server options.
        """
        return self.options
