from modules.core.color import Colorate, Colors, Add


def load_ui(
    banner: str, 
) -> None:
    print(
        Colorate.Diagonal(
           Colors.DynamicMIX(
               (Colors.green, Colors.white),
               Add.Add(banner, None, center=True)
           )
        )
    )


def home() -> None:
    banner = """
        ╔═════════════════════════════════════════════════════╗
        ║ ███╗   ██╗██████║         ██████╗ ███████╗██╗   ██╗ ║
        ║ ████╗  ██║██  ██║         ██╔══██╗██╔════╝██║   ██║ ║
        ║ ██╔██╗ ██║██████║ ██████╗ ██║  ██║███████╗╚██╗ ██╔╝ ║
        ║ ██║╚██╗██║██╔═══╝ ╚═════╝ ██║  ██║██╔════╝ ╚████╔╝  ║
        ║ ██║ ╚████║██║             ██████╔╝███████╗  ╚██╔╝   ║
        ║ ╚═╝  ╚═══╝╚═╝             ╚═════╝ ╚══════╝   ╚═╝    ║
        ╠═════════════════════════════════════════════════════╣
        ║> Author   : PhcNguyenz                              ║
        ║> Support  : 0937.127.172                            ║
        ╚═════════════════════════════════════════════════════╝
    """
    load_ui(banner)


def menu() -> None:
    banner = """
        ╔══════════════════════════════════╗
        ║               Menu               ║
        ║ 1.Run Server                     ║
        ║                                  ║
        ║ 3.Github                         ║
        ╚══════════════════════════════════╝
    """
    load_ui(banner)