import os
import shutil
from matplotlib.figure import Figure


def savefig(fig: Figure, script_name: str, file_name: str):
    _file_name = '{}-{}'.format(
        os.path.splitext(os.path.basename(script_name))[0], file_name)
    _file_name = os.path.join(os.getcwd(), 'Images', _file_name)

    if not os.path.exists(os.path.dirname(_file_name)):
        os.makedirs(os.path.dirname(_file_name))

    fig.savefig(_file_name)
    
    