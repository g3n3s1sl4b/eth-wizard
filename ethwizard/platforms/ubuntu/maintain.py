from ethwizard.platforms.ubuntu.common import save_state, log, quit_app

from ethwizard.constants import (
    CTX_SELECTED_EXECUTION_CLIENT,
    CTX_SELECTED_CONSENSUS_CLIENT,
    EXECUTION_CLIENT_GETH,
    CONSENSUS_CLIENT_LIGHTHOUSE,
    WIZARD_COMPLETED_STEP_ID
)

import pprint

def enter_maintenance(context):
    # Maintenance entry point for Ubuntu.
    # Maintenance is started after the wizard has completed.

    log.info(f'Entering maintenance mode.')

    if context is None:
        log.error('Missing context.')

    context = use_default_client(context)

    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(context)

    if context is None:
        log.error('Missing context.')

    return True

def use_default_client(context):
    # Set the default clients in context if they are not provided

    selected_execution_client = CTX_SELECTED_EXECUTION_CLIENT
    selected_consensus_client = CTX_SELECTED_CONSENSUS_CLIENT

    updated_context = False

    if selected_execution_client not in context:
        context[selected_execution_client] = EXECUTION_CLIENT_GETH
        updated_context = True
    
    if selected_consensus_client not in context:
        context[selected_consensus_client] = CONSENSUS_CLIENT_LIGHTHOUSE
        updated_context = True

    if updated_context:
        if not save_state(WIZARD_COMPLETED_STEP_ID, context):
            return None

    return context