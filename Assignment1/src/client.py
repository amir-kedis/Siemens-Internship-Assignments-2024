"""Client: connects to the server as a master or slave to perform test case logic."""

###################################################################
#
#
#     ██████╗██╗     ██╗███████╗███╗   ██╗████████╗ ██╗ ██╗
#    ██╔════╝██║     ██║██╔════╝████╗  ██║╚══██╔══╝██╔╝██╔╝
#    ██║     ██║     ██║█████╗  ██╔██╗ ██║   ██║  ██╔╝██╔╝
#    ██║     ██║     ██║██╔══╝  ██║╚██╗██║   ██║  ╚██╗╚██╗
#    ╚██████╗███████╗██║███████╗██║ ╚████║   ██║   ╚██╗╚██╗██╗
#     ╚═════╝╚══════╝╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═╝ ╚═╝╚═╝
#
#
#       Author: Amir Kedis
#
#       A stub for the server module.
#
#
###################################################################


class Client:
    """
    Talks to a server too set and change it's configurations.

    Attributes:
        is_master (bool): is this a master client or slave
        server: an instance of the Server.

    Methods:
        __init__(self, server, is_master=False):
            Initializes the client type and reference server.

        configure_server(self, config_options):
            Tries to change the server configurations, it's behaviour depends
            on the type of the client.
    """

    def __init__(self, server, is_master=False) -> None:
        """
        Initialize the client type and reference server.

        Args:
            server (Server): A server reference
            is_master (bool): a bool represents whether this client is master or slave.
        """
        self.server = server
        self.is_master = is_master

    def configure_server(self, config_options) -> str:
        """
        Configure the server based on the type of the client and given options.

        Args:
            config_options (dict): A dictionary of options and values to set the server to.
        """
        if self.is_master:
            self.server.configure(config_options)
        else:
            # NOTE: Here I'm assuming that if:
            #       master options are all None is just as if all is True
            #       because true is the default option
            #       M_OPT1, M_OPT2, S_OPT1, S_OPT2
            #       None,   None,   True,   True     => Valid
            #       None,   None,   False,  True     => Invalid
            #       True,   True,   True,   True     => Valid
            for option, value in config_options.items():
                if value is not None and value != self.server.get_options()[option]:
                    self.server.configure(
                        {option: None for option in config_options.keys()})
                    return "Error: Cannot change {0}".format(option)
        return "Server configured successfully"
