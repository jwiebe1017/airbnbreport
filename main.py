import geopy.distance
import pandas as pd
from itertools import chain
import requests
from toolz import pipe

from utils.bnb_utils import var_edit, parse_bnb_info, build_bnb_req
from utils.config import relevant_columns, url, headers
from utils.req_utils import request_to_bnb


def calc_distance_cols(df):
    #  use as static metric in below calc
    tarryall = (39.296114, -105.7186119)

    df = df.assign(
        **{
            'distanceFromTarryallCabin_w': df.coords.apply(
                lambda coordinates:
                geopy.distance.geodesic(tarryall, coordinates).mi
            ),
        }
    )
    return df.assign(
        **{
            'distanceFromTarryallCabin': df.distanceFromTarryallCabin_w.apply(
                lambda coordinates:
                f'{coordinates} miles'
            ),

        }
    )


def total_stays_for_time(checkin_date, checkout_date, items):
    rel_cols = relevant_columns

    # set up all the requests to the api for 20-items-per-page approach
    pipe(
        (checkin_date, checkout_date, items),
        build_bnb_req,
        request_to_bnb
    )
    final_res = list()
    for item in items:
        querystring['variables'] = var_edit(checkin_date, checkout_date, item)
        final_res.append(
            requests.request("GET", url, headers=headers, params=querystring)
        )

    #  remove failed requests
    final_res = list(
        filter(
            None,
            final_res
        )
    )

    #  drilldown to relevant section in airbnb (as of Aug2022)
    json_total_data = list(
        map(
            lambda response:
            response.json()['data']['presentation']['explore']['sections']['sections'][2][
                'section']['child']['section']['items'],
            final_res
        )
    )

    #  some vals are getting mixed, store to QA
    backup_json_total = json_total_data

    #  update/consolidate information into a single dict
    list(
        chain(
            *list(
                map(
                    lambda stays_chunk:
                    map(
                        lambda stay:
                        # stay['listing'].update(stay['pricingQuote']['structuredStayDisplayPrice']),
                        stay['listing'].update(stay['pricingQuote']),
                        stays_chunk
                    ),
                    json_total_data
                )
            )
        )
    )

    #  merge list of lists for ease of use
    json_total_listings = list(
        chain(
            *json_total_data
        )
    )

    df = pipe(
        pd.concat(
            list(
                map(
                    lambda stay:
                    pd.json_normalize(
                        stay['listing']
                    ),
                    json_total_listings
                )
            )
        ),
        parse_bnb_info,
        calc_distance_cols,
        lambda all_listings_in_jefferson:
        all_listings_in_jefferson[rel_cols].drop_duplicates(
        ).reset_index(
        ).drop(
            columns='index'
        ),
    )
    return df.sort_values(
        'distanceFromTarryallCabin_w'
    )

