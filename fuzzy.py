#!/usr/bin/env python3

# pip install fuzzywuzzy python-Levenshtein

from fuzzywuzzy import fuzz


def fuzzy_match(msg1, msg2, threshold=70):
    score = fuzz.token_set_ratio(msg1, msg2)
    print(score)
    return score >= threshold, score


if __name__ == "__main__":
    msg1 = "error: ‘MSM_UART_CR_CMD_RESET_RX’ undeclared (first use in this function); did you mean ‘UART_CR_CMD_RESET_RX’?"
    msg2 = "error: use of undeclared identifier 'MSM_UART_CR_CMD_RESET_RX'"

    fuzzy_match(msg1, msg2)

    msg3 = """
ERROR: modpost: module binfmt_misc uses symbol override_creds from namespace VFS_internal_I_am_really_a_filesystem_and_am_NOT_a_driver, but does not import it.
ERROR: modpost: module binfmt_misc uses symbol revert_creds from namespace VFS_internal_I_am_really_a_filesystem_and_am_NOT_a_driver, but does not import it.
ERROR: modpost: module binfmt_misc uses symbol dentry_open from namespace ANDROID_GKI_VFS_EXPORT_ONLY, but does not import it.
"""
    msg4 = """
ERROR: modpost: module binfmt_misc uses symbol dentry_open from namespace ANDROID_GKI_VFS_EXPORT_ONLY, but does not import it.
ERROR: modpost: module binfmt_misc uses symbol override_creds from namespace VFS_internal_I_am_really_a_filesystem_and_am_NOT_a_driver, but does not import it.
ERROR: modpost: module binfmt_misc uses symbol revert_creds from namespace VFS_internal_I_am_really_a_filesystem_and_am_NOT_a_driver, but does not import it.
ERROR: modpost: module autofs4 uses symbol d_drop from namespace ANDROID_GKI_VFS_EXPORT_ONLY, but does not import it.
ERROR: modpost: module autofs4 uses symbol path_get from namespace ANDROID_GKI_VFS_EXPORT_ONLY, but does not import it.
ERROR: modpost: module autofs4 uses symbol dentry_open from namespace ANDROID_GKI_VFS_EXPORT_ONLY, but does not import it.
ERROR: modpost: module loop uses symbol path_get from namespace ANDROID_GKI_VFS_EXPORT_ONLY, but does not import it.
ERROR: modpost: module loop uses symbol vfs_getattr from namespace ANDROID_GKI_VFS_EXPORT_ONLY, but does not import it.
ERROR: modpost: module loop uses symbol vfs_statfs from namespace ANDROID_GKI_VFS_EXPORT_ONLY, but does not import it.
"""
    fuzzy_match(msg2, msg1)
