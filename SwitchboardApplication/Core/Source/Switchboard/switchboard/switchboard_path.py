import os
import pathlib
import sys

#查找引擎的上层目录
def find_engine_ancestor_dir(start: pathlib.Path) -> pathlib.Path:
    ''' Searches parent directories recursively for SB prerequisites. '''
    # 检索的起始位
    search = start
    while search != search.parent:
        sb_thirdparty_subdir = (
            # 修改
            search / 'Extras/ThirdParty/SwitchboardThirdParty')
        # 如果这个目录存在就不存在问题
        if sb_thirdparty_subdir.is_dir():
            return search
        else:
            search = search.parent

    raise RuntimeError("Couldn't find prerequisites in ancestor directories")


SWITCHBOARD_PATH = pathlib.Path(__file__).parent
ENGINE_PATH = find_engine_ancestor_dir(SWITCHBOARD_PATH)
THIRDPARTY_PATH = ENGINE_PATH / 'Extras/ThirdParty'
SB_THIRDPARTY_PATH = THIRDPARTY_PATH / 'SwitchboardThirdParty'

CWRSYNC_SRC_DIR = THIRDPARTY_PATH / 'cwrsync'
CWRSYNC_DEST_DIR = SB_THIRDPARTY_PATH / 'cwrsync'
CWRSYNC_FSTAB_PATH = CWRSYNC_DEST_DIR / 'etc/fstab'
CWRSYNC_FSTAB_CONTENTS = '''\
# This is equivalent to the default, except for the addition of the "noacl"
# option, which skips any attempt by Cygwin to store POSIX permissions via the
# Windows host's NTFS access control lists.
none /cygdrive cygdrive binary,posix=0,user,noacl 0 0
'''
