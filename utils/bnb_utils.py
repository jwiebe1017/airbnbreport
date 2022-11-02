import pandas as pd

from utils.config import url, headers, check_in_date, check_out_date, querystring


def var_edit(checkin, checkout, itemindex):
    """
    format yyyy-mm-dd
    """
    return r'{\"isInitialLoad\":true,\"hasLoggedIn\":true,\"cdnCacheSafe\":false,' \
           r'\"source\":\"EXPLORE\",\"exploreRequest\":{\"metadataOnly\":false,' \
           r'\"version\":\"1.8.3\",\"placeId\":\"ChIJW8vuDrriaocRRu1CVaEuuW8\",\"checkin\":\"' + \
           checkin + r'\",\"checkout\":\"' + \
           checkout + r'\",\"datePickerType\":\"calendar\",\"adults\":2,' \
                      r'\"searchType\":\"unknown\",\"tabId\":\"home_tab\",' \
                      r'\"flexibleTripLengths\":[\"one_week\"],\"priceFilterNumNights\":1,' \
                      r'\"refinementPaths\":[\"/homes\"],' \
                      r'\"federatedSearchSessionId\":\"85b528f4-8e63-4b2c-a35a-ebba07489c1d\",' \
                      r'\"itemsOffset\":' + \
           str(itemindex) + r',\"sectionOffset\":2,\"query\":\"Jefferson, Colorado, United ' \
                            r'States\",\"itemsPerGrid\":20,\"cdnCacheSafe\":false,' \
                            r'\"treatmentFlags\":[' \
                            r'\"flex_destinations_june_2021_launch_web_treatment\",' \
                            r'\"new_filter_bar_v2_fm_header\",' \
                            r'\"merch_header_breakpoint_expansion_web\",' \
                            r'\"flexible_dates_12_month_lead_time\",' \
                            r'\"storefronts_nov23_2021_homepage_web_treatment\",' \
                            r'\"lazy_load_flex_search_map_compact\",' \
                            r'\"lazy_load_flex_search_map_wide\",' \
                            r'\"im_flexible_may_2022_treatment\",' \
                            r'\"im_flexible_may_2022_treatment\",' \
                            r'\"flex_v2_review_counts_treatment\",' \
                            r'\"flexible_dates_options_extend_one_three_seven_days\",' \
                            r'\"super_date_flexibility\",\"micro_flex_improvements\",' \
                            r'\"micro_flex_show_by_default\",' \
                            r'\"search_input_placeholder_phrases\",\"pets_fee_treatment\"],' \
                            r'\"screenSize\":\"large\",\"isInitialLoad\":true,' \
                            r'\"hasLoggedIn\":true}}","extensions":"{\"persistedQuery\":{' \
                            r'\"version\":1,' \
                            r'\"sha256Hash' \
                            r'\":\"ef48c5cbc4059de87060d37d4c62b72ad708e5ffba74fb8f042c970f0664f0c5\"} '


def query_update(query, checkin, checkout, items):
    dicts = []
    for item in items:
        query_i = query.copy()
        query_i.update({'variables': var_edit(checkin, checkout, item)})
        dicts.append(query_i)
    return dicts


def build_bnb_req(checkin_date, checkout_date, items):
    return map(
        lambda query:
        {
            'method': 'GET',
            'url': url,
            'headers': headers,
            'params': query
        },
        query_update(
            querystring,
            checkin_date,
            checkout_date,
            items
        )
    )


def parse_bnb_info(df):
    return df.assign(
        **{
            'availableBeds': df.loc[:, 'structuredContent.primaryLine'].apply(
                lambda x: ';'.join([m['body'] for m in x])
            ),
            'costBreakdown': df.loc[:,
                             'structuredStayDisplayPrice.explanationData.priceDetails'].apply(
                pull_cost_breakdown
            ),
            'coords': df.apply(
                lambda x: (x.lat, x.lng),
                axis=1
            ),
            'amenities': df.loc[:, 'previewAmenityNames'].apply(
                lambda listing_list:
                ' | '.join(listing_list)
            ),
            'timeBooked': f'{check_in_date}:{check_out_date}',
            'start_date': pd.to_datetime(check_in_date),

        }
    )


def pull_cost_breakdown(pricedetailsobj):
    try:
        price_dict = pricedetailsobj[0]
        return ' | '.join([
            f"{key['description']}: {key['priceString']}" for key in price_dict['items']]
        )
    except:
        return 'unable to parse'
