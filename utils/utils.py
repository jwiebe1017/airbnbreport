import datetime
import yaml


def safe_config_load(filepath: str) -> dict:
    with open(filepath) as yaml_file:
        return yaml.safe_load(yaml_file)


def calc_time(start, end, daysbetween):
    time_iters = list(range(0, (end-start).days, daysbetween))
    dates = []
    for i in range(len(time_iters)):
        try:
            dates.append(
                (
                    str(start + datetime.timedelta(days=time_iters[i])),
                    str(start + datetime.timedelta(days=time_iters[i+1]))
                )
            )
        except IndexError:
            continue
    return dates