import requests


def request_to_bnb(queries):

    return list(
        filter(
            None,
            map(
                lambda query:
                requests.request(
                    **query
                ),
                queries
            )
        )
    )
