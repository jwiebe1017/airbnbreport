import datetime as dt

from .utils import safe_config_load

data = safe_config_load('config.yml')

url = data['url']
headers = data['headers']
relevant_columns = data['relevant_columns']

check_in_date = data['CHECK_IN_DATE'] if data['CHECK_IN_DATE'] else dt.date.today().isoformat()
check_out_date = data['CHECK_OUT_DATE'] if data['CHECK_OUT_DATE'] else (
        dt.date.today() + dt.timedelta(31)
).isoformat()

items = list(range(0, data['ITEMS'], 20)) if data['ITEMS'] else list(range(0, 250, 20))


url = "https://www.airbnb.com/api/v3/ExploreSections"

querystring = {"operationName":"ExploreSections",
               "locale":"en",
               "currency":"USD",
               "variables":r"{\"isInitialLoad\":true,\"hasLoggedIn\":true,\"cdnCacheSafe\":false,"
                           r"\"source\":\"EXPLORE\",\"exploreRequest\":{\"metadataOnly\":false,"
                           r"\"version\":\"1.8.3\",\"placeId\":\"ChIJW8vuDrriaocRRu1CVaEuuW8\","
                           r"\"checkin\":\"2022-10-02\",\"checkout\":\"2022-10-03\","
                           r"\"datePickerType\":\"calendar\",\"adults\":2,"
                           r"\"searchType\":\"unknown\",\"tabId\":\"home_tab\","
                           r"\"flexibleTripLengths\":[\"one_week\"],\"priceFilterNumNights\":1,"
                           r"\"refinementPaths\":[\"/homes\"],"
                           r"\"federatedSearchSessionId\":\"85b528f4-8e63-4b2c-a35a-ebba07489c1d"
                           r"\",\"itemsOffset\":0,\"sectionOffset\":2,\"query\":\"Jefferson, "
                           r"Colorado, United States\",\"itemsPerGrid\":20,"
                           r"\"cdnCacheSafe\":false,\"treatmentFlags\":["
                           r"\"flex_destinations_june_2021_launch_web_treatment\","
                           r"\"new_filter_bar_v2_fm_header\","
                           r"\"merch_header_breakpoint_expansion_web\","
                           r"\"flexible_dates_12_month_lead_time\","
                           r"\"storefronts_nov23_2021_homepage_web_treatment\","
                           r"\"lazy_load_flex_search_map_compact\","
                           r"\"lazy_load_flex_search_map_wide\","
                           r"\"im_flexible_may_2022_treatment\","
                           r"\"im_flexible_may_2022_treatment\","
                           r"\"flex_v2_review_counts_treatment\","
                           r"\"flexible_dates_options_extend_one_three_seven_days\","
                           r"\"super_date_flexibility\",\"micro_flex_improvements\","
                           r"\"micro_flex_show_by_default\",\"search_input_placeholder_phrases\","
                           r"\"pets_fee_treatment\"],\"screenSize\":\"large\","
                           r"\"isInitialLoad\":true,\"hasLoggedIn\":true}}","extensions":"{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"ef48c5cbc4059de87060d37d4c62b72ad708e5ffba74fb8f042c970f0664f0c5\"}}"}

headers = {
    "authority": "www.airbnb.com",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "referer": "https://www.airbnb.com/s/Jefferson--Colorado--United-States/homes"
               "?flexible_trip_dates%5B%5D=october&date_picker_type=flexible_dates&search_type"
               "=unknown&tab_id=home_tab&adults=2&refinement_paths%5B%5D=%2Fhomes"
               "&flexible_trip_lengths%5B%5D=weekend_trip&federated_search_session_id=bbcfac66"
               "-2fe4-40f1-a432-b03d9eccf31a&pagination_search=true&items_offset=0&section_offset"
               "=3",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, "
                  "like Gecko) Chrome/102.0.5005.61 Safari/537.36",
    "x-airbnb-api-key": "d306zoyjsyarp7ifhu67rjxn52tv0t20",
    "x-airbnb-graphql-platform": "web",
    "x-airbnb-graphql-platform-client": "minimalist-niobe",
    "x-airbnb-supports-airlock-v2": "true",
    "x-csrf-without-token": "1",
    "x-niobe-short-circuited": "true"
}
