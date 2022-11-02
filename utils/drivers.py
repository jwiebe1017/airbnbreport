from toolz import pipe

from utils.bnb_utils import build_bnb_req
from utils.req_utils import request_to_bnb


def gather_all_requests(checkin_date, checkout_date, items):
    return pipe(
        build_bnb_req(checkin_date, checkout_date, items),
        request_to_bnb
    )
